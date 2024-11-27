from sqlalchemy.orm import Session
from fastapi import APIRouter, Body, Depends
from pydantic import SecretStr

from authenticateUser import getAccessToken
from database.database import get_db
from registerUser import registerNewUser
# from schemas.tokenSchemas import Token

router = APIRouter()


@router.post("/login",
             tags=["auth"],
             response_model=Token)
def loginForAccessToken(
    db: Session = Depends(get_db),
    email: str = Body(...),
    password: SecretStr = Body(...),
) -> Token:
    return getAccessToken(db, email, password)


@router.post("/register",
             tags=["auth"],
             response_model=dict)
def registerUser(
    db: Session = Depends(get_db),
    email: str = Body(...),
    password: SecretStr = Body(...),
) -> dict:
    return registerNewUser(db, email, password)
