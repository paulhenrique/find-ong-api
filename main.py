from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from pydantic import BaseModel
from typing import List  # Import the List type

# FastAPI app instance
app = FastAPI()

# Database setup
DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


# Database model
class Item(Base):
	__tablename__ = "items"
	id = Column(Integer, primary_key=True, index=True)
	name = Column(String, index=True)
	description = Column(String)


# Create tables
Base.metadata.create_all(bind=engine)

# Dependency to get the database session
def get_db():
	db = SessionLocal()
	try:
		yield db
	finally:
		db.close()

# Pydantic model for request data
class ItemCreate(BaseModel):
	name: str
	description: str
	
# Pydantic model for request data
class ItemUpdate(BaseModel):
	name: str
	description: str

# Pydantic model for response data
class ItemResponse(BaseModel):
	id: int
	name: str
	description: str

# API endpoint to create an item
@app.post("/items/", response_model=ItemResponse)
async def create_item(item: ItemCreate, db: Session = Depends(get_db)):
	db_item = Item(**item.dict())
	db.add(db_item)
	db.commit()
	db.refresh(db_item)
	return db_item

# API endpoint to update an item by ID
@app.put("/items/{item_id}", response_model=ItemResponse)
async def update_item(item_id: int, item: ItemUpdate, db: Session = Depends(get_db)):
    updated_item = db.query(Item).filter(Item.id == item_id)
    updated_item.first()
    if updated_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    updated_item.update(item.dict(), synchronize_session=False)
    db.commit()
    return updated_item.first()  # Refresh and return updated item

# API endpoint to read an item by ID
@app.get("/items/{item_id}", response_model=ItemResponse)
async def read_item(item_id: int, db: Session = Depends(get_db)):
	db_item = db.query(Item).filter(Item.id == item_id).first()
	if db_item is None:
		raise HTTPException(status_code=404, detail="Item not found")
	return db_item

# API endpoint to retrieve all items
@app.get("/items/", response_model=List[ItemResponse])
async def read_items(db: Session = Depends(get_db)):
    items = db.query(Item).all()
    return items

@app.delete("/items/{item_id}", status_code=204)
async def delete_item(item_id: int, db: Session = Depends(get_db)):
    db_item = db.query(Item).filter(Item.id == item_id).first()
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    db.delete(db_item)
    db.commit()
    return 

if __name__ == "__main__":
	import uvicorn

	# Run the FastAPI application using Uvicorn
	uvicorn.run(app, host="127.0.0.1", port=8000)
