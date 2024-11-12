import random


def mask_word(word):
    print(word)
    masked_word = ""
    for i in range(len(word)):
        if i == 0 or i == (len(word) - 1) or i == (len(word) // 2):
            masked_word += word[i]
        else:
            masked_word += "_"

    print(masked_word)
    return masked_word


def update_mask(masked_word, correct_guess, letter_guess):
    new_mask = ""
    for i in range(len(correct_guess)):
        print((i, correct_guess[i]))
        if correct_guess[i] in masked_word[i]:
            new_mask += correct_guess[i]
        elif correct_guess[i] == letter_guess:
            new_mask += letter_guess
        else:
            new_mask += "_"

    return new_mask


def main():
    playing = False

    wants_to_play = input("Would you like to play hangman (yes/no) ? ")
    if wants_to_play == "yes":
        playing = True

    random_word = "hangman"
    correct_guess = [x for x in random_word]
    print(correct_guess)
    print("Welcome to hangman! ")
    masked_word = mask_word(random_word)
    count = 0
    while count < 7:

        letter_guess = input(f"Please guess a letter. Lives count: {count}. ")

        if letter_guess in correct_guess and letter_guess not in masked_word:

            print("here")
            masked_word = update_mask(masked_word, random_word, letter_guess)
            print(masked_word, f" Lives count: {count}. ")
        else:
            if letter_guess in masked_word and correct_guess.count(
                letter_guess
            ) == masked_word.count(letter_guess):
                print(correct_guess.count(letter_guess))
                masked_word.count(letter_guess)
                print(
                    "This letter has already been revealed in the answer, Please eneter another guess. "
                )
                print(masked_word, f" Lives count: {count}. ")
            elif letter_guess in masked_word and correct_guess.count(
                letter_guess
            ) > masked_word.count(letter_guess):
                print("here")
                masked_word = update_mask(masked_word, random_word, letter_guess)
                print(masked_word, f" Lives count: {count}. ")
            else:

                print(f"Incorrect Guess, try again. Lives count: {count}. ")
                count += 1

        if masked_word.strip() == "".join(correct_guess).strip():
            print("You have won congratulations")
            return
        if count == 7:
            print("Sorry your out of lives you lose :( ")


if __name__ == "__main__":
    main()
