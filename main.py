meme_dict ={
    "LOL" : "una respuesta a algo gracioso",
    "CHEVERE": "Algo genial",
    "CREEPY": "Aterrador"
}
word = input("Ingresa la palabra a consultar").upper()

if word in meme_dict.keys():
    print("lo que significa es: ", meme_dict[word])
else:
    print("La palabra no existe o esta mal escrita")
