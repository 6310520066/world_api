import csv

# For tutorial on FastAPI
# See https://fastapi.tiangolo.com/tutorial/first-steps/
from fastapi import FastAPI

# get country data from csv file  
filename = "world_table_country.csv"
with open(filename, "r", encoding="utf8") as csv_file:
    csv_reader = csv.reader(csv_file)
    headers = next(csv_reader)
    data_country = [{k: v for (k, v) in zip(headers, row)} for row in csv_reader]

# create an instance of class FastAPI named "app"
app = FastAPI()

# define function that handles "GET" request with endpoint "/"
@app.get("/")
async def read_root() -> dict:
    return {"message": "Hello there"}


# define function that handles "GET" request with endpoint "/world"
# list all countries
@app.get("/world")
async def read_countries() -> dict:
    return {"result": data_country}
