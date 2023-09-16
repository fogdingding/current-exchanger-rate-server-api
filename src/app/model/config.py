from functools import lru_cache
from pydantic import BaseSettings


class Settings(BaseSettings):
    timezone: int = 8
    exchange_rate_table: dict = {
        "currencies": {
            "TWD": {"TWD": 1, "JPY": 3.669, "USD": 0.03281},
            "JPY": {"TWD": 0.26956, "JPY": 1,"USD": 0.00885},
            "USD": {"TWD": 30.444, "JPY": 111.801, "USD": 1}
        }
    }
    # class Config:
    #     env_file = "setting.env"


@lru_cache()
def get_settings():
    return Settings()
