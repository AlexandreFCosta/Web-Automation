import Automacao_Moeda 
import Bitcoin


escolha = input("Escolha qual moeda deseja saber o valor: \n 1- Dolar \n 2- Bitcoin \n R: ")

if escolha == "1":
    Automacao_Moeda.find_dolar()
elif escolha == "2":
    Bitcoin.find_bitcoin()
else:
    print("O formato escolhido é invalido, escolha entre 1 e 2")



