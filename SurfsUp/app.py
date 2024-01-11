# Import the dependencies.
import pandas as pd
import numpy as np
import datetime as dt
import sqlalchemy

from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

import flask
from flask import Flask, jsonify

#################################################
# Database Setup
#################################################
engine= create_engine("sqlite:///Resources.hawaii.sqlite")

# reflect an existing database into a new model
base=automap_base()

# reflect the tables
base.prepare(engine,reflect=True)

# Save references to each table
measurement = base.classes.measurement
station= base.classes.station

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
    