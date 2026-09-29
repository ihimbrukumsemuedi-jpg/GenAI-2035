from pydantic import BaseModel, Field
from .models import create_model
from config import QWEN

model=create_model()
# Create the blueprint for the output of the model

class Player(BaseModel):
    name: str = Field(description="The name of the football player")
    age: int = Field(description="The age of the football player")
    club: str = Field(description="The club of the football player")
    nationality: str = Field(description="The nationality of the football player")
    national_flag:str = Field(description="The national flag of the football player as an emoji")

class TopTen(BaseModel):
    opinion: str = Field(description="The opinion of the model about the top ten footballers of all time")
    players: list[Player] = Field(description="list of top ten footballers of all time")

structured_model=model.with_structured_output(TopTen)
result=structured_model.invoke("Give me the top ten footballers of all time")
print(result.model_dump())


#print(f"the player namev is : {result.name}")
#print(f"the player age is : {result.age}")   