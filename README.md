# ImmoEliza - Deploying an app through Heroku

By: [Kristof Vandewynckel](https://github.com/KristofVandewynckel) - Junior Data Scientist at BeCode
--------------------------------------------------------------------------------------------------------

## Project Description

This project followed upon an older webscraping project, found [here](https://github.com/IrinaSing/immo-scraping). Where we used Selennium to scrape real estate information from the website ImmoWeb. The assignment given by ImmoEliza was to create a machine learning model to predict housing prices based on user input, and deploy this in an workable app through Heroku.

## Software Used

Code Used:
- Python

Libraries Used:
- Pandas
- Numpy
- Pickle
- Sklearn
- Flask
- Math

Deployment through Heroku and Git.

## Folder structure

- model: - Our saved Machine Learning model to be used in our prediction.
- predict: - Our function to be used in our Heroku application to predict the price.
- preprocessing: - Our function to preprocess the scraped data and make it usable for our predict.
- static: - Contains the .CSS document used in our app.
- templates: - Contains the .html documents used in our app


## Step 1: Preprocessing the data

Folder used: [/Preprocessing](https://github.com/KristofVandewynckel/Deployment_Project/tree/main/preprocessing)

To begin we take the housing data we got from our webscraping project. We use our function preprocess() to clean up all the data, this includes; removing NaN, dealing with unreadable or incomplete data, simplifying values with the same meaning, changing strings to dummies (0/1) for better model comprehension,..

Once this is done everything is saved in a filtered .csv file to be used by our model.

## Step 2: Training our model

Once we have our clean data we use our train() function from the prediction.py file in our predict folder, to train our model with the filtered data. Here we can change Machine Learning models for increasing accuracy in the future. Just run the train() function with the correct path to the .csv and it will save a Machine Learning model in our model folder with Pickle.

## Step 3: Predicing a price

Folder used: [/Predict](https://github.com/KristofVandewynckel/Deployment_Project/tree/main/predict)

Try for yourself [here](https://app-kristof-vandewynckel.herokuapp.com/).
Once the model is trained and saved by pickle our predict() function (currently inside our app.py file) will take the input given from the user and apply our Machine Learning model to it. This will then give us an estimation on the price of our given house through Flask. We can navigate on the pages to Home or Predict, to query a new estimation.

![image](https://user-images.githubusercontent.com/98815092/167114598-eb18b8b2-2657-4710-97b5-403cef94a80c.png)
![image](https://user-images.githubusercontent.com/98815092/167114667-c42b2419-60c4-4421-91bd-98157ef64318.png)

## Step 4: Improvement

This project can still be improved upon by more data, other Machine Learning models and a more extensive app. Feel free to play around with the estimates and create an even better model/app.
