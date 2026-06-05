import sys
import os
import time
import subprocess
import random

def limpar():
    comando = 'cls' if os.name == 'nt' else 'clear'
    subprocess.run(comando, shell=True)

limpar()
print(">>>> ELEIÇÕES <<<<")
print()

while True:
    desejo=input("Deseja votar? [1. Sim. 2. Não]: ")
    if desejo=="1":
        break
    if desejo=="2":
        sys.exit()
    else:
        print("Opção inválida!")
limpar()

candidatos = {
    "Candidato 1": 0,
    "Candidato 2": 0,
    "Candidato 3": 0,
    "Candidato 4": 0,
    "Candidato 5": 0,
    "Voto Nulo":   0,
    "Voto Branco": 0
}

while True:
    modo=input("Deseja inserir manualmente ou automaticamente os votos? Manual. [1] | Auto. [2]: ")
    if modo =="1" or "2":
        break
    else:
        print("Opção inválida!")

if modo =="1":
        print()
        print("Você escolheu votar manualmente.")
        time.sleep(1)
        limpar()

while True:
    if modo=="2":
        print()
        print("Voce escolheu votar automaticamente.")
        time.sleep(1)
        limpar()
        MinimoVotosCandidatos=int(input("A *estimativa* do mínimo de votos em um candidato é de 40.000 nas eleições para presidência do Brasil.\n\nInsira o mínimo de votos para cada candidato: "))
        limpar()
        MaximoVotosCandidatos=int(input("A *estimativa* do máximo de votos em um candidato é de 70.000.000 nas eleições para presidência do Brasil.\n\nInsira o máximo de votos para cada candidato: "))

        candidatos["Candidato 1"]=random.randint(MinimoVotosCandidatos,MaximoVotosCandidatos)
        candidatos["Candidato 2"]=random.randint(MinimoVotosCandidatos,MaximoVotosCandidatos)
        candidatos["Candidato 3"]=random.randint(MinimoVotosCandidatos,MaximoVotosCandidatos)
        candidatos["Candidato 4"]=random.randint(MinimoVotosCandidatos,MaximoVotosCandidatos)
        candidatos["Candidato 5"]=random.randint(MinimoVotosCandidatos,MaximoVotosCandidatos)
        candidatos["Voto Branco"]=random.randint(MinimoVotosCandidatos,MaximoVotosCandidatos)
        candidatos["Voto Nulo"]=random.randint(MinimoVotosCandidatos,MaximoVotosCandidatos)
        time.sleep(0.8)
        break

    print(f">>>> CANDIDATOS <<<<\n\n"
      f"| Candidato 1 | [22] |\n"
      f"| Candidato 2 | [13] |\n"
      f"| Candidato 3 | [11] |\n"
      f"| Candidato 4 | [26] |\n"
      f"| Candidato 5 | [33] |\n\n"
      f"| Voto nulo   | [  ] |\n"
      f"| Voto branco | [B]  |\n\n")

    voto=input("Insira seu voto: ").lower()

    if voto == "22":
        print("Voto computado.")
        candidatos["Candidato 1"] += 1
    elif voto == "13":
        print("Voto computado.")
        candidatos["Candidato 2"] += 1
    elif voto == "11":
        print("Voto computado.")
        candidatos["Candidato 3"] += 1
    elif voto == "26":
        print("Voto computado.")
        candidatos["Candidato 4"] += 1
    elif voto == "33":
        print("Voto computado.")
        candidatos["Candidato 5"] += 1
    elif voto == "b":
        print("Voto em branco computado!")
        candidatos["Voto Branco"] += 1
    else:
        print("Voto computado como nulo!")
        candidatos["Voto Nulo"] += 1

    time.sleep(1.3)
    limpar()

    while True:
        votarDenovo=input("Deseja votar novamente? [1. Sim. 2. Não]: ")
        if votarDenovo == "1" or votarDenovo == "2":
            break
        else:
            print("Opção Inválida!")
    if votarDenovo == "2":
        break
        
    limpar()

limpar()
votosTotal=(candidatos["Candidato 1"]+candidatos["Candidato 2"]+candidatos["Candidato 3"]+candidatos["Candidato 4"]+candidatos["Candidato 5"]+candidatos["Voto Nulo"]+candidatos["Voto Branco"])
percVotosCandidato1=(candidatos["Candidato 1"]/votosTotal)*100
percVotosCandidato2=(candidatos["Candidato 2"]/votosTotal)*100
percVotosCandidato3=(candidatos["Candidato 3"]/votosTotal)*100
percVotosCandidato4=(candidatos["Candidato 4"]/votosTotal)*100
percVotosCandidato5=(candidatos["Candidato 5"]/votosTotal)*100
percVotosNulo=(candidatos["Voto Nulo"]/votosTotal)*100
percVotosBranco=(candidatos["Voto Branco"]/votosTotal)*100

print(f">>>>APURAÇÃO DOS VOTOS<<<<\n\n"
    f"| Total de Votos    | {votosTotal}\n\n"
    f"| Votos Candidato 1 | {candidatos["Candidato 1"]} > {percVotosCandidato1:.2f}%\n"
    f"| Votos Candidato 2 | {candidatos["Candidato 2"]} > {percVotosCandidato2:.2f}%\n"
    f"| Votos Candidato 3 | {candidatos["Candidato 3"]} > {percVotosCandidato3:.2f}%\n"
    f"| Votos Candidato 4 | {candidatos["Candidato 4"]} > {percVotosCandidato4:.2f}%\n"
    f"| Votos Candidato 5 | {candidatos["Candidato 5"]} > {percVotosCandidato5:.2f}%\n\n"
    f"| Voto nulo         | {candidatos["Voto Nulo"]} > {percVotosNulo:.2f}%\n"
    f"| Voto branco       | {candidatos["Voto Branco"]} > {percVotosBranco:.2f}%\n\n")

vencedor=max(candidatos, key=candidatos.get)
votosVencedor=(candidatos[vencedor])
percVotosVencedor=(votosVencedor/votosTotal)*100

time.sleep(3)
print(f"O {vencedor} é eleito com {votosVencedor} votos representando {percVotosVencedor:.2f}% do total de votos.")






  
    

        