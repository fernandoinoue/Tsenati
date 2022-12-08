print("*****Restaurante punto azul****")
while True:
    print("""Menu:
    1) desayuno
    2) almuerzo
    3) Cena
    4) Salir """)
    
    opcion=int(input())
    if opcion==1:
        print("1- Pan con huevo       4.50 soles")
        print("2- Pan con palta       4 soles")
        print("3- Jugo de fresa       5 soles")
        print("4- Jugo de naranja     7 soles")
       
        p1=(input("Que deseas comprar: "))
        p2=float(input("precio de lo que deseas comprar: "))
        cant1=float(input("Cantidad: "))
        print("""¿Desea comprar algo mas?
        1)Si
        2)no""")

        opcion=int(input())

        if opcion==2:
            Subto1 = p2 * cant1
            Igv1 = Subto1 * 0.15
            Total1 =  Subto1 + Igv1
            print("Subtotal: ",p1," : " ,Subto1,)
            print("IGV: ",Igv1)
            print("Total: ",Total1)
        


    if opcion==1:
        print("1- Pan con huevo       4.50 soles")
        print("2- Pan con palta       4 soles")
        print("3- Jugo de fresa       5 soles")
        print("4- Jugo de naranja     7 soles")
       
        p3=(input("Que deseas comprar: "))
        p4=float(input("precio de lo que deseas comprar: "))
        cant2=float(input("Cantidad: "))
        print("""¿Desea comprar algo mas?
        1)Si
        2)no""")

        opcion=int(input())

        if opcion==2:
            Subto2 = p2 * cant1 + p4 * cant2
            Igv2 = Subto2 * 0.15
            Total2 =  Subto2 + Igv2
            print("Subtotal: ",p1, "+",p3,":",Subto2,)
            print("IGV: ",Igv2)
            print("Total: ",Total2)
    



    if opcion==1:
        print("1- Pan con huevo       4.50 soles")
        print("2- Pan con palta       4 soles")
        print("3- Jugo de fresa       5 soles")
        print("4- Jugo de naranja     7 soles")
       
        p5=(input("Que deseas comprar: "))
        p6=float(input("precio de lo que deseas comprar: "))
        cant3=float(input("Cantidad: "))
        print("""¿Desea comprar algo mas?
        1)Si
        2)no""")

        opcion=int(input())

        if opcion==2:
            Subto3 = p2 * cant1 + p4 * cant2 * p6 + cant3
            Igv3 = Subto3 * 0.15
            Total3 =  Subto3 + Igv3
            print("Subtotal: ",p1,"+",p3,"+",p5,":",Subto3,)
            print("IGV: ",Igv3)
            print("Total: ",Total3) 
    

    

    if opcion==1:
        print("1- Pan con huevo       4.50 soles")
        print("2- Pan con palta       4 soles")
        print("3- Jugo de fresa       5 soles")
        print("4- Jugo de naranja     7 soles")
       
        p7=(input("Que deseas comprar: "))
        p8=float(input("precio de lo que deseas comprar: "))
        cant4=float(input("Cantidad: "))
        print("""¿Desea comprar algo mas?
        1)Si
        2)no""")

        opcion=int(input())

        if opcion==2:
            Subto4 = p2 * cant1 + p4 * cant2 * p6 + cant3 * p8 + cant4
            Igv4 = Subto4 * 0.15
            Total4 =  Subto4 + Igv4
            print("Subtotal: ",p1,"+",p3,"+",p5,"+",p7,":",Subto4,)
            print("IGV: ",Igv4)
            print("Total: ",Total4)  
    
 




    elif opcion==2:
        print("1- Seco de carne       11 soles")
        print("2- Aji de gallina       10 soles")
        print("3- Mondonguito italiano       12 soles")
        print("4- Gaseosa    7 soles")
       
        p1=(input("Que deseas comprar: "))
        p2=float(input("precio de lo que deseas comprar: "))
        cant1=float(input("Cantidad: "))
        print("""¿Desea comprar algo mas?
        1)Si
        2)no""")

        opcion=int(input())

        if opcion==2:
            Subto1 = p2 * cant1
            Igv1 = Subto1 * 0.15
            Total1 =  Subto1 + Igv1
            print("Subtotal: ",p1," : " ,Subto1,)
            print("IGV: ",Igv1)
            print("Total: ",Total1)
        


    if opcion==1:
        print("1- Seco de carne       11 soles")
        print("2- Aji de gallina       10 soles")
        print("3- Mondonguito italiano       12 soles")
        print("4- Gaseosa    7 soles")
       
        p3=(input("Que deseas comprar: "))
        p4=float(input("precio de lo que deseas comprar: "))
        cant2=float(input("Cantidad: "))
        print("""¿Desea comprar algo mas?
        1)Si
        2)no""")

        opcion=int(input())

        if opcion==2:
            Subto2 = p2 * cant1 + p4 * cant2
            Igv2 = Subto2 * 0.15
            Total2 =  Subto2 + Igv2
            print("Subtotal: ",p1, "+",p3,":",Subto2,)
            print("IGV: ",Igv2)
            print("Total: ",Total2)
    



    if opcion==1:
        print("1- Seco de carne       11 soles")
        print("2- Aji de gallina       10 soles")
        print("3- Mondonguito italiano       12 soles")
        print("4- Gaseosa    7 soles")
       
        p5=(input("Que deseas comprar: "))
        p6=float(input("precio de lo que deseas comprar: "))
        cant3=float(input("Cantidad: "))
        print("""¿Desea comprar algo mas?
        1)Si
        2)no""")

        opcion=int(input())

        if opcion==2:
            Subto3 = p2 * cant1 + p4 * cant2 * p6 + cant3
            Igv3 = Subto3 * 0.15
            Total3 =  Subto3 + Igv3
            print("Subtotal: ",p1,"+",p3,"+",p5,":",Subto3,)
            print("IGV: ",Igv3)
            print("Total: ",Total3) 
    

    

    if opcion==1:
        print("1- Seco de carne       11 soles")
        print("2- Aji de gallina       10 soles")
        print("3- Mondonguito italiano       12 soles")
        print("4- Gaseosa    7 soles")
       
        p7=(input("Que deseas comprar: "))
        p8=float(input("precio de lo que deseas comprar: "))
        cant4=float(input("Cantidad: "))
        print("""¿Desea comprar algo mas?
        1)Si
        2)no""")

        opcion=int(input())

        if opcion==2:
            Subto4 = p2 * cant1 + p4 * cant2 * p6 + cant3 * p8 + cant4
            Igv4 = Subto4 * 0.15
            Total4 =  Subto4 + Igv4
            print("Subtotal: ",p1,"+",p3,"+",p5,"+",p7,":",Subto4,)
            print("IGV: ",Igv4)
            print("Total: ",Total4)  
    






    elif opcion==3:
        print("1- Sopa a la minuta       13 soles")
        print("2- Pollo a la brasa       20 soles")
        print("3- Helado      10 soles")
        print("4- Gaseosa    7 soles")
       
        p1=(input("Que deseas comprar: "))
        p2=float(input("precio de lo que deseas comprar: "))
        cant1=float(input("Cantidad: "))
        print("""¿Desea comprar algo mas?
        1)Si
        2)no""")

        opcion=int(input())

        if opcion==2:
            Subto1 = p2 * cant1
            Igv1 = Subto1 * 0.15
            Total1 =  Subto1 + Igv1
            print("Subtotal: ",p1," : " ,Subto1,)
            print("IGV: ",Igv1)
            print("Total: ",Total1)
        


    if opcion==1:
        print("1- Sopa a la minuta       13 soles")
        print("2- Pollo a la brasa       20 soles")
        print("3- Helado      10 soles")
        print("4- Gaseosa    7 soles")
       
        p3=(input("Que deseas comprar: "))
        p4=float(input("precio de lo que deseas comprar: "))
        cant2=float(input("Cantidad: "))
        print("""¿Desea comprar algo mas?
        1)Si
        2)no""")

        opcion=int(input())

        if opcion==2:
            Subto2 = p2 * cant1 + p4 * cant2
            Igv2 = Subto2 * 0.15
            Total2 =  Subto2 + Igv2
            print("Subtotal: ",p1, "+",p3,":",Subto2,)
            print("IGV: ",Igv2)
            print("Total: ",Total2)
    



    if opcion==1:
        print("1- Sopa a la minuta       13 soles")
        print("2- Pollo a la brasa       20 soles")
        print("3- Helado      10 soles")
        print("4- Gaseosa    7 soles")
       
        p5=(input("Que deseas comprar: "))
        p6=float(input("precio de lo que deseas comprar: "))
        cant3=float(input("Cantidad: "))
        print("""¿Desea comprar algo mas?
        1)Si
        2)no""")

        opcion=int(input())

        if opcion==2:
            Subto3 = p2 * cant1 + p4 * cant2 * p6 + cant3
            Igv3 = Subto3 * 0.15
            Total3 =  Subto3 + Igv3
            print("Subtotal: ",p1,"+",p3,"+",p5,":",Subto3,)
            print("IGV: ",Igv3)
            print("Total: ",Total3) 
    

    

    if opcion==1:
        print("1- Sopa a la minuta       13 soles")
        print("2- Pollo a la brasa       20 soles")
        print("3- Helado      10 soles")
        print("4- Gaseosa    7 soles")
       
        p7=(input("Que deseas comprar: "))
        p8=float(input("precio de lo que deseas comprar: "))
        cant4=float(input("Cantidad: "))
        print("""¿Desea comprar algo mas?
        1)Si
        2)no""")

        opcion=int(input())

        if opcion==2:
            Subto4 = p2 * cant1 + p4 * cant2 * p6 + cant3 * p8 + cant4
            Igv4 = Subto4 * 0.15
            Total4 =  Subto4 + Igv4
            print("Subtotal: ",p1,"+",p3,"+",p5,"+",p7,":",Subto4,)
            print("IGV: ",Igv4)
            print("Total: ",Total4)  

    
        

    elif opcion==4: 
     print("Gracias")
     break


    else:
        print("Presiona una opcion coreccta")








        
    
            

