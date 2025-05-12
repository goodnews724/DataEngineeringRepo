from settings import DB_SETTINGS
from db.connector import DBConnector
from pipeline.extract import extractor
from pipeline.transform import transformer
from pipeline.load import loader

def main():
    print("데이터 파이프라인 시작..!")
    # 파라미터 선언부
    mysql_conn = DBConnector(**DB_SETTINGS['mysql_params']).sqlalchemy_connection()
    pg_conn = DBConnector(**DB_SETTINGS['pg_params']).sqlalchemy_connection()
    query = "SELECT * FROM pokemon"
    table_name = "pokemon_type"

    # 함수 실행부
    df = extractor(mysql_conn, query)
    t_df = transformer(df)
    loader(t_df, pg_conn, table_name)
    print("데이터 파이프라인 종료..!")

main()