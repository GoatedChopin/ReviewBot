import openai
from os import environ


openai.api_key = environ("OPENAI_API_KEY")


class CompanyDetails:
    def __init__(self, company_name: str, company_bio: str, contact_info: str) -> None:
        self.company_name = company_name
        self.company_bio = company_bio
        self.contact_info = contact_info


def generate_prompt(review: str, company_details: CompanyDetails) -> str:
    company_bio = company_details.company_bio
    contact_info = company_details.contact_info
    prompt = f"Pretend you are the owner of the following company:\n{company_bio}\nCraft a response to the following review. Be sure to mention that they should reach out to {contact_info} to make things right:\n{review}"
    return prompt


def get_manager_response(review: str, company_details: CompanyDetails) -> str:
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=generate_prompt(review, company_details),
        temperature=0.6,
        max_tokens=250,
        )
    return response