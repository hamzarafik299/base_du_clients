from sqlalchemy import Column , Integer , String
from .database import Base
class Contact(Base):
    __tablename__="contacts"
    id = Column(Integer, primary_key=True, index=True)
    nom = Column(String , nullable = False)
    categorie = Column(String , nullable = False)
    telephone = Column ( String  , nullable= False)
    service = Column (String , nullable = False)
class User(Base):
    __tablename__="users"
    id=Column(Integer , primary_key = True , index= True)
    username = Column(String, unique=True, nullable=False)
    password = Column(String , nullable=False)
    