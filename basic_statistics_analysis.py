import csv
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import pandas as pd


# Wczytanie danych z pliku CSV
data = []
with open('ceny_2023_proba.csv', 'r', encoding='utf-8') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        if len(row) > 0:  # Upewniamy się, że są jakieś dane w wierszu
            last_value = row[-1]  # Pobieramy ostatnią wartość z wiersza
            try:
                data.append(float(last_value))  # Konwertujemy na float i dodajemy do listy
            except ValueError:
                pass  # Pomijamy wiersze z niepoprawnymi wartościami

# Obliczenia miar statystycznych
mean = np.mean(data)
median = np.median(data)
std_dev = np.std(data)
min_val = np.min(data)
max_val = np.max(data)
q1 = np.percentile(data, 25)
q3 = np.percentile(data, 75)
skewness = stats.skew(data)

# Tworzenie histogramu
plt.hist(data, bins=9, edgecolor='black')
plt.title('Histogram występowania cen prądu')
plt.xlabel('Wartość')
plt.ylabel('Liczebność')

# Dodawanie etykiet z wartościami granic przedziałów
bin_edges = np.histogram_bin_edges(data, bins=9)
for i in range(len(bin_edges) - 1):
    plt.text((bin_edges[i] + bin_edges[i+1]) / 2, 5, f'{bin_edges[i]:.2f}', ha='center', va='bottom')

plt.show()

# Obliczanie dystrybuanty
sorted_data = np.sort(data)
cdf = np.arange(1, len(sorted_data) + 1) / len(sorted_data)

# Zapis wyników do pliku CSV
with open('wyniki_statystyki.csv', 'w', newline='', encoding='utf-8') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(['Miarа', 'Wartosc'])
    csv_writer.writerow(['Srednia', mean])
    csv_writer.writerow(['Mediana', median])
    csv_writer.writerow(['Odchylenie standardowe', std_dev])
    csv_writer.writerow(['Wartosc minimalna', min_val])
    csv_writer.writerow(['Wartosc maksymalna', max_val])
    csv_writer.writerow(['Kwartyl 1 (Q1)', q1])
    csv_writer.writerow(['Kwartyl 3 (Q3)', q3])
    csv_writer.writerow(['Wspolczynnik skosnosci', skewness])

    # csv_writer.writerow([])  # Pusta linia oddzielająca miary statystyczne od dystrybuanty
    # csv_writer.writerow(['Wartość', 'Dystrybuanta'])
    # for i in range(len(sorted_data)):
    #     csv_writer.writerow([sorted_data[i], cdf[i]])

print("Wyniki zapisane do pliku wyniki_statystyki.csv")

# Tworzenie DataFrame z wynikami
results = {
    'Miarа': ['Średnia', 'Mediana', 'Odchylenie standardowe', 'Wartość minimalna', 'Wartość maksymalna', 'Kwartyl 1 (Q1)', 'Kwartyl 3 (Q3)', 'Współczynnik skośności'],
    'Wartość': [mean, median, std_dev, min_val, max_val, q1, q3, skewness]
}
results_df = pd.DataFrame(results)

# Zapis wyników do pliku Excel
results_df.to_excel('wyniki_statystyki_excel.xlsx', index=False)
