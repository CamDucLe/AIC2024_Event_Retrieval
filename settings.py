from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # Indexing parameters
    TEMPERATURE: float = 0.27
    MAX_ANSWER_TOKEN: int = 600
    CLAUDE_MODEL_ID: str = "claude-3-5-sonnet-20240620"
    GPT_MODEL_ID: str = "gpt-4o"
    GEMINI_MODEL_ID: str = "gemini-1.5-pro"
    EMBEDDING_MODEL_ID: str = "text-embedding-3-large"
    TOP_K: int = 5
    COSINE_SIMILARITY: float = 0.8

    # DB
    DB_CONNECTION_STRING: str
    TABLE_ABC: str = "clip_feature"
    TABLE_XYZ: str = "image_caption"

    # Credentials
    OPENAI_API_KEY: str
    GOOGLE_API_KEY: str
