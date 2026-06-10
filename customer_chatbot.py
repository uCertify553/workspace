from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage
import openai
# Set API configuration
openai.api_key = "sk-proj-UCf7Gh3PqXa2ZLm4Rt6Yw8Nv0Bd5Kj1HrQeCsuTuVoMiXpAzEnLbYcDgFksjWhUoP1RaA"
openai.api_base = "https://www.ucertify.com/custom/openai/v1"
# Initialize chat model
chat_model = ChatOpenAI(
    model_name="gpt-3.5-turbo",
    openai_api_key=openai.api_key,
    openai_api_base=openai.api_base,
    temperature=0
)
# Function to generate chatbot response
def generate_response(user_query):
    messages = [HumanMessage(content=user_query)]
    response = chat_model.invoke(messages)
    return response.content
# Customer query
customer_query = "My order has not arrived yet. What should I do?"
# Generate response
result = generate_response(customer_query)
# Display output
print("\nCustomer Query:\n")
print(customer_query)
print("\nChatbot Response:\n")
print(result)