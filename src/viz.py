import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

"""VISUALIZACIÓN DE DATOS"""
def plot_most_demanding_nationality(df):
    """
    Genera y guarda el gráfico de barras que muestra las nacionalidades más exigentes
    """
    top_presents_nationalities = df['Reviewer_Nationality'].value_counts().head(11).index
    df_top_countries = df[df['Reviewer_Nationality'].isin(top_presents_nationalities)]
    most_negative_review = df_top_countries.groupby('Reviewer_Nationality')['Reviewer_Score'].mean().sort_values()#ordenamos por media

    #3.Levantamos el grafico con matplotlib
    plt.figure(figsize=(10, 5))
    most_negative_review.plot(kind='bar', color='#e74c3c', edgecolor='black')

    #4. Personalizamos el grafico
    plt.title('Most demanding nationality')
    plt.xlabel('Nationality')
    plt.ylabel('Score mean')

    plt.ylim(7, 10) #zoom para notar mas la diferencia
    plt.xticks(rotation=45, ha='right') #giramos los nombres de los paises para que no se pisen
    plt.tight_layout()
    #guardamos el grafico antes de mostrarlo
    plt.savefig('most_demanding_nationality.png', dpi=300)
    plt.show() 
    plt.close()

def plot_top_complaints_emiratis (df):
    """"
    Ahora descubramos de que se quejan tanto los emiraties
    """
    df['Reviewer_Nationality'] = df['Reviewer_Nationality'].astype(str).str.strip().str.lower()
    # 1. Creamos el filtro de los emiratíes AQUÍ MISMO para asegurar que tenga datos
    df_eau = df[df['Reviewer_Nationality'] == 'united arab emirates']
    # 2. unimos todas las palabras de la columna ya limpia en un unico string 
    complaint_clean = " ".join(df_eau['Negative_Review_Clean'].astype(str).tolist())
    # 3. rompemos el texto en palabras sueltas
    important_words = complaint_clean.split()
    # 4. contamos cuales se repiten mas
    top_complaint = pd.Series(important_words).value_counts().head(10)
    # 5. levantamos grafico
    plt.figure(figsize=(10, 5))

    top_complaint.plot(kind='bar', color='indianred', edgecolor='black')
    plt.title('Top 10 complaints for EAU tourist')
    plt.xlabel('Key words', fontsize=12)
    plt.ylabel('Frequency', fontsize=12)
    plt.xticks(rotation=45, ha='right', fontsize=11)
    plt.grid(axis='y', linestyle='--', alpha=0.5)
    
    # 6. guardamos el grafico
    plt.tight_layout()
    plt.savefig('top_complaints_eau.png', dpi=300)
    plt.show()
    plt.close()

def plot_monthly_trend (df):
    """
    Genera y guarda el grafico de tendencia temporal (estacionalidad)
    """
    # 1. Contar cuántas reviews (quejas) hay en cada mes del año y ordenarlos cronológicamente
    month_complaints = df['Month'].value_counts().sort_index()
    # 2. mapeamos
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    month_complaints.index = months

    # 3. levantamos el grafico
    plt.figure(figsize=(10, 5))
    plt.plot(month_complaints.index, month_complaints.values, marker='o', color='teal', linewidth=3)

    plt.title('When do people travel and complain the most?')
    plt.xlabel('Months')
    plt.ylabel('Total reviews')
    plt.grid(True, linestyle='--', alpha=0.6) # Añadimos cuadrícula para ver mejor los picos
    plt.tight_layout()

    # Guardamos el gráfico en la raíz antes de mostrarlo
    plt.savefig('monthly_trend.png', dpi=300)
    plt.show()
    plt.close()

def plot_summer_trend (df):
    """
    Genera y guarda el grafico con las 10 quejas mas comunes en verano (Julio y Agosto)
    """    
    # 1. nos aseguramos de solo incluir los meses de julio (7) y agosto (8)
    df_summer = df[df['Month'].isin([7, 8])]

    complaint_summer = " ".join(df_summer['Negative_Review_Clean'].astype(str).tolist())
    important_words_summer = complaint_summer.split()
    top_complaint_summer = pd.Series(important_words_summer).value_counts().head(10)

    plt.figure(figsize=(10, 5))
    top_complaint_summer.plot(kind='bar', color='indianred', edgecolor='black')
    
    plt.title('Top 10 complaints in summer')
    plt.xlabel('Key words', fontsize=12)
    plt.ylabel('Frequency', fontsize=12)
    plt.xticks(rotation=45, ha='right', fontsize=11)
    plt.grid(axis='y', linestyle='--', alpha=0.5)
    
    plt.tight_layout()
    plt.savefig('top_complaints_summer.png', dpi=300)
    plt.show()
    plt.close()

def plot_leng_complaint (df):
    # Scatterplot. Longitud de la queja y la puntuacion del hotel. Veamos si hay algun tipo de relacion 

    plt.figure(figsize=(10,6))
    sns.scatterplot(data=df, x='Review_Total_Negative_Word_Counts', y='Reviewer_Score', alpha=0.5)

    plt.title('Relation between complaint size and hotel score', fontsize=12)
    plt.xlabel('Negative words in complaints', fontsize=12)
    plt.ylabel('Reviewer score', fontsize=12)

    plt.tight_layout()
    plt.savefig('complaint_size_vs_score.png', dpi=300)    
    plt.show()
    plt.close()


def plot_mean_nationalities (df):
    """
    Genera y guarda el mapa de calor cruzando las TOP nacionalidades y meses para detectar puntos negros de insatisfacción (Mean score).
    """
    top_countries = df['Reviewer_Nationality'].value_counts().head(10).index
    df_filtered = df[df['Reviewer_Nationality'].isin(top_countries)]
    #necesitamos un pivot_table para calcular la puntuacion media, calculamos la media para ver los puntos negros de insatisfaccion
    heat_matrix = df_filtered.pivot_table(
        values='Reviewer_Score', 
        index='Reviewer_Nationality', 
        columns='Month', 
        aggfunc='mean'
    )

    months_names = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'] 
    heat_matrix.columns = months_names
    #creamos el mapa
    plt.figure(figsize=(12,6))

    sns.heatmap(
        heat_matrix, 
        cmap='coolwarm', 
        annot=True, 
        fmt=".2f", 
        linewidths=0.5,
        cbar_kws={'label': 'Mean score'}
    )
    
    #lo personalizamos como siempre
    plt.title('Mean score for nationality and month', fontsize=14, fontweight='bold', pad=15)
    plt.xlabel('Review month', fontsize=12)
    plt.ylabel('Nationality', fontsize=12)
    plt.xticks(rotation=0)
    plt.yticks(rotation=0)

    plt.tight_layout()
    plt.savefig('seasonal_heatmap.png', dpi=300)
    plt.show()
    plt.close()

