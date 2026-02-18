from langchain_openai import ChatOpenAI
from app.core.config import settings

def get_llm():
    if settings.LLM_PROVIDER == "openai":
        return ChatOpenAI(
            model = "gpt-4o-mini",
            temperature = 0,
            openai_api_key = settings.OPENAI_API_KEY,
        )
    else:
        raise ValueError("Unsupported LLM")