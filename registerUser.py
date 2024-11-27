from fastapi import HTTPException
from sqlalchemy.orm import Session
from pydantic import SecretStr

from crud.user.userCreate import createUser
from passwordOperations import getPasswordHash


def registerNewUser(db: Session, email: str, password: SecretStr):
    # complete the code to register a user and return a message when successful
    # and raise an HTTPException when the user is already registered (400)
    return {"message": "User created successfully"}
