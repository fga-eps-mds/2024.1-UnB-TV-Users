import os
from fastapi import Depends, HTTPException
from datetime import datetime, timedelta
from passlib.context import CryptContext
from jose import JWTError, jwt
from fastapi.security import OAuth2PasswordBearer

SECRET_KEY = os.getenv("SECRET")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def verify_password(plain_password, hashed_password) -> bool:
  return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password) -> str:
  return pwd_context.hash(password)

def validate_password(password: str) -> bool:
  return (
    len(password) >= 8 and
    any(ch.islower() for ch in password) and
    any(ch.isupper() for ch in password) and
    any(ch.isdigit() for ch in password) and
    any(ch in "!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~" for ch in password)
  )

def create_access_token(data: dict):
  access_token_expires = timedelta(minutes=int(ACCESS_TOKEN_EXPIRE_MINUTES))

  to_encode = data.copy()
  if access_token_expires:
     expire = datetime.utcnow() + access_token_expires
  else:
     expire = datetime.utcnow() + timedelta(minutes=15)
  
  to_encode.update({"exp": expire})
  encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
  return encoded_jwt

def verify_token(token: str = Depends(oauth2_scheme)):
  try:
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    return payload
  except JWTError:
    raise HTTPException(status_code=401, detail="Invalid token")
