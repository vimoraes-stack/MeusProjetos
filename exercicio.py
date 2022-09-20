nivel = input("Qual o seu nivel de acesso ? ").upper()
genero = input("Qual o seu genero ? (F/M)").upper()

if nivel == "ADM":
    if genero =="F":
        print("Olá administradora")
    elif genero=="M":
        print("Olá administrador")
    else:
        print(" Responda genero com F ou M")
elif nivel == "USUARIO":
    if genero =="F":
        print("Olá usuaria")
    elif genero=="M":
        print("Olá usuario")
    else:
        print(" Responda genero com F ou M")
elif nivel == "GUEST":
    if genero =="F":
        print("Olá convidada")
    elif genero == "M":
        print("Olá convidado")
    else:
        print(" Responda genero com F ou M")
else:
        print("Olá descconhecido(a)")