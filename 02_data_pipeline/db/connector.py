from sqlalchemy import create_engine, text
import pymysql, psycopg2

class DBConnector:
    def __init__(self,engine_name,user,password,host,port,database):
            self.engine_name = engine_name
            self.user = user
            self.password = password
            self.host = host
            self.port = port
            self.database = database

    def pymysql_connection(self):
          pymysql_conn = pymysql.connect(
            user=self.user,
            password=self.password,
            host=self.host,
            port=int(self.port), # 몇년째 안고쳐주는 버그때문에 이렇게 해야함
            database=self.database,
            charset='utf8'
            )
          return pymysql_conn
    
    def psycopg2_connection(self):
          psycopg2_conn = psycopg2.connect(
            user=self.user,
            password=self.password,
            host=self.host,
            port=self.port,
            dbname=self.database,
            )
          return psycopg2_conn  
          
    # SQLALCHEMY 연결
    def sqlalchemy_connection(self):
          sqlalchemy_conn = create_engine(f"{self.engine_name}://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}")
          return sqlalchemy_conn