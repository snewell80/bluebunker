from pymongo.collection import T
import bcrypt
import config
from enums import UserType

userCollection = config.userCollection


def register(username, password):
    try:
        if not UserExists(username):
            salt = bcrypt.gensalt()
            hashedpw = bcrypt.hashpw(password.encode('utf-8'), salt)
            userCollection.insert_one({
                "username":username,
                "salt": salt,
                "password": hashedpw,
                "userType": UserType.User,
                "isActive": True,
                "chagnePassword": False
            })
            #TODO log the user creation return user to sig on page
        else:
            print("User already registered")
    except Exception as e:
        #TODO log exception return error message to user  
        print(e)

def authenticate(username, password):
    user = userCollection.find_one({"username": username})
    if user:
        salt = user["salt"]
        pwHash = user["password"]
        if bcrypt.checkpw(password.encode('utf-8'), pwHash):
            print('login successful')
            return True
        else:
            print('Login failed')
            return False
    else:
        print('User not foun dplease register')
        return False

def UserExists(username):
    if config.userCollection.find_one({"username": username}):
        print(username)
        print(userCollection.find({"username": username}))
        return True
    else:
        return False


#Register example usage
#register("testuser", "securepassword123")
#Authenticate example usage
authenticate("testuser", "securepassword123")
authenticate("testuser", "wrongpassword")