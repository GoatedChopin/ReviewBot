from fastapi import FastAPI
from pydantic import BaseModel
from prompt import get_manager_response
from fake_database import fake_database


app = FastAPI()


class Review(BaseModel):
    review_text: str
    company_name: str


@app.post("/")
async def review_response(review: Review):
    company_details = fake_database[review.company_name]
    response = get_manager_response(review.review_text, company_details)
    return {"response": response, "status": 200}


if __name__ == "__main__":
    from os import system
    system("uvicorn main:app --host 0.0.0.0 --port 80")