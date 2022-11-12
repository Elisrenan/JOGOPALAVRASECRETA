"""
JOGO PALAVRA SECRETA - TEMA COMIDA
"""
print("-------JOGO PALAVRA SECRETA - TEMA COMIDA---------")
print("VOCÊ TEM TRÊS TENTATIVAS, PARA ACERTAR A PALAVRA")
palavras_secretas = ["CHOCOLATE", "BISCOITO", "SUCO", "LARANJA"]
palavras_certas = list()
score = 0
tentativas = 1

#rodando o jogo

while True:
  palpite = str(input("INFORME SEU PALPITE: ")).upper()
  acertou = bool(palpite in palavras_secretas)
  if acertou:
    print("VOCÊ ACERTOU!")
    score = score + 1
    palavras_certas.append(palpite)
    palavras_secretas.remove(palpite)
    qtd_palavras = len(palavras_secretas)
    if qtd_palavras == 0:
      print("O JOGO ACABOU!")
      break
  else:
    if tentativas == 3:
      print("Game Over")
      break
    print(f"{tentativas}º Tentativa")
    print("Você errou!!!")
    tentativas += 1

print(f"Seu score foi de: {score}")
print("Você acertou as seguintes palavras: ", palavras_certas)