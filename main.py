from fastapi import FastAPI, Path
from typing import Annotated
import data_conslidator
from mangum import Mangum


app = FastAPI()
handler = Mangum(app)

@app.get("/")
async def root():
    return {"message": "Hello and Thank you for using my project"}

@app.get("/book/{item_id}")
async def read_item(item_id: Annotated[int, Path(title='The ISBN Number of the book', 
                                                 min_length=10, max_length=13, 
                                                 description='The ISBN number is 10 before 2007 and from January 2007 it was 13 digits', 
                                                 example ='9781617295980')]):
    """
    Reads the ISBN number off and responds back with all the associated data

    """
    data = data_conslidator.data_conslidator(item_id)
    payload = data.get_data()
    return payload