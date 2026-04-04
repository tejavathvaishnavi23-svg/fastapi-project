from pydantic_settings import BaseSettings, SettingsConfiDict

class Settings(BaseSettings):
    model_config = SettingsConfiDict(env_file=".env", extra="ignore")

    DB_CONNECTION:str


settings = Settings()