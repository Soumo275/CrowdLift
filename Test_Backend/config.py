from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    SECRET_KEY: str = "dAytE3tEgU9niRMeblMrzDshGGGJEMup"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    MONGODB_URL: str = "mongodb://localhost:27017"
    DATABASE_NAME: str = "crowdfunding_db"

settings = Settings()