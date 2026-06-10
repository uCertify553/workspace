from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI
import openai# Set API configuration
openai.api_key = "sk-proj-UCf7Gh3PqXa2ZLm4Rt6Yw8Nv0Bd5Kj1HrQeCsuTuVoMiXpAzEnLbYcDgFksjWhUoP1RaA"
openai.api_base = "https://www.ucertify.com/custom/openai/v1"
# Initialize Chat Model
chat_model = ChatOpenAI(
    model_name="gpt-3.5-turbo",
    openai_api_key=openai.api_key,
    openai_api_base=openai.api_base,
    temperature=0.7
)
# Define prompt template
prompt_template = PromptTemplate(
    input_variables=["topic"],
    template="""
    Write a short article about the following topic:
    {topic}    The article should include:
    - Introduction
    - Key benefits
    - Conclusion
    """
)
# Create LangChain chain
chain = LLMChain(
    llm=chat_model,
    prompt=prompt_template
)
# Topic input
topic = "Benefits of Artificial Intelligence in Healthcare"
# Generate article
response = chain.run(topic)
# Display output
print("\nGenerated Article:\n")
print(response)