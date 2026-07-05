from pydantic import BaseModel 


class ContactBase(BaseModel):
    nom : str
    categorie : str
    telephone :str
    service :str
    
class ContactCreate(ContactBase):
    pass
class ContactUpdate(ContactBase):
    pass
class ContactResponse(ContactBase):
    id : int 
    class config:
        from_attributes = True
class UserBase(BaseModel):
    username : str
    
class UserCreate(UserBase):
    password : str
    
class UserLogin(UserBase):
    password : str
    
class Token(BaseModel):
    access_token: str 
    token_type: str