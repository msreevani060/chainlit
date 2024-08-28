import chainlit as cl
from src.llm import ask_bot


@cl.on_message
async def main(user_message: str): #user_message passing as str
    # Your custom logic goes here...
    response=ask_bot(user_message)

    # Send a response back to the user
    await cl.Message(
        content=f"Received: {response.content}",
    ).send()
