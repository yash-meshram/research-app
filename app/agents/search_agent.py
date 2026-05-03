from app.schemas.schemas import ResearchState, Referance
# from app.services.llm import llm
from app.services.websearch import search_tool
from app.services.embedding import get_embedding, get_similarity_score
from typing import List, Dict

# llm = llm(temperature = 0.3)
web_search_tool = search_tool()

def search_agent(state: ResearchState):
    """will generate different queries for search and then will search the web"""
    question = state["question"]
    embeded_question = get_embedding(query = question)
    state["embeded_question"] = embeded_question
    
    chat_history = state["chat_history"]
    
    prev_questions_high: List[int] = []
    prev_questions_medium: List[int] = []
    
    if chat_history:
        state["current_message_id"] = chat_history[-1].message_id + 1
        
        similarity_scores: Dict[int, float] = get_similarity_score(embeded_query = embeded_question, chat_history = chat_history)
    
        for message_id, score in similarity_scores.items():
            if score > 0.9:
                prev_questions_high.append(message_id)
            elif score > 0.75:
                prev_questions_medium.append(message_id)
    
    if prev_questions_high:
        # return prev response
        response = ""
        references: List[Referance] = []
        for message_id in prev_questions_high:
            response += f"\n\n{chat_history[message_id].response}"
            
            for ref in chat_history[message_id].referances:
                references.append(ref)            
        
        state["response"] = response
        state["referances"] = references
        state["next_agent"] = "end"
    
    elif prev_questions_medium:
        # store prev conversation and call writter agent, skip ranker agent
       state["relevant_prev_message_id"] = prev_questions_medium
       state["next_agent"] = "writter"
    
    else:
        # do web search
        results = web_search_tool.invoke(question)
        relevant_results = [result for result in results if result['score'] > 0.9]
        
        state["raw_search_data"] = relevant_results
        
        state["next_agent"] = "writter"
        
    return state["next_agent"]