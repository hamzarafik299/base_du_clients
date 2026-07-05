from fastapi import APIRouter, Depends, HTTPException 
from sqlalchemy.orm import Session
from .database import get_db 
from . import crud, schemas

router = APIRouter( prefix="/contacts", tags=["Contacts"] )

#get all the contacts
@router.get("/", response_model=list[schemas.ContactResponse])
def get_contacts(db : Session = Depends(get_db)):
    return crud.get_contacts(db)

#create a contact
@router.post("/", response_model=schemas.ContactResponse)
def create_contact(contact : schemas.ContactCreate , db :Session = Depends(get_db)):
    return crud.create_contact(db , contact)


#recherche  un contact

@router.get("/{id}" , response_model= schemas.ContactResponse)
def read_contact(id : int , db : Session = Depends(get_db)):
    contact = crud.get_contact(db,id)
    if not contact:
        raise HTTPException(
            status_code=404,
            detail="Contact introuvable"
        )
    return contact

#modifier un contact 

@router.put("/{id}", response_model= schemas.ContactResponse)
def modifier_contact(id : int , contact : schemas.ContactUpdate , db : Session = Depends(get_db)):
    new_contact = crud.update_contact(db ,contact, id)
    if not  new_contact:
        raise HTTPException(
            status_code=404,
            detail= "contact introuvable"
        )
    return new_contact

#suuprime contact 
@router.delete("/{id}" , response_model=schemas.ContactResponse)
def supprimer_contact(id : int , db : Session = Depends(get_db)):
    contact = crud.delete_contact(db , id)
    if not contact: 
        raise HTTPException(
            status_code=404,
            detail ="contact introuvable"
        )
    return contact
