from pydantic_settings import BaseSettings
from pydantic import Field

class Settings(BaseSettings):
    ebay_api_host: str = Field(..., env="EBAY_API_HOST")
    ebay_api_port: int = Field(..., env="EBAY_API_PORT")

settings = Settings()
