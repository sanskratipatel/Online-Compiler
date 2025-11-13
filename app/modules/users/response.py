
from pydantic import BaseModel
class UserSignupResponse(BaseModel) :
    message :str 
    user_id : int 
    email :str 

    