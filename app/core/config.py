from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # These must match the variable names in your .env file
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    POSTGRES_HOST: str
    POSTGRES_PORT: int

    # This is the new way (Pydantic v2) to specify the .env file
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",  # Ignores extra variables in the .env file
    )

    @property
    def database_url(self) -> str:
        """
        Generates the full database connection string.
        """
        return (
            f"postgresql+psycopg2://"
            f"{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@"
            f"{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/"
            f"{self.POSTGRES_DB}"
        )


# Create a single, globally-used instance of the settings
settings = Settings()
