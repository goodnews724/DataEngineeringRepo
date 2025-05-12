def loader(pandas_df, connection_obj, table_name):
    try:
        pandas_df.to_sql(
            name = table_name,
            con = connection_obj,
            if_exists='replace',
            index = False
        )
        print("POSTGRESQL에 테이블 저장이 완료되었습니다.")

    except:
        print("저장에 실패했습니다.")