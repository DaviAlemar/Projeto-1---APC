def frases(texto1,texto2):
 for c in range(2):
  indini1 = texto1.find(f"{c}") + 2
  indini2 = texto2.find(f"{c}") + 2


  indfim1 = texto1[indini1:].find(f"{c}")+ indini1 - 1
  indfim2 = texto2[indini2:].find(f"{c}")+ indini2 -1
 

  frase1 = texto1[indini1:indfim1]
  frase2 = texto2[indini2:indfim2]
  print(frase1)
  print(frase2)
  print(" ")

textoportugues = input()
textoticuna = input()

frases(textoportugues,textoticuna)