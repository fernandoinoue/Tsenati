igv = float()

precio = float()

total = float()

impuesto = float()

opcion = str()

desayuno = str()

almuerzo = str()

cena = str()

igv = 0.16

while True:
    print("""
|================================|
|        RESTAURANTE S.A         |
|              MENÚ              |
|================================|
| A | DESAYUNO                   |
| B | ALMUERZO                   |
| C | CENA                       |
|--------------------------------|
| D |         SALIR              |
|================================|
""")
    while True:
        opcion = input("Digite un valor:")

        opcion = str.lower(opcion)

        if not (opcion == "a" or opcion == "b" or opcion == "c" or opcion == "d"):

            print("Entrada inválida")

        if (opcion == "a" or opcion == "b" or opcion == "c" or opcion == "d"):
            break

    if opcion == "a":
        print("""
|================================|
|            DESAYUNO            |
|================================|
| A | CAFÉ              | S/4.50 |
| B | CHOCOLATE         | S/5.00 |
| C | JUGO DE FRESA     | S/9.00 |
| D | JUGO DE PAPAYA    | S/8.00 |
| E | PAN CON POLLO     | S/7.00 |
| F | PAN CON JAMÓN     | S/7.00 |
| G | PAN CON TORTILLA  | S/7.00 |
|--------------------------------|
| H |         SALIR              |
|================================|""")
        while True:
            desayuno = input("Digite un valor: ")

            desayuno = str.lower(desayuno)

            if not (desayuno == "a" or desayuno == "b" or desayuno == "c" or desayuno == "d" or desayuno == "e" or desayuno == "f" or desayuno == "g" or desayuno == "h"):

                print("Entrada inválida")

            if (desayuno == "a" or desayuno == "b" or desayuno == "c" or desayuno == "d" or desayuno == "e" or desayuno == "f" or desayuno == "g" or desayuno == "h"):
                break
        if desayuno == "a":

            precio = 4.50

            impuesto = precio*igv

            total = precio+impuesto

        elif desayuno == "b":

            precio = 5.00

            impuesto = precio*igv

            total = precio+impuesto

        elif desayuno== "c":

            precio = 9.00

            impuesto = precio*igv

            total = precio+impuesto

        elif desayuno== "d":

            precio = 8.00

            impuesto = precio*igv

            total = precio+impuesto

        elif desayuno == "e":

            precio = 7.00

            impuesto = precio*igv

            total = precio+impuesto

        elif desayuno == "f":

            precio = 7.00

            impuesto = precio*igv

            total = precio+impuesto

        elif desayuno == "g":

            precio = 7.00

            impuesto = precio*igv

            total = precio+impuesto

    if opcion == "b":

        print("""
|================================|
|            ALMUERZO            |
|================================|
| A | CAFÉ              | S/4.50 |
| B | CHOCOLATE         | S/5.00 |
| C | JUGO DE FRESA     | S/9.00 |
| D | JUGO DE PAPAYA    | S/8.00 |
| E | PAN CON POLLO     | S/7.00 |
| F | PAN CON JAMÓN     | S/7.00 |
| G | PAN CON TORTILLA  | S/7.00 |
|--------------------------------|
| H |         SALIR              |
|================================|""")

        while True:
    
            almuerzo = input("Digite un valor: ")

            almuerzo = str.lower(almuerzo)

            if not (almuerzo == "a" or almuerzo == "b" or almuerzo == "c" or almuerzo == "d" or almuerzo == "e" or almuerzo == "f" or almuerzo == "g" or almuerzo == "h"):

                print("Entrada inválida")

            if (almuerzo == "a" or almuerzo == "b" or almuerzo == "c" or almuerzo== "d" or almuerzo == "e" or almuerzo == "f" or almuerzo == "g" or almuerzo == "h"):
                break
        if almuerzo == "a":
    
            precio = 4.50

            impuesto =   precio*igv

            total = precio+impuesto

        elif almuerzo == "b":

            precio = 5.00

            impuesto =   precio*igv

            total = precio+impuesto

        elif almuerzo == "c":

            precio = 9.00

            impuesto = precio*igv

            total = precio+impuesto

        elif almuerzo == "d":

            mnto = 8.00

            impuesto = precio*igv

            total = precio+impuesto

        elif almuerzo == "e":

                precio= 7.00

                impuesto =   precio*igv

                total = precio+impuesto

        elif almuerzo == "f":

            precio = 7.00

            impuesto =   precio*igv

            total = precio+impuesto

        elif almuerzo == "g":

            precio = 7.00

            impuesto =   precio*igv

            total = precio+impuesto        

    if opcion == "c":
        print("""
|================================|
|              CENA              |
|================================|
| A | QUINUA CON LECHE    S/2.00 |
| B | EMOLIENTE           S/2.00 |
| C | PAN CON POLLO       S/1.50 |
| D | JUGO DE PAPAYA      S/2.00 |
|--------------------------------|
| G |         SALIR              |
|================================|""")
        while True:

            cena = input("Digite un valor: ")

            cena = str.lower(cena)

            if not (cena == "a" or cena == "b" or cena == "c" or cena == "d" or cena == "e" or cena == "f" or cena == "g"):

                print("Entrada inválida")

            if ( cena== "a" or  cena== "b" or  cena== "c" or cena == "d" or cena == "e" or cena == "f" or cena == "g"):
                break
        if cena == "a":
    
            precio = 9.50

            impuesto = precio*igv

            total = mnto+impuesto

        elif cena == "b":

            precio = 7.50

            impuesto =   precio*igv

            total = precio+impuesto

        elif cena == "c":

            precio = 6.00

            impuesto =   precio*igv

            total  = precio+impuesto

        elif cena == "d":

            precio = 6.00

            impuesto = precio*igv

            total = precio+impuesto

        elif cena == "e":

            precio = 5.50

            impuesto = precio*igv

            total = precio+impuesto

        elif cena == "f":

            precio = 4.00

            impuesto = precio*igv

            total = precio+impuesto
    print("|================================|")
    print("|        BOLETA DE VENTAS        |")
    print("|================================|")
    print("| Subtotal:          S/.",precio, "|")
    print("| Igv:               S/.",impuesto,  "|")
    print("| Total a pagar:     S/.",total,"|")
    print("|--------------------------------|")
    print("|      Gracias por su compra     |")
    print("|================================|")
    if opcion == "d":
        break