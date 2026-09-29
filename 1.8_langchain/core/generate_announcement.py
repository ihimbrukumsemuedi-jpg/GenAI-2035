from pydantic import BaseModel, Field
from .chains import announcement_chain, model
from .prompt import announcement_prompt

result = announcement_chain.invoke(
    {
        "tone": "formal",
        "audience": "employees",
        "announcement_details": "We are pleased to announce that our company has achieved record profits this quarter, thanks to the hard work and dedication of our team. We will be hosting a celebratory event next week to recognize everyone's contributions."
    })

class announcement(BaseModel):
    tone: str = Field(description="{result}")
    announcement_details: str = Field(description="{result}")



structured_model=model.with_structured_output(announcement)
results = structured_model.invoke("{prompt}")
print(results.model_dump())