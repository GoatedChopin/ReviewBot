from fastapi import FastAPI
from prompt import get_manager_response
from fake_database import fake_database
from review import Review, get_review_sentiment


app = FastAPI()


@app.post("/")
async def review_response(review: Review):
    company_details = fake_database[review.company_name]
    if get_review_sentiment(review.review_text) <= company_details.negative_response_threshold:
        response = get_manager_response(review.review_text, company_details)
        return {"response": response, "status": 200}


if __name__ == "__main__":
    from os import system
    system("uvicorn main:app --host 0.0.0.0 --port 80")