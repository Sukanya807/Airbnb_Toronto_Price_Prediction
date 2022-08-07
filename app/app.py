from flask import Flask, render_template, request
import pandas as pd
import xgboost as xgb
from sklearn import model_selection
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def home():
    if request.method == "POST":      

        columns = ['host_is_superhost','host_listings_count','host_identity_verified','accommodates','bathrooms','minimum_nights',
        'maximum_nights','has_availability','availability_90','number_of_reviews','instant_bookable','host_active_days','avg_rating_overall',
        'amenities_sum','host_response_time_a few days or more','host_response_time_unknown','host_response_time_within a day',
        'host_response_time_within a few hours','host_response_time_within an hour','host_response_rate_0-49%','host_response_rate_100%',
        'host_response_rate_50-89%','host_response_rate_90-99%','host_response_rate_unknown','borough_Central Toronto','borough_Downtown Toronto',
        'borough_East Toronto','borough_East York','borough_East YorkEast Toronto','borough_Etobicoke','borough_EtobicokeNorthwest','borough_North York',
        'borough_Scarborough','borough_West Toronto','borough_York','borough_unkown','property_type_Apartment','property_type_House','property_type_One Room',
        'property_type_Other','property_type_Shared Room','neighbourhood_Agincourt North','neighbourhood_Agincourt South-Malvern West',
        'neighbourhood_Alderwood','neighbourhood_Annex','neighbourhood_Banbury-Don Mills','neighbourhood_Bathurst Manor','neighbourhood_Bay Street Corridor',
        'neighbourhood_Bayview Village','neighbourhood_Bayview Woods-Steeles','neighbourhood_Bedford Park-Nortown','neighbourhood_Beechborough-Greenbrook',
        'neighbourhood_Bendale','neighbourhood_Birchcliffe-Cliffside','neighbourhood_Black Creek','neighbourhood_Blake-Jones',
        'neighbourhood_Briar Hill-Belgravia','neighbourhood_Bridle Path-Sunnybrook-York Mills','neighbourhood_Broadview North',
        'neighbourhood_Brookhaven-Amesbury','neighbourhood_Cabbagetown-South St.James Town','neighbourhood_Caledonia-Fairbank','neighbourhood_Casa Loma',
        'neighbourhood_Centennial Scarborough','neighbourhood_Church-Yonge Corridor','neighbourhood_Clairlea-Birchmount','neighbourhood_Clanton Park',
        'neighbourhood_Cliffcrest','neighbourhood_Corso Italia-Davenport','neighbourhood_Danforth','neighbourhood_Danforth East York',
        'neighbourhood_Don Valley Village','neighbourhood_Dorset Park','neighbourhood_Dovercourt-Wallace Emerson-Junction',
        'neighbourhood_Downsview-Roding-CFB','neighbourhood_Dufferin Grove','neighbourhood_East End-Danforth','neighbourhood_Edenbridge-Humber Valley',
        'neighbourhood_Eglinton East','neighbourhood_Elms-Old Rexdale','neighbourhood_Englemount-Lawrence','neighbourhood_Eringate-Centennial-West Deane',
        'neighbourhood_Etobicoke West Mall','neighbourhood_Flemingdon Park','neighbourhood_Forest Hill North','neighbourhood_Forest Hill South',
        'neighbourhood_Glenfield-Jane Heights','neighbourhood_Greenwood-Coxwell','neighbourhood_Guildwood','neighbourhood_Henry Farm',
        'neighbourhood_High Park North','neighbourhood_High Park-Swansea','neighbourhood_Highland Creek','neighbourhood_Hillcrest Village',
        'neighbourhood_Humber Heights-Westmount','neighbourhood_Humber Summit','neighbourhood_Humbermede','neighbourhood_Humewood-Cedarvale',
        'neighbourhood_Ionview','neighbourhood_Islington-City Centre West','neighbourhood_Junction Area','neighbourhood_Keelesdale-Eglinton West',
        'neighbourhood_Kennedy Park','neighbourhood_Kensington-Chinatown','neighbourhood_Kingsview Village-The Westway','neighbourhood_Kingsway South',
        "neighbourhood_L'Amoreaux",'neighbourhood_Lambton Baby Point','neighbourhood_Lansing-Westgate','neighbourhood_Lawrence Park North',
        'neighbourhood_Lawrence Park South','neighbourhood_Leaside-Bennington','neighbourhood_Little Portugal','neighbourhood_Long Branch',
        'neighbourhood_Malvern','neighbourhood_Maple Leaf','neighbourhood_Markland Wood','neighbourhood_Milliken',
        'neighbourhood_Mimico (includes Humber Bay Shores)','neighbourhood_Morningside','neighbourhood_Moss Park','neighbourhood_Mount Dennis',
        'neighbourhood_Mount Olive-Silverstone-Jamestown','neighbourhood_Mount Pleasant East','neighbourhood_Mount Pleasant West','neighbourhood_New Toronto',
        'neighbourhood_Newtonbrook East','neighbourhood_Newtonbrook West','neighbourhood_Niagara','neighbourhood_North Riverdale',
        'neighbourhood_North St.James Town',"neighbourhood_O'Connor-Parkview",'neighbourhood_Oakridge','neighbourhood_Oakwood Village',
        'neighbourhood_Old East York','neighbourhood_Palmerston-Little Italy','neighbourhood_Parkwoods-Donalda','neighbourhood_Pelmo Park-Humberlea',
        'neighbourhood_Playter Estates-Danforth','neighbourhood_Pleasant View','neighbourhood_Princess-Rosethorn','neighbourhood_Regent Park',
        'neighbourhood_Rexdale-Kipling','neighbourhood_Rockcliffe-Smythe','neighbourhood_Roncesvalles','neighbourhood_Rosedale-Moore Park',
        'neighbourhood_Rouge','neighbourhood_Runnymede-Bloor West Village','neighbourhood_Rustic','neighbourhood_Scarborough Village',
        'neighbourhood_South Parkdale','neighbourhood_South Riverdale','neighbourhood_St.Andrew-Windfields','neighbourhood_Steeles',
        'neighbourhood_Stonegate-Queensway',"neighbourhood_Tam O'Shanter-Sullivan",'neighbourhood_Taylor-Massey','neighbourhood_The Beaches',
        'neighbourhood_Thistletown-Beaumond Heights','neighbourhood_Thorncliffe Park','neighbourhood_Trinity-Bellwoods','neighbourhood_University',
        'neighbourhood_Victoria Village','neighbourhood_Waterfront Communities-The Island','neighbourhood_West Hill','neighbourhood_West Humber-Clairville',
        'neighbourhood_Westminster-Branson','neighbourhood_Weston','neighbourhood_Weston-Pellam Park','neighbourhood_Wexford/Maryvale',
        'neighbourhood_Willowdale East','neighbourhood_Willowdale West','neighbourhood_Willowridge-Martingrove-Richview','neighbourhood_Woburn',
        'neighbourhood_Woodbine Corridor','neighbourhood_Woodbine-Lumsden','neighbourhood_Wychwood','neighbourhood_Yonge-Eglinton',
        'neighbourhood_Yonge-St.Clair','neighbourhood_York University Heights','neighbourhood_Yorkdale-Glen Park','host_active_days_cat_less than 3 years',
        'host_active_days_cat_3-5 years','host_active_days_cat_5-8 years','host_active_days_cat_8-10 years','host_active_days_cat_more than 10 years',
        'avg_rating_overall_cat_average','avg_rating_overall_cat_excellent','avg_rating_overall_cat_poor']
            
        # Prepare data for the model
        neighbourhood_col = 'neighbourhood_'+ request.form.get("neighbourhood")
        borough_col = 'borough_' + request.form.get("borough")
        host_response_time_col = 'host_response_time_' + request.form.get("host_response_time")
        host_response_rate_col = 'host_response_rate_' + request.form.get("host_response_rate")
        property_type_col = 'property_type_' + request.form.get("property_type")
        host_active_days_col = 'host_active_days_' + request.form.get("host_since")

        print(request.form.get("avg_rating_overall"))

        avg_rating_overall = int(request.form.get("avg_rating_overall"))
        
        if avg_rating_overall < 2:
            avg_rating_overall_col = 'avg_rating_overall_' + 'poor'
        elif avg_rating_overall < 4:
            avg_rating_overall_col = 'avg_rating_overall_' + 'average'
        else:
            avg_rating_overall_col = 'avg_rating_overall_' + 'excellent'
        
        toiletries = int(request.form.get("toiletries"))
        high_end_electronics = int(request.form.get("high_end_electronics"))
        ac_heater = int(request.form.get("ac_heater"))
        internet = int(request.form.get("internet"))
        bbq = int(request.form.get("bbq"))
        home_appliances = int(request.form.get("home_appliances"))
        coffee_machine = int(request.form.get("coffee_machine"))
        long_term_stays = int(request.form.get("long_term_stays"))
        host_greeting = int(request.form.get("host_greeting"))
        safety = int(request.form.get("safety"))
        outdoor_space = int(request.form.get("outdoor_space"))
        hot_tub_sauna_or_pool = int(request.form.get("hot_tub_sauna_or_pool"))
        room_features = int(request.form.get("room_features"))
        parking = int(request.form.get("parking"))
        kitchen = int(request.form.get("kitchen"))
        elevator = int(request.form.get("elevator"))
        private_entrance = int(request.form.get("private_entrance"))
        gym = int(request.form.get("gym"))
        other_facilities = int(request.form.get("other_facilities"))
        breakfast = int(request.form.get("breakfast"))
        child_friendly = int(request.form.get("child_friendly"))
        nature_and_views = int(request.form.get("nature_and_views"))
        event_suitable = int(request.form.get("event_suitable"))
        smoking_allowed = int(request.form.get("smoking_allowed"))
        accessible = int(request.form.get("accessible"))

        amenities_sum = other_facilities + toiletries + high_end_electronics + ac_heater + internet + bbq + home_appliances + coffee_machine + long_term_stays + host_greeting + safety + outdoor_space + hot_tub_sauna_or_pool + room_features + private_entrance + parking + kitchen + elevator + gym + breakfast + child_friendly + nature_and_views + event_suitable + smoking_allowed + accessible

        data = {
            host_active_days_col : 1,
            host_response_time_col : 1,
            host_response_rate_col: 1,
            'has_availability': int(request.form.get("has_availability")),
            'host_listings_count' : int(request.form.get("host_listings_count")),
            'host_identity_verified' : int(request.form.get("host_identity_verified")),
            'host_is_superhost' : int(request.form.get("host_is_superhost")),
            neighbourhood_col : 1,
            borough_col : 1,
            'instant_bookable' : int(request.form.get("instant_bookable")),
            property_type_col : 1,
            'accommodates' : int(request.form.get("accommodates")),
            'minimum_nights' : int(request.form.get("minimum_nights")),
            'maximum_nights' : int(request.form.get("maximum_nights")),
            'availability_90' : int(request.form.get("availability_90")),
            'number_of_reviews' : int(request.form.get("number_of_reviews")),
            avg_rating_overall_col : 1,
            'avg_rating_overall' : avg_rating_overall,
            'amenities_sum' : amenities_sum
        }

        data = {k:[v] for k,v in data.items()}

        # Create dataframe
        data_df = pd.DataFrame(data)

        # Fill columns not created by the dictionary
        for c in columns:
            if c not in data_df.columns:
                data_df[c] = 0

        # Load the model
        model = xgb.XGBRegressor()
        model.load_model("model.bst")

        data_df = data_df[columns]

        prediction = model.predict(data_df)

        prediction_text = (f'<div class="alert alert-primary" role="alert">Your property should be listed for $ {str(int(prediction[0]))}</div>')

        return prediction_text
    return render_template('index.html')
if __name__ == '__main__':
   app.run()