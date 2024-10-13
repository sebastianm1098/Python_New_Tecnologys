import pandas as pd
from tabulate import tabulate

# Crear Data Frame
df = pd.read_csv("base_datos_hospital.csv", header=0)

# Filtrar médicos que atienden casos de gripa y covid19
medicos_gripa_covid = df[df['Diagnostico'].str.contains('Gripe', case=False) | 
                        df['Diagnostico'].str.contains('Covid19', case=False)]

# Obtener los médicos únicos que atienden estos casos
medicos_unicos = medicos_gripa_covid['Medico_Asignado'].unique()

# Comprobar si hay resultados
if len(medicos_unicos) > 0:
    # Mostrar los resultados de forma tabulada
    print("\nMédicos que atienden casos de gripa y COVID-19:")
    print(tabulate(medicos_unicos.reshape(-1, 1), headers=['Médico'], tablefmt='grid'))
else:
    print("\nNo se encontraron médicos que atiendan casos de gripa y COVID-19.")
