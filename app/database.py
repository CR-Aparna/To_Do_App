import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base
from dotenv import load_dotenv

load_dotenv()

DB_User=os.getenv('DB_USER')
DB_Pass=os.getenv('DB_PASS')
DB_Host=os.getenv('DB_HOST')
DB_Port=os.getenv('DB_PORT')
DB_Name=os.getenv('DB_NAME')

DATABASE_URL = f"mysql+pymysql://{DB_User}:{DB_Pass}@{DB_Host}:{DB_Port}/{DB_Name}"

engine = create_engine(DATABASE_URL,future=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()