import firebase_admin
from firebase_admin import credentials, firestore, auth
import os

script_dir = os.path.dirname(__file__)
path_name = os.path.join(
    script_dir, "connectd-beta-firebase-adminsdk-uk7sw-57796ab912.json"
)
cred = credentials.Certificate(path_name)
default_app = firebase_admin.initialize_app(cred)


def create_user(email, password):
    user = auth.create_user(email=email, email_verified=False, password=password)
    print("Sucessfully created new user: {0}".format(user.uid))
    return user


def get_user(uid):
    user = auth.get_user(uid)
    print("Sucessfully fetched user: {0}".format(user.uid))
    return user


def get_user_by_email(email):
    user = auth.get_user_by_email(email)
    print("Sucessfully fetched user: {0}".format(user.uid))
    return user


def verify_id_token(token):
    decoded_token = auth.verify_id_token(token)
    print("Sucessfully verified ID token: {0}".format(decoded_token))
    return decoded_token
