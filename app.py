import ntpfuctions

HistorialRpts = []
Historialf1 = []
Historialf2 = []
Historialf3 = []

while True:
    print('''
        --------------------------------------------
        Bienvenido, factoriza con productos notables  
        --------------------------------------------
        
        ''')
    print('''-------------------------------------------------------
        ### Valores válidos: 
        -Binomio suma cuadrado: a**2 + 2ab + b**2
        -Binomio resta cuadrado: a**2 - 2ab + b**2
        -Diferencia de cuadrados: a**2 - b**2
        -Historial: Abrir el historial
        -Salir: Salir del programa
-------------------------------------------------------
    ''')
    NotableProduct = input("¿Por que tipo de producto notable vas a factorizar?: ")

    ValidNotableProducts = "binomio suma cuadrado", "binomio resta cuadrado", "diferencia de cuadrados"

    if NotableProduct.lower() == ValidNotableProducts[0]:
        f1 = input("f1: ")
        f2 = input("f2: ")
        f3 = input("f3 : ")
        Respuesta = ntpfuctions.BinSum2(f1,f2,f3)
        HistorialRpts.append(Respuesta)
        Historialf1.append(f1)
        Historialf2.append(f2)
        Historialf3.append(f3)
        print(Respuesta)
        input('''
              Presiona Enter para seguir...
              ''')
    elif NotableProduct.lower() == ValidNotableProducts[1]:
        f1 = input("f1: ")
        f2 = input("f2: ")
        f3 = input("f3 : ")
        Respuesta = ntpfuctions.BinDif2(f1,f2,f3)
        HistorialRpts.append(Respuesta)
        Historialf1.append(f1)
        Historialf1.append(f2)
        Historialf1.append(f3)
        print(Respuesta)
        input('''
              Presiona Enter para seguir...
              ''')
    elif NotableProduct.lower() == ValidNotableProducts[2]:
        f1 = input("f1: ")
        f2 = input("f2: ")
        Respuesta = ntpfuctions.Dif2(f1,f2)
        HistorialRpts.append(Respuesta)
        Historialf1.append(f1)
        Historialf2.append(f2)
        Historialf3.append(None)
        print(Respuesta)
        input('''
              Presiona Enter para seguir...
              ''')
    elif NotableProduct.lower() == "historial":
        for i in range(0,len(HistorialRpts)):
            print("----------------------------------------------------------------------------")
            print(f"Respuesta: {HistorialRpts[i]}")
            print("")
            print(f"f1: {Historialf1[i]}")
            print(f"f2: {Historialf2[i]}")
            print(f"f3: {Historialf3[i]}")
            print("----------------------------------------------------------------------------")
        input('''
              Presiona Enter para seguir...
              ''')
    elif NotableProduct.lower() == "salir":
        break
    else:
        print("Ingrese un valor válido")
        input('''
              Presiona Enter para seguir...
              ''')
