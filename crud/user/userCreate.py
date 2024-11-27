from crud.user.userGet import getUser
from database.tableRelationship import User
from sqlalchemy.orm import Session


def createUser(db: Session, email: str, password: str) -> User | None:
    is_user_already_registered = getUser(db, email)
    if is_user_already_registered:
        return None
    user = User(email=email, hashed_password=password)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
