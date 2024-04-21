from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List  # Import the List type
from schemas import ItemCreate, ItemUpdate, ItemResponse, InstitutionCreate, InstitutionUpdate, InstitutionResponse, UserCreate, UserResponse, UserUpdate 
from models import Item, Institution, User
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

# CRUD DE INSTITUIÇÕES

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

# CRUD DE USUÁRIOS

# API endpoint to create an user
@app.post("/users/", response_model=UserResponse)
async def create_user(user: UserCreate, db: Session = Depends(get_db)):
	db_user = User(**user.dict())
	db.add(db_user)
	db.commit()
	db.refresh(db_user)
	return db_user

# API endpoint to update an user by ID
@app.put("/users/{user_id}", response_model=UserResponse)
async def update_user(user_id: int, user: UserUpdate, db: Session = Depends(get_db)):
    updated_user = db.query(User).filter(User.id == user_id)
    updated_user.first()
    if updated_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    updated_user.update(user.dict(), synchronize_session=False)
    db.commit()
    return updated_user.first()  # Refresh and return updated user

# API endpoint to read an user by ID
@app.get("/users/{user_id}", response_model=UserResponse)
async def read_user(user_id: int, db: Session = Depends(get_db)):
	db_user = db.query(User).filter(User.id == user_id).first()
	if db_user is None:
		raise HTTPException(status_code=404, detail="User not found")
	return db_user

# API endpoint to retrieve all users
@app.get("/users/", response_model=List[UserResponse])
async def read_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return users

@app.delete("/users/{user_id}", status_code=204)
async def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(db_user)
    db.commit()
    return 



if __name__ == "__main__":
	import uvicorn

	# Run the FastAPI application using Uvicorn
	uvicorn.run(app, host="127.0.0.1", port=3380)
