import os
from langchain.llms import OpenAI
from langchain import PromptTemplate
from langchain.chains import LLMChain

openai = OpenAI(temperature=0.9)
template = """Answer the question based on the context below. If the
question cannot be answered using the information provided answer
with "I don't know".

Context:

Question: What would be a good company name for a company that makes {product}?

Answer: """

prompt_template = PromptTemplate(
    input_variables=["product"],
    template=template
)

chain = LLMChain(llm=openai, prompt=prompt_template)
#print(chain.run("colorful socks"))

second_prompt = PromptTemplate(
    input_variables=["company_name"],
    template="Write a catchphrase for the following company: {company_name}",
)

chain_two = LLMChain(llm=openai, prompt=second_prompt)

from langchain.chains import SimpleSequentialChain
overall_chain = SimpleSequentialChain(chains=[chain, chain_two], verbose=True)

# Run the chain specifying only the input variable for the first chain.
catchphrase = overall_chain.run("colorful socks")
print(catchphrase)
