from utils import AgentState,ocr,call_model,respond
from langgraph.prebuilt import ToolNode
from langgraph.graph import StateGraph,END
from utils import should_continue
from connect_mongo import connect_mongo
def model():
    return "everything sucess"
def ingestion(result):
    db=connect_mongo()
    collection=db.list_collection_names()
    if result['type_document'] not in collection:
        db.create_collection(result['type_document'])
        db[result['type_document']].insert_one(result)
    else:
        db[result['type_document']].insert_one(result)

def model1():
    workflow = StateGraph(AgentState)
    tools=[ocr()]
    workflow.add_node("llm", call_model)
    workflow.add_node("tools", ToolNode(tools))
    workflow.add_node("respond", respond)

    workflow.set_entry_point("llm")

    workflow.add_conditional_edges(
        "llm",
    
        should_continue,
        {
            "continue": "tools",
            "respond": "respond",
        },
    )

    workflow.add_edge("tools", "respond")
    workflow.add_edge("respond", END)
    graph = workflow.compile()
    return graph


def preprocessed_data():
    
    return 