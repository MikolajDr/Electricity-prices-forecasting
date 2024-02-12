import os
import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import autocorrelation_plot
from statsmodels.graphics.tsaplots import plot_pacf
import re

# Wczytanie pliku Excel
file_path = 'dane_zbiorcze.xlsx'
df = pd.read_excel(file_path)

# Stworzenie folderu na wykresy, jeśli nie istnieje
output_folder = 'wykresy_autokorelacji'
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Funkcja do oczyszczania nazw kolumn
def clean_column_name(col_name):
    cleaned_name = re.sub(r'[^\w\s]', '', col_name)
    return cleaned_name

# Lista nazw kolumn (z pominięciem pierwszej kolumny)
column_names = df.columns[1:]


# Narysowanie wykresów dla każdej serii danych
for col_name in column_names:
    col_data = df[col_name]

     # Oczyszczenie nazwy kolumny
    cleaned_col_name = clean_column_name(col_name)
    cleaned_col_name = cleaned_col_name.replace(' ', '_').replace('[', '').replace(']', '').replace('/', '_')

    # Przekształcenie nazwy pliku do formy kompatybilnej z danym systemem operacyjnym
    file_name = f'autokorelacja_{cleaned_col_name}.png'
    file_path = os.path.normpath(os.path.join(output_folder, file_name))
    
    # Narysowanie wykresu autokorelacji
    plt.figure(figsize=(10, 6))
    autocorrelation_plot(col_data)
    plt.xlabel('Lag (Opóźnienie)')
    plt.ylabel('Autokorelacja')
    plt.grid(True)
    plt.xlim(0, 50)
    #plt.title(f'Autokorelacja - {col_name}')
    plt.savefig(output_folder + '/' + file_name)
    plt.close()

    plt.figure(figsize=(10, 6))
    autocorrelation_plot(col_data)
    plt.xlabel('Lag (Opóźnienie)')
    plt.ylabel('Autokorelacja')
    plt.grid(True)
    plt.xlim(0, 100)
    #plt.title(f'Autokorelacja - {col_name}')
    plt.savefig(output_folder + '/' + file_name)
    plt.close()

    plt.figure(figsize=(10, 6))
    autocorrelation_plot(col_data)
    plt.xlabel('Lag (Opóźnienie)')
    plt.ylabel('Autokorelacja')
    plt.grid(True)
    plt.xlim(0, 1000)
    #plt.title(f'Autokorelacja - {col_name}')
    plt.savefig(output_folder + '/' + file_name)
    plt.close()

    plt.figure(figsize=(10, 6))
    autocorrelation_plot(col_data)
    plt.xlabel('Lag (Opóźnienie)')
    plt.ylabel('Autokorelacja')
    plt.grid(True)
    plt.xlim(0, 3600)
    #plt.title(f'Autokorelacja - {col_name}')
    plt.savefig(output_folder + '/' + file_name)
    plt.close()

    # Przygotowanie wykresu cząstkowej autokorelacji
    plt.figure(figsize=(10, 6))
    plot_pacf(col_data, lags=50)
    plt.xlabel('Lag')
    plt.ylabel('Cząstkowa Autokorelacja')
    plt.grid(True)
    #plt.title(f'Cząstkowa Autokorelacja - {col_name}')
    plt.savefig(output_folder + '/' + file_name)
    plt.close()


    plt.figure(figsize=(10, 6))
    plot_pacf(col_data, lags=250)
    plt.xlabel('Lag')
    plt.ylabel('Cząstkowa Autokorelacja')
    plt.grid(True)
    #plt.title(f'Cząstkowa Autokorelacja - {col_name}')
    plt.savefig(output_folder + '/' + file_name)
    plt.close()

print("Wygenerowano wykresy i zapisano w folderze 'wykresy_autokorelacji'.")
