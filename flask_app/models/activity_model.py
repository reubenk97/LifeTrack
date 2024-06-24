from flask_app.config.mysqlconnection import connect_to_mysql
from flask_app import DB

class Activity:
    def __init__(self, data) -> None:
        self.id = data['id']
        self.title = data['title']
        self.start_time = data['start_time']
        self.end_time = data['end_time']
        self.notes = data['notes']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']
        self.category_id = data['category_id']