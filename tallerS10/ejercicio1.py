import pandas as pd
from tabulate import tabulate

# Leer los datos desde el archivo CSV en un DataFrame
data = pd.read_csv("base_datos_hospital.csv", header=0)

# Se filtra mujeres mayor de 80 años con diagnostico de Covid-19
mujeres_covid_80 = data[(data['Genero'] == 'Femenino') & (data['Edad'] > 80) & (data['Diagnostico'].str.contains('Covid19', case=False))]

# se cumple con los critorios
if not mujeres_covid_80.empty:
    # Imprimir en formato tabla con tabulate
    print("\nPacientes femeninas mayores de 80 años con COVID-19:")
    print(tabulate(mujeres_covid_80, headers='keys', tablefmt='grid'))
else:
    print("\nNo se encontraron pacientes femeninas mayores de 80 años con COVID-19.")