from datetime import datetime, timedelta 
from jose import jwt 
from passlib.context import CryptContext

pwd_context = CryptContext( schemes=["bcrypt"], deprecated="auto" )
#bcrypt est un algorithme reconnu et sécurisé pour stocker les mots de passe.
SECRET_KEY = "zxcvbnmasdfghjklqwertyuio1s2f4h" 
ALGORITHM = "HS256" 
ACCESS_TOKEN_EXPIRE_MINUTES = 30