# -*- coding: utf-8 -*-
def sentence_maker(phrase):
    interrogatives = ("how", "what", "why", "who")
    capitalized = phrase.capitalize()
    if phrase.startswith(interrogatives):
        return f"{capitalized}? "
    else:
        return f"{capitalized}. "
    

frase = ''
texto_completo = []

while frase != "\end":
    frase = input("Escribe algo: ")
    texto_completo.append(sentence_maker(frase))

print("".join(texto_completo))
