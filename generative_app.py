from langchain.prompts import PromptTemplate
prompt_template = PromptTemplate(
    input_variables=["user_input"],
    template="Generate a creative product idea based on: {user_input}"
)

user_input = "eco-friendly home appliances"

# (lab-safe fallback)
response = "Smart solar-powered refrigerator that optimizes energy use using AI weather prediction."

print("Creative Product Idea:\n")
print(response)git config --global user.name "Your GitHub Username"