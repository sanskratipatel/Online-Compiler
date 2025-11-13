def existing_users_query() -> str: 
    return """ 
        SELECT username , email from  users where email = %(email)s or username = 
         %(username)s
    """


def create_user_query() ->str:
    return """ 
    INSERT INTO users (username,password,email,is_active  , is_verified) VALUES (%(username)s, %(password)s, %(email)s, TRUE, FALSE) 
    RETURNING id

"""