from langchain_community.tools.tavily_search import TavilySearchResults
from config import settings

def _search_tool() -> TavilySearchResults:
    return TavilySearchResults(
        tavily_api_key = settings.TAVILY_API_KEY,
        max_results = settings.TAVILY_MAX_RESULTS
    )
    
def search_tool():
    return _search_tool()