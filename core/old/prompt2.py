
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

llm = ChatOpenAI(temperature=1)

# num of tokens
#resposta = llm.invoke("My name is Fabio")
#print(resposta)

#print(resposta.content)

#print("\n\n)

# stateless
#resposta = llm.invoke("What is my name?")
#print(resposta) #with header

# higher temperature creates diverse answers

#prompt = ChatPromptTemplate.from_messages([
#("human", "Hello", how are you") # human is a role! I can't create a new one. Human and User are the same and Assistant and AI are the same.
#("ai", "I'm doing well, thanks!"),
#("human", "...")

user_query = "O que é refatoração"

prompt = ChatPromptTemplate.from_messages([
("system", "Eu quero que você atue com um expert em design de código"),
("user", "{user_query}"),
])

#prompt out of the model

# combine both

prompt.pipe(llm)

# chain at least one prompt and a model
# chain = prompt | llm | ... | ...

response = chain.invoke({"user_query" : user_query})


