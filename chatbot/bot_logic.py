def find_answers(df, question, limit=10):
    question = question.lower()
    filtered_df = df.copy()

    if 'bmw' in question:
        filtered_df = filtered_df[filtered_df['CarType'].str.lower().str.contains('bmw')]

    if 'problem' in question or 'problème' in question:
        return filtered_df[['CarType', 'CarModel', 'Problem']].head(limit).to_dict(orient='records')
    
    if 'price' in question or 'prix' in question:
        return filtered_df[['CarType', 'CarModel', 'Price']].head(limit).to_dict(orient='records')
    
    if 'kilometrage' in question or 'mileage' in question:
        return filtered_df[['CarType', 'CarModel', 'Kilometrage']].head(limit).to_dict(orient='records')
    
    return [{"message": "Je ne comprends pas la question."}]
