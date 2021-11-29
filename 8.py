frequencia=int(input("coloque a freuquencia do aluno:  "))
nota=int(input("coloque a nota do aluno:  "))
if frequencia > 75 and nota >=7:
    print("Parabéns, você foi aprovado !")
if frequencia >75 and nota <7:
    print("Você está de recuperação")
if frequencia <75 and nota <7:
    print ("Você foi reprovado !")