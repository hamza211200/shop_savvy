from .models import Profile
import json
import jwt
import datetime
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from django.conf import settings

def get_user(request):
    return list(Profile.objects.values('phone','address','email', "username", "first_name", "last_name"))

def get_user_id(request,user_id):
    user = Profile.objects.filter(id=user_id).values('phone','address','email', "username", "first_name", "last_name").first()
    if user :
        return{"user":user}
    else:
        return {"message": f"{user_id} not found in the data base"}
    
def add_user(request):
    data = json.loads(request.body)
    hashed = make_password(data.get("password"))
    Profile.objects.create(username=data.get("username"), password=hashed,
    phone=data.get("phone"),address=data.get("address"),email =data.get("email"),first_name=data.get('first_name'),last_name=data.get('last_name'))
    return {"message":"user is added successfully."}

def login_user(request):
        try:
            data = json.loads(request.body)
            username = data.get("username")
            password = data.get("password")

            user = authenticate(username=username, password=password)
            if user is not None:
                payload = {
                    "user_id": user.id,
                    "user_email": user.username,
                    "exp": datetime.datetime.utcnow() + datetime.timedelta(seconds=settings.JWT_EXP_DELTA_SECONDS),
                    "iat": datetime.datetime.utcnow(),
                }
                token = jwt.encode(payload, settings.JWT_SECRET, algorithm=settings.JWT_ALGORITHM)

                return {"token": token}
            else:
                return {"error": "Invalid credentials"}

        except Exception as e:
            return {"error": str(e)}

def update_user(request):
    try:
        user = Profile.objects.get(id=request.user_id)
    except Profile.DoesNotExist:
        return {"error":f"this is not present in the {request.user_id}"}
    
    data =json.loads(request.body)

    user.phone = data.get('phone')
    user.address = data.get('address')
    user.username = data.get('username')
    user.first_name = data.get('first_name')
    user.last_name = data.get('last_name')
    user.save()
    return {"message":"user is updated successfully"}

def change_user_password(request):    
    data =json.loads(request.body)

    auth = authenticate(username=request.user_email, password=data.get('old_password'))
    if auth is not None:
        if(data.get('new_password') == data.get('confirm_password')):
            auth.set_password(data.get('new_password'))
            auth.save()
            return {"message":"password changed successfully"}
        else:
            return {"message":"password mismatched."}
    else:
        return {"message":"Incorrect password"}
