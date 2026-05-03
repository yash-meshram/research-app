from pydantic import BaseModel, Field
from typing import Optional, List, TypedDict, Dict, Any
from datetime import datetime

class ResearchRequest(BaseModel):
    """input we will give"""
    question: str = Field(..., min_length = 10, description = "Research topic or question")
    session_id: Optional[str] = Field(default = None, description = "Pass an existing session_id")
    
class Referance(BaseModel):
    """web search referance we will get from web search"""
    title: str
    url: str
    
class ResearchResponse(BaseModel):
    """final output we will get"""
    session_id: str
    report: str
    referances: List[Referance]
    
class Score(BaseModel):
    """scrores to rank the Referance"""
    relevance_score: float = 0.0             # How directly this source answers the research question (0–10)
    quality_score: float = 0.0               # How detailed and informative the content is (0–10)
    credibility_score: float = 0.0           # How trustworthy the source is (academic/gov = high, forums = low) (0–10)
    total_score: float = 0.0                 # Sum of the three scores above (max 30)
    
class SessionMessage(BaseModel):
    """One Q&A session"""
    message_id: int
    question: str
    embeded_question: List[float]
    response: str
    referances: List[Referance]
    created_at: datetime
    
class SessionDetail(BaseModel):
    """Full session data - contains all the messages"""
    session_id: str
    messages: List[SessionMessage]
    created_at: datetime
    
    
class ResearchState(TypedDict):
    """State for graph"""
    question: str
    embeded_question: List[float]
    current_message_id: int = 0
    session_id: str
    chat_history: List[SessionMessage]
    relevant_prev_message_id: List[int]
    search_queries: List[str]
    raw_search_data: List[Dict[str, Any]]
    # ranked_search_data: List[Dict[str, Any]]
    response: str
    referances: List[Referance]
    next_agent: str
    