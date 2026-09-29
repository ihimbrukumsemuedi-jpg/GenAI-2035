from core.models import create_model
from config import QWEN

def test_model(question, model_name):
    model = create_model(model_name)
    return model.invoke(question)

question = "what is the difference between a car and a bike"
test_result = test_model(question, QWEN)
print(test_result.content)
 