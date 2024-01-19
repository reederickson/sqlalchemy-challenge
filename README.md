# sqlalchemy-challenge
I appologise for turning this assignment in a day late. I had it done on Monday but wasn't able to book a tutor session until Friday at 2pm where we went over my code and found an issue in the precipitation app for loop where i was trying to convert a tuple (oops) but the issue has been resolved and i am thrilled!

##Introduction
Congratulations! You've decided to treat yourself to a long holiday vacation in Honolulu, Hawaii. To help with your trip planning, you decide to do a climate analysis about the area. The following sections outline the steps that you need to take to accomplish this task.

#Part 1: Analyze and Explore the Climate Data
In this section, you’ll use Python and SQLAlchemy to do a basic climate analysis and data exploration of your climate database. My results of the Precipitation Analysis and the Station Analysis can be found under climate_erickson.ipynb. The gaphs for this section can also be found under SurfsUp/Images

#Part 2: Design Climate App
I used a Flask API which runs as follows:
/ is the homepage
/api/v1.0/precipitation converts the query results from the precipitation analysis to a dictionary using date as the key and prcp as the value. It will return the JSON list of the dictionary
/api/v1.0/stations returns JSON list of stations from the dataset
/api/v1.0/tobs querys the dates and temperature observations of the most-active station for the previous year of data and returns a JSON list of temperature observations for the previous year
/api/v1.0/<start> and /api/v1.0/<start>/<end>
Returns a JSON list of the minimum temperature, the average temperature, and the maximum temperature for a specified start or start-end range. For a specified start, calculate TMIN, TAVG, and TMAX for all the dates greater than or equal to the start date. For a specified start date and end date, calculate TMIN, TAVG, and TMAX for the dates from the start date to the end date, inclusive.





