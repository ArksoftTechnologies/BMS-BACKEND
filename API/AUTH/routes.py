from flask import Blueprint, json, jsonify, url_for, current_app, request, render_template
from API.model import *
from API.settings import App_name
from API.email_sender import *
import json
import random
from itsdangerous import URLSafeTimedSerializer
from API import mail, Message

app = current_app

auth_bp = Blueprint("auth_bp", __name__, template_folder='templates', static_folder='static')

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.form
    name = data['name']
    address = data['address']
    email = data['email']
    phone = data['phone']
    password = data['password']

    # Check if user with the provided SCN number or email already exists
    existing_user = User.query.filter_by(email=email).first()
    if existing_user:
        return jsonify({'error': 'User with the email already exists'}), 409

    # Create a new user
    new_user = User(name, email, phone, address)
    new_user.set_password(password)
    db.session.add(new_user)
    db.session.commit()

    # Generate verification code
    verification_code = generate_verification_code()  # You'll need to implement this function
    new_user.set_verification_code(str(verification_code))
    db.session.add(new_user)
    db.session.commit()

    # Send verification email
    send_verification_email(email, verification_code)  # You'll need to implement this function


    return jsonify({'message': 'User created successfully'}), 201

def generate_verification_code():
    # Return the generated verification code
    code = random.randint(100000, 999999)
    return code

def send_verification_email(email, verification_code):
    msg = Message('Verification Code', recipients=[email])
    user = User.query.filter_by(email=email).first().obj_to_dict()
    msg.html = render_template('email/confirmation.html', verification_code=verification_code, user=user, title=App_name)
    mail.send(msg)

@auth_bp.route('/verify_email', methods=[ 'POST', "GET" ])
def verify_email():
    if request.method == "POST":
        details = request.form
        user = User.query.filter_by(email=details[ 'email' ]).first()
        if user.status != "ACTIVE":
            if user and user.check_verification_code(str(details[ 'code' ])):
                user.status = "ACTIVE"
                db.session.add(user)
                db.session.commit()
                send_welcome_email(user.email, user.name, user.email)
                
                return jsonify({ 'account_verified': True, }), 200
            return jsonify({ 'account_verified': False, 'error': 'Invalid Verification code.' }), 401
        return jsonify({ 'error': "Your account has been verified and is Active, proceed to login." }), 401

    # id = request.args.get('email')
    # user = User.query.filter_by(email=id).first()
    # if user and user.status == 'PENDING':
    #     # Generate verification code
    #     verification_code = generate_verification_code()  # You'll need to implement this function
    #     user.set_verification_code(str(verification_code))

    #     # Send verification email
    #     send_verification_email(user.email, verification_code)  # You'll need to implement this function
    #     return jsonify({'error': 'Your email has not been verified, please check your email, a new verification code has been sent again.' })

    # return jsonify({ 'error': f'User account is active.' }), 401

def send_welcome_email(email, name, scn):

    # Render the welcome email template with user data
    html_content = render_template('email/welcome.html', name=name, scn_no=scn, title=App_name)

    # Send the welcome email
    msg = Message(f'WELCOME TO {App_name}', recipients=[ email ])
    msg.html = html_content
    mail.send(msg)