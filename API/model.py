from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from passlib.hash import sha256_crypt
from datetime import datetime as dt, date
today_raw = date.today()
today = date.isoformat(today_raw)
month = f"{ today_raw.month }-{ today_raw.year }"
from sqlalchemy.orm import relationship

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    address = db.Column(db.String(500), nullable=False)
    status = db.Column(db.String(50), default="PENDING")
    date_registered = db.Column(db.String(20), default=today)
    month = db.Column(db.String(20), default=month)
    year = db.Column(db.String(20), default=today_raw.year)
    verification_code = db.Column(db.String(20), nullable=True)
    password_hash = db.Column(db.String(128), nullable=False)
    # order = relationship('Order', foreign_keys='Order.id', backref='users')
    

    def __init__(self, name, email, phone, address):
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def set_verification_code(self, verification_code):
        self.verification_code = sha256_crypt.encrypt(verification_code)

    def check_verification_code(self, verification_code):
        return sha256_crypt.verify(verification_code, self.verification_code)

    def obj_to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}








