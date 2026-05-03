from config import settings
from sentence_transformers import SentenceTransformer, util
from typing import List, Dict
from app.schemas.schemas import SessionMessage

embedding_model = SentenceTransformer(settings.EMBEDDING_MODEL)

def get_embedding(query: str) -> List[float]:
    return embedding_model.encode(query, convert_to_tensor = True)

def get_similarity_score(embeded_query: List[float], chat_history: List[SessionMessage]) -> Dict[int, float]:
    scores: Dict[int, float] = {}
    
    for message in chat_history:
        score = util.cos_sim(embeded_query, message.embeded_question)
        scores[message.message_id] = score.item()
    
    return scores