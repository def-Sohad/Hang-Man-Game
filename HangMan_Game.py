print("""                                         


                                                    WELCOME TO HANGMAN GAME
                                                        &&&&&&&&&&&&&&&&&&
It's a game for tow Players.
The rowls are so easy.
one player puts a word and you need to guess it, one charcter by the other.
think hard because if you don't you die.
be smart and save your life.
                                                    
                                                    
                                                     >>>>>>LET'S GO<<<<<<


    """)
for ___ in range(100):
    Tword = input('Enter the Guessing Word: ')
    print(""" 































    """)
    TA = 0
    TF = 0
    print("                                  It's a word from ",len(Tword)," Charcters")
    print("                                      So ..",len(Tword),"wrong guesses")
    print("                                        .. And you die ..")
    print("""

    """)
    TCH=[]
    FCH=[]
    for __ in range(100):
        Gchar = input('Put a Guess: ')
        if Gchar in Tword:
            print("""                                      Right Guess
                            let's see if you will keep wining...
                                            """)
            if Gchar not in TCH:
                TCH.append(Gchar)
                TA += 1

                if TA == len(Tword):
                    print("""                           It seems you will be staying alive for now
                                   ..congratulation..
                                       .YOU WIN.
                                                            """)
                    break
            continue
        elif Gchar not in Tword :
            print("""                                      WRONG GUESS
                                .. Think Harder Looser ..
                                                """)
            if Gchar not in FCH:
                FCH.append(Gchar)
                TF += 1
                
                if TF == len(Tword):
                    print ("""                  I don't now for sure if you'r a real person or a robot
                                .. It does not matter any more ..
                                    . Now you'r a dead hangman .
                                            YOU LOSE
                                                                """)
                    break

            continue
        