from flask import Flask,request,jsonify,render_template
import pickle
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler

application = Flask(__name__)
app = application

ridge_model = pickle.load(open('Models/ridge.pkl','rb'))
standard_scaler = pickle.load('Models/scaler.pkl','rb')

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "main":
    app.run(host="0.0.0.0")
