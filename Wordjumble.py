import random

# Function to load words based on difficulty level
def load_words(level):
    try:
        with open('word.txt', 'r') as file:
            all_words = file.read().splitlines()  # Read all lines and split into a list
    except FileNotFoundError:
        print("The word file was not found.")
        return []

    # Categorize words based on difficulty level
    if level == 'easy':
        return [word for word in all_words if len(word) <= 3]  # Easy words (3 letters or less)
    elif level == 'medium':
        return [word for word in all_words if 4 <= len(word) <= 6]  # Medium words (4 to 6 letters)
    elif level == 'hard':
        return [word for word in all_words if len(word) > 6]  # Hard words (more than 6 letters)
    else:
        return []

# Function to save the highest score to a file
def save_high_score(name, score):
    with open('high_scores.txt', 'a') as file:
        file.write(f'{name}: {score}\n')

# Function to get the highest score from the file
def get_high_score():
    try:
        with open('high_scores.txt', 'r') as file:
            scores = file.readlines()
            if scores:
                return max(scores, key=lambda x: int(x.split(': ')[1].strip()))
    except FileNotFoundError:
        return None

def main():
    print("Welcome to the Word Jumble Game!")
    print("Prepared by Hojaifa Hossain, MD Labib, MD. Shadman Tahsin Khan!!")
    high_score = get_high_score()
    if high_score:
        print(f"The highest score is: {high_score.strip()}")
    name = input("Please enter your name: ")
    
    score = 0
    level = 'easy'
    
    while True:
        words = load_words(level)
        if not words:
            print("No words available for the current level.")
            break
        
        word = random.choice(words)
        jumbled_word = ''.join(random.sample(word, len(word)))
        
        print(f"\nJumbled word: {jumbled_word}")
        guess = input("Your guess: ")
        
        if guess.lower() == word:
            score += 5
            print("Correct! You've earned 5 points.")
        else:
            print(f"Wrong! The correct word was '{word}'.")
        
        print(f"Your current score: {score}")
        
        # Level up logic
        if score >= 200:
            level = 'hard'
            print("Congratulations! You've reached the hard level.")
        elif score >= 100:
            level = 'medium'
            print("Congratulations! You've reached the medium level.")
        
        # Check if the player wants to continue
        continue_game = input("Do you want to continue playing? (y/n): ").strip().lower()
        if continue_game != 'y':
            break
    
    print(f"Game over! Your final score: {score}")
    
    # Save the high score
    save_high_score(name, score)
    
    # Display the highest score
    high_score = get_high_score()
    if high_score:
        print(f"The highest score is: {high_score.strip()}")

if __name__ == "__main__":
    main()
