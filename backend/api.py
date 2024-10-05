import csv
from fastapi import FastAPI


app = FastAPI()
aot_data = []

with open('backend/aerosol_data_riyadh.csv', mode='r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # Read and skip the header
    for row in csv_reader:
        aot_data.append(row)  # Append the row directly (as a list)

@app.get("/get-aot")
def get_aot():
    return aot_data

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
