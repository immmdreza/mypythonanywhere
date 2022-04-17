from dotenv import load_dotenv  # type: ignore
import os


def load_account_details_from_env():
    load_dotenv()

    username = os.getenv('PYTHONANYWHERE_USERNAME')
    if not username:
        raise ValueError('USERNAME is not set in the environment')
    token = os.getenv('PYTHONANYWHERE_TOKEN')
    if not token:
        raise ValueError('TOKEN is not set in the environment')
    account_type = os.getenv('PYTHONANYWHERE_ACCOUNT_TYPE')
    if not account_type:
        raise ValueError('ACCOUNT_TYPE is not set in the environment')

    return username, token, int(account_type)
