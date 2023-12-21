import pymysql as pms

class Connection:
    __UserName = "root"
    __password = "@karthiKeyan1234"
    __DB = "karthikeyan"

    @staticmethod
    def sqlConnector():
        user_name = Connection.__UserName
        pwd = Connection.__password
        DB_name = Connection.__DB

        conn = pms.connect(user=user_name, password=pwd, db=DB_name, host='localhost')
        c = conn.cursor()
        return conn, c