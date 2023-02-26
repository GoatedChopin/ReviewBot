from pydantic import BaseModel


class Review(BaseModel):
    review_text: str
    company_name: str


def get_review_sentiment(review_text):
    """
    Placeholder function, needs to be replaced with a transformer estimator or other nlp method.
    """
    return 0.1