import pandas as pd
from tabulate import tabulate

# Crear dataframe para la BD
datos_hospital = pd.read_csv("base_datos_hospital.csv", header=0)

# Aplicar filtros requeridos de los hombre que diagnostico el doctor perez
hombres_covid_dr_perez = datos_hospital[(datos_hospital['Genero'] == 'Masculino') & 
                                        (datos_hospital['Edad'] > 80) & 
                                        (datos_hospital['Diagnostico'].str.contains('Covid19', case=False)) & 
                                        (datos_hospital['Medico_Asignado'].str.contains('Perez', case=False))]

if not hombres_covid_dr_perez.empty:
    #Se hace lo mismo mostratando los datos en la tabla
    print("\nPacientes masculinos mayores de 80 años con COVID-19 tratados por el Dr. Pérez:")
    print(tabulate(hombres_covid_dr_perez, headers='keys', tablefmt='grid'))
else:
    print("\nNo se encontraron pacientes masculinos mayores de 80 años con COVID-19 atendidos por el Dr. Pérez.")
