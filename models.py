from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

# Database model
class Item(Base):
	__tablename__ = "items"
	id = Column(Integer, primary_key=True, index=True)
	name = Column(String, index=True)
	description = Column(String)


# Database model
class Institution(Base):
	__tablename__ = "institution"
	id = Column(Integer, primary_key=True, index=True)
	name = Column(String, index=True)
	address = Column(String)
	latitude = Column(String)
	longitude = Column(String)
	responsibleUserId = Column(Integer)
	created = Column(String)
	visitTime = Column(String)
	visitDates = Column(String)

	
