from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "Rakshak.AI"
    VERSION: str = "0.1.0"
    
    HOST: str = "0.0.0.0"
    PORT: int = 8000
    RELOAD: bool = True
    
    NEO4J_URI: str = "bolt://localhost:7687"
    NEO4J_USER: str = "neo4j"
    NEO4J_PASSWORD: str = "cnipassword123"
    
    OPENAI_API_KEY: str = ""
    
    class Config:
        env_file = ".env"

settings = Settings()
