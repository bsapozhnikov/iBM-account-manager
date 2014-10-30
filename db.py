from pymongo import Connection

conn = Connection()

db = conn['iBM-Brian-Michael']

print db.collection_names()


def registerUser(user,name,color,pw):
    x = db.users.find_one({"user":user})
    if x == None && pw != None:
        db.users.insert({"user":user,
                         "name":name,
                         "color":color,
                         "password":pw})
        return True
    else:
        return False

def updateUserInfo(user,pw,newpw,name,color):
    x = db.users.find_one({"user":user})
    if x[password] == pw:
        
    

        
    

#user
#name
#color
#pw

#register
#check if user/pw valid
#update user info
