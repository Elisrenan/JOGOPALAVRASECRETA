print("-------JOGO PALAVRA SECRETA - TEMA COMIDA---------")
print("VOCÊ TEM TRÊS TENTATIVAS, PARA ACERTAR A PALAVRA")
palavra_secreta = "CHOCOLATE"

for tentativa in range(1, 3+1):
  print(f"{tentativa}º Tentativa")
  palpite = str(input("INFORME SEU PALPITE: ")).upper()
  acertou = bool(palpite == palavra_secreta)
  if acertou:
    print("PARABÉNS VOCÊ GANHOU!!!")
    break
  else:
    print("Você errou!!!")