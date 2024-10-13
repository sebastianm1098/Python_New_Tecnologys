import pandas as pd
from tabulate import tabulate

# Crear DataFrame
datos = pd.read_csv("base_datos_hospital.csv", header=0)

# Aplicar filtro de pacientes menores de edad con diagnóstico de gripe en el año 2020
menores_gripa_2020 = datos[(datos['Edad'] < 18) & 
                        (datos['Diagnostico'].str.contains('Gripe', case=False)) & 
                        (datos['Fecha_Ingreso'] == 2020)]

# Verificar si hay resultados que mostrar
if not menores_gripa_2020.empty:
    # Presentamo los datos en formato tabla
    print("\nPacientes menores de edad con gripe en el año 2020:")
    print(tabulate(menores_gripa_2020, headers='keys', tablefmt='grid'))
else:
    print("\nNo se encontraron pacientes menores de edad con gripe en el año 2020.")
