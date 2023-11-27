from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "DESKTOP-U46HO21;Initial Catalog=CLINICA_DB;Integrated Security=True;"

engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

#Apagar todas as tabelas
#Base.metadata.drop_all(engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()