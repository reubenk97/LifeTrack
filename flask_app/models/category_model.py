from flask_app.config.mysqlconnection import connect_to_mysql
from flask_app import DB

class Category:
    def __init__(self, data) -> None:
        self.id = data['id']
        self.title = data['title']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        activities = []