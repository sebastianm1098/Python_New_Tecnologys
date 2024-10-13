import pandas as pd
from tabulate import tabulate

# Crear dataFrame
datos_hospital = pd.read_csv("base_datos_hospital.csv", header=0)

# Filtrar pacientes con apellido Rodríguez, mayores de 50 años, excluyendo diagnósticos de gripe y fractura
rodriguez_mayores_50 = datos_hospital[(datos_hospital['Apellido'].str.contains('Rodriguez', case=False)) & 
                                    (datos_hospital['Edad'] > 50) & 
                                    (~datos_hospital['Diagnostico'].str.contains('Gripe', case=False)) & 
                                    (~datos_hospital['Diagnostico'].str.contains('Fractura', case=False))]

# existen datos??
if not rodriguez_mayores_50.empty:
    # Tabla para los datos
    print("\nPacientes de apellido Rodríguez mayores de 50 años con diagnósticos distintos a gripe y fractura:")
    print(tabulate(rodriguez_mayores_50, headers='keys', tablefmt='grid'))
else:
    print("\nNo se encontraron pacientes de apellido Rodríguez mayores de 50 años con diagnósticos distintos a gripe y fractura.")
