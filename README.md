# Capstone_Project_Group_01

![Untitled design (7)](https://user-images.githubusercontent.com/100486461/179129676-dd07e65c-6cae-4643-9e7a-96702fd7aa43.png)

# Project Overview and Purpose

Airbnb is an online marketplace for short term rentals. Airbnb hosts are allowed to rent their entire homes, apartments, single or shared bedrooms. One of the main challenges faced by the Airbnb hosts is to determine the optimal rent prices. Price depends on number of factors such as property type, room types, ammetities, customer reviews and ratings, neighbourhoods, etc. The aim of this project is to propose a data driven solution by using machine learning to predict rental prices that would help the Toronto Airbnb hosts while renting out their properties.


# Reason for choosing this data

We have chosen to work with this dataset as Airbnb is market leader in this field. The dataset is challenging, recent, detailed, and includes many features and variables that would allow us to gain valuable insights into Airbnb's business model and would also allow us to utilize machine learning tools such as Linear Regression Model for price predictions. We have chosen the Toronto market since we are familiar with the city, but the same model can be used for similar predictions in any other cities where Airbnb is currently operating. Our interests and backgrounds in Retail/Tourism industries have also inspired us to take up this dataset.


# Data Source

Find the Inside Airbnb data on the following [link](http://insideairbnb.com/get-the-data). The datasets can be found inside the Resources folder on the project Github page. Airbnb does not provide open data. However, Inside Airbnb utlizes public information complied from the Airbnb website and allows analysis of publicly availible information about a city's Airbnb listings. Inside Airbnb is an independent, non commercial set of tools and the data is not associated with or endorsed by Airbnb or any of it's competitors.


# Tools Used

For this project we have used the following tools and technologies:

Analysis:
- Python (Pandas, Numpy, Matplotlib, Seaborn)

Database
- MongoDB

Visualization
- Python
- Tableau

Machine Learning
- Regression Model (Scikit-learn)

Notebook
- Jupyter Notebook
- Google Colab


Using Inside Airbnb data, this project will include descriptive analysis, using Pandas for data cleansing and MongoDB to store the data. It will also use machine learning to compare listings and predict the target value, using linear regression. Some of the features will include the neighborhood, type of listing, amenities, and information about the host. Visualization will be presented in Tableau dashboard, including visualizations.


# Hypothesis

Prices are dependent on factors such as neighbourhoods, room types, number of bedrooms, amenities, customer reviews and ratings for the host and proporty.

The images have been attached below for reference. 

## ERD Diagram
![airbnb_db_erd](Resources/images/airbnb_db_erd.png)


## Machine Learning Model
![machine_learning](Resources/images/ML_steps_Linear_Regression.png)


## ETL Pipeline Diagram
![etl_pipeline_project](Resources/images/etl_pipeline_project.png)


We are currently working on the [clean_data_final.ipynb](clean_data_final.ipynb) jupyter notebook file for the project.

