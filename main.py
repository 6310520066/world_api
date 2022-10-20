# For tutorial on FastAPI
# See https://fastapi.tiangolo.com/tutorial/first-steps/
from fastapi import FastAPI

from utils import get_data_from_csv

data_country = get_data_from_csv("world_table_country.csv")
data_city = get_data_from_csv("world_table_city.csv")

# create an instance of class APIRouter named "app"
app = FastAPI()

# define function that handles "GET" request with endpoint "/"
@app.get("/")
async def read_root() -> dict:
    return {"message": "Hello there"}


# define function that handles "GET" request with endpoint "/world" and "/world/"
@app.get("/world")
async def read_countries() -> dict:
    return {"result": data_country}


# define function that handles "GET" request with endpoint "/world/country/{name}"
# "/world/country/{name}" is a "path paramter" endpoint
@app.get("/world/country/{name}")
async def read_country(name: str) -> dict:
    for row in data_country:
        if row["Name"].lower() == name.lower():
            return {"result": row}
    return {"result": {}}


# define function that handles "GET" request with endpoint "/world/city/{name}"
# "/world/city/{name}" is a "path paramter" endpoint
@app.get("/world/city/{name}")
async def read_city(name: str) -> dict:
    for row in data_city:
        if row["Name"].lower() == name.lower():
            return {"result": row}
    return {"result": {}}
