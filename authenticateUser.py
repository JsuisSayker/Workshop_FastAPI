import os
from pydantic import SecretStr
from sqlalchemy.orm import Session

from dotenv import load_dotenv

from crud.user.userGet import getUser
from passwordOperations import verifyPassword


load_dotenv()


ACCESS_TOKEN_EXPIRE_MINUTES = os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")


def authenticateUser(db: Session, email: str, password: SecretStr):
    user = getUser(db, email)

    if not verifyPassword(password, user.password):
        return False
    return user


def getAccessToken(db: Session, email: str, password: SecretStr):
    # complete the code to generate an access token and raise an error (404)
    # if the user does not exist
    return Token(access_token=access_token, token_type="bearer")