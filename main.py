# hangman
import random


def word_choice():
   word_bank = ["champion", "chimney", "school", "shrink", "persist",
                "facility", "recovery", "concede", "veil", "medium",
                "interrupt", "straw", "jest", "housewife", "jump",
                "distortion", "lean", "eject" "diagram", "survivor"]
   word = random.choice(word_bank)
   return word


def hangman_full(count):
   if count == 6:
       return True
   else:
       return False


def hidden_word(word):
   hidden_letters = []
   for e in word.upper():
       hidden_letters.append(e)
   return hidden_letters


def letter_list(word):
   letter_board = []
   for i in range(1, len(word) + 1):
       letter_board.append("_")
   return letter_board


def game_board(letter_board, count):
   board_1 = ""
   if count == 0:
       board_1 = """
    +---+
        |
        |
        |
       ===
   """
   elif count == 1:
       board_1 = """
    +---+
    o   |
        |
        |
       ===
   """
   elif count == 2:
       board_1 = """
    +---+
    o   |
    |   |
        |
       ===
   """
   elif count == 3:
       board_1 = """
    +---+
    o   |
   /|   |
        |
       ===
   """
   elif count == 4:
       board_1 = """
    +---+
    o   |
   /|\  |
        |
       ===
   """
   elif count == 5:
       board_1 = """
    +---+
    o   |
   /|\  |
   /    |
       ===
   """
   elif count == 6:
       board_1 = """
    +---+
    o   |
   /|\  |
   / \  |
       ===
   """
   board_2 = ""
   for index in letter_board:
       board_2 = board_2 + index + " "
   print(board_1)
   print("Missing Letters:")
   print(board_2)


def guess_letter(guessed_letters):
   while True:
       letter = str(input("Guess a Letter: "))
       letter = letter.upper()
       if len(letter) != 1:
           print("INVALID LETTER")
           continue
       if letter in guessed_letters:
           print("You have already guessed this letter, Try Again!!!")
           continue
       else:
           return letter


def letter_move(letter, hidden_letters, letter_board, guessed_letters):
   guessed_letters.append(letter)
   if letter not in hidden_letters:
       return False
   else:
       i = [index for index, value in enumerate(hidden_letters) if value == letter]
       for n in i:
           letter_board.insert(n, letter)
           letter_board.pop(n + 1)
       return True


def game():
   word = word_choice()
   count = 0
   letter_board = letter_list(word)
   hidden_letters = hidden_word(word)
   guessed_letters = []
   print("H A N G M A N")
   print("There are", len(word), "letters in the word!")
   while True:
       game_board(letter_board, count)
       letter = guess_letter(guessed_letters)
       letter_move(letter, hidden_letters, letter_board, guessed_letters)
       if not letter_move(letter, hidden_letters, letter_board, guessed_letters):
           print("Letter not in word!!!")
           count += 1
       if letter_board == hidden_letters:
           game_board(letter_board, count)
           print("You have won the game!!!")
           return
       elif hangman_full(count):
           game_board(letter_board, count)
           print("You have run out of turns and lost!!!")
           print("The word was", word, "!!!")
           return
   

def play():
   replay = "Yes"
   while replay == "Yes":
       game()
       replay = input("Would you like to play again (Yes or No): ")
   print("Thanks for Playing!")


play()
