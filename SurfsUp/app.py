# Import the dependencies.
import pandas as pd
import numpy as np
import datetime as dt
import sqlalchemy

from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask
from flask import jsonify


#################################################
# Database Setup
#################################################
engine= create_engine("sqlite:///../Resources.hawaii.sqlite")

# reflect an existing database into a new model
Base=automap_base()

# reflect the tables
Base.prepare(engine, reflect=True)
print(Base.classes.keys())

# Save references to each table
Measurement = Base.classes.measurement
Station= Base.classes.station 

# Create our session (link) from Python to the DB
session= Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################
@app.route("/")
def welcome():
    # """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        '''
        Welcome to the Climate Analysis API!  <br/>
        The Available Routes:
        /api/v1.0/precipitation
        /api/v1.0/stations
        /api/v1.0/tobs
        /api/v1.0/temp/start/end
        '''
    )

#Precipitation
# Convert the query results from your precipitation analysis 
#(i.e. retrieve only the last 12 months of data) to a dictionary using date as the key and prcp as the value.
# Return the JSON representation of your dictionary.
@app.route("/api/v1.0/precipitation")
def precipitation():
    previous_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    precipitation = session.query(Measurement.date, Measurement.prcp).\
    filter(Measurement.date >= previous_year).all()
    precipitation= {date: precipitation for date in precipitation}
    return jsonify(precipitation)

#stations
# Return a JSON list of stations from the dataset.
@app.route("/api/v1.0/stations")
def stations():
    results= session.query(Station.station).all()
    stations=list(np.ravel(results))
    return jsonify(stations=stations)

#tobs
# Query the dates and temperature observations of the most-active station for the previous year of data.
# Return a JSON list of temperature observations for the previous year.
@app.route("/api/v1.0/tobs")
def temp_monthly():
    previous_year= dt.date(2017,8,23)- dt.timedelta(days=365)
    results=session.query(Measurement.tobs).\
    filter(Measurement.station == 'USC00519281').\
    filter(Measurement.date >= previous_year).all()
    temps= list(np.ravel(results))
    return jsonify(temps=temps)

#temp start/end
# Return a JSON list of the minimum temperature, the average temperature, and the maximum temperature for a specified start or start-end range.
# For a specified start, calculate TMIN, TAVG, and TMAX for all the dates greater than or equal to the start date.
# For a specified start date and end date, calculate TMIN, TAVG, and TMAX for the dates from the start date to the end date, inclusive.# /api/v1.0/<start> and /api/v1.0/<start>/<end>
@app.route("/api/v1.0/<start>")
@app.route("/api/v1.0/<start>/<end>")
def stats(start=None, end=None):
    sel= [func.min(Measurement.tobs), func.avg(Measurement.tobs),func.max(Measurement.tobs)]
    if not end:
        results=session.query(*sel).\
            filter(Measurement.date >= start).\
            filter(Measurement.date <= end).all()
        temps= list(np.ravel(results))
        return jsonify(temps)
    else:
        results.session.query(*sel).\
            filter(Measurement.date >= start).\
            filter(Measurement.date <= end).all()
        temps=list(np.ravel(results))
        return jsonify(temps=temps)

if __name__ == '__main__':
    app.run(debug=True)

#################################################
#################################################
#################################################
