import os

from dotenv import load_dotenv

load_dotenv()


class Settings:

    DATABASE_URL = os.getenv(
        "DATABASE_URL"
    )

    SECRET_KEY = os.getenv(
        "SECRET_KEY"
    )

    ALGORITHM = os.getenv(
        "ALGORITHM"
    )

    ACCESS_TOKEN_EXPIRE_MINUTES = int(
        os.getenv(
            "ACCESS_TOKEN_EXPIRE_MINUTES"
        )
    )

    MAIL_USERNAME = os.getenv(
        "MAIL_USERNAME"
    )

    MAIL_PASSWORD = os.getenv(
        "MAIL_PASSWORD"
    )

    MAIL_FROM = os.getenv(
        "MAIL_FROM"
    )

    MAIL_PORT = int(
        os.getenv(
            "MAIL_PORT"
        )
    )

    MAIL_SERVER = os.getenv(
        "MAIL_SERVER"
    )

    MAIL_FROM_NAME = os.getenv(
        "MAIL_FROM_NAME"
    )


settings = Settings()