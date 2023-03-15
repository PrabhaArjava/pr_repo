from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#Creates database engine
engine = create_engine('mysql+pymysql://muthu:Prabha5215@aws-rds-db.c6qlau4lseex.ap-south-1.rds.amazonaws.com:3306/dummy')

Base = declarative_base()

SessionLocal = sessionmaker(bind=engine, expire_on_commit=False)
