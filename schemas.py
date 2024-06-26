from pydantic import BaseModel as PydanticBaseModel
from typing import List  # Import the List type

class BaseModel(PydanticBaseModel):
	class Config:
		orm_mode = True

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
	id: int
	name: str
	email: str
	cnpj: str
	password: str
	
# Pydantic model for request data
class InstitutionUpdate(BaseModel):
	id: int
	name: str
	email: str
	cnpj: str
	password: str

# Pydantic model for response data
class InstitutionResponse(BaseModel):
	id: int
	name: str
	email: str
	cnpj: str
	password: str
	
class UserCreate(BaseModel):
	name: str
	email: str
	username: str
	password: str 
	isInstitution: bool = False
	cnpj: str  = ""
	
# Pydantic model for request data
class UserUpdate(BaseModel):
	name: str
	email: str
	username: str
	password: str

# Pydantic model for response data
class UserResponse(BaseModel):
	id: int
	name: str
	email: str
	username: str
	isInstitution: bool
	cnpj: str

	
class CommentCreate(BaseModel):
	userId: int
	comment: str
	postId: int
	
# Pydantic model for request data
class CommentUpdate(BaseModel):
	userId: int
	comment: str
	postId: int
	timeStamp: str

# Pydantic model for response data
class CommentResponse(BaseModel):
	id: int
	userId: int
	comment: str
	postId: int
	timeStamp: str
	user: UserResponse
	
class PostCreate(BaseModel):
	userId: int
	text: str
	title: str
	imgLink: str
	
# Pydantic model for request data
class PostUpdate(BaseModel):
	userId: int
	text: str
	title: str
	institutionId: int
	timeStamp: str
	imgLink: str

class PostLikesCreate(BaseModel):
	userId: int
	postId: int
	
# Pydantic model for request data
class PostLikesUpdate(BaseModel):
	userId: int
	postId: int

# Pydantic model for response data
class PostLikesResponse(BaseModel):
	id: int
	userId: int
	postId: int
	timeStamp: str

# Pydantic model for response data
class PostResponse(BaseModel):
	id: int
	userId: int
	text: str
	title: str
	institutionId: int
	timeStamp: str
	imgLink: str
	user: UserResponse
	comments: List[CommentResponse]
	likes: List[PostLikesResponse]
	
class UserFavoritesCreate(BaseModel):
	userId: int
	InstitutionId: int
	
# Pydantic model for request data
class UserFavoritesUpdate(BaseModel):
	userId: int
	InstitutionId: int

# Pydantic model for response data
class UserFavoritesResponse(BaseModel):
	id: int
	userId: int
	InstitutionId: int
	
class UserCompleteResponse(BaseModel):
	id: int
	name: str
	email: str
	username: str
	isInstitution: bool
	cnpj: str
	posts: List[PostResponse]
	posts: List[PostResponse]
	comments: List[CommentResponse]
	likes: List[PostLikesResponse]