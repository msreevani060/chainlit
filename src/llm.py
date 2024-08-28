import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()
GOOGLE_API_KEY=os.getenv("GOOGLE_API_KEY")
os.environ["GOOGLE_API_KEY"]=GOOGLE_API_KEY

def ask_bot(message): #message is user input.
    llm=ChatGoogleGenerativeAI(model="gemini-pro")
    response=llm.invoke(message)
    return response.content

#def load_model(model_name):
#    if model_name=="gemini-pro":
#        llm=ChatGoogleGenerativeAI(model="gemini-pro")
#    else:
#        llm=ChatGoogleGenerativeAI(model="gemini-pro-vision")

if __name__=="__main__":
    print("welcome to the chatbot")
    message=ask_bot("what is meaning of large language models?")
    print('message', message)