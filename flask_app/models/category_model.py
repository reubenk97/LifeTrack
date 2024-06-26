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