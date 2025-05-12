def transformer(pandas_df):
    print("transformer함수 돌아가기 시작..!")
    t_df = pandas_df.value_counts('type1').to_frame().reset_index()

    return t_df