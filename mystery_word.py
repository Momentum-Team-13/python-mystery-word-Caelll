import random
# Generates a random word from the list
def generate_word(text):
    random_word = random.choice(text)
    print('WELCOME TO MYSTERY WORD! The computer has selected a random word.\n')
    print('Can you guess a letter in the word? \n ')
    #print(random_word)
    return random_word
# Displays the word to unveil
def display_word(text):
    mystery_word = str('_'*len(text))
    #print(mystery_word)
    return mystery_word
def user_guess(text):
    guess = input("guess a letter: ")
    if guess.isalpha() and len(guess) == 1:
        return guess
    else:
        print("That wasn't a single letter! Try again.")
    return user_guess(text)
    
def play_game():
    #Reads in the text as a list
    with open("words.txt") as file:
        read_file = file.read()
        read_file_list = read_file.split()
    # Generate random word
    random_word = generate_word(read_file_list)
    # Display mystery word
    word_to_guess = display_word(random_word)
    # Asks user for input of a letter
    letters_guessed = []
    correct_guess = []
    incorrect_guess = []
    remaining_guesses = 8
    #print(word_to_guess)
    word_to_guess = list(word_to_guess)
    print(word_to_guess)
    while remaining_guesses > 0 and "_" in word_to_guess:
        guess_letter = user_guess(word_to_guess)
        if guess_letter in random_word:
            correct_guess.append(guess_letter)
            for letter_index in range(len(list(random_word))):
                if list(random_word)[letter_index] == guess_letter:
                    word_to_guess[letter_index] = guess_letter

            print(word_to_guess)
            print("Correct! Keep going")
        else:
            remaining_guesses -= 1
            incorrect_guess.append(guess_letter)
            print(f"Incorrect. You have {remaining_guesses} guesses left.")
        all_guesses = set(correct_guess + incorrect_guess)
        print(f"Letters already guessed: {' '.join(all_guesses)}")
    if "_" in word_to_guess:
        print(f"Sorry, you didn't win this time. The secret word was: {''.join(random_word)}. Try again.")
    else:
        print(f" Congrats! The secret word was: {''.join(word_to_guess)}. YOU WON!!")

if __name__ == "__main__":
    play_game()
