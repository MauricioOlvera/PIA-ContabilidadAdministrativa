from string import punctuation


continuar = True

while continuar:

    tpl_prod = ()
    tpl_reqprod = ()
    tpl_infoinv = ()
    n = 0
    m = 0
    let = ("A","B","C")
    wrd = ("inicial","final")
    num = 2

    menu = str(input('''
===============================================
                    MENU
===============================================

1.- Empezar
2.- Salir

Seleccione la opcion que desea: '''))

    if menu == "1":
        nomEmpresa = str(input("Ingrese el nombre de su empresa/organizacion: "))
        numNomEmp = (65 - len(nomEmpresa))/2
        año = int(input("Ingrese el año en que desea trabajar: "))

        #---Balance General---
        print("*** Estado de Situacion Financiera ***")
        #Activos
        Efectivo = int(input("Ingrese el saldo de la cuenta de Efectivo: "))
        Clientes = int(input("Ingrese el saldo de la cuenta de Clientes: "))
        InvMat = int(input("Ingrese el saldo de la cuenta de Inventarios de Materiales: "))
        InvArtTerm = int(input("Ingrese el saldo de la cuenta de Inv. de articulos terminados: "))
        Terreno = int(input("Ingrese el saldo de la cuenta de Terreno: "))
        PlantEqui = int(input("Ingrese el saldo de la cuenta de Planta y Equipo: "))
        DeprAcu = int(input("Ingrese el saldo de la cuenta de Depreciacion Acumulada: "))
        #Pasivos
        Prov = int(input("Ingrese el saldo de la cuenta de Proveedores: "))
        DocsXpag = int(input("Ingrese el saldo de la cuenta de Documentos por Pagar: "))
        ISRacu = int(input("Ingrese el saldo de la cuenta de ISR por Pagar: "))
        ObliXpag = int(input("Ingrese el saldo de la cuenta de Obligaciones por Pagar: "))
        #Capital
        CapAport = int(input("Ingrese el saldo de la cuenta de Capital Aportado: "))
        CapGanado = int(input("Ingrese el saldo de la cuenta de Capital Ganado: "))
        print()

        #---Requisitos de productos---
        print("*** Requisitos de los Productos ***")
        for x in range(3):
            tplreq = ()
            matA = int(input(f"Ingrese cuanto Material A requiere el Producto {let[x]}: "))
            matB = int(input(f"Ingrese cuanto Material B requiere el Producto {let[x]}: "))
            matC = int(input(f"Ingrese cuanto Material C requiere el Producto {let[x]}: "))
            manoObra = int(input(f"Ingrese cuantas horas requiere el Producto {let[x]}: "))
            print()
            tplreq = tplreq + (matA, matB, matC, manoObra)
            tpl_reqprod = tpl_reqprod + (tplreq,)

        costManObra1 = int(input("Ingrese cuanto costara la mano de obra el primer semestre: "))
        costManObra2 = int(input("Ingrese cuanto costara la mano de obra el segundo semestre: "))
        print()

        #---Informacion de inventarios---
        print("*** Informacion de Inventarios ***")
        for y in range(num):
            tplSem1 = ()
            m += 1
            InvMatA = int(input(f"Ingrese el inventario {wrd[y]} del Semestre {m} del Material A: "))
            InvMatB = int(input(f"Ingrese el inventario {wrd[y]} del Semestre {m} del Material B: "))
            InvMatC = int(input(f"Ingrese el inventario {wrd[y]} del Semestre {m} del Material C: "))
            print()
            CostMatA = float(input(f"Ingrese el costo del Material A en el Semestre {m}: "))
            CostMatB = float(input(f"Ingrese el costo del Material B en el Semestre {m}: "))
            CostMatC = float(input(f"Ingrese el costo del Material C en el Semestre {m}: "))
            print()
            InvProdA = int(input(f"Ingrese el inventario {wrd[y]} del Semestre {m} del Producto A: "))
            InvProdB = int(input(f"Ingrese el inventario {wrd[y]} del Semestre {m} del Producto B: "))
            InvProdC = int(input(f"Ingrese el inventario {wrd[y]} del Semestre {m} del Producto C: "))
            print()
            tplSem1 = tplSem1 + (InvMatA,InvMatB,InvMatC,CostMatA,CostMatB,CostMatC,InvProdA,InvProdB,InvProdC)
            tpl_infoinv = tpl_infoinv + (tplSem1,)

        #---Productos---
        print("*** Productos ***")
        for z in range(num):
            tplSem2 = ()
            n += 1
            PreVenA = int(input(f"Ingrese el precio de venta del semestre {n} del producto A: "))
            VenPlanA = int(input(f"Ingrese las ventas planeadas del semestre {n} del producto A: "))
            PreVenB = int(input(f"Ingrese el precio de venta del semestre {n} del producto B: "))
            VenPlanB = int(input(f"Ingrese las ventas planeadas del semestre {n} del producto B: "))
            PreVenC = int(input(f"Ingrese el precio de venta del semestre {n} del producto C: "))
            VenPlanC = int(input(f"Ingrese las ventas planeadas del semestre {n} del producto C: "))
            print()
            tplSem2 = tplSem2 + (PreVenA,VenPlanA,PreVenB,VenPlanB,PreVenC,VenPlanC)
            tpl_prod = tpl_prod + (tplSem2,)

        #---Gastos de Administracion y Ventas---
        print("*** Gastos de Administracion y Ventas ***")
        DeprAyV = int(input("Ingrese los gastos de Depreciacion: "))
        SuelYSal = int(input("Ingrese los gastos en Sueldos Y Salarios: "))
        Comis = int(input("Ingrese el porcentaje de las comisiones [%]: ")) / 100
        VarAyV = ()
        for a in range(2):
            Var = int(input(f"Ingrese los gastos varios del semestre {a+1}: "))
            VarAyV = VarAyV + (Var,)

        InterXObli = int(input("Ingrese los gastos de Interses por obligaciones: "))
        print()

        #---Gastos de Fabricacion Indirectos---
        print("*** Gastos de Fabricacion Indirectos ***")
        DeprFI = int(input("Ingrese los gastos de Depreciacion: "))
        Seguros = int(input("Ingrese los gastos de Seguros: "))
        Mant = ()
        for b in range(2):
            man = int(input(f"Ingrese los gastos de mantenimiento del semestre {b+1}: "))
            Mant = Mant + (man,)

        Energ = ()
        for c in range(2):
            ene = int(input(f"Ingrese los gastos energeticos del semestre {c+1}: "))
            Energ = Energ + (ene,)

        VarFI = int(input("Ingrese los gastos varios: "))
        print()

        #---Datos Adicionales---
        print("*** Datos Adicionales ***")
        while True:
            respuesta1 = str(input("¿Se compro maquinaria nueva en este año? [Y/N]: "))
            if respuesta1.upper() == "Y":
                MaqNueva = int(input("Ingrese en cuanto esta valuada la maquina: "))
                break
            elif respuesta1.upper() == "N":
                break
            else:
                print("Respuesta no valida, vuelva a intentarlo.")

        ISr = int(input("Ingrese de cuanto sera el ISR [%]: ")) / 100
        PTu = int(input("Ingrese de cuanto sera el PTU [%]: ")) / 100
        extra1 = int(input("Ingrese cuanto se pagara de los materiales comprados [%]: ")) / 100
        extra2 = int(input("Ingrese cuanto se pagara de las ventas [%]: ")) / 100

        print()
        print("="*65)
        print("                       PRESUPUESTO MAESTRO")
        if float(numNomEmp).is_integer:
            numNomEmp = int(numNomEmp)
            ast = "*"*(numNomEmp - 1)
            print(f"{ast} {nomEmpresa} {ast}")
        else:
            nNERed = round(numNomEmp)
            ast1 = "*"*(nNERed - 1)
            ast2 = "*"*(nNERed - 2)
            print(f"{ast1} {nomEmpresa} {ast2}")
        print("="*65)
        print("                   I. Presupuesto de Operación")
        print("="*65)
        print()

        #---1. Presupuesto de ventas---

        ImpVen1A = tpl_prod[0][0] * tpl_prod[0][1]
        ImpVen2A = tpl_prod[1][0] * tpl_prod[1][1]
        ImpVenAñoA = ImpVen1A + ImpVen2A

        ImpVen1B = tpl_prod[0][2] * tpl_prod[0][3]
        ImpVen2B = tpl_prod[1][2] * tpl_prod[1][3]
        ImpVenAñoB = ImpVen1B + ImpVen2B

        ImpVen1C = tpl_prod[0][4] * tpl_prod[0][5]
        ImpVen2C = tpl_prod[1][4] * tpl_prod[1][5]
        ImpVenAñoC = ImpVen1C + ImpVen2C

        TotalVen1 = ImpVen1A + ImpVen1B + ImpVen1C
        TotalVen2 = ImpVen2A + ImpVen2B + ImpVen2C
        TotalAño = ImpVenAñoA + ImpVenAñoB + ImpVenAñoC

        print("-"*65)
        print("******************* 1.- PRESUPUESTO DE VENTAS *******************")
        print("-"*65)
        print(f"\t\t\t1er Semestre\t2do Semestre\t{año + 1}")
        print("-"*65)
        print("Producto A")
        print(f"Unidades a Vender\t{tpl_prod[0][1]}\t\t{tpl_prod[1][1]}")
        print(f"Precio de Venta\t\t{tpl_prod[0][0]}\t\t{tpl_prod[1][0]}")
        print(f"Importe de Venta\t{ImpVen1A}\t\t{ImpVen2A}\t\t{ImpVenAñoA}")
        print("-"*65)
        print("Producto B")
        print(f"Unidades a Vender\t{tpl_prod[0][3]}\t\t{tpl_prod[1][3]}")
        print(f"Precio de Venta\t\t{tpl_prod[0][2]}\t\t{tpl_prod[1][2]}")
        print(f"Importe de Venta\t{ImpVen1B}\t\t{ImpVen2B}\t\t{ImpVenAñoB}")
        print("-"*65)
        print("Producto C")
        print(f"Unidades a Vender\t{tpl_prod[0][5]}\t\t{tpl_prod[1][5]}")
        print(f"Precio de Venta\t\t{tpl_prod[0][4]}\t\t{tpl_prod[1][4]}")
        print(f"Importe de Venta\t{ImpVen1C}\t\t{ImpVen2C}\t\t{ImpVenAñoC}")
        print("-"*65)
        print(f"Total Ventas X Semestre\t{TotalVen1}\t\t{TotalVen2}\t\t{TotalAño}")
        print()

        #---2. Determinación del saldo de Clientes y Flujo de Entradas---

        TotalCli = Clientes + TotalAño
        CobraAño2 = TotalAño * extra2
        TotalEnt = Clientes + CobraAño2
        SaldoCli = TotalCli - TotalEnt

        print("-"*65)
        print("* 2.- Determinación del saldo de Clientes y Flujo de Entradas *")
        print("-"*65)
        print(f"Descripcion\t\t\tImporte\t\tTotal")
        print("-"*65)
        print(f"Saldo de clientes 31-Dic-{año}\t\t\t{Clientes}")
        print(f"Ventas {año + 1}\t\t\t\t\t{TotalAño}")
        print(f"Total de clientes {año + 1}\t\t\t\t{TotalCli}")
        print()
        print("Entradas de efectivo:")
        print(f"Por cobranza del {año}\t\t{Clientes}")
        print(f"Por cobranza del {año + 1}\t\t{CobraAño2}")
        print(f"Total de entradas {año + 1}\t\t\t\t{TotalEnt}")
        print()
        print(f"Saldo de clientes del {año + 1}\t\t\t{SaldoCli}")
        print()

        #---3. Presupuesto de Producción---

        totalUniA1 = tpl_infoinv[0][6] + tpl_prod[0][1]
        UniProdA1 = totalUniA1 - tpl_infoinv[0][6]
        totalUniA2 = tpl_infoinv[1][6] + tpl_prod[1][1]
        UniProdA2 = totalUniA2 - tpl_infoinv[0][6]
        totalUVenderA = tpl_prod[0][1] + tpl_prod[1][1]
        totalUA = totalUVenderA + tpl_infoinv[1][6]
        UniProdA = totalUA - tpl_infoinv[0][6]

        totalUniB1 = tpl_infoinv[0][7] + tpl_prod[0][3]
        UniProdB1 = totalUniB1 - tpl_infoinv[0][7]
        totalUniB2 = tpl_infoinv[1][7] + tpl_prod[1][3]
        UniProdB2 = totalUniB2 - tpl_infoinv[0][7]
        totalUVenderB = tpl_prod[0][3] + tpl_prod[1][3]
        totalUB = totalUVenderB + tpl_infoinv[1][7]
        UniProdB = totalUB - tpl_infoinv[0][7]

        totalUniC1 = tpl_infoinv[0][8] + tpl_prod[0][5]
        UniProdC1 = totalUniC1 - tpl_infoinv[0][8]
        totalUniC2 = tpl_infoinv[1][8] + tpl_prod[1][5]
        UniProdC2 = totalUniC2 - tpl_infoinv[0][8]
        totalUVenderC = tpl_prod[0][5] + tpl_prod[1][5]
        totalUC = totalUVenderC + tpl_infoinv[1][8]
        UniProdC = totalUC - tpl_infoinv[0][8]

        print("-"*65)
        print("***************** 3.- PRESUPUESTO DE PRODUCCION *****************")
        print("-"*65)
        print(f"\t\t\t1er Semestre\t2do Semestre\t{año + 1}")
        print("-"*65)
        print("Producto A")
        print(f"Unidades a Vender\t{tpl_prod[0][1]}\t\t{tpl_prod[1][1]}\t\t{totalUVenderA}")
        print(f"Inventario Final\t{tpl_infoinv[0][6]}\t\t{tpl_infoinv[1][6]}\t\t{tpl_infoinv[1][6]}")
        print(f"Total de Unidades\t{totalUniA1}\t\t{totalUniA2}\t\t{totalUA}")
        print(f"Inventario Inicial\t{tpl_infoinv[0][6]}\t\t{tpl_infoinv[0][6]}\t\t{tpl_infoinv[0][6]}")
        print(f"Unidades a Producir\t{UniProdA1}\t\t{UniProdA2}\t\t{UniProdA}")
        print("-"*65)
        print("Producto B")
        print(f"Unidades a Vender\t{tpl_prod[0][3]}\t\t{tpl_prod[1][3]}\t\t{totalUVenderB}")
        print(f"Inventario Final\t{tpl_infoinv[0][7]}\t\t{tpl_infoinv[1][7]}\t\t{tpl_infoinv[1][7]}")
        print(f"Total de Unidades\t{totalUniB1}\t\t{totalUniB2}\t\t{totalUB}")
        print(f"Inventario Inicial\t{tpl_infoinv[0][7]}\t\t{tpl_infoinv[0][7]}\t\t{tpl_infoinv[0][7]}")
        print(f"Unidades a Producir\t{UniProdB1}\t\t{UniProdB2}\t\t{UniProdB}")
        print("-"*65)
        print("Producto C")
        print(f"Unidades a Vender\t{tpl_prod[0][5]}\t\t{tpl_prod[1][5]}\t\t{totalUVenderC}")
        print(f"Inventario Final\t{tpl_infoinv[0][8]}\t\t{tpl_infoinv[1][8]}\t\t{tpl_infoinv[1][8]}")
        print(f"Total de Unidades\t{totalUniC1}\t\t{totalUniC2}\t\t{totalUC}")
        print(f"Inventario Inicial\t{tpl_infoinv[0][8]}\t\t{tpl_infoinv[0][8]}\t\t{tpl_infoinv[0][8]}")
        print(f"Unidades a Producir\t{UniProdC1}\t\t{UniProdC2}\t\t{UniProdC}")
        print()

        #---4. Presupuesto de Requerimiento de Materiales---

        totalMatA1_A = UniProdA1 * tpl_reqprod[0][0]
        totalMatA2_A = UniProdA2 * tpl_reqprod[0][0]
        totalMatA_A = UniProdA * tpl_reqprod[0][0]
        totalMatB1_A = UniProdA1 * tpl_reqprod[0][1]
        totalMatB2_A = UniProdA2 * tpl_reqprod[0][1]
        totalMatB_A = UniProdA * tpl_reqprod[0][1]
        totalMatC1_A = UniProdA1 * tpl_reqprod[0][2]
        totalMatC2_A = UniProdA2 * tpl_reqprod[0][2]
        totalMatC_A = UniProdA * tpl_reqprod[0][2]

        totalMatA1_B = UniProdB1 * tpl_reqprod[1][0]
        totalMatA2_B = UniProdB2 * tpl_reqprod[1][0]
        totalMatA_B = UniProdB * tpl_reqprod[1][0]
        totalMatB1_B = UniProdB1 * tpl_reqprod[1][1]
        totalMatB2_B = UniProdB2 * tpl_reqprod[1][1]
        totalMatB_B = UniProdB * tpl_reqprod[1][1]
        totalMatC1_B = UniProdB1 * tpl_reqprod[1][2]
        totalMatC2_B = UniProdB2 * tpl_reqprod[1][2]
        totalMatC_B = UniProdB * tpl_reqprod[1][2]

        totalMatA1_C = UniProdC1 * tpl_reqprod[2][0]
        totalMatA2_C = UniProdC2 * tpl_reqprod[2][0]
        totalMatA_C = UniProdC * tpl_reqprod[2][0]
        totalMatB1_C = UniProdC1 * tpl_reqprod[2][1]
        totalMatB2_C = UniProdC2 * tpl_reqprod[2][1]
        totalMatB_C = UniProdC * tpl_reqprod[2][1]
        totalMatC1_C = UniProdC1 * tpl_reqprod[2][2]
        totalMatC2_C = UniProdC2 * tpl_reqprod[2][2]
        totalMatC_C = UniProdC * tpl_reqprod[2][2]

        totalMatA1 = totalMatA1_A + totalMatA1_B + totalMatA1_C
        totalMatA2 = totalMatA2_A + totalMatA2_B + totalMatA2_C
        totalMatA = totalMatA_A + totalMatA_B + totalMatA_C
        totalMatB1 = totalMatB1_A + totalMatB1_B + totalMatB1_C
        totalMatB2 = totalMatB2_A + totalMatB2_B + totalMatB2_C
        totalMatB = totalMatB_A + totalMatB_B + totalMatB_C
        totalMatC1 = totalMatC1_A + totalMatC1_B + totalMatC1_C
        totalMatC2 = totalMatC2_A + totalMatC2_B + totalMatC2_C
        totalMatC = totalMatC_A + totalMatC_B + totalMatC_C


        print("-"*65)
        print("******** 4.- Presupuesto de Requerimiento de Materiales *******")
        print("-"*65)
        print(f"\t\t\t1er Semestre\t2do Semestre\t{año + 1}")
        print("-"*65)
        print("Producto A")
        print(f"Unidades a Producir\t{UniProdA1}\t\t{UniProdA2}\t\t{UniProdA}")
        print()
        print("Material A")
        print(f"Req. de Material\t{tpl_reqprod[0][0]}\t\t{tpl_reqprod[0][0]}\t\t{tpl_reqprod[0][0]}")
        print(f"Total Mat.A Req.\t{totalMatA1_A}\t\t{totalMatA2_A}\t\t{totalMatA_A}")
        print("Material B")
        print(f"Req. de Material\t{tpl_reqprod[0][1]}\t\t{tpl_reqprod[0][1]}\t\t{tpl_reqprod[0][1]}")
        print(f"Total Mat.B Req.\t{totalMatB1_A}\t\t{totalMatB2_A}\t\t{totalMatB_A}")
        print("Material C")
        print(f"Req. de Material\t{tpl_reqprod[0][2]}\t\t{tpl_reqprod[0][2]}\t\t{tpl_reqprod[0][2]}")
        print(f"Total Mat.C Req.\t{totalMatC1_A}\t\t{totalMatC2_A}\t\t{totalMatC_A}")
        print("-"*65)
        print("Producto B")
        print(f"Unidades a Producir\t{UniProdB1}\t\t{UniProdB2}\t\t{UniProdB}")
        print()
        print("Material A")
        print(f"Req. de Material\t{tpl_reqprod[1][0]}\t\t{tpl_reqprod[1][0]}\t\t{tpl_reqprod[1][0]}")
        print(f"Total Mat.A Req.\t{totalMatA1_B}\t\t{totalMatA2_B}\t\t{totalMatA_B}")
        print("Material B")
        print(f"Req. de Material\t{tpl_reqprod[1][1]}\t\t{tpl_reqprod[1][1]}\t\t{tpl_reqprod[1][1]}")
        print(f"Total Mat.B Req.\t{totalMatB1_B}\t\t{totalMatB2_B}\t\t{totalMatB_B}")
        print("Material C")
        print(f"Req. de Material\t{tpl_reqprod[1][2]}\t\t{tpl_reqprod[1][2]}\t\t{tpl_reqprod[1][2]}")
        print(f"Total Mat.C Req.\t{totalMatC1_B}\t\t{totalMatC2_B}\t\t{totalMatC_B}")
        print("-"*65)
        print("Producto C")
        print(f"Unidades a Producir\t{UniProdC1}\t\t{UniProdC2}\t\t{UniProdC}")
        print()
        print("Material A")
        print(f"Req. de Material\t{tpl_reqprod[2][0]}\t\t{tpl_reqprod[2][0]}\t\t{tpl_reqprod[2][0]}")
        print(f"Total Mat.A Req.\t{totalMatA1_C}\t\t{totalMatA2_C}\t\t{totalMatA_C}")
        print("Material B")
        print(f"Req. de Material\t{tpl_reqprod[2][1]}\t\t{tpl_reqprod[2][1]}\t\t{tpl_reqprod[2][1]}")
        print(f"Total Mat.B Req.\t{totalMatB1_C}\t\t{totalMatB2_C}\t\t{totalMatB_C}")
        print("Material C")
        print(f"Req. de Material\t{tpl_reqprod[2][2]}\t\t{tpl_reqprod[2][2]}\t\t{tpl_reqprod[2][2]}")
        print(f"Total Mat.C Req.\t{totalMatC1_C}\t\t{totalMatC2_C}\t\t{totalMatC_C}")
        print("-"*65)
        print("Total de Requerimientos (Gramos)")
        print(f"Material A\t\t{totalMatA1}\t\t{totalMatA2}\t\t{totalMatA}")
        print(f"Material B\t\t{totalMatB1}\t\t{totalMatB2}\t\t{totalMatB}")
        print(f"Material C\t\t{totalMatC1}\t\t{totalMatC2}\t\t{totalMatC}")
        print()

        #---5. Presupuesto de Compra de Materiales---

        ttlMatA1 = totalMatA1 + tpl_infoinv[0][0]
        ttlMatA2 = totalMatA2 + tpl_infoinv[1][0]
        ttlMatA = totalMatA + tpl_infoinv[1][0]
        matCompA1 = ttlMatA1 - tpl_infoinv[0][0]
        matCompA2 = ttlMatA2 - tpl_infoinv[0][0]
        matCompA = ttlMatA - tpl_infoinv[0][0]
        ttlEfecMatA1 = matCompA1 * tpl_infoinv[0][3]
        ttlEfecMatA2 = matCompA2 * tpl_infoinv[1][3]
        ttlEfecMatA = ttlEfecMatA1 + ttlEfecMatA2

        ttlMatB1 = totalMatB1 + tpl_infoinv[0][1]
        ttlMatB2 = totalMatB2 + tpl_infoinv[1][1]
        ttlMatB = totalMatB + tpl_infoinv[1][1]
        matCompB1 = ttlMatB1 - tpl_infoinv[0][1]
        matCompB2 = ttlMatB2 - tpl_infoinv[0][1]
        matCompB = ttlMatB - tpl_infoinv[0][1]
        ttlEfecMatB1 = matCompB1 * tpl_infoinv[0][4]
        ttlEfecMatB2 = matCompB2 * tpl_infoinv[1][4]
        ttlEfecMatB = ttlEfecMatB1 + ttlEfecMatB2

        ttlMatC1 = totalMatC1 + tpl_infoinv[0][2]
        ttlMatC2 = totalMatC2 + tpl_infoinv[1][2]
        ttlMatC = totalMatC + tpl_infoinv[1][2]
        matCompC1 = ttlMatC1 - tpl_infoinv[0][2]
        matCompC2 = ttlMatC2 - tpl_infoinv[0][2]
        matCompC = ttlMatC - tpl_infoinv[0][2]
        ttlEfecMatC1 = matCompC1 * tpl_infoinv[0][5]
        ttlEfecMatC2 = matCompC2 * tpl_infoinv[1][5]
        ttlEfecMatC = ttlEfecMatC1 + ttlEfecMatC2

        compTotal1 = ttlEfecMatA1 + ttlEfecMatB1 + ttlEfecMatC1
        compTotal2 = ttlEfecMatA2 + ttlEfecMatB2 + ttlEfecMatC2
        compTotal = ttlEfecMatA + ttlEfecMatB + ttlEfecMatC

        print("-"*65)
        print("************ 5. Presupuesto de Compra de Materiales ***********")
        print("-"*65)
        print(f"\t\t\t1er Semestre\t2do Semestre\t{año + 1}")
        print("-"*65)
        print("Material A")
        print(f"Req. de Material\t{totalMatA1}\t\t{totalMatA2}\t\t{totalMatA}")
        print(f"Inventario Final\t{tpl_infoinv[0][0]}\t\t{tpl_infoinv[1][0]}\t\t{tpl_infoinv[1][0]}")
        print(f"Total de Material\t{ttlMatA1}\t\t{ttlMatA2}\t\t{ttlMatA}")
        print(f"Inventario Inicial\t{tpl_infoinv[0][0]}\t\t{tpl_infoinv[0][0]}\t\t{tpl_infoinv[0][0]}")
        print(f"Material a Comprar\t{matCompA1}\t\t{matCompA2}\t\t{matCompA}")
        print(f"Precio de Compra\t{tpl_infoinv[0][3]}\t\t{tpl_infoinv[1][3]}")
        print(f"Total Mat.A en $\t{ttlEfecMatA1}\t{ttlEfecMatA2}\t{ttlEfecMatA}")
        print("-"*65)
        print("Material B")
        print(f"Req. de Material\t{totalMatB1}\t\t{totalMatB2}\t\t{totalMatB}")
        print(f"Inventario Final\t{tpl_infoinv[0][1]}\t\t{tpl_infoinv[1][1]}\t\t{tpl_infoinv[1][1]}")
        print(f"Total de Material\t{ttlMatB1}\t\t{ttlMatB2}\t\t{ttlMatB}")
        print(f"Inventario Inicial\t{tpl_infoinv[0][1]}\t\t{tpl_infoinv[0][1]}\t\t{tpl_infoinv[0][1]}")
        print(f"Material a Comprar\t{matCompB1}\t\t{matCompB2}\t\t{matCompB}")
        print(f"Precio de Compra\t{tpl_infoinv[0][4]}\t\t{tpl_infoinv[1][4]}")
        print(f"Total Mat.B en $\t{ttlEfecMatB1}\t{ttlEfecMatB2}\t\t{ttlEfecMatB}")
        print("-"*65)
        print("Material C")
        print(f"Req. de Material\t{totalMatC1}\t\t{totalMatC2}\t\t{totalMatC}")
        print(f"Inventario Final\t{tpl_infoinv[0][2]}\t\t{tpl_infoinv[1][2]}\t\t{tpl_infoinv[1][2]}")
        print(f"Total de Material\t{ttlMatC1}\t\t{ttlMatC2}\t\t{ttlMatC}")
        print(f"Inventario Inicial\t{tpl_infoinv[0][2]}\t\t{tpl_infoinv[0][2]}\t\t{tpl_infoinv[0][2]}")
        print(f"Material a Comprar\t{matCompC1}\t\t{matCompC2}\t\t{matCompC}")
        print(f"Precio de Compra\t{tpl_infoinv[0][5]}\t\t{tpl_infoinv[1][5]}")
        print(f"Total Mat.C en $\t{ttlEfecMatC1}\t{ttlEfecMatC2}\t{ttlEfecMatC}")
        print()
        print(f"Compras Totales\t\t{compTotal1}\t{compTotal2}\t{compTotal}")
        print()

        #---6. Determinación del saldo de Proveedores y Flujo de Salidas---

        TotalProv = Prov + compTotal
        ProvAño = compTotal * extra1
        TotalSal = Prov + ProvAño
        SaldoProv = TotalProv - TotalSal

        print("-"*65)
        print("* 6. Determinación del saldo de Proveedores y Flujo de Salidas *")
        print("-"*65)
        print(f"Descripcion\t\t\tImporte\t\tTotal")
        print("-"*65)
        print(f"Saldo de Proveedores 31-Dic-{año}\t\t{Prov}")
        print(f"Compras {año + 1}\t\t\t\t\t{compTotal}")
        print(f"Total de Proveedores {año + 1}\t\t\t{TotalProv}")
        print()
        print("Salidas de efectivo:")
        print(f"Por Proveedores del {año}\t{Prov}")
        print(f"Por Proveedores del {año + 1}\t{ProvAño}")
        print(f"Total de salidas {año + 1}\t\t\t\t{TotalSal}")
        print()
        print(f"Saldo de Proveedores del {año + 1}\t\t\t{SaldoProv}")
        print()

        #---7. Presupuesto de Mano de Obra Directa---

        totalHrsReqA1 = UniProdA1 * tpl_reqprod[0][3]
        totalHrsReqA2 = UniProdA2 * tpl_reqprod[0][3]
        totalHrsReqA = UniProdA * tpl_reqprod[0][3]
        impMODa1 = totalHrsReqA1 * costManObra1
        impMODa2 = totalHrsReqA2 * costManObra2
        impMODa = impMODa1 + impMODa2

        totalHrsReqB1 = UniProdB1 * tpl_reqprod[1][3]
        totalHrsReqB2 = UniProdB2 * tpl_reqprod[1][3]
        totalHrsReqB = UniProdB * tpl_reqprod[1][3]
        impMODb1 = totalHrsReqB1 * costManObra1
        impMODb2 = totalHrsReqB2 * costManObra2
        impMODb = impMODb1 + impMODb2

        totalHrsReqC1 = UniProdC1 * tpl_reqprod[2][3]
        totalHrsReqC2 = UniProdC2 * tpl_reqprod[2][3]
        totalHrsReqC = UniProdC * tpl_reqprod[2][3]
        impMODc1 = totalHrsReqC1 * costManObra1
        impMODc2 = totalHrsReqC2 * costManObra2
        impMODc = impMODc1 + impMODc2

        ttlHrsReqSem1 = totalHrsReqA1 + totalHrsReqB1 + totalHrsReqC1
        ttlHrsReqSem2 = totalHrsReqA2 + totalHrsReqB2 + totalHrsReqC2
        ttlHrsReqSem = totalHrsReqA + totalHrsReqB + totalHrsReqC

        ttlMODsem1 = impMODa1 + impMODb1 + impMODc1
        ttlMODsem2 = impMODa2 + impMODb2 + impMODc2
        ttlMODsem = impMODa + impMODb + impMODc

        print("-"*65)
        print("************ 7.- Presupuesto de Mano de Obra Directa ************")
        print("-"*65)
        print(f"\t\t\t1er Semestre\t2do Semestre\t{año + 1}")
        print("-"*65)
        print("Producto A")
        print(f"Unidades a Producir\t{UniProdA1}\t\t{UniProdA2}\t\t{UniProdA}")
        print(f"Hrs Req. X Unidad\t{tpl_reqprod[0][3]}\t\t{tpl_reqprod[0][3]}\t\t{tpl_reqprod[0][3]}")
        print(f"Total de hrs req.\t{totalHrsReqA1}\t\t{totalHrsReqA2}\t\t{totalHrsReqA}")
        print(f"Cuota por hora\t\t{costManObra1}\t\t{costManObra2}")
        print(f"Importe de M.O.D.\t{impMODa1}\t\t{impMODa2}\t\t{impMODa}")
        print("-"*65)
        print("Producto B")
        print(f"Unidades a Producir\t{UniProdB1}\t\t{UniProdB2}\t\t{UniProdB}")
        print(f"Hrs Req. X Unidad\t{tpl_reqprod[1][3]}\t\t{tpl_reqprod[1][3]}\t\t{tpl_reqprod[1][3]}")
        print(f"Total de hrs req.\t{totalHrsReqB1}\t\t{totalHrsReqB2}\t\t{totalHrsReqB}")
        print(f"Cuota por hora\t\t{costManObra1}\t\t{costManObra2}")
        print(f"Importe de M.O.D.\t{impMODb1}\t\t{impMODb2}\t\t{impMODb}")
        print("-"*65)
        print("Producto C")
        print(f"Unidades a Producir\t{UniProdC1}\t\t{UniProdC2}\t\t{UniProdC}")
        print(f"Hrs Req. X Unidad\t{tpl_reqprod[2][3]}\t\t{tpl_reqprod[2][3]}\t\t{tpl_reqprod[2][3]}")
        print(f"Total de hrs req.\t{totalHrsReqC1}\t\t{totalHrsReqC2}\t\t{totalHrsReqC}")
        print(f"Cuota por hora\t\t{costManObra1}\t\t{costManObra2}")
        print(f"Importe de M.O.D.\t{impMODc1}\t\t{impMODc2}\t\t{impMODc}")
        print("-"*65)
        print(f"Total hrs req x sem\t{ttlHrsReqSem1}\t\t{ttlHrsReqSem2}\t\t{ttlHrsReqSem}")
        print(f"Total M.O.D. x sem\t{ttlMODsem1}\t\t{ttlMODsem2}\t\t{ttlMODsem}")
        print()

        #---8. Presupuesto de Gastos Indirectos de Fabricación---

        ttlGIFsem1 = (DeprFI/2) + (Seguros/2) + Mant[0] + Energ[0] + (VarFI/2)
        ttlGIFsem2 = (DeprFI/2) + (Seguros/2) + Mant[1] + Energ[1] + (VarFI/2)
        ttlGIFsem = DeprFI + Seguros + (Mant[0] + Mant[1]) + (Energ[0] + Energ[1]) + VarFI
        costHrGIF = ttlGIFsem / ttlHrsReqSem

        print("-"*65)
        print("****** 8.- Presupuesto de Gastos Indirectos de Fabricación ******")
        print("-"*65)
        print(f"\t\t\t1er Semestre\t2do Semestre\t{año + 1}")
        print("-"*65)
        print(f"Depreciacion\t\t{DeprFI/2}\t\t{DeprFI/2}\t\t{DeprFI}")
        print(f"Seguros\t\t\t{Seguros/2}\t\t{Seguros/2}\t\t{Seguros}")
        print(f"Mantenimiento\t\t{Mant[0]}\t\t{Mant[1]}\t\t{Mant[0]+Mant[1]}")
        print(f"Energeticos\t\t{Energ[0]}\t\t{Energ[1]}\t\t{Energ[0]+Energ[1]}")
        print(f"Varios\t\t\t{VarFI/2}\t\t{VarFI/2}\t\t{VarFI}")
        print(f"Total GIFxSem\t\t{ttlGIFsem1}\t{ttlGIFsem2}\t{ttlGIFsem}")
        print("-"*65)
        print("Coeficiente para determinar el costo x hora de G.I.F.")
        print(f"Total de G.I.F.\t\t\t\t\t\t{ttlGIFsem}")
        print(f"Total hrs M.O.D. Anual\t\t\t\t\t{ttlHrsReqSem}")
        print(f"Costo x hora de G.I.F.\t\t\t\t\t{costHrGIF}")
        print()

        #---9. Presupuesto de Gastos de Operación---

        coms1 = TotalVen1 * Comis
        coms2 = TotalVen2 * Comis
        coms = coms1 + coms2

        ttlGasOp1 = (DeprAyV/2) + (SuelYSal/2) + coms1 + VarAyV[0] + (InterXObli/2)
        ttlGasOp2 = (DeprAyV/2) + (SuelYSal/2) + coms2 + VarAyV[1] + (InterXObli/2)
        ttlGasOp = DeprAyV + SuelYSal + coms + (VarAyV[0] + VarAyV[1]) + InterXObli

        print("-"*65)
        print("************* 9. Presupuesto de Gastos de Operación *************")
        print("-"*65)
        print(f"\t\t\t1er Semestre\t2do Semestre\t{año + 1}")
        print("-"*65)
        print(f"Depreciacion\t\t{DeprAyV/2}\t\t{DeprAyV/2}\t\t{DeprAyV}")
        print(f"Sueldos y Salarios\t{SuelYSal/2}\t{SuelYSal/2}\t{SuelYSal}")
        print(f"Comisiones\t\t{coms1}\t{coms2}\t{coms}")
        print(f"Varios\t\t\t{VarAyV[0]}\t\t{VarAyV[1]}\t\t{VarAyV[0]+VarAyV[1]}")
        print(f"Ints.X Obls\t\t{InterXObli/2}\t\t{InterXObli/2}\t\t{InterXObli}")
        print(f"Total Gastos Oper.\t{ttlGasOp1}\t{ttlGasOp2}\t{ttlGasOp}")
        print()

        #---10.- Determinación del Costo Unitario de Productos Terminados---

        CUmatAa = tpl_infoinv[1][3] * tpl_reqprod[0][0]
        CUmatBa = tpl_infoinv[1][4] * tpl_reqprod[0][1]
        CUmatCa = tpl_infoinv[1][5] * tpl_reqprod[0][2]
        CUmanoOa = costManObra2 * tpl_reqprod[0][3]
        CUgifA = costHrGIF * tpl_reqprod[0][3]
        CUa = CUmatAa + CUmatBa + CUmatCa + CUmanoOa + CUgifA

        CUmatAb = tpl_infoinv[1][3] * tpl_reqprod[1][0]
        CUmatBb = tpl_infoinv[1][4] * tpl_reqprod[1][1]
        CUmatCb = tpl_infoinv[1][5] * tpl_reqprod[1][2]
        CUmanoOb = costManObra2 * tpl_reqprod[1][3]
        CUgifB = costHrGIF * tpl_reqprod[1][3]
        CUb = CUmatAb + CUmatBb + CUmatCb + CUmanoOb + CUgifB

        CUmatAc = tpl_infoinv[1][3] * tpl_reqprod[2][0]
        CUmatBc = tpl_infoinv[1][4] * tpl_reqprod[2][1]
        CUmatCc = tpl_infoinv[1][5] * tpl_reqprod[2][2]
        CUmanoOc = costManObra2 * tpl_reqprod[2][3]
        CUgifC = costHrGIF * tpl_reqprod[2][3]
        CUc = CUmatAc + CUmatBc + CUmatCc + CUmanoOc + CUgifC

        print("-"*65)
        print("* 10.- Determinación del Costo Unitario de Productos Terminados *")
        print("-"*65)
        print("************************** Producto A ***************************")
        print("Descripcion\t\tCosto\tCantidad\tCosto Unitario")
        print("-"*65)
        print(f"Material A\t\t{tpl_infoinv[1][3]}\t{tpl_reqprod[0][0]}\t\t{CUmatAa}")
        print(f"Material B\t\t{tpl_infoinv[1][4]}\t{tpl_reqprod[0][1]}\t\t{CUmatBa}")
        print(f"Material C\t\t{tpl_infoinv[1][5]}\t{tpl_reqprod[0][2]}\t\t{CUmatCa}")
        print(f"Mano de Obra\t\t{costManObra2}\t{tpl_reqprod[0][3]}\t\t{CUmanoOa}")
        print(f"G.I.F.\t\t\t{costHrGIF}\t{tpl_reqprod[0][3]}\t\t{CUgifA}")
        print(f"Costo Unitario\t\t\t\t\t{CUa}")
        print("-"*65)
        print("************************** Producto B ***************************")
        print("Descripcion\t\tCosto\tCantidad\tCosto Unitario")
        print("-"*65)
        print(f"Material A\t\t{tpl_infoinv[1][3]}\t{tpl_reqprod[1][0]}\t\t{CUmatAb}")
        print(f"Material B\t\t{tpl_infoinv[1][4]}\t{tpl_reqprod[1][1]}\t\t{CUmatBb}")
        print(f"Material C\t\t{tpl_infoinv[1][5]}\t{tpl_reqprod[1][2]}\t\t{CUmatCb}")
        print(f"Mano de Obra\t\t{costManObra2}\t{tpl_reqprod[1][3]}\t\t{CUmanoOb}")
        print(f"G.I.F.\t\t\t{costHrGIF}\t{tpl_reqprod[1][3]}\t\t{CUgifB}")
        print(f"Costo Unitario\t\t\t\t\t{CUb}")
        print("-"*65)
        print("************************** Producto C ***************************")
        print("Descripcion\t\tCosto\tCantidad\tCosto Unitario")
        print("-"*65)
        print(f"Material A\t\t{tpl_infoinv[1][3]}\t{tpl_reqprod[2][0]}\t\t{CUmatAc}")
        print(f"Material B\t\t{tpl_infoinv[1][4]}\t{tpl_reqprod[2][1]}\t\t{CUmatBc}")
        print(f"Material C\t\t{tpl_infoinv[1][5]}\t{tpl_reqprod[2][2]}\t\t{CUmatCc}")
        print(f"Mano de Obra\t\t{costManObra2}\t{tpl_reqprod[2][3]}\t\t{CUmanoOc}")
        print(f"G.I.F.\t\t\t{costHrGIF}\t{tpl_reqprod[2][3]}\t\t{CUgifC}")
        print(f"Costo Unitario\t\t\t\t\t{CUc}")
        print()

        #---11.- Valuación de Inventarios Finales---

        cosTotalMatA = tpl_infoinv[1][0] * tpl_infoinv[1][3]
        cosTotalMatB = tpl_infoinv[1][1] * tpl_infoinv[1][4]
        cosTotalMatC = tpl_infoinv[1][2] * tpl_infoinv[1][5]
        invFinalMat = cosTotalMatA + cosTotalMatB + cosTotalMatC
        
        cosTotalProdA = tpl_infoinv[1][6] * CUa
        cosTotalProdB = tpl_infoinv[1][7] * CUb
        cosTotalProdC = tpl_infoinv[1][8] * CUc
        invFinalProdTer = cosTotalProdA + cosTotalProdB + cosTotalProdC 

        print("-"*65)
        print("************* 11.- Valuación de Inventarios Finales *************")
        print("-"*65)
        print("**************** Inventario Final de Materiales *****************")
        print("Descripcion\tUnidades\tCosto Unitario\tCosto Total")
        print("-"*65)
        print(f"Material A\t{tpl_infoinv[1][0]}\t\t{tpl_infoinv[1][3]}\t\t{cosTotalMatA}")
        print(f"Material B\t{tpl_infoinv[1][1]}\t\t{tpl_infoinv[1][4]}\t\t{cosTotalMatB}")
        print(f"Material C\t{tpl_infoinv[1][2]}\t\t{tpl_infoinv[1][5]}\t\t{cosTotalMatC}")
        print(f"Inv. Final de Mat.\t\t\t\t{invFinalMat}")
        print("-"*65)
        print("************ Inventario Final de Producto Terminado *************")
        print("Descripcion\tUnidades\tCosto Unitario\tCosto Total")
        print("-"*65)
        print(f"Producto A\t{tpl_infoinv[1][6]}\t\t{CUa}\t\t{cosTotalProdA}")
        print(f"Producto B\t{tpl_infoinv[1][7]}\t\t{CUb}\t\t{cosTotalProdB}")
        print(f"Producto C\t{tpl_infoinv[1][8]}\t\t{CUc}\t\t{cosTotalProdC}")
        print(f"Inv. Final de Prod. Terminado\t\t\t{invFinalProdTer}")
        print()

        print("="*65)
        print("                   II. Presupuesto Financiero.")
        print("="*65)
        print()

        matDisp = InvMat + compTotal
        matUti = matDisp - invFinalMat
        costoProd = matUti + ttlMODsem + ttlGIFsem
        totalProdDisp = costoProd + InvArtTerm
        costoVen = totalProdDisp - invFinalProdTer

        print("-"*65)
        if float(numNomEmp).is_integer:
            print(f"{ast} {nomEmpresa} {ast}")
        else:
            print(f"{ast1} {nomEmpresa} {ast2}")
        print("-"*65)
        print("             Estado de Costo de Producción y Ventas")
        print("      Presupuesto del 1 de Enero al 31 de Diciembre del 2009")
        print("-"*65)
        print(f"Saldo Inicial de Materiales\t\t\t\t{InvMat}")
        print(f"Compras de Materiales\t\t\t\t\t{compTotal}")
        print(f"Material Disponible\t\t\t\t\t{matDisp}")
        print(f"Invebtario Final de Materiales\t\t\t\t{invFinalMat}")
        print(f"Materiales Utilizados\t\t\t\t\t{matUti}")
        print(f"Mano de Obra Directa\t\t\t\t\t{ttlMODsem}")
        print(f"Gastos de Fabricación Indirectos\t\t\t{ttlGIFsem}")
        print(f"Costo de Produccion\t\t\t\t\t{costoProd}")
        print(f"Inventario Inicial de Productos Terminados\t\t{InvArtTerm}")
        print(f"Total de Producción Disponible\t\t\t\t{totalProdDisp}")
        print(f"Inventario Final de Productos Terminados\t\t{invFinalProdTer}")
        print(f"Costo de Ventas\t\t\t\t\t\t{costoVen}")
        print()

        utiBruta = TotalAño - costoVen
        utiOperacion = utiBruta - ttlGasOp
        isr = utiOperacion * ISr
        isr = round(isr)
        ptu = utiOperacion * PTu
        ptu = round(ptu)
        utiNeta = (utiOperacion - isr) - ptu

        print("-"*65)
        if float(numNomEmp).is_integer:
            print(f"{ast} {nomEmpresa} {ast}")
        else:
            print(f"{ast1} {nomEmpresa} {ast2}")
        print("-"*65)
        print("                      Estado de Resultados")
        print("      Presupuesto del 1 de Enero al 31 de Diciembre del 2009")
        print("-"*65)
        print(f"Ventas\t\t\t\t\t\t\t{TotalAño}")
        print(f"Costo de Ventas\t\t\t\t\t\t{costoVen}")
        print(f"Utilidad Bruta\t\t\t\t\t\t{utiBruta}")
        print(f"Gastos de Operacion\t\t\t\t\t{ttlGasOp}")
        print(f"Utilidad de Operacion\t\t\t\t\t{utiOperacion}")
        print(f"ISR\t\t\t\t\t\t\t{isr}")
        print(f"PTU\t\t\t\t\t\t\t{ptu}")
        print(f"Utilidad Neta\t\t\t\t\t\t{utiNeta}")

        ttlEntra = CobraAño2 + Clientes
        efecDisp = ttlEntra + Efectivo
        GIFsinDepr = ttlGIFsem - DeprFI
        GOsinDepr = ttlGasOp - DeprAyV
        ttlSalidas = ProvAño + Prov + ttlMODsem + GIFsinDepr + GOsinDepr + MaqNueva + ISRacu + isr
        fluEfecActual = efecDisp - ttlSalidas

        print("-"*65)
        if float(numNomEmp).is_integer:
            print(f"{ast} {nomEmpresa} {ast}")
        else:
            print(f"{ast1} {nomEmpresa} {ast2}")
        print("-"*65)
        print("                   Estado de Flujo de Efectivo")
        print("      Presupuesto del 1 de Enero al 31 de Diciembre del 2009")
        print("-"*65)
        print(f"""Saldo Inicial de Efectivo\t\t\t\t{Efectivo}
Entradas:
Cobranza 2009\t\t\t\t{CobraAño2}
Cobranza 2008\t\t\t\t{Clientes}
Total de Entradas\t\t\t\t\t{ttlEntra}
Efectivo Disponible\t\t\t\t\t{efecDisp}
Salidas:
Proveedores 2009\t\t\t{ProvAño}
Proveedores 2008\t\t\t{Prov}
Pago Mano de Obra Directa\t\t{ttlMODsem}
Pago Gastos Indirectos de Fabricación\t{GIFsinDepr}
Pago de Gastos de Operación\t\t{GOsinDepr}
Compra de Activo Fijo (Maquinaria)\t{MaqNueva}
Pago ISR 2008\t\t\t\t{ISRacu}
Pago ISR 2009\t\t\t\t{isr}
Total de Salidas\t\t\t\t\t{ttlSalidas}
Flujo de Efectivo Actual\t\t\t\t{fluEfecActual}""")

        ttlActCirc = fluEfecActual + SaldoCli + invFinalMat + invFinalProdTer
        PyE = PlantEqui + MaqNueva
        DeprAcu2 = DeprAcu + DeprAyV + DeprFI
        ttlActNoCirc = Terreno + PyE - DeprAcu2
        ActivoTotal = ttlActCirc + ttlActNoCirc
        ttlPasivoCP = SaldoProv + DocsXpag + ptu
        PasivoTotal = ttlPasivoCP + ObliXpag
        ttlCapiCont = CapAport + CapGanado + utiNeta
        sumPasCap = PasivoTotal + ttlCapiCont

        print("-"*65)
        if float(numNomEmp).is_integer:
            print(f"{ast} {nomEmpresa} {ast}")
        else:
            print(f"{ast1} {nomEmpresa} {ast2}")
        print("-"*65)
        print("                         Balance General")
        print("      Presupuesto del 1 de Enero al 31 de Diciembre del 2009")
        print("-"*65)
        print(f"""ACTIVO
Circulante
Efectivo\t\t\t\t{fluEfecActual}
Clientes\t\t\t\t{SaldoCli}
Inventario de Materiales\t\t{invFinalMat}
Inventario de Producto Terminado\t{invFinalProdTer}
Total de Activos Circulantes:\t\t\t\t{ttlActCirc}

No Circulante
Terreno\t\t\t\t\t{Terreno}
Planta y Equipo\t\t\t\t{PyE}
Depreciación Acumulada\t\t\t{DeprAcu2}
Total Activos No Circulante\t\t\t\t{ttlActNoCirc}

ACTIVO TOTAL\t\t\t\t\t\t{ActivoTotal}

PASIVO
Corto Plazo
Proveedores\t\t\t\t{SaldoProv}
Documentos por Pagar\t\t\t{DocsXpag}
ISR por Pagar\t\t\t\t0
PTU por Pagar\t\t\t\t{ptu}
Total de Pasivo Corto Plazo:\t\t\t\t{ttlPasivoCP}

Largo Plazo
Obligaciones por Pagar\t\t\t{ObliXpag}
Total de Pasivo Largo Plazo:\t\t\t\t{ObliXpag}

PASIVO TOTAL\t\t\t\t\t\t{PasivoTotal}

CAPITAL CONTABLE
Capital Aportado\t\t\t{CapAport}
Capital Ganado\t\t\t\t{CapGanado}
Utilidad del Ejercicio\t\t\t{utiNeta}
Total de Capital Contable\t\t\t\t{ttlCapiCont}

SUMA DE PASIVO Y CAPITAL\t\t\t\t{sumPasCap}""")
        print()

        print(f"Activo Total - Suma de Pasivo y Capital: {ActivoTotal - sumPasCap}")

    elif menu == "2":
        print("Gracias por usar nuestro programa!")
        continuar = False

    else:
        print("Opcion no valida")