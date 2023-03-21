from pydantic import BaseSettings


class Settings(BaseSettings):
    host: str = '0.0.0.0'
    port: int = 5873
    backend_url: str = "carprices_backend"
    dash_login: str
    dash_password: str
    notify_auto_close_time: int = 2500
    debug_mode: bool = False


settings = Settings(
    _env_file=".env",
    _env_file_encoding="utf-8"
)
