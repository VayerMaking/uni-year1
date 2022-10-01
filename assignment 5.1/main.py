from datetime import datetime
from flask import Flask, render_template, request
import csv
import pandas as pd
 
app = Flask(__name__) 
 
@app.route("/") 
def index(): 
    data = pd.read_csv("statistics.csv")
    
    statistics = {
        "avg_temperature" : data["temperature"].mean(),
        "avg_humidity" : data["humidity"].mean(),
        "min_temperature" : data["temperature"].min(),
        "min_humidity" : data["humidity"].min(),
        "max_temperature" : data["temperature"].max(),
        "max_humidity" : data["humidity"].max()
    }

    return render_template('index.html', latest_data=data.iloc[-1], statistics=statistics)

@app.route("/post_data", methods=['POST'])
def post_data():
    print(request.json)
    with open('statistics.csv', 'a') as statistics:
        writer = csv.writer(statistics)
        data = [datetime.now(), request.json['temperature'], request.json['humidity'], request.remote_addr]
        writer.writerow(data)
    return "ok"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)