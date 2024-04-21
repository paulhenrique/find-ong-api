from pydantic import BaseModel

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


# Pydantic model for request data
class InstitutionCreate(BaseModel):
	name: str
	address: str
	latitude: str
	longitude: str
	responsibleUserId: int
	created: str
	visitTime: str
	visitDates: str
	
# Pydantic model for request data
class InstitutionUpdate(BaseModel):
	name: str
	address: str
	latitude: str
	longitude: str
	responsibleUserId: int
	created: str
	visitTime: str
	visitDates: str

# Pydantic model for response data
class InstitutionResponse(BaseModel):
	id: int
	name: str
	address: str
	latitude: str
	longitude: str
	responsibleUserId: int
	created: str
	visitTime: str
	visitDates: str
	
class UserCreate(BaseModel):
	name: str
	email: str
	socialUid: str
	
# Pydantic model for request data
class UserUpdate(BaseModel):
	name: str
	email: str
	socialUid: str

# Pydantic model for response data
class UserResponse(BaseModel):
	id: int
	name: str
	email: str
	socialUid: str