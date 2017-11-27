import time
import sys


def registrar(lista):
    lista = {"a": ">> Matematica I", "b": ">> Fisica I", "c": ">> Introduccion a la Ciencia de la Computación",
             "d": ">> Desafios Globales", "e": ">> Lab. de Comunicación I",
             "f": ">> Quimica General", "g": ">> Quimica Experimental", "h": ">> Matematica II", "i": ">> Fisica II",
             "j": ">> Ciencias de los Materiales", "k": ">> Programación Orientada a Objetos",
             "l": ">> Lab. de Comunicación II", "m": ">> Ingles I", "n": ">> Proyecto Interdisciplinario I",
             "o": ">> Intro. al Desarrollo de Empresas", "p": ">> Matematica III",
             "q": ">> Termodinamica", "r": ">> Estadistica y Probabilidades", "s": ">> Ingles II",
             "t": ">> Gestion de Empresas", "u": ">> Proyecto Interdisciplinario II"}

    if cil == "1":
        print(" "+"\nII) Estos son los cursos que llevaras durante el ciclo:")
        for i in cursos2:
            print(i)
            print("")
            print("*¡GRACIAS POR REGISTRARTE!*\n¿Deseas entrar a comsultar?")
            perm = input("-> ")
            if perm =="si":
                print(opte())
            elif perm != "si":
                return("¡Vuelva pronto!...")




    elif cil =="2" or cil=="3":
        var2 = int(input(" "+"\n¿Cuantos cursos vas a llevar?(≤8):"))
        if var2 > 8:
            print("¡Lo sentimos, a sobrepasado el limite de cursos a llevar!")
            sys.exit(0)


        else:
            for i in cursos4:
                print(i)
                print("")
                print("Ahora, ¿Qué cursos deseas llevar? ")
            for j in range(1, var2 + 1):
                var3 = input("Curso#" + str(j) + ":")
            print(" " + "\nII) Estos son los cursos que llevaras durante el ciclo:")
            for i in var3:
                print(lista[i])



        print(" ")
        print("*¡GRACIAS POR REGISTRARTE!*\n¿Deseas entrar a comsultar?")
        pom = input("--> ")
        if pom == "si":
            print("-"*23+"¡Bienvenido Kachimbo!!"+"-"*23)
            print(opta())
        elif pom != "no":
            return ("¡Vuelva pronto!...")


    else:
        print(">-"*21+"\nEste ciclo no esta dentro de las consultas\n"
              "\t ¡Por favor ingrese de nuevo!\n"+">-"*21)
        sys.exit(0)


def iniciar_sesion():
    c = input("Ingresa tu código: ")
    s = input("Ingresa tu carrera: ")
    print("-"*25+ "¡Bienvenido " + nomb +"!!"+"-"*25+"\n¿Que deseas consultar? \n1. Créditos\n2. Pensiones\n3. Menú de la semana\n4. Cubiculos")
    op = int(input("-->"))
    if op == 1:
        print("-"*24+"CREDITOS"+"-"*24)
        creditos()
        opt()
    elif op == 2:
        print("-"*24+"PENSIONES"+"-"*24)
        pensiones()
        opt()
    elif op == 3:
        print("-"*29+"MENU DE LA SEMANA"+"-"*29)
        menu()
        opt()
    elif op == 4:
        print("-"*30+"RESERVACION DE CUBICULOS"+"-"*30)
        cubiculos()
        opt()


def cubiculos():
    preg = input("¿Que espera...quiere reservar un cubiculo? -->")
    while preg == "no" or preg == "No" or preg != "si":
        return (opt())
    while preg == "si":
        for i in cubi:
            print(i)
            print(reserva_cubi())

def reserva_cubi():
        I = "E800"
        II = "E801"
        III = "E802"
        IV = "E803"
        V = "E804"
        VI = "E805"

        A = "11:00am a 1:00pm"
        B = "1:00pm a 3:00pm"
        C = "3:00pm a 5:00pm"
        D = "12:00pm a 2:00pm"
        E = "9:00am a 11:00am"
        F = "2:00pm a 4:00pm"
        G = "4:00pm a 6:00pm"
        H = "10:00am a 12:00pm"

        op1 = input("Para registrarse elija un cubiculo --> ")
        if op1 == "I":
            print("-"*55+"\n  \t      Este cubiculo esta disponible\n\t Tiene para elegir los siguientes horarios:\n 11:00am a 1:00pm - 1:00pm a 3:00pm - 3:00pm a 5:00pm\n"+"-"*55)
            print("A. 11:00am a 1:00pm\nB. 1:00pm a 3:00pm\nC. 3:00pm a 5:00pm")
            op2 = input("Ahora, escoja el horario --> ")
            if  op2 == "A":
                print(">"*41+"\n  \tSe ha reservado el cubiculo",I,"\n \tEn el horario de",A,"\n" + ">"*41)

            elif op2 == "B":
                print(">"*41+"\n  \tSe ha reservado el cubiculo",I,"\n \tEn el horario de",B,"\n"+">"*41)

            elif op2 == "C":
                print(">"*41+"\n  \tSe ha reservado el cubiculo",I,"\n \tEn el horario de",C,"\n"+">"*41)

            else:
                print(">-"*20+"\n¡ERROR!, Este horario no esta disponible \n"+">-"*20)
                return(reserva_cubi())

        elif op1 == "II":
            print("-"*55+"\n  \t      Este cubiculo esta disponible\n\t Tiene para elegir los siguientes horarios:\n 10:00am a 12:00pm - 12:00pm a 2:00pm - 2:00pm a 4:00pm\n \t \t \t  -4:00pm a 6:00pm\n"+"-"*55)
            print("H. 10:00am a 12:00pm\nD. 12:00pm a 2:00pm\nF. 2:00pm a 4:00pm\nG. 4:00pm a 6:00pm")
            op3 = input("Ahora, escoja el horario --> ")
            if op3 == "H":
                print(">"*41+"\n  \tSe ha reservado el cubiculo", II,"\n \tEn el horario de", H, "\n"+">"*41)

            elif op3 =="D":
                print(">"*41+"\n  \tSe ha reservado el cubiculo", II,"\n \tEn el horario de", D, "\n"+">"*41)

            elif op3 =="F":
                print(">"*41+"\n  \tSe ha reservado el cubiculo", II,"\n \tEn el horario de", F, "\n"+">"*41)

            elif op3 =="G":
                print(">"*41+"\n  \tSe ha reservado el cubiculo", II,"\n \tEn el horario de", G, "\n"+">"*41)

            else:
                print(">-" * 20 + "\n¡ERROR!, Este horario no esta disponible \n" + ">-" * 20)
                return (reserva_cubi())

        elif op1 == "III":
            print(">-"*20+"\n  \t      Este cubiculo esta disponible\n\t Tiene para elegir los siguientes horarios:\n 11:00pm a 1:00pm - 1:00pm a 3:00pm - 3:00pm a 5:00pm\n-------------------------------------------------------")
            print("A. 11:00pm a 1:00pm\nB. 1:00pm a 3:00pm\nC. 3:00pm a 5:00pm")
            op4 = input("Ahora, escoja el horario --> ")
            if op4 == "A":
                print(">"*41+"\n  \tSe ha reservado el cubiculo", III,"\n \tEn el horario de", A, "\n"+">"*41)

            elif op4 == "B":
                print(">"*41+"\n  \tSe ha reservado el cubiculo", III,"\n \tEn el horario de", B, "\n"+">"*41)

            elif op4 == "C":
                print(">"*41+"\n  \tSe ha reservado el cubiculo", III,"\n \tEn el horario de", C, "\n"+">"*41)

            else:
                print(">-" * 20 + "\n¡ERROR!, Este horario no esta disponible \n" + ">-" * 20)
                return (reserva_cubi())

        elif op1 == "IV":
            print(">-"*20+"\n  \t      Este cubiculo esta disponible\n\t Tiene para elegir los siguientes horarios:\n 9:00am a 11:00am - 11:00am a 1:00pm - 1:00pm a 3:00pm\n \t \t \t  - 3:00pm a 5:00pm\n-------------------------------------------------------")
            print("E. 9:00am a 11:00am\nA. 11:00am a 1:00pm\nB. 1:00pm a 3:00pm\nC. 3:00pm a 5:00pm")
            op5 = input("Ahora, escoja el horario --> ")
            if op5 == "E":
                print(">"*41+"\n  \tSe ha reservado el cubiculo", IV,"\n \tEn el horario de", E, "\n"+">"*41)

            elif op5 == "A":
                print(">"*41+"\n  \tSe ha reservado el cubiculo", IV,"\n \tEn el horario de", A, "\n"+">"*41)

            elif op5 == "B":
                print(">"*41+"\n  \tSe ha reservado el cubiculo", IV,"\n \tEn el horario de", B, "\n"+">"*41)

            elif op5 == "C":
                print(">"*41+"\n  \tSe ha reservado el cubiculo", IV,"\n \tEn el horario de", C, "\n"+">"*41)

            else:
                print(">-" * 20 + "\n¡ERROR!, Este horario no esta disponible \n" + ">-" * 20)
                return (reserva_cubi())

        elif op1 == "V":
            print(">-"*20+"\n  \t      Este cubiculo esta disponible\n\t Tiene para elegir los siguientes horarios:\n 10:00am a 12:00pm - 12:00pm a 2:00pm - 2:00pm a 4:00pm\n \t \t \t  - 4:00pm a 6:00pm\n-------------------------------------------------------")
            print("H. 10:00am a 12:00pm\nD. 12:00pm a 2:00pm\nF. 2:00pm a 4:00pm\nG. 4:00pm a 6:00pm")
            op6 = input("Ahora, escoja el horario --> ")
            if op6 == "H":
                print(">"*41+"\n  \tSe ha reservado el cubiculo", V,"\n \tEn el horario de", H, "\n"+">"*41)

            elif op6 == "D":
                print(">"*41+"\n  \tSe ha reservado el cubiculo", V,"\n \tEn el horario de", D, "\n"+">"*41)

            elif op6 == "F":
                print(">"*41+"\n  \tSe ha reservado el cubiculo", V,"\n \tEn el horario de", F, "\n"+">"*41)

            elif op6 == "G":
                print(">"*41+"\n  \tSe ha reservado el cubiculo", V,"\n \tEn el horario de", G, "\n"+">"*41)

            else:
                print(">-" * 20 + "\n¡ERROR!, Este horario no esta disponible \n" + ">-" * 20)
                return (reserva_cubi())

        elif op1 == "VI":
            print(">-"*20+"\n  \t      Este cubiculo esta disponible\n\t Tiene para elegir los siguientes horarios:\n 9:00am a 11:00am - 11:00am a 1:00pm - 1:00pm a 3:00pm\n \t \t \t  - 3:00pm 5:00pm\n-------------------------------------------------------")
            print("E. 9:00am a 11:00am\nA. 11:00am a 1:00pm\nB. 1:00pm a 3:00pm\nC. 3:00pm 5:00pm")
            op7 = input("Ahora, escoja el horario --> ")
            if op7 == "E":
                print(">"*41+"\n  \tSe ha reservado el cubiculo", VI,"\n \tEn el horario de", E, "\n"+">"*41)

            elif op7 == "A":
                print(">"*41+"\n  \tSe ha reservado el cubiculo", VI,"\n \tEn el horario de", A, "\n"+">"*41)

            elif op7 == "B":
                print(">"*41+"\n  \tSe ha reservado el cubiculo", VI,"\n \tEn el horario de", B, "\n"+">"*41)

            elif op7 == "C":
                print(">"*41+"\n  \tSe ha reservado el cubiculo", VI,"\n \tEn el horario de", C, "\n"+">"*41)
            else:
                print(">-" * 20 + "\n¡ERROR!, Este horario no esta disponible \n" + ">-" * 20)
                return (reserva_cubi())

        elif op1 == "VII":
            print(">-"*20+"\n  \t      Este cubiculo esta disponible\n\t Tiene para elegir los siguientes horarios:\n 10:00am a 12:00pm - 12:00pm a 2:00pm - 2:00pm a 4:00pm\n \t \t \t  - 4:00pm a 6:00pm\n-------------------------------------------------------")
            print("H. 10:00am a 12:00pm\nD. 12:00pm a 2:00pm\nE. 2:00pm a 4:00pm\nG. 4:00pm a 6:00pm")
            op8 = input("Ahora, escoja el horario --> ")
            if op8 == "H":
                print(">"*41+"\n  \tSe ha reservado el cubiculo", VII,"\n \tEn el horario de", H, "\n"+">"*41)

            elif op8 == "D":
                print(">"*41+"\n  \tSe ha reservado el cubiculo", VII,"\n \tEn el horario de", D, "\n"+">"*41)

            elif op8 == "E":
                print(">"*41+"\n  \tSe ha reservado el cubiculo", VII,"\n \tEn el horario de", E, "\n"+">"*41)

            elif op8 == "G":
                print(">"*41+"\n  \tSe ha reservado el cubiculo", VII,"\n \tEn el horario de", G, "\n"+">"*41)

            else:
                print(">-" * 20 + "\n¡ERROR!, Este horario no esta disponible \n" + ">-" * 20)
                return (reserva_cubi())

        else:
            while op1 != "I" or op1 != "II" or op1 != "III" or op1 != "IV" or op1 != "V" or op1 != "VI" or op1 != "VII" or op1 != "VIII" or op1 != "IX":
                print(">-" * 20 + "\n¡ERROR!, Este horario no esta disponible \n" + ">-" * 20)
                return (reserva_cubi())

        opt()


def creditos():
    print("¿En que ciclo estas?:\n1. Primer Ciclo \t   2. Segundo Ciclo \t   3. Tercer Ciclo")
    ci = input("-->")
    if ci == "1":
        for i in cur1:
            print(i)
        cu = input(">> Ingresa el curso:")
        if cu == "a":
            for i in mat:
                print(i)
        elif cu == "b":
            for i in fis:
                print(i)
        elif cu == "c":
            for i in compu:
                print(i)
        elif cu == "d":
            for i in glob:
                print(i)
        elif cu == "e":
            for i in coe:
                print(i)
        elif cu == "f":
            for i in quig:
                print(i)
        elif cu == "g":
            for i in quie:
                print(i)
        else:
            while cu != "a" or cu != "b" or cu != "c" or cu != "d" or cu != "e" or cu != "f" or cu != "g":
                print(">-"*25+"\nERROR...curso invalido, por favor ingrese de nuevo!\n"+">-"*25)
                return (creditos())
    elif ci == "2":
        for i in cur2:
            print(i)
        cu2 = input(">> Ingresa el curso:")
        if cu2 == "a":
            for i in mat2:
                print(i)
        elif cu2 == "b":
            for i in fis2:
                print(i)
        elif cu2 == "c":
            for i in cm:
                print(i)
        elif cu2 == "d":
            for i in po:
                print(i)
        elif cu2 == "e":
            for i in coe2:
                print(i)
        elif cu2 == "f":
            for i in ing:
                print(i)
        elif cu2 == "g":
            for i in pi:
                print(i)
        elif cu2 == "h":
            for i in ide:
                print(i)
        else:
            while cu2 != "a" or cu2 != "b" or cu2 != "d" or cu2 != "e" or cu2 != "f" or cu2 != "c" or cu2 != "g" or cu2 != "h":
                print(">-" * 25 + "\nERROR...curso invalido, por favor ingrese de nuevo!\n" + ">-" * 25)
                return (creditos())
    elif ci == "3":
        for i in cur3:
            print(i)
        cu3 = input(">> Ingresa el curso:")
        if cu3 == "a":
            for i in mat3:
                print(i)
        elif cu3 == "b":
            for i in ter:
                print(i)
        elif cu3 == "c":
            for i in ep:
                print(i)
        elif cu3 == "d":
            for i in ing2:
                print(i)
        elif cu3 == "e":
            for i in ge:
                print(i)
        elif cu3 == "f":
            for i in pi2:
                print(i)
        else:
            while cu3 != "matematica III" or cu3 != "Matematica III" or cu3 != "Termodinamica" or cu3 != "termodinamica" or cu3 != "Estadistica y Probabilidades" or cu3 != "estadistica y probabilidades" or cu3 != "Gestion de Empresas" or cu3 != "gestion de empresas" or cu3 != "Ingles II" or cu3 != "ingles II" or cu3 != "Proyecto Interdisciplinario II" or cu3 != "proyecto interdisciplinario II":
                print(">-" * 25 + "\nERROR...curso invalido, por favor ingrese de nuevo!\n" + ">-" * 25)
                return (creditos())
    opt()


def pensiones():
    e = input("Ingresa tu escala(A - B - C - D - E): ")
    if e == "A":
        print(
            "\n"+"-"*32+"\n Su pensión es: S/.875 x Crédito \n"+"-"*32+"\n>> El monto mensual es: S/."+str((24*875)//5))
    elif e == "B":
        print(
            " \n"+"-"*32+"\n Su pensión es: S/.733 x Crédito \n"+"-"*32+"\n>> El monto mensual es: S/."+str((24*733)//5))
    elif e == "C":
        print(
            " \n"+"-"*32+"\n Su pensión es: S/.618 x Crédito \n"+"-"*32+"\n>> El monto mensual es: S/."+str((24*618)//5))
    elif e == "D":
        print(
            " \n"+"-"*32+"\n Su pensión es: S/.500 x Crédito \n"+"-"*32+"\n>> El monto mensual es: S/."+str((24*500)//5))
    elif e == "E":
        print(
            " \n"+"-"*32+"\n Su pensión es: S/.414 x Crédito \n"+"-"*32+"\n>> El monto mensual es: S/."+str((24*414)//5))
    else:
        while e != "A" or e != "B" or e != "C" or e != "D" or e != "E":
            print(">-"*15+"\n ERROR, escala no admitida \n Intentelo de nuevo por favor\n"+">-"*15)
            return (pensiones())
    opt()


def menu():
    print("Elige el día del menú:\nI. Lunes\nII. Martes\nIII. Miercoles\nIV. Jueves\nV. Viernes")
    dm = input("-->")
    if dm == "I":
        for i in lu:
            print(i)
    elif dm == "II":
        for i in mar:
            print(i)
    elif dm == "III":
        for i in mier:
            print(i)
    elif dm == "IV":
        for i in juev:
            print(i)
    elif dm == "V":
        for i in vier:
            print(i)
    else:
        while dm != "I" or dm != "II" or dm != "III" or dm != "IV" or dm != "V":
            print(">-"*27+"\nUpps...No hay menu disponible en este dia,lo sentimos!\n"+ ">-"*27)
            return (menu())
    opt()


def opt():
    print(
        "¡Bien " + nomb + "!, Ahora...\n¿Deseas consultar algo más?\n1. Créditos\n2. Pensiones\n3. Menú de la semana\n4. Cubiculos")
    o = int(input("-->"))
    if o == 1:
        print("-"*24+"CREDITOS"+"-"*24)
        creditos()
    elif o == 2:
        print("-"*24+"PENSIONES"+"-"*24)
        pensiones()
    elif o == 3:
        print("-"*29+"MENU DE LA SEMANA"+"-"*29)
        menu()
    elif o == 4:
        print("-"*30+"RESERVACION DE CUBICULOS"+"-"*30)
        cubiculos()


def creditos2():
    print("-"*24+"CREDITOS"+"-"*24+"\nEn este ciclo llevara")


def opte():
    usuar =input("¡Por favor!, Ingrese los siguentes datos:\n>> Usuario: ")
    if usuar == correo:
        contr = input(">> Contraseña: ")
        if contr == contra:
            print("-" * 23 + "¡Bienvenido Kachimbo!!" + "-" * 23 + "\n¡Bien " + nomb + ",¿Qué deseas consultar?\n1. Créditos\n2. Pensiones\n3. Menú de la semana\n4 .Cubiculos")
            k = int(input("-->"))
            if k == 1:
                print("-"*29+"CREDITOS"+"-"*29)
                for i in cursos1:
                    print(i)
                    print(opt())
            elif k == 2:
                print("-"*24+"PENSIONES"+"-"*24)
                pensiones()
            elif k == 3:
                print("-"*29+"MENU DE LA SEMANA"+"-"*29)
                menu()
            elif k == 4:
                print("-"*30+"RESERVACION DE CUBICULOS"+"-"*30)
                cubiculos()
            else:
                sys.exit(0)
        else:
            print("¡Contraseña Invalida ,Ingrese de nuevo!"+"\n"+" ")
            print(opte())
    else:
        print("¡Nombre de usuario no registrado!\nRegistrese antes de iniciar sesion\n1. Registrar\n2. Intentar de nuevo\n3. Salir")
        resp = input("--> ")
        if resp == "1":
            print(volver_registrar())
        elif resp =="2":
            print(opte())
        elif resp=="3":
            sys.exit(0)


def volver_registrar():
    nomb2 = input("I) Para registrarse, por favor ingrese los siguientes datos:\n>> Nombre: ")
    apell2 = input(">> Apellido: ")
    cod2 = input(">> Codigo: ")
    cil2 = input(">> Ciclo: ")
    print("¡Hola", nomb2 + "!" + "\n" + "Tu correo de utec es el siguiente:",nomb2 + "." + apell2 + "@utec.edu.pe")
    correo2 = nomb2 + "." + apell2 + "@utec.edu.pe"
    contra2 = input(">> Contraseña: ")
    if cil2 == "1":
        print(" " + "\nII) Estos son los cursos que llevara durante el ciclo:")
        for i in cursos2:
            print(i)
            print("")
            print("*¡GRACIAS POR REGISTRARSE!*\n¿Desea entrar a comsultar?")
            perm = input("-> ")
            if perm =="si":
                usuar2 = input("¡Por favor!, Ingrese los siguentes datos:\n>> Usuario: ")
                if usuar2 == correo2:
                    contr2 = input(">> Contraseña: ")
                    if contr2 == contra2:
                        print(
                            "-" * 23 + "¡Bienvenido Kachimbo!!" + "-" * 23 + "\n¡Bien " + nomb2 + ",¿Qué deseas consultar?\n1. Créditos\n2. Pensiones\n3. Menú de la semana\n4 .Cubiculos")
                        k = int(input("-->"))
                        if k == 1:
                            print("-" * 29 + "CREDITOS" + "-" * 29)
                            for i in cursos1:
                                print(i)
                                print(opt())
                        elif k == 2:
                            print("-" * 24 + "PENSIONES" + "-" * 24)
                            pensiones()
                        elif k == 3:
                            print("-" * 29 + "MENU DE LA SEMANA" + "-" * 29)
                            menu()
                        elif k == 4:
                            print("-" * 30 + "RESERVACION DE CUBICULOS" + "-" * 30)
                            cubiculos()
                        else:
                            sys.exit(0)
                    else:
                        print("¡Contraseña Invalida ,Ingrese de nuevo!" + "\n" + " ")
                        print(opte())
                else:
                    print(
                        "¡Nombre de usuario no registrado!\nRegistrese antes de iniciar sesion\n1. Registrar\n2. Salir")
                    resp = input("--> ")
                    if resp == "1":
                        print(volver_registrar())
                    else:
                        sys.exit(0)
            elif perm != "si":
                return("¡Vuelva pronto!...")




    elif cil2 =="2" or cil2=="3":
        var2 = int(input("¿Cuantos cursos va a llevar?(≤8):"))
        if var2 > 8:
            print("¡Lo sentimos, a sobrepasado el limite de cursos a llevar!")
            sys.exit(0)


        else:
            for i in cursos4:
                print(i)
                print("")
                print("Ahora, ¿Qué cursos deseas llevar? ")
            for j in range(1, var2 + 1):
                var3 = input(">> Curso#" + str(j) + ":")

        print(" ")
        print("*¡GRACIAS POR REGISTRARSE!*\n¿Desea entrar a comsultar?")
        pom = input("--> ")
        if pom == "si":
            print("-"*23+"¡Bienvenido Kachimbo!!"+"-"*23)
            print(opta())
        elif pom != "si":
            return ("¡Vuelva pronto!...")


    else:
        print(">-"*21+"\nEste ciclo no esta dentro de las consultas\n"
              "\t ¡Por favor ingrese de nuevo!\n"+">-"*21)
        sys.exit(0)



def opta():
    print("¡Bien " + nomb + ",¿Qué deseas consultar?\n1. Créditos\n2. Pensiones\n3. Menú de la semana\n4 .Cubiculos")
    q = int(input("-->"))
    if q == 1:
        print("-"*29+"CREDITOS"+"-"*29)
        print(creditos())
    elif q == 2:
        print("-"*24+"PENSIONES"+"-"*24)
        pensiones()
    elif q == 3:
        print("-"*29+"MENU DE LA SEMANA"+"-"*29)
        menu()
    elif q == 4:
        print("-"*30+"RESERVACION DE CUBICULOS"+"-"*30)
        cubiculos()


cur1 = ["CURSOS DE 1ER CICLO:\na) Matematica I\nb) Fisica I\nc) Intro. a la Ciencia de la computacion\nd) Desafios Globales\ne) Lab. de Comunicacion I\nf) Quimica General\ng) Quimica Experimental"]
cur2 = ["CURSOS DE 2DO CICLO:\na) Matematica II\nb) Fisica II\nc) Ciencias de los Materiales\nd) Programacion Orientada a Objetos\ne) Lab. de Comunicacion II\nf) Ingles I\ng) Proyecto Interdisciplinario I\nh) Intro. al Desarrollo de Empresas"]
cur3 = ["CURSOS DE 3ER CICLO:\na) Matematica III\nb) Termodinamica\nc) Estadistica y Probabilidades\nd) Ingles II\ne) Gestion de Empresas\nf) Proyecto Interdisciplinario II"]
mat = ["-"*29+"\nMatematica I vale 4 créditos\n"+"-"*29]
mat2 = ["-"*29+"\nMatematica II vale 4 créditos\n"+"-"*29]
mat3 = ["-"*29+"\nMatematica III vale 4 créditos\n"+"-"*29]
fis = ["-"*29+"\nFisica I vale 4 créditos\n"+"-"*29]
fis2 = ["-"*29+"\nFisica II vale 4 créditos\n"+"-"*29]
ter = ["-"*29+"\nTermodinamica vale 4 créditos\n"+"-"*29]
cm = ["-"*44+"\nCiencias de los Materiales vale 4 créditos\n"+"-"*44]
compu = ["-"*60+"\nIntroducción a la Ciencia de la Computación vale 4 créditos\n"+"-"*60]
po = ["-"*50+"\nProgramacion Orientada a objetos vale 4 créditos\n"+"-"*50]
glob = ["-"*34+"\nDesafíos Goblales vale 3 créditos\n"+"-"*34]
coe = ["-"*46+"\nLaboratorio de Comunicación I vale 3 créditos\n"+"-"*46]
coe2 = ["-"*46+"\nLaboratorio de Comunicacion II vale 3 créditos\n"+"-"*46]
quig = ["-"*31+"\nQuímica General vale 3 créditos\n"+"-"*31]
quie = ["-"*36+"\nQuímca Expermiental vale 3 créditos\n"+"-"*36]
ing = ["-"*25+"\nIngles I vale 3 créditos\n"+"-"*25]
ing2 = ["-"*25+"\nIngles II vale 3 créditos\n"+"-"*25]
pi = ["-"*46+"\nProyecto Interdisciplinario I vale 2 créditos\n"+"-"*46]
pi2 = ["-"*46+"\nProyecto Interdisciplinario II vale 2 créditos\n"+"-"*46]
ge = ["-"*36+"\nGestion de Empresas vale 2 créditos\n"+"-"*36]
ep = ["-"*44+"\nEstadistica y Probabilidades vale 4 créditos\n"+"-"*44]
ide = ["-"*54+"\nIntroducción al Desarrollo de Empresas vale 2 creditos\n"+"-"*54]


lu = [">"*32+"\n"+"-"*32+"\n Económico: \nPollo a la plancha  -   S/.7.50 \n"+"-"*32+"\n Estudiantil: \nCausa de atún \t -  \tS/.8.50 \n"+"-"*32+"\n Ejecutivo: \nLomo saltado \t - \tS/.7.50 \n"+"-"*32+" \n"+">"*32]
mar = [">"*32+"\n"+"-"*32+"\n Económico: \nAji de gallina \t   -\tS/.7.50 \n"+"-"*32+"\n Estudiantil: \nChoclo con queso   - \tS/.8.50 \n"+"-"*32+"\n Ejecutivo: \nChicarron de pescado - \tS/.7.50 \n"+"-"*32+" \n"+">"*32]
mier = [">"*37+"\n"+">"*37+"\n Económico: \nArroz con pollo \t-    S/.7.50 \n"+">"*37 +"\n Estudiantil: \nPapa a la huancaina \t-    S/.8.50 \n"+">"*37 +"\n Ejecutivo: \nOcopa \t\t  -\t     S/.7.50  \n"+"-"*37+" \n"+"-"*37]
juev = [">"*32+"\n"+"-"*32+"\n Económico: \nMilanesa \t- \tS/.7.50 \n"+"-"*32+"\n Estudiantil: \nSopa de casa \t- \tS/.8.50 \n"+"-"*32+"\n Ejecutivo: \nArroz a la cubana  -\tS/.7.50 \n"+"-"*32+" \n"+">"*32]
vier = [">"*40+"\n"+"-"*40+" \nEconómico: \nArroz chaufa \t   -\t\tS/.7.50 \n"+"-"*40+" \n Estudiantil: \nFrijoles rojos con carne    - \tS/.8.50 \n"+"-"*40+" \n Ejecutivo: \nTallarines rojos \t- \tS/.7.50 \n"+"-"*40+" \n"+">"*40]

cursos1 = [">> Matematica I ---------> vale 4 créditos \n>> Fisica I ---------> vale 4 créditos \n>> Intro. a la Ciencia de la Computación ---------> vale 4 créditos \n>> Desafios Globales ---------> vale 3 créditos \n>> Lab. de Comunicacion I ---------> vale 3 créditos \n>> Quimica General ---------> vale 3 créditos \n>> Quimica Experimental ---------> vale 3 créditos \n"+" "+"\nTotal de creditos: 24\n-----------------------"]
cursos2=[">> Matematica I \n>> Fisica I \n>> Intro. a la Ciencia de la Computación \n>> Desafios Globales \n>> Lab. de Comunicación I \n>> Quimica General \n>> Quimica Experimental "]
cursos4 = ["a) Matematica I\nb) Fisica I\nc) Intro. a la Ciencia de la computacion\nd) Desafios Globales\ne) Lab. de Comunicacion I\nf) Quimica General\n"
           "g) Quimica Experimental\nh) Matematica II\ni) Fisica II\nj) Ciencias de los Materiales\nk) Programación Orientada a Objetos\nl) Lab. de Comunicación II\nm) Ingles I\nn) Proyecto Interdisciplinario I\n"
           "o) Intro. al Desarrollo de Empresas\np) Matematica III\nq) Termodinamica\nr) Estadistica y Probabilidades\ns) Ingles II\nt) Gestion de Empresas\nu) Proyecto Interdisciplinario II"]

matema1 =[">> Matematica I ---------> vale 4 créditos"]
fisica =[">> Fisica I ---------> vale 4 créditos"]
introdu=[">> Intro. a la Ciencia de la Computación ---------> vale 4 créditos"]
desafio = [">> Desafios Globales ---------> vale 3 créditos"]
comunica =[">> Lab. de Comunicacion I ---------> vale 3 créditos"]
quimica = [">> Quimica General ---------> vale 3 créditos"]
quimica2 = [">> Quimica Experimental ---------> vale 3 créditos"]
matema2 = [">> Matematica II ---------> vale 4 créditos"]
fisica2 = [">> Fisica II ---------> vale 4 créditos"]
ciencias =[">> Ciencias de los Materiales ---------> vale 4 créditos"]
progra = [">> Programación Orientada a Objetos ---------> vale 4 créditos"]
comunica2 = [">> Lab. de Comunicación II ---------> vale 3 créditos"]
ingles1 =[">> Ingles I ---------> vale 3 créditos"]
proyecto = [">> Proyecto Interdisciplinario I ---------> vale 2 créditos"]
empresas = [">> Intro. al Desarrollo de Empresas ---------> vale 2 créditos"]
matema3 = [">> Matematica III ---------> vale 4 créditos"]
termodi = [">> Termodinamica ---------> vale 4 créditos"]
estadis = [">> Estadistica y Probabilidades ---------> vale 4 créditos"]
ingles2 = [">> Ingles II ---------> vale 3 créditos"]
gestion = [">> Gestion de Empresas ---------> vale 2 créditos"]
proyecto2 = [">> Proyecto Interdisciplinario II ---------> vale 2 créditos"]


cubi = [">"*99+"\n "+"-"*98+ "\n Cubiculos: \t    \t    \t  Horarios: "
        "\nI) E800------------------------> 11:00am a 1:00pm - 1:00pm a 3:00pm - 3:00pm a 5:00pm"
        "\nII) E801------------------------> 10:00am a 12:00pm - 12:00pm a 2:00pm - 2:00pm a 4:00pm - 4:00pm a 6:00pm"
        "\nIII) E802------------------------> 11:00pm a 1:00pm - 1:00pm a 3:00pm - 3:00pm a 5:00pm"
        "\nIV) E803------------------------> 9:00am a 11:00am - 11:00am a 1:00pm - 1:00pm a 3:00pm - 3:00pm a 5:00pm"
        "\nV) E804------------------------> 10:00am a 12:00pm - 12:00pm a 2:00pm - 2:00pm a 4:00pm - 4:00pm a 6:00pm"
        "\nVI) E805------------------------> 9:00am a 11:00am - 11:00am a 1:00pm - 1:00pm a 3:00pm - 3:00pm 5:00pm"
        "\nVII) E806------------------------> 10:00am a 12:00pm - 12:00pm a 2:00pm - 2:00pm a 4:00pm - 4:00pm a 6:00pm"
        "\nVIII) E807------------------------> 11:00pm a 1:00pm - 1:00pm a 3:00pm - 3:00pm a 5:00pm"
        "\nIX) E808------------------------> 9:00am a 11:00am - 11:00am a 1:00pm - 1:00pm a 3:00pm a 5:00pm\n" +"-"*98+"\n"+">"*98]

print("-"*11+"Welcome to UTEC"+"-"*11+"\n"+time.strftime("%d/%m/%y %H:%M")+"\n¡¡QUE TAL FUTURO INGENIERO DE UTEC!!\nCOMENZEMOS...\n¿Que accion quiere realizar?\n1. Registrarse \t   2. Iniciar Sesión")
var1 = input("--> ")
lista = []
if var1 == "1":
    nomb = input("I) Para registrarse, por favor ingrese los siguientes datos:\n>> Nombre: ")
    apell = input(">> Apellido: ")
    cod = input(">> Codigo: ")
    cil = input(">> Ciclo: ")
    contra = input(">> Contraseña: ")
    print("¡Hola", nomb + "! Te acabas de crear una cuenta UTEC" + "\n" + "Tu correo de utec :", nomb + "." + apell + "@utec.edu.pe"+"\nTu contraseña:",contra)
    correo = nomb + "." + apell + "@utec.edu.pe"
    print("\n"+" "+"\n",registrar(lista))
elif var1 == "2":
    nomb = input("Ingresa tu usuario: ")
    print(iniciar_sesion())