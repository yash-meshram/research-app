from langchain_groq.chat_models import ChatGroq
from config import settings

def _llm(temperature: float = 0.0) -> ChatGroq:
    return ChatGroq(
        api_key = settings.GROQ_API_KEY,
        model = settings.GROQ_MODEL,
        temperature = temperature
    )
    
def llm(temperature: float = 0.0):
    return _llm(temperature = temperature)