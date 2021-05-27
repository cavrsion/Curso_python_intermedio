import random
import time
import os
from functools import reduce
IMAGENES_AHORCADO = ['''

   +---+
   |   |
       |
       |
       |
       |
=========''', '''

  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']


def show_letter(word,word_user,letter):
    for i in range(0,len(word)):
        if word[i] == letter:
            word_user[i] = letter
    return word_user

def valid_data(letter):
    if len(letter)!=1:
        print("Debes ingresar un solo digito..")
        return False
    
    if str(letter).isnumeric():
        print("Debes ingresar solo letras..")
        return False

    return True
    

def paint(word_user,fails):
    word = reduce(lambda a, b: a + ' ' + b, word_user)
    os.system("cls")
    print("¡Adivina la palabra!\n")
    if fails > 0:
        print(IMAGENES_AHORCADO[fails-1]+"\n"+"Aun tienes "+str((7-fails))+" intentos...\n")
    
    print(word + '\n')
    
def select_word(list_word):
    word = [letter for letter in list_word[random.randint(0,len(list_word))]]
    return word

def load_words():
    list_words = []
    try:
        with open("./archivos/data.txt","r",encoding="utf-8") as f:
            list_words = [linea.replace('\n','').upper() for linea in f]
        return list_words
    except FileNotFoundError:
        print("No se pudo cargar el archivo correctamente: ")


def run():
    word = select_word(load_words())
    word_user = ['_' for letter in word]
    fails = 0

    while True:

        paint(word_user,fails)

        if fails == 7:
            print("Perdiste!, Intentalo de nuevo...")
            break

        if set(word) == set(word_user):
            print("ganaste!")
            break

        letter = input("Ingresa una letra: ").upper()

        if not valid_data(letter):
            time.sleep(2)
            continue
        else:
            if letter in word:
                word_user = show_letter(word,word_user,letter)       
            else:
                fails += 1
                



if __name__ == "__main__":
    run()