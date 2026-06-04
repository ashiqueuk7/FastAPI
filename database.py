from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

db_url="postgresql://postgres:777@localhost:5432/fast"
engine=create_engine(db_url)
SessionLocal=sessionmaker(autoflush=False,autocommit=False,bind=engine)