# BaseSettings auto-reads values from a .env file into a Python class
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # LLM
    GROQ_API_KEY: str
    GROQ_MODEL: str
    
    # Tavily
    TAVILY_API_KEY: str
    TAVILY_MAX_RESULTS: int
    
    # Database
    MONGODB_ATLAS_CLUSTER_URI: str
    MONGODB_ATLAS_DB: str
    
    # LangSmith
    LANGCHAIN_API_KEY: str
    LANGSMITH_PROJECT: str
    LANGSMITH_TRACING: bool
    
    # API
    API_BASE_URL: str
    
    # Inner class that tells pydantic-settings HOW to load the values
    class Config:
        env_file = ".env"
        extra = "ignore"

settings = Settings()

def configure_tracing() -> None:
    """Activate Langsmith tracing when API key is given and tracing is set as true"""
    
    if settings.LANGCHAIN_API_KEY and settings.LANGSMITH_TRACING:
        print(f"[Tracing] LangSmith enable. Project - {settings.LANGSMITH_PROJECT}")
    else:
        print("[Tracing] LangSmith not configured. Set LANGCHAIN_API_KEY and LANGSMITH_TRACING as True")