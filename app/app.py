from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def home():
    if request.method == "POST":
        data ={
            'host_since' : request.form.get("host_since"),
            'host_response_time' : request.form.get("host_response_time"),
            'host_response_rate' : request.form.get("host_response_rate"),
            'host_listings_count' : request.form.get("host_listings_count"),
            'host_identity_verified' : request.form.get("host_identity_verified"),
            'host_is_superhost' : request.form.get("host_is_superhost"),
            'neighbourhood' : request.form.get("neighbourhood"),
            'borough' : request.form.get("borough"),
            'instant_bookable' : request.form.get("instant_bookable"),
            'property_type' : request.form.get("property_type"),
            'accommodates' : request.form.get("accommodates"),
            'minimum_nights' : request.form.get("minimum_nights"),
            'maximum_nights' : request.form.get("maximum_nights"),
            'availability_90' : request.form.get("availability_90"),
            'number_of_reviews' : request.form.get("number_of_reviews"),
            'average_rating_overall' : request.form.get("average_rating_overall"),
            'toiletries' : request.form.get("toiletries"),
            'high_end_electronics' : request.form.get("high_end_electronics"),
            'ac_heater' : request.form.get("ac_heater"),
            'internet' : request.form.get("internet"),
            'bbq' : request.form.get("bbq"),
            'home_appliances' : request.form.get("home_appliances"),
            'coffee_machine' : request.form.get("coffee_machine"),
            'long_term_stays' : request.form.get("long_term_stays"),
            'host_greeting' : request.form.get("host_greeting"),
            'safety' : request.form.get("safety"),
            'outdoor_space' : request.form.get("outdoor_space"),
            'hot_tub_sauna_or_pool' : request.form.get("hot_tub_sauna_or_pool"),
            'room_features' : request.form.get("room_features"),
            'parking': request.form.get("parking"),
            'kitchen': request.form.get("kitchen"),
            'elevator': request.form.get("elevator"),
            'private_entrance': request.form.get("private_entrance"),
            'gym' : request.form.get("gym"),
            'other_facilities' : request.form.get("other_facilities")
        }
        return data
    return render_template('index.html')
if __name__ == '__main__':
   app.run()