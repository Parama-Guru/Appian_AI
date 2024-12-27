import os 
from pydantic import BaseModel
from pydantic import Field
from langgraph.graph import MessagesState
from langchain_core.tools import tool
from langchain_groq import ChatGroq
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.prebuilt import ToolNode
from langchain_core.messages import HumanMessage


def delete_previous_file(save_dir):
    for file_name in os.listdir(save_dir):
        if file_name.endswith('.pdf'):
            os.remove(os.path.join(save_dir, file_name))

class Categorization(BaseModel):
    """Respond to the user with this"""
    summarize_content: str = Field(description="give me a meaningful consise summarization of the document")
    person_name: str = Field(description="Name of the person in the document")
    govertment_id: str = Field(description="Government ID of the person in the document")
    email_address: str = Field(description="Email address of the person in the document")
    type_of_document: str = Field(description=''' the document is of what type, cho0se from the folllowing
                                  credit card,
                                  savings account,
                                  driver's license,
                                  state/country identification,
                                  passport,
                                  income statements/paystubs,
                                  tax returns,
                                  Receipts''')
    

class AgentState(MessagesState):
    final_response:Categorization

@tool
def detect(state: AgentState):
    '''To the detect the required item fro the documents'''
    messages = state['messages']
    question = messages[-1]
    llm=ChatGroq(model_name="Gemma2-9b-It")
    model_with_structured_output = llm.with_structured_output(Categorization)
    return model_with_structured_output.invoke([HumanMessage(content=question)])

@tool
def ocr(self):
    ''' large language model inbuilt with Optical character recognition for generating the output from the diretory'''
    tool = ChatGoogleGenerativeAI(model_name="gemini-1.5-flash")
    tools=[tool]
    self.tool_node=ToolNode(tools)
    self.llm_with_tools=self.model.bind_tools(tools)

def should_continue(state: AgentState):
    messages = state["messages"]
    last_message = messages[-1]
    
    # If there is no function call, then we respond to the user
    if not last_message.tool_calls:
        return "respond"
    # Otherwise if there is, we continue with the tool
    else:
        return "continue"
llm=ChatGroq(model_name="Gemma2-9b-It")
model_with_structured_output = llm.with_structured_output(Categorization)


def call_model(state: AgentState):
    print(f" this is 01 input from call model {state}")
    response = llm.invoke(state['messages'],prompt='give a summary of the ')
    print(f"this is 02 response from call model  {response}")
    # We return a list, because this will get added to the existing list
    return {"messages": [response]}


def respond(state: AgentState):
    print(f"here is 03 state from respond {state}")
    response = model_with_structured_output.invoke([HumanMessage(content=state['messages'][-1].content)])
    # We return the final answer
    print(f"this is 04 response from respond{response}")
    return {"final_response": response}




