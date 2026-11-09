def hangman_():
    print("Welcome to Hangman Game")
    c_word=input("Enter the word to guess: ")
    word=list(c_word)
    guessed="_"*len(c_word)
    guessed=list(guessed)
    lstguessed=[]
    g=False
    chance=6
    while g!=True:
        n=input("Enter a letter to guess:")
        if n.upper() in lstguessed:
            n=""
            print("Already guessed that letter!")
            
        elif n.upper() in word:
            index=word.index(n.upper())
            guessed[index]=n
            word[index]="_"
            print("Correct guess!")
            print("".join(guessed))

        else:
            lstguessed.append(n.upper())
            chance-=1
            print("Incorrect guess!")
            print("".join(guessed))
            print(f"You have {chance} chances left.")
            if chance==0:
                print("You have run out of chances! Game Over!")
                g=True
                confirm=input("Do you want to play again? Y/N: ")
                if confirm.upper()=="Y":
                    hangman_()
                else:
                    print("Thanks for playing!")
                    break
            

        if "_" not in guessed:
            g=True
            print(f"You guessed the word correctly! The word was: {c_word}")
            confirm=input("Do you want to play again? Y/N: ")
            if confirm.upper()=="Y":
                hangman_()
            else:
                print("Thanks for playing!")
                break

    
    

if __name__=="__main__":
    hangman_()
            


        
    


