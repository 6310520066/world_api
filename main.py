# For tutorial on FastAPI
# See https://fastapi.tiangolo.com/tutorial/first-steps/
from fastapi import FastAPI

# create an instance of class FastAPI named "app"
app = FastAPI()

# define function that handles "GET" request with endpoint "/"
@app.get("/")
async def read_root() -> dict:
    return {"message": "Hello there"}
