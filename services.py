from langchain_groq import ChatGroq
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.prebuilt import ToolNode
from langchain_core.tools import tool
def model():
    return "everything success"

class Chatbot():
    def __init__(self):
        self.llm=ChatGroq(model_name="Gemma2-9b-It")
        self.model=ChatGroq(model_name="llama-3.3-70b-versatile")


    @tool
    def ocr(self):
        ''' large language model inbuilt with Optical character recognition for generating the output'''
        tool = ChatGoogleGenerativeAI(model_name="gemini-1.5-flash")
        tools=[tool]
        self.tool_node=ToolNode(tools)
        self.llm_with_tools=self.model.bind_tools(tools)

    def __call__(self):
        