from flask import jsonify
from os import environ
from flask_restful import Resource, reqparse
from models.user import UserModel
from sqlalchemy.exc import SQLAlchemyError
from werkzeug.security import safe_str_cmp, check_password_hash, generate_password_hash
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    jwt_required,
    create_access_token,
    get_jwt_identity,
    set_access_cookies,
    set_refresh_cookies,
    unset_jwt_cookies,
    get_csrf_token,
)
# from flask_mail import Message
# from mail import mail
import random
import string


class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        "first_name", type=str, required=True, help="First name is required."
    )
    parser.add_argument(
        "last_name", type=str, required=True, help="Last name is required."
    )
    parser.add_argument("email", type=str, required=True, help="Email is required.")
    parser.add_argument(
        "password", type=str, required=True, help="Password is required."
    )
    parser.add_argument(
        "phone", type=str, required=True, help="Phonenumber is required."
    )

    def post(self):
        data = UserRegister.parser.parse_args()
        if UserModel.find_by_email(data["email"]):
            print(data["email"] + " does already exist.")
            return {"message": "User does alredy exist"}, 409
        else:
            user = UserModel(**data)
            try:
                user.save_to_db()

            except SQLAlchemyError as e:
                error = str(e.__dict__["orig"])
                return error, 500

            print(user.email + " is registered")
            return {"registered": True}, 201


# class EmailValidation(Resource):
#     parser = reqparse.RequestParser()
#     parser.add_argument("email", type=str, required=True, help="Email is required.")

#     def post(self):
#         data = EmailValidation.parser.parse_args()
#         if UserModel.find_by_email(data["email"]):
#             print("User exists")
#             return {"message": "User does alredy exist"}, 409

#         return {"message": "User name is not taken."}, 200


class User(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        "first_name", type=str, required=True, help="First name is required."
    )
    parser.add_argument(
        "last_name", type=str, required=True, help="Last name is required."
    )
    parser.add_argument("email", type=str, required=True, help="Email is required.")

    parser.add_argument(
        "phone", type=str, required=True, help="Phonenumber is required."
    )

    @jwt_required
    def get(self):
        user = UserModel.find_by_email(get_jwt_identity())
        if not user:
            return {"message": "User not found"}, 404

        print(user.email)

        if user.admin:
            return user.adminJson()

        return user.json()

    @jwt_required
    def put(self):
        data = User.parser.parse_args()
        print(data)
        user = UserModel.find_by_email(get_jwt_identity())
        if not user:
            return {"message": "User not found"}, 404

        user.first_name = data["first_name"]
        user.last_name = data["last_name"]
        user.email = data["email"]
        user.phone = data["phone"]

        user.save_to_db()

        return user.json(), 200


class UserLogin(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("email", type=str, required=True, help="Email is required.")
    parser.add_argument(
        "password", type=str, required=True, help="Password is required."
    )

    def post(self):
        data = self.parser.parse_args()

        if data["email"] == "" or data["password"] == "":
            return {"message": "Invalid credentials"}, 401

        user = UserModel.find_by_email(data["email"])

        if user and check_password_hash(user.password, data["password"]):
            print(user.email)
            access_token = create_access_token(identity=user.email)
            refresh_token = create_refresh_token(identity=user.email)
            if user.admin:
                resp = jsonify(
                    {
                        "login": True,
                        "admin": True,
                        "email": user.email,
                        "phone": user.phone,
                        "first_name": user.first_name,
                        "last_name": user.last_name,
                    }
                )
            else:
                resp = jsonify(
                    {
                        "login": True,
                        "email": user.email,
                        "phone": user.phone,
                        "first_name": user.first_name,
                        "last_name": user.last_name,
                    }
                )

            set_access_cookies(resp, access_token)
            set_refresh_cookies(resp, refresh_token)
            resp.status_code = 200
            return resp

        return {"message": "Invalid credentials"}, 401


class UserLogout(Resource):
    def post(self):
        resp = jsonify({"login": False})
        unset_jwt_cookies(resp)
        resp.status_code = 200

        return resp


# class Refresh(Resource):
#     @jwt_refresh_token_required
#     def post(self):
#         current_user = get_jwt_identity()
#         access_token = create_access_token(identity=current_user)

#         resp = jsonify({"refresh": True})
#         set_access_cookies(resp, access_token)
#         resp.status_code = 200
#         return resp


# class SendConfirmationMail(Resource):
#     @jwt_required
#     def post(self):
#         user = UserModel.find_by_email(get_jwt_identity())
#         if not user:
#             return {'message': 'User does not exist'}

#         if not user.admin:
#             return {"message": "Permission denied."}, 401

#         user.confirmation_code = random.randint(1000, 9999)
#         user.confirmation_tries = 0
#         user.save_to_db()

#         msg = Message('Verifiera ditt konto', sender = 'admin@kvillebackenif.se', recipients = [user.email])
#         msg.body = 'Din verifieringskod är: {}'.format(user.confirmation_code)
#         msg.html = '<div style="justify-content: center; background-color:#faf6c9;"><img style:"height:40px;" src="https://www.dropbox.com/sh/gs4nv2diiz3dszj/AAA95hCVw_VuB40-_DgxNVy4a/Design/8.To%20do/Logo%20up%20to%20date/Logo%20hockey.png?raw=1"><br /><h1 style="color:black;">Din verificationskod är: {}</h1></div>'.format(user.confirmation_code)
#         mail.send(msg)

#         return {'message': 'Email sent.'}, 200


# class VerifyEmail(Resource):
#     parser = reqparse.RequestParser()
#     parser.add_argument('confirmation_code', type=int, required=True, help='This field is required.')
#     @jwt_required
#     def put(self):
#         user = UserModel.find_by_email(get_jwt_identity())
#         if not user:
#             return {'message': 'User does not exist'}

#         if not user.admin:
#             return {"message": "Permission denied."}, 401

#         data = VerifyEmail.parser.parse_args()
#         if data['confirmation_code'] == user.confirmation_code:
#             print('YES')
#             user.confirmed = True
#             user.save_to_db()

#             return {'message': 'User is confirmed.'}, 200

#         user.confirmation_tries = user.confirmation_tries + 1
#         user.save_to_db()
#         return {'message': 'Could not verify user.'}


# class ResetPassword(Resource):
#     parser = reqparse.RequestParser()
#     parser.add_argument('email', type=str, required=True, help='Email is needed.')

#     def put(self):
#         data = ResetPassword.parser.parse_args()
#         user = UserModel.find_by_email(data['email'])

#         if user:
#             chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
#             size = random.randint(8, 12)
#             password = ''.join(random.choice(chars) for x in range(size))
#             user.password = generate_password_hash(password, method=environ.get('HASH_METHOD'))

#             try:
#                 user.save_to_db()

#             except SQLAlchemyError as e:
#                 error = str(e.__dict__["orig"])
#                 return error, 500

#             msg = Message('Nytt lösenord', sender = 'admin@kvillebackenif.se', recipients = [user.email])
#             msg.body = 'Ditt nya lösenord är: {}'.format(password)
#             mail.send(msg)

#             return {'reset': True}, 200

#         return {'message': 'User not found.'}, 400