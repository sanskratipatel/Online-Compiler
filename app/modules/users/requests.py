from pydantic import BaseModel ,Field,EmailStr

class UserSignupRequests(BaseModel) :
    username : str = Field(..., min_length =3 )
    password :str = Field(...,min_length = 4)
    email : EmailStr 


class UsersLoginRequests(BaseModel) : 
    email : EmailStr 
    password : str  
    