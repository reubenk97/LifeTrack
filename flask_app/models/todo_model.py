from flask_app.config.mysqlconnection import connect_to_mysql
from flask_app import DB

class Todo:
    def __init__(self, data) -> None:
        self.id = data['id']
        self.title = data['title']
        self.description = data['description']
        self.date = data['date']
        self.location = data['location']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']
        related_goals = []