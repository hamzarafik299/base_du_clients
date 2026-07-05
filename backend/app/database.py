from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Adresse de la base SQLite
DATABASE_URL = "sqlite:///../contacts.db"

# Création du moteur SQLAlchemy
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

# Création des sessions
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Classe de base pour tous les modèles
Base = declarative_base()


# Fonction qui fournit une session à FastAPI
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()