import hangman_art
import hangman_words
import random

chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

print(hangman_art.logo)
# Testing code
# print(f'Pssst, the solution is {chosen_word}.')

# Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print("\nYou have already guessed that letter")

    # Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    # Check if user is wrong.
    if guess not in chosen_word:
        print(f"\nThe letter {guess} is not in the word.")
        lives -= 1

    # Join all the elements in the list and turn it into a String.
    print(f"\n{' '.join(display)}")

    # Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("\nYou win.")

    # Print Stages
    print(hangman_art.stages[lives])
    # End Game when lives are over
    if lives == 0:
        end_of_game = True
        print(f"You lose. The word was {chosen_word}.")