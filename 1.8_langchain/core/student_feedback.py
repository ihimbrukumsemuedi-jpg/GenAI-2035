from pydantic import BaseModel, Field
from .models import create_model
from config import QWEN

model=create_model()

class CourseFeedback(BaseModel):
    sentiment: str = Field(description="The sentiment of the student feedback: positive, negative, or neutral")
    key_points: list[str] = Field(description="A list of key points mentioned in the feedback")
    suggested_actions: list[str] = Field(description="A list of suggested actions for improvement based on the student feedback")
    original_text: str = Field(description="The original student feedback text")


def build_feedback_classifier():
    structured_model=model.with_structured_output(CourseFeedback)
    return structured_model

classifier = build_feedback_classifier()

results = []

feedback_list = [
    "The course was very informative and well-structured. I particularly enjoyed the hands-on projects.",
    "I found the course content to be outdated and not relevant to current industry standards.",
    "The instructor was engaging, but the pace of the course was too fast for me to keep up.",
    "I appreciated the real-world examples provided in the lectures, but I wish there were more interactive sessions.",
    "The course materials were comprehensive, but I struggled with some of the advanced topics."
]

for feedback in feedback_list:
    result = classifier.invoke(feedback)
    results.append(result.model_dump())
