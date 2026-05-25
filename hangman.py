import random

def hangman():
   words=["Lubna","Tabbu","Haqila","Izhaan","Ishrath"]
   secret_words=random.choice(words)
   guessed_word=[]
   incorrect_guess = 0
   max_guess = 6

   print("Welcome to Hangman game")
   print("_" * len(secret_words))
   
   while incorrect_guess < max_guess:

      display_word=""

      for letter in secret_words:
         if letter in guessed_word:
            display_word+=letter+" "
         else:
            display_word+="_ "

      print(display_word)

      if "_" not in display_word:
         print("Congratulations! you guessed the word:",secret_words)
         break

      guess=input("enter word:")

      if len(guess)!=1 or not guess.isalpha():
         print("invalid input. Please enter correctly")
         continue

      if guess in guessed_word:
         print("you already guessed this one!")
         continue

      if guess in secret_words:
         print("you guessed correct!")
         guessed_word.append(guess)
      else:
         print("incorrect guessing!")
         guessed_word.append(guess)
         incorrect_guess+=1 
         print(f"you have {max_guess - incorrect_guess} incorrect guesses left.")

         if max_guess==incorrect_guess:
            print("You ran out of guesses! The secrect word was",secret_words)
            break


if __name__ == "__main__":
   hangman()
   
