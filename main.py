from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List  # Import the List type
from schemas import ItemCreate, ItemUpdate, ItemResponse, InstitutionCreate, InstitutionUpdate, InstitutionResponse 
from models import Item, Institution
from database import get_db


# FastAPI app instance
app = FastAPI()

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

# API endpoint to create an Institution
@app.post("/institutions/", response_model=InstitutionResponse)
async def create_Institution(institution: InstitutionCreate, db: Session = Depends(get_db)):
	db_Institution = Institution(**institution.dict())
	db.add(db_Institution)
	db.commit()
	db.refresh(db_Institution)
	return db_Institution

# API endpoint to update an Institution by ID
@app.put("/institutions/{Institution_id}", response_model=InstitutionResponse)
async def update_Institution(Institution_id: int, institution: InstitutionUpdate, db: Session = Depends(get_db)):
    updated_Institution = db.query(Institution).filter(institution.id == Institution_id)
    updated_Institution.first()
    if updated_Institution is None:
        raise HTTPException(status_code=404, detail="Institution not found")
    updated_Institution.update(institution.dict(), synchronize_session=False)
    db.commit()
    return updated_Institution.first()  # Refresh and return updated Institution

# API endpoint to read an Institution by ID
@app.get("/institutions/{Institution_id}", response_model=InstitutionResponse)
async def read_Institution(Institution_id: int, db: Session = Depends(get_db)):
	db_Institution = db.query(Institution).filter(Institution.id == Institution_id).first()
	if db_Institution is None:
		raise HTTPException(status_code=404, detail="Institution not found")
	return db_Institution

# API endpoint to retrieve all Institutions
@app.get("/institutions/", response_model=List[InstitutionResponse])
async def read_Institutions(db: Session = Depends(get_db)):
    Institutions = db.query(Institution).all()
    return Institutions

@app.delete("/institutions/{Institution_id}", status_code=204)
async def delete_Institution(Institution_id: int, db: Session = Depends(get_db)):
    db_Institution = db.query(Institution).filter(Institution.id == Institution_id).first()
    if db_Institution is None:
        raise HTTPException(status_code=404, detail="Institution not found")
    db.delete(db_Institution)
    db.commit()
    return 




if __name__ == "__main__":
	import uvicorn

	# Run the FastAPI application using Uvicorn
	uvicorn.run(app, host="127.0.0.1", port=3380)
