import random
import os
from colorama import Fore, init

init(autoreset=True)

def clearscreen():
    os.system('cls' if os.name == 'nt' else 'clear')

def load_words():
    try:
        file = open("words.txt", "r")
        words = file.read().splitlines()
        file.close()
        return words

    except FileNotFoundError:
        print("[>] " + Fore.RED + "words.txt file not found")
        return []

    except Exception as e:
        print("[>] " + Fore.RED + "Error:", e)
        return []


def check_guess(word, guess):
    output = ""
    for i in range(len(word)):
        if guess[i] == word[i]:
            output += Fore.GREEN + "[" + guess[i].upper() + "] "
        elif guess[i] in word:
            output += Fore.YELLOW + "(" + guess[i] + ") "
        else:
            output += Fore.RED + "_ "

    return output


def game():
    words = load_words()
    if len(words) == 0:
        return
    word = random.choice(words).lower()
    tries = 6
    clearscreen()
    print(Fore.CYAN + "\tMy First Game - Word Guessing Game")
    print("[>] " + Fore.BLUE + "Word Length:", len(word))

    while tries > 0:

        try:
            guess = input("[>] " + Fore.WHITE + "Guess: ").lower()
            if not guess.isalpha():
                print("[>] " + Fore.RED + "Only letters allowed")
                continue
            if len(guess) != len(word):
                print("[>] " + Fore.RED + "Word must be", len(word), "letters")
                continue
            result = check_guess(word, guess)
            print("[>] ",result)

            if guess == word:
                print("[>] " + Fore.GREEN + "You Won")
                return
            tries -= 1
            print("[>] " + Fore.MAGENTA + "Tries Left:", tries)
        except KeyboardInterrupt:
            print("[>] " + Fore.RED + "Game Closed")
            return

        except Exception as e:
            print("[>] " + Fore.RED + "Error:", e)
    print("[>] " + Fore.RED + "Word was:", word)


game()
