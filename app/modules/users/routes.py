# app/
# ├── main.py
# ├── database.py
# └── modules/
#     └── users/
#         ├── routes.py
#         ├── queries.py
#         ├── requests.py
#         ├── responses.py
#         ├── utils.py
#         ├── __init__.py



# from psycopg import AsyncConnection
# from utils.logger import logger


from sqlite3 import Connection
from fastapi import APIRouter, HTTPException , Depends 
from .response import UserSignupResponse
from .requests import UserSignupRequests,UsersLoginRequests
from app.database import get_db_connection, execute_sql
from .query import existing_users_query
from app.utils.hash_password import hash_password

router  = APIRouter(prefix = "/users" , tags = ["Users"]) 


@router.post("/signup", response_model =UserSignupResponse ) 
async def signup_user( 
    requests : UserSignupRequests,  
    connection : Connection = Depends(get_db_connection)
):
    try : 
        existing_users = execute_sql ( 
             existing_users_query() , 
             connection:connection , 
             params={"email": requests.email , "username" : requests.username}, 
             fetchone=True, 
             raise_error=True,
             rollback_on_error=False
         )
        if existing_users : 
            if existing_users["email"] == requests.email:
                raise HTTPException(status_code = 400 , detail = f"Email Alreaady Exists. Please Log in ")
            if existing_users["username"] == requests.username: 
                raise HTTPException(status_code =400 , detail = f"Username Already Exists. Please Choose Another.")
        hashed_pwd = hash_password(requests.password) 

        create_user = execute_sql( 
            
        )

    except Exception as e : 
        raise HTTPException ( status_code = 500 , detail= f"Internal Server Error {str(e)}")