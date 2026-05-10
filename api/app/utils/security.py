import jwt
from passlib.context import CryptContext
from datetime import timezone, datetime, timedelta


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def check_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def add_token(uid:int, time, secret)->str:
    expire_time = datetime.now(timezone.utc) + timedelta(minutes=time)
    payload = {'uid': f'{uid}', 'exp': expire_time}
    return jwt.encode(payload, secret, algorithm='HS256')

def get_uid_by_token(token:str, secret)->int | None:
    try:
        payload = jwt.decode(token, secret, algorithms=['HS256'])
        return int(payload['uid'])
    except (jwt.PyJWTError, ValueError, KeyError) as e:
        print(e)
        return None