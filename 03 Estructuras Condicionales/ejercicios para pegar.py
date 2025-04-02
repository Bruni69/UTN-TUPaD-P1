# El usuario ingresa el hemisferio, que mes del año y que dia es, el 
#programa imprime la estacion del año en que se imprime

hemisferio = input("Por favor ingrese el hemisferio en que se encuentra ").lower()
dia = int(input("por favor ingrese el dia  "))
mes = int(input("el mes que transcurre (en numero, ejemplo 1=enero) "))

# Condicional y salida
if hemisferio == "norte":
    if dia >= 21 and mes == 12 or mes == 1 or mes == 2 or mes == 3 and dia < 20:
        print("Esta en temporada de invierno")
    elif dia >= 21 and mes == 3 or mes == 4 or mes == 5 or mes == 6 and dia < 20:
        print("Esta en temporada de primavera")
    elif dia >= 21 and mes == 6 or mes == 7 or mes == 8 or mes == 9 and dia < 20:
        print("Esta en temporada de verano")
    elif dia >= 21 and mes == 9 or mes == 10 or mes == 11 or mes == 12 and dia < 20:
        print("Esta en temporada de otoño")        
elif hemisferio == "sur":
    if dia >= 21 and mes == 12 or mes == 1 or mes == 2 or mes == 3 and dia < 20:
        print("Esta en temporada de verano")
    elif dia >= 21 and mes == 3 or mes == 4 or mes == 5 or mes == 6 and dia < 20:
        print("Esta en temporada de otoño")
    elif dia >= 21 and mes == 6 or mes == 7 or mes == 8 or mes == 9 and dia < 20:
        print("Esta en temporada de invierno")     
    elif dia >= 21 and mes == 9 or mes == 10 or mes == 11 or mes == 12 and dia < 20:
        print("Esta en temporada de primavera")      
    
            