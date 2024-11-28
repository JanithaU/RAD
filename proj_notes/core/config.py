# from dotenv import load_dotenv
import os
# load_dotenv(".env")


def get_database_url():
    """Fetch the correct database URL based on the environment."""
    use_local_db = os.environ.get("USE_LOCAL_DB", "false").lower() == "true"
    if use_local_db:
        return os.environ.get("LOCAL_DATABASE_URL")
    return os.environ.get("DATABASE_URL")


class Settings:
    PROJECT_VERSION: str = os.environ.get("PROJECT_VERSION")
    SECRET_KEY: str = os.environ.get("SECRET_KEY")
    ALGORITHM: str = os.environ.get("ALGORITHM")
    ACCESS_TOKEN_EXPIRE_MINUTES = os.environ.get("ACCESS_TOKEN_EXPIRE_MINUTES")
    aws_access_key_id: str= os.environ.get("aws_access_key_id")
    aws_secret_access_key: str=os.environ.get("aws_secret_access_key")
    region_name: str=os.environ.get("region_name")
    lambda_function: str=os.environ.get("lambda_function")


settings = Settings()