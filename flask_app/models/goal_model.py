from flask_app.config.mysqlconnection import connect_to_mysql
from flask_app import DB

class Goal:
    def __init__(self, data) -> None:
        self.id = data['id']
        self.title = data['title']
        self.description = data['description']
        self.start_date = data['start_date']
        self.end_date = data['end_date']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']
        related_todos = []

    @classmethod
    def create(cls, data):
        query = """
            INSERT INTO goals (title, description, start_date, end_date, user_id)
            VALUES (%(title)s, %(description)s, %(start_date)s, %(end_date)s, %(user_id)s);
        """
        return connect_to_mysql(DB).query_db(query, data)
    
    @classmethod
    def get_all(cls, data):
        query = """
            SELECT * FROM goals
            WHERE user_id = %(id)s;
        """
        results = connect_to_mysql(DB).query_db(query, data)
        goals_list = []
        for row in results:
            this_goal= cls(row)
            goals_list.append(this_goal)
        return goals_list
    
    @classmethod
    def remove(cls, data):
        query = """
            DELETE FROM goals
            WHERE id = %(id)s;
        """
        return connect_to_mysql(DB).query_db(query, data)

    @classmethod
    def update(cls, data):
        query = """
            UPDATE goals
            SET title = %(title)s,
            description = %(description)s,
            start_date = %(start_date)s,
            end_date = %(end_date)s
            WHERE id = %(id)s;
        """
        return connect_to_mysql(DB).query_db(query, data)

    @staticmethod
    def validate(data):
        errors = []
        if len(data['title']) < 1 or len(data['description']) < 1 or len(data['start_date']) < 1 or len(data['end_date']) < 1:
            errors.append("All fields required")
            # errors.append({'cat':'what', 'error':"what is required"})

        return errors