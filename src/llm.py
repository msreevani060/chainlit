import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from src.config import instruction

load_dotenv()
GOOGLE_API_KEY=os.getenv("GOOGLE_API_KEY")
os.environ["GOOGLE_API_KEY"]=GOOGLE_API_KEY

#defining the behaviour of system for gemini api
user_message="can you tell me about menu?"
#message=[{"role":"system", "content":instruction}, 
#         {"role":"user","content":user_message}]

#modfied the behaviour of system for gemini api and pass inside method
def ask_bot(user_message):
    messages=[{"role":"system", "content":instruction}, 
              {"role":"user","content":user_message}]
    llm=ChatGoogleGenerativeAI(model="gemini-pro")
    response=llm.invoke(messages)
    return response.content


#A mthod to pass the user messages. 
#def ask_bot(message): #message is user input.
#    llm=ChatGoogleGenerativeAI(model="gemini-pro")
#    response=llm.invoke(message)
#    return response.content

#now we are passing user messages in beahvior of system
#message=[{"role":"system", "content":instruction}, 
#         {"role":"user","content":user_message}]

llm=ChatGoogleGenerativeAI(model="gemini-pro", convert_system_message_to_human=True)
response=llm.invoke(message)
print(response.content)

#def load_model(model_name):
#    if model_name=="gemini-pro":
#        llm=ChatGoogleGenerativeAI(model="gemini-pro")
#    else:
#        llm=ChatGoogleGenerativeAI(model="gemini-pro-vision")

#Just to test Gemini pro llm.invoke()
#if __name__=="__main__":
#    print("welcome to the chatbot")
#    message=ask_bot("what is meaning of large language models?")
#    print('message', message)