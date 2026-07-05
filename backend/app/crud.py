from sqlalchemy.orm import Session

from . import models, schemas


#get all the contacts 
def get_contacts(db: Session):
    return db.query(models.Contact).all()

#create a new contact
def create_contact(db: Session, contact: schemas.ContactCreate):

    db_contact = models.Contact(
        nom=contact.nom,
        categorie=contact.categorie,
        telephone=contact.telephone,
        service=contact.service
    )

    db.add(db_contact)

    db.commit()

    db.refresh(db_contact)

    return db_contact

#search a contact 
def get_contact(db : Session , contact_id : int ) :
    return db.query(models.Contact).filter(models.Contact.id == contact_id).first()

#Update contact 
def update_contact(db : Session , contact : schemas.ContactUpdate , contact_id : int):
    db_contact = get_contact(db ,contact_id )
    if not db_contact:
        return None
    db_contact.nom = contact.nom
    db_contact.categorie = contact.categorie
    db_contact.telephone = contact.telephone
    db_contact.service = contact.service
    db.commit()
    db.refresh(db_contact)
    return db_contact

#delet contact 
def delete_contact(db : Session , contact_id : int):
    db_contact = db_contact = get_contact(db ,contact_id )
    if not db_contact: 
        return None
    db.delete(db_contact)
    db.commit()
    return db_contact