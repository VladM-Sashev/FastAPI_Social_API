from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    database_username: str
    database_hostname: str
    database_password: str
    database_port: int
    database_name: str

    access_token_time: int
    secret_key: str
    algorithm: str

    model_config = SettingsConfigDict(
        env_file=".env"
    )


settings = Settings()

