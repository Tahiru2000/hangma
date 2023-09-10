def hangman():
    word= "DOG"
    wrong_guesses=0
    stages= ["","______","|  |","| 0","| /|\ ","| / \\", "|" ]
    score_board= ['__']* len(word)
    win=False
    print('Welcome to Hangman')
    while wrong_guesses < len(stages) - 1 :
        print('\n')
        guess= input("Guess letter:")
        if guess in word:
            score_board[word.index(guess)]=guess
        else:
            wrong_guesses += 1
        print((' '.join(score_board)))
        print('  \n'.join(stages[0: wrong_guesses + 1]))
        if '__' not in score_board:
            print('You win! The word was:')
            print(' ' .join(score_board))
            win=True
            break
    if not win:
        print(' \n' .join(stages[0: wrong_guesses]))
        print('You lose!')
hangman()
        