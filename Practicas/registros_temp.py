temperaturas = []
cont_days = 0
for i in range(5):
    #Ingreso de temperaturas
    temp = float(input(f"Ingrese la temperatura del día {i + 1}: "))
    temperaturas.append(temp)
    
    #Contador de días con temperatura mayor a 25 grados
    if temp > 25:
        cont_days += 1
        
print(f"Las temperaturas registradas son: {temperaturas}")
#Promedio de temperaturas
print(f"Temperatura promedio: {sum(temperaturas) / len(temperaturas)}")
#Temperatura máxima y mínima
print(f"Temperatura máxima: {max(temperaturas)}")
print(f"Temperatura mínima: {min(temperaturas)}")
#Cantidad de días con temperatura mayor a 25 grados
print(f"Cantidad de días con temperatura mayor a 25 grados: {cont_days}")