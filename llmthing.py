import dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage


dotenv.load_dotenv()

def get_def(word):
    chat = ChatOpenAI(model="gpt-3.5-turbo-1106", temperature=0.2)
    output = chat.invoke(
        [
            HumanMessage(
                content=f"Give the definition of this word: {word} in coding and AI terms"
            )
        ]
    ).content
    return (output)