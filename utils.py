import os 
from pydantic import BaseModel
from pydantic import Field


def delete_previous_file(save_dir):
    for file_name in os.listdir(save_dir):
        if file_name.endswith('.pdf'):
            os.remove(os.path.join(save_dir, file_name))



class Categorization(BaseModel):
    """Respond to the user with this"""
    summarize_content: str = Field(description="give me a meaningful consise summarization of the document")
    person_name: str = Field(description="Name of the person in the document")
    govertment_id: str = Field(description="Government ID of the person in the document")
    email_address: str = Field(description="Email address of the person in the document")
    type_of_document: str = Field(description=''' the document is of what type, cho0se from the folllowing
                                  credit card,
                                  savings account,
                                  driver's license,
                                  state/country identification,
                                  passport,
                                  income statements/paystubs,
                                  tax returns,
                                  Receipts''')