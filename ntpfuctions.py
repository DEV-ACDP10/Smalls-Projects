def Dif2(f1, f2):
    try:
        a = float(f1) ** (1/2)
        b = float(f2) ** (1/2)
        stra = str(a)
        strb = str(b)
        if stra.endswith(".0"):
            a = int(a)
        if strb.endswith(".0"):
            b = int(b)
        return f"({a} + {b}) ({a} - {b})"
    except:
        return "Ingresa números válidos"
        input('''
              Presiona Enter para seguir...
              ''')
        
def BinSum2(f1,f2,f3):
    try:
        a = float(f1) ** (1/2)
        b = float(f3) ** (1/2)
        stra = str(a)
        strb = str(b)
        if stra.endswith(".0"):
            a = int(a)
        if strb.endswith(".0"):
            b = int(b)
        if 2*(a*b) != float(f2):
            return "Valores ingresados no válidos, la forma debe ser: a**2 , 2ab , b**2"
            input('''
              Presiona Enter para seguir...
              ''')
        else:
            return f"({a} + {b})**2"
    except:
        return "Ingrese números válidos"
        input('''
              Presiona Enter para seguir...
              ''')

def BinDif2(f1,f2,f3):
    try:
        a = float(f1) ** (1/2)
        b = float(f3) ** (1/2)
        stra = str(a)
        strb = str(b)
        if stra.endswith(".0"):
            a = int(a)
        if strb.endswith(".0"):
            b = int(b)
        if 2*(a*b) != float(f2):
            return "Valores ingresados no válidos, la forma debe ser: a**2 , 2ab , b**2"
            input('''
              Presiona Enter para seguir...
              ''')
        else:
            return f"({a} - {b})**2"
    except:
        return "Ingrese números válidos"
        input('''
              Presiona Enter para seguir...
              ''')
        
# Agregar suma de cubos y resta de cubos