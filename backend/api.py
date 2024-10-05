import csv
from fastapi import FastAPI
from ai.aot_prediction import predict_aot_batch
import numpy as np
from datetime import datetime


app = FastAPI()
aot_data = []

with open('backend/aerosol_data_riyadh.csv', mode='r') as file:
    csv_data = csv.reader(file)
    next(csv_data) # Skip header
    for row in csv_data:
        aot_data.append(row)

@app.get("/data/get-all")
def get_all():
    return aot_data


@app.post("/data/get-one")
def get_one(date: str):
    date_values = []
    for row in aot_data:
        if row[0] == date:
            date_values.append(row)
    return date_values

@app.get('/ai/predict_aot')
def predict_aot(prediction_date):
    y, m, d = prediction_date.split('-')
    prediction_date = datetime(int(y), int(m), int(d))
    processed_inputs = np.array(aot_data)
    predicted_aots = predict_aot_batch(processed_inputs, prediction_date)
    print(type(predicted_aots))
    # for i, prediction in enumerate(predicted_aots):
    #     print(f"Prediction {i+1}: {}")
    print(5)
    


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
