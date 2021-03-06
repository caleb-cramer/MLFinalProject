# Rainfall Prediction in Australia

## Team Members
Eric Av and Caleb Cramer

## Dataset Description

1. **Source**:  [Australia Rain](https://www.kaggle.com/jsphyg/weather-dataset-rattle-package) and [Seattle Rain](https://www.kaggle.com/rtatman/did-it-rain-in-seattle-19482017/metadata)
1. **Format**: CSV file
1. **Contents**: This file contains weather data from 10 years across 49 cities in Australia. There are 145k rows and 23 columns. The second file contains weather data from Sea-Tac airport since 1948. It has 25000 instances and 5 attributes.
1. **Column Names**: Date, Location, MinTemp, MaxTemp, Rainfall, Evaporation, Sunshine, WindGustDir, WindGustSpeed, WindDir9am, WindDir3pm, WindSpeed9am, WindSpeed3pm, Humidity9am, Humidity3pm, Pressure9am, Pressure3pm, Cloud9am, Cloud3pm, Temp9am, Temp3pm, RainToday 
1. **Class Label**: RainTomorrow, a Yes/No string which will tell us if it is going to rain tomorrow...

## Implementation/ Technical Merit
1. **Anticipated challenges in pre-processing and/or classification?**: Cleaning data and making more readable with additional functions. Perhaps a date organizer, location organizer. Also it has 145k rows which is larger than we have ever worked with before so debugging on this dataset will take a very long time
1. **If the number of attributes is large, how will you explore feature selection techniques to pare down the attributes?**: We can see certain attributes that are mostly NA and some that have do not correspond directly with rainfall (wind direction). We can get rid of one of the wind direction attributes, since it is recorded twice daily) and the evaporation and sunshine attributes if we so desire.

## Potential impact of the results
1. **Why should I care?**: These results can help us predict rainfall on a given day, week, even month averages due to the dataset being from 10 consecutive years all over Australia’s regions. Therefore this might have been useful when the fires were raging in Australia last year to forecast rain based on a previous years.
1. **Who cares?**: Well Eric and I want to get a good grade so we care. Also anyone who lives in Australia might care, even though the data is old-ish. Fellow machine learning people. Meteorologists too.

## How to Run our Heroku App
Visit https://rain-app-eric-caleb.herokuapp.com
Input endpoints in result? as -> att0='year-month' -> att1='float' (high temp in F) -> att2='float' (low temp in F)
Example: https://rain-app-eric-caleb.herokuapp.com/predict?att0=13-Aug&att1=89.0&att2=54.0

## Project Organization


