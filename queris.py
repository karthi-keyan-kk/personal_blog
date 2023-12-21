from db_connection import Connection as connect
import pymysql as pms


class Query:

    @staticmethod
    def auth():
        conn, c = connect.sqlConnector()
        query = "SELECT * FROM Auth"
        c.execute(query)
        data = c.fetchall()
        conn.commit()
        conn.close()
        c.close()
        return data[0]

    @staticmethod
    def insert_data(title: str, content: str, date: str):
        conn, c = connect.sqlConnector()
        content_escaped = conn.escape_string(content)
        query = "INSERT INTO user(title, content, date) VALUES('{}', '{}', '{}')".format(title, content_escaped, date)
        c.execute(query)
        conn.commit()
        conn.close()
        c.close()
    
    @staticmethod
    def all_data():
        conn, c = connect.sqlConnector()
        query = "SELECT * FROM user"
        c.execute(query)
        data = c.fetchall()
        conn.commit()
        conn.close()
        c.close()
        return data
    
    @staticmethod
    def data(id: int):
        conn, c = connect.sqlConnector()
        query = f"SELECT * FROM user WHERE id={int(id)}"
        c.execute(query)
        data = c.fetchall()
        conn.commit()
        conn.close
        c.close()
        return data
    
    @staticmethod
    def update_blog(id: int, title: str, content: str, date: str):
        conn, c = connect.sqlConnector()
        content_escaped = conn.escape_string(content)
        query = "UPDATE user SET title='{}', content='{}', date='{}' WHERE id={}".format(title, content_escaped, date, int(id))
        c.execute(query)
        conn.commit()
        conn.close()
        c.close()

    @staticmethod
    def count_user(id: int):
        conn, c = connect.sqlConnector()
        user = f"SELECT COUNT(*) FROM user WHERE id={int(id)}"
        a = c.execute(user)
        conn.commit()
        conn.close()
        c.close()
        return a
        
    @staticmethod
    def delete_blog(id: int):
        conn, c = connect.sqlConnector()
        query = f"DELETE FROM user WHERE id={int(id)}"
        c.execute(query)
        conn.commit()
        conn.close()
        c.close()

