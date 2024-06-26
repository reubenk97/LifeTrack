from flask_app.config.mysqlconnection import connect_to_mysql
from flask_app import DB

class Category:
    def __init__(self, data) -> None:
        self.id = data['id']
        self.title = data['title']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        activities = []

    @classmethod
    def get_all(cls):
        query = """
            SELECT * FROM categories;
        """
        results = connect_to_mysql(DB).query_db(query)
        categories_list = []
        for row in results:
            this_category = cls(row)
            categories_list.append(this_category)
        return categories_list
    
    @classmethod
    def create(cls, data):
        query = """
            INSERT INTO categories (title)
            VALUES (%(title)s);
        """
        return connect_to_mysql(DB).query_db(query, data)
    
    @staticmethod
    def validate(data):
        errors = []
        if len(data['title']) < 1:
            errors.append("Title is required")
            # errors.append({'cat':'what', 'error':"what is required"})
        return errors