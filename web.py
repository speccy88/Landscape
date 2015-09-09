# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, jsonify
from flask.ext.triangle import Triangle
from datetime import datetime
import shelve
import json
import os

d = shelve.open("data.db")
app = Flask(__name__)
Triangle(app)

@app.route("/")
def Index():
    return render_template("index.html")

@app.route("/api/getData")
def getData():
    data = d["week"]
    #print data
    return json.dumps(data)    
    
@app.route("/api/getState")
def getState():
    data = d["week"]
    now = datetime.now()
    weekday = now.weekday()
    startTime = now.replace(hour=int(data[weekday]["startHour"]), minute=int(data[weekday]["startMinute"]), second=0, microsecond=0)
    stopTime = now.replace(hour=int(data[weekday]["stopHour"]), minute=int(data[weekday]["stopMinute"]), second=0, microsecond=0)
    if startTime < now < stopTime:
        state = "ON"
    else:
        state = "OFF"
        
    #print startTime
    #print stopTime
    #print now
    
    return jsonify({"state":state})    
    
@app.route("/api/postData",  methods=['POST'])
def postUpdate():
    data = json.loads(request.data)
    #print data
    d["week"] = data
    return "Success"	

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)
    
    
#week = [
#    {"day":"LUNDI","startHour":10,"startMinute":10,"stopHour":10,"stopMinute":10},
#    {"day":"MARDI","startHour":10,"startMinute":10,"stopHour":10,"stopMinute":10},
#    {"day":"MERCREDI","startHour":10,"startMinute":10,"stopHour":10,"stopMinute":10},
#    {"day":"JEUDI","startHour":10,"startMinute":10,"stopHour":10,"stopMinute":10},
#    {"day":"VENDREDI","startHour":10,"startMinute":10,"stopHour":10,"stopMinute":10},
#    {"day":"SAMEDI","startHour":10,"startMinute":10,"stopHour":10,"stopMinute":10},
#    {"day":"DIMANCHE","startHour":10,"startMinute":10,"stopHour":10,"stopMinute":10},
#    ]
