import sys

lluvia = input(f'Indique condicion meteorologica "True = llueve / False = No llueve: {sys.argv[0]}')
temperatura = input(f'Ingrese temperatura: {sys.argv[0]}')
humedad= input(f'Ingrese % humedad: {sys.argv[0]}')

linea = temperatura + ',' + humedad + ',' + lluvia
    
logs_lluvia = open('clase09_ej2_1.csv', 'a')
logs_lluvia.write(linea+'\n')
logs_lluvia.close()    
    


    
    
