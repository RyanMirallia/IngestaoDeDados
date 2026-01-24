import pandas as pd
import os

df = pd.read_csv('data/netflix_titles.csv')

INPUT_PATH = 'data/netflix_titles.csv'
OUTPUT_PATH = 'data/netflix_titles_cleaned.csv'

def processa_dados():

    if not os.path.exists(INPUT_PATH):
        print(f"arquivo {INPUT_PATH} não foi encontrado!")
        return
        
    df = pd.read_csv(INPUT_PATH)

    #clear null values 

    df['director'] = df['director'].fillna('Not Listed')
    df['cast'] = df['cast'].fillna('Unknown Cast')
    df['country'] = df['country'].fillna('Unknown')
    df['rating'] = df['rating'].fillna('NR')

    df = df.dropna(subset=['duration', 'date_added'])

    #the date_added columns data types defined as date_time 

    df['date_added'] = pd.to_datetime(df['date_added'].str.strip())

    df.to_csv(OUTPUT_PATH, index=False)
    print(f"arquivo limpo salvo em: {OUTPUT_PATH}")

if __name__ == "__main__":
    processa_dados()

