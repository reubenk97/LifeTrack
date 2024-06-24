from flask_app.config.mysqlconnection import connect_to_mysql
from flask import flash
from flask_app import DB
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
PASSWORD_REGEX = re.compile(r'^(?=.*[A-Z])(?=.*[0-9])')

class User:
    def __init__(self,data) -> None:
        self.id = data['id']
        self.username = data['username']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    # Needs to be changed
    @classmethod
    def get_by_id(cls, data):
        query = """
            SELECT * FROM users
            WHERE users.id = %(id)s;
        """
        results = connect_to_mysql(DB).query_db(query,data)
        if results:
            return cls(results[0])
        return False
    

    @classmethod
    def get_by_email(cls, data):
        query = """
            SELECT * FROM users
            WHERE email = %(email)s;
        """
        results = connect_to_mysql(DB).query_db(query,data)
        if results:
            return cls(results[0])
        return False

    # Needs to be changed
    @classmethod
    def create(cls, data):
        query = """
            INSERT INTO users (username, email, password)
            VALUES (%(username)s, %(email)s, %(password)s);
        """
        return connect_to_mysql(DB).query_db(query, data)


    @staticmethod
    def validate(data):
        is_valid = True

        # First name validation
        if len(data['username']) < 1:
            is_valid = False
            flash('Username is required.', 'reg')
        elif len(data['username']) < 2:
            is_valid = False
            flash('Username must be at least 2 characters.', 'reg')

        # Email validation
        if len(data['email']) < 1:
            is_valid = False
            flash('Email is required.', 'reg')
        elif not EMAIL_REGEX.match(data['email']):
            is_valid = False
            flash('Email must be in a valid format.', 'reg')
        else:
            potential_user = User.get_by_email({'email':data['email']})
            if potential_user:
                is_valid = False
                flash('Email is currently in use. Please try another email or log in.', 'reg')
        
        # Password validation
        if len(data['password']) < 1:
            is_valid = False
            flash('Please provide a password.', 'reg')
        elif not PASSWORD_REGEX.match(data['password']):
            is_valid = False
            flash('Password must contain an uppercase letter and a number.', 'reg')
        elif data['password'] != data['confirm_password']:
            is_valid = False
            flash('Passwords do not match.', 'reg')

        return is_valid
    

    @staticmethod
    def ajax_validate(data):
        errors = []

        # First name validation
        if len(data['username']) < 1:
            errors.append('Username is required.')
        elif len(data['username']) < 2:
            errors.append('Username must be at least 2 characters.')

        # Email validation
        if len(data['email']) < 1:
            errors.append('Email is required.')
        elif not EMAIL_REGEX.match(data['email']):
            errors.append('Email must be in a valid format.')
        else:
            potential_user = User.get_by_email({'email':data['email']})
            if potential_user:
                errors.append('Email is currently in use. Please try another email or log in.')
        
        # Password validation
        if len(data['password']) < 1:
            errors.append('Please provide a password.')
        elif not PASSWORD_REGEX.match(data['password']):
            errors.append('Password must contain an uppercase letter and a number.')
        elif data['password'] != data['confirm_password']:
            errors.append('Passwords do not match.')

        return errors