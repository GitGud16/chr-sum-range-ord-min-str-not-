import csv
from fastapi import FastAPI


app = FastAPI()
aot_data = []

with open('backend/aerosol_data_riyadh.csv', mode='r') as file:
    csv_data = csv.reader(file)
    next(csv_data)  # Read and skip the header
    for row in csv_data:
        aot_data.append(row)  # Append the row directly (as a list)

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

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
