from flask_app.config.mysqlconnection import connect_to_mysql
from flask_app import DB

class Todo:
    def __init__(self, data) -> None:
        self.id = data['id']
        self.title = data['title']
        self.description = data['description']
        self.date = data['date']
        self.location = data['location']
        self.completed = data['completed']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']
        self.related_goals = []

    @classmethod
    def create(cls, data):
        query = """
            INSERT INTO todos (title, description, date, location, completed, user_id)
            VALUES (%(title)s, %(description)s, %(date)s, %(location)s, 0, %(user_id)s);
        """
        return connect_to_mysql(DB).query_db(query, data)
    
    @classmethod
    def get(cls, data):
        query = """
            SELECT * FROM todos
            WHERE id = %(id)s;
        """
        return cls(connect_to_mysql(DB).query_db(query, data)[0])
    
    @classmethod
    def get_all(cls, data):
        query = """
            SELECT * FROM todos
            WHERE user_id = %(id)s AND completed = %(completed)s;
        """
        results = connect_to_mysql(DB).query_db(query, data)
        todos_list = []
        for row in results:
            this_todo = cls(row)
            todos_list.append(this_todo)
        return todos_list
    
    @classmethod
    def remove(cls, data):
        query = """
            DELETE FROM todos
            WHERE id = %(id)s;
        """
        return connect_to_mysql(DB).query_db(query, data)

    @classmethod
    def update(cls, data):
        query = """
            UPDATE todos
            SET title = %(title)s,
            description = %(description)s,
            date = %(date)s,
            location = %(location)s,
            completed = %(completed)s
            WHERE id = %(id)s;
        """
        return connect_to_mysql(DB).query_db(query, data)
    
    @classmethod
    def complete(cls, data):
        query = """
            UPDATE todos
            SET completed = 1
            WHERE id = %(id)s;
        """
        return connect_to_mysql(DB).query_db(query, data)

    @staticmethod
    def validate(data):
        errors = []
        if len(data['title']) < 1 or len(data['description']) < 1 or len(data['date']) < 1 or len(data['location']) < 1:
            errors.append("All fields required")
            # errors.append({'cat':'what', 'error':"what is required"})

        return errors