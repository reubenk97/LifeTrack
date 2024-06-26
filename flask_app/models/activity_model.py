from flask_app.config.mysqlconnection import connect_to_mysql
from flask_app import DB

class Activity:
    def __init__(self, data) -> None:
        self.id = data['id']
        self.title = data['title']
        self.start_time = data['start_time']
        self.end_time = data['end_time']
        self.location = data['location']
        self.notes = data['notes']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']
        self.category_id = data['category_id']

    @classmethod
    def create(cls, data):
        query = """
            INSERT INTO activities (title, start_time, end_time, location, notes, user_id, category_id)
            VALUES (%(title)s, %(start_time)s, %(end_time)s, %(location)s, %(notes)s, %(user_id)s, %(category_id)s);
        """
        return connect_to_mysql(DB).query_db(query, data)
    
    @classmethod
    def get_all(cls, data):
        query = """
            SELECT * FROM activities
            WHERE user_id = %(id)s;
        """
        results = connect_to_mysql(DB).query_db(query, data)
        activities_list = []
        for row in results:
            this_activity = cls(row)
            activities_list.append(this_activity)
        return activities_list
    
    @classmethod
    def remove(cls, data):
        query = """
            DELETE FROM activities
            WHERE id = %(id)s;
        """
        return connect_to_mysql(DB).query_db(query, data)

    @classmethod
    def update(cls, data):
        query = """
            UPDATE activities
            SET title = %(title)s,
            start_time = %(start_time)s,
            end_time = %(end_time)s,
            location = %(location)s,
            notes = %(notes)s,
            category_id = %(category_id)s
            WHERE id = %(id)s;
        """
        return connect_to_mysql(DB).query_db(query, data)

    @staticmethod
    def validate(data):
        errors = []
        if len(data['title']) < 1 or len(data['start_time']) < 1 or len(data['end_time']) < 1 or len(data['location']) < 1 or len(data['notes']) < 1:
            errors.append("All fields required")
            # errors.append({'cat':'what', 'error':"what is required"})

        return errors