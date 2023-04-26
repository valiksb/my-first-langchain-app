import os
from langchain.llms import OpenAI
from langchain import PromptTemplate

openai = OpenAI(temperature=0.9)
template = """Answer the question based on the context below. If the
question cannot be answered using the information provided answer
with "I don't know".

Context:

Question: {query}

Answer: """

#print(llm(prompt))

prompt_template = PromptTemplate(
    input_variables=["query"],
    template=template
)

print(
    prompt_template.format(
        query="What would be a good company name for a company that makes colorful socks?"
    )
)

print(openai(
    prompt_template.format(
        query="What would be a good company name for a company that makes colorful socks?"
    )
))
