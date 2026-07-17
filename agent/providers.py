
import os
from typing import Optional
from pydantic_ai.providers.openai import OpenAIProvider
from pydantic_ai.models.openai import OpenAIChatModel, OpenAIResponsesModel
import openai
from dotenv import load_dotenv


load_dotenv()


def get_openai_base_url() -> Optional[str]:
    """Return the OpenAI-compatible API base URL, if configured."""
    return (
        os.getenv("OPENAI_BASE_URL")
        or os.getenv("LLM_BASE_URL")
        or os.getenv("BASE_URL")
        or os.getenv("base_url")
    )


def get_openai_api_key() -> Optional[str]:
    """Return the API key for OpenAI-compatible providers."""
    return (
        os.getenv("OPENAI_API_KEY")
        or os.getenv("LLM_API_KEY")
        or os.getenv("API_KEY")
        or os.getenv("api_key")
    )


def get_embedding_base_url() -> Optional[str]:
    """Return the embedding API base URL, falling back to the LLM base URL."""
    return os.getenv("EMBEDDING_BASE_URL") or get_openai_base_url()


def get_embedding_api_key() -> Optional[str]:
    """Return the embedding API key, falling back to the LLM API key."""
    return (
        os.getenv("EMBEDDING_API_KEY")
        or os.getenv("EMBEDDING_OPENAI_API_KEY")
        or get_openai_api_key()
    )


def get_openai_api_mode() -> str:
    """Return the OpenAI-compatible API mode: chat or responses."""
    return os.getenv("OPENAI_API_MODE", os.getenv("LLM_API_MODE", "chat")).strip().lower()


def get_llm_model(model_choice: Optional[str] = None) -> OpenAIChatModel | OpenAIResponsesModel:
    """
    Get LLM model configuration based on environment variables.
    
    Args:
        model_choice: Optional override for model choice
    
    Returns:
        Configured OpenAI-compatible model
    """
    llm_choice = model_choice or os.getenv('LLM_CHOICE', 'gpt-4-turbo-preview')
    api_key = get_openai_api_key()
    base_url = get_openai_base_url()

    provider = OpenAIProvider(api_key=api_key, base_url=base_url)
    if get_openai_api_mode() == "responses":
        return OpenAIResponsesModel(llm_choice, provider=provider)

    return OpenAIChatModel(llm_choice, provider=provider)


def get_embedding_client() -> openai.AsyncOpenAI:
    """
    Get embedding client configuration based on environment variables.
    
    Returns:
        Configured OpenAI-compatible client for embeddings
    """
    api_key = get_embedding_api_key()
    base_url = get_embedding_base_url()
    
    return openai.AsyncOpenAI(
        api_key=api_key,
        base_url=base_url
    )


def get_embedding_model() -> str:
    """
    Get embedding model name from environment.
    
    Returns:
        Embedding model name
    """
    return os.getenv('EMBEDDING_MODEL', 'text-embedding-3-small')
