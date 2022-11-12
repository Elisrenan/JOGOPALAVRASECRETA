palavra_secreta = "CHOCOLATE"

while True:
  palpite = str(input("INFORME SEU PALPITE")).upper()
  acertou = bool(palpite == palavra_secreta)
  if acertou:
    print("Você acertou!!!")
    break
  else:
    print("Você errou!!!")