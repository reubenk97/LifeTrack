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

    @classmethod
    def create(cls, data):
        query = """
            INSERT INTO todos (title, description, date, location, user_id)
            VALUES (%(title)s, %(description)s, %(date)s, %(location)s, %(user_id)s)
        """
        return connect_to_mysql(DB).query_db(query, data)
    
    @classmethod
    def get_all(cls, data):
        query = """
            SELECT * FROM todos
            WHERE user_id = %(id)s;
        """
        results = connect_to_mysql(DB).query_db(query, data)
        todos_list = []
        for row in results:
            this_todo = cls(row)
            todos_list.append(this_todo)
        return todos_list



    @staticmethod
    def validate(data):
        errors = []
        if len(data['title']) < 1:
            errors.append("Title is required")
            # errors.append({'cat':'what', 'error':"what is required"})

        return errors