# Realizar un programa para saber si eres adulto.

# e = int(input("¿Es usted un adulto? "))
# if e >= 18:
#     print("Eres un adulto")
# elif e == 32:
#     print("Eres un adulto de ", e)
# else: 
#     print("No eres un adulto")


# Crear un programa, donde ingreses tu edad e imprimir si eres mayor de edad o menor de edad. 

# a = int(input("Ingresa tu edad: "))
# if a >= 18:
#     print("Es usted mayor de edad")
# else:
#     print("No es usted mayor de edad")


# Escribir un programa que compare 2 números e imprime si son iguales o no son iguales.

# n1 = int(input("Ingrese un digito: ")) 
# n2 = int(input("Ingrese segundo un digito: ")) 
# if n1 == n2:
#     print("Los numeros digitados son iguales")
# else:
#     print("No son iguales")


# Realizar un programa para saber etapas de la vida y acorde a tu edad imprimir lo siguiente

# Niñez (6-11) 
# Adolescencia (12-18) 
# Juventud (18-26) 
# Adultez (27-59) 
# Vejez (60 a más) 

# etapa_de_vida = int(input("Ingrese su edad:"))
# while True:
#     if 6 <= etapa_de_vida <= 11:
#         print("Usted esta en la etapa de la niñez.")
#     if 12 <= etapa_de_vida <= 18:
#         print("Usted esta en la etapa de la Adolescencia.")
#     if 18 <= etapa_de_vida <= 28:
#             print("Usted esta en la etapa de la Juventud.")
#     if 28 <= etapa_de_vida <= 59:
#         print("Usted esta en la etapa de la Adultez.")
#     if 59 <= etapa_de_vida <= 100:
#         print("Usted esta en la etapa de la vejez.")
#     break

# Realizar un ejemplo para imprimir el mes del año de acuerdo con el número ingresado, si se ingresa un número fuera del rango imprimir debe mostrar el mensaje “valor invalido”, ejemplo: 

# Número 12 es igual a diciembre.     

# meses = int(input("Digite numero segun los meses:"))
# while True:
#     if meses==1:
#         print("Mes", meses, 'Enero')
#     if meses==2:
#         print("Mes", meses, 'Febrero')
#     if meses==3:
#         print("Mes", meses, 'Marzo')
#     if meses==4:
#         print("Mes", meses, 'Abril')
#     if meses==5:
#         print("Mes", meses, 'Mayo')
#     if meses==6:
#         print("Mes", meses, 'Junio')                                
#     break
# asi sucesivamente con los demas mes...


# Crear un programa para verificar el usuario y contraseña, si ingreso correctamente los datos imprimir “Bienvenido” en caso contrario “Inténtelo de nuevo”.


# user = "Pepito"
# pwd = "Pepito123"
# usuario = input("Usuario: ")
# password = input("Password: ")

# if usuario == user and password == pwd :
#     print("Inciando Session")
#     print("Session successfully")
# else:
#     print("Intente Nuevamente")


# Crear un programa que permita saber si un año es bisiesto, si es bisiesto imprimir “Este año es bisiesto” o en caso contrario “No es un año bisiesto”.

# año = 2016

# if año % 4 == 0 and (año % 100 != 0 or año % 400 == 0):
# 	print("Es bisiesto")
# else:
# 	print("No es bisiesto")


# Realizar un programa que permita saber el día de acuerdo con el número ingresado.

# print('Complete los datos')
# n = int(input("Dia: "))
# n2 = int(input("Mes:"))
# n3 = int(input("Año:"))
# print(f"Fechas ingresadas\n {n}", n2, n3, sep=('/'))


# Ingresar dos números e imprimir cuál de los dos es mayor.
# n1 = int(input("Digite un numero mayor: "))
# var_n = int(input("Digite un numero menor: "))

# if n1 > var_n:
#     print("Es mayor", n1)
# elif n1 < var_n:
#     print("Es menor", var_n)
# elif n1 == var_n:
#     print("Son numero Iguales")
# else:
#     print("Error Try again.") 

