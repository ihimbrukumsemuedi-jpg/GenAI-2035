from .models import create_model
from config import QWEN

model = create_model(QWEN)
response = model.invoke("who is the first lady of the united states of America")

print(response.content)

#for chunk in model.stream(" who is the GOAT of all time in football"):
    #print(f"{chunk.text}", flush=True, end="|")

message_batch=[
    'why do they call black Americans Nigros'
    'who was the first president of cameroon'
    'who started the first world war 2?'
]

responses=model.batch(message_batch)

for r in responses:
    print(r.text)