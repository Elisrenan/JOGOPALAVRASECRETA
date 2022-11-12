"""
JOGO PALAVRA SECRETA - TEMA COMIDA
"""
print("-------JOGO PALAVRA SECRETA - TEMA COMIDA---------")
print("VOCÊ TEM TRÊS TENTATIVAS, PARA ACERTAR A PALAVRA")
palavras_secretas = ["CHOCOLATE", "BISCOITO", "SUCO", "LARANJA"]
palavras_certas = list()
score = 0
tentativas = 1
qtd_palavras = len(palavras_secretas)

for i in range(1, qtd_palavras+1):
  palpite = str(input("INFORME SEU PALPITE: ")).upper()
  acertou = bool(palpite in palavras_secretas)
  if acertou:
    print("VOCÊ ACERTOU!")
    score = score + 1
  else:
    if tentativas == 3:
      print("Game Over")
      break
    print(f"{tentativas}º Tentativa")
    print("Você errou!!!")
    tentativas += 1

print(f"Seu score foi de: {score}")