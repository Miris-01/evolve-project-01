import pandas as pd


def clean_data (df):

    print('Loading original dataset...')

    print('Date formatting to avoid problems:')
    df['Review_Date'] = pd.to_datetime(df['Review_Date'])

    print('Removing duplicate records...')
    df = df.drop_duplicates()

    print('We handle null values for longitude and latitude: ')
    #el codigo agrupa los datos por el nombre del hotel y calcula el valor medio de lat y lng para ese hotel especifico.
    df['lat'] = df.groupby('Hotel_Name')['lat'].transform(lambda x:x.fillna(x.mean()))
    df['lng'] = df.groupby('Hotel_Name')['lng'].transform(lambda x:x.fillna(x.mean()))
    #nos aseguramos de eliminarlo correctamente sin alterar el resto del dataset
    df = df.dropna(subset=['lat', 'lng'])

    print('We filter out the noise and clean the dataset...')
    df['Negative_Review_Clean'] = df['Negative_Review'].astype(str).str.strip().str.lower()
    df = df[df['Negative_Review_Clean'] != 'no negative']

    #aplicamos el regex y stopwords para la mineria de texto
    stopwords = {
        'the', 'and', 'was', 'not', 'for', 'with', 'but', 'room', 'hotel', 'nothing','when',
        'they', 'have', 'there', 'you', 'that', 'this', 'were', 'had', 'from', 'our', 'too'
        'all', 'very', 'one', 'would', 'about', 'good', 'get', 'been', 'location', 
        'too', 'like', 'which', 'out', 'bad', 'more', 'are', 'no', 'negative',
    }
    
    def clean_text (text) :
        import re

        words = re.findall(r'\b[a-z]{3,}\b', str(text))
        filtered_words = [w for w in words if w not in stopwords]
        return " ".join(filtered_words)
    
    df['Negative_Review_Clean'] = df['Negative_Review_Clean'].apply(clean_text)

    print('Cleaning done.')
    return df 


