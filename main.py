import random

playing = True

weapons = {
    'rock': 'scissors',
    'paper': 'rock',
    'scissors': 'paper'
}

def play():
    userInput = input("Enter \'rock\' if you pick rock\nEnter \'paper\' if you pick paper\nEnter \'scissors\' if you pick scissors\nEnter \'q\' if you quit\nInput: ")
    
    playerChoice = "{}"
    computerChoice = "{}"

    if userInput == "q":
        playing = False
    else:
        playerChoice = userInput
        playing = False
    
    computerChoice = random.choice(list(weapons))
 
    for k, v in weapons.items():
        if playerChoice == str(k) and computerChoice == str(v):
            print(f"You won!\nComputer picked: {computerChoice}\nYou picked: {playerChoice}")
        elif computerChoice == str(k) and playerChoice == str(v):
            print(f"You lost!\nComputer picked: {computerChoice}\nYou picked: {playerChoice}")
        elif computerChoice == str(k) and playerChoice == str(k):
            print(f"You tied!\nComputer picked: {computerChoice}\nYou picked: {playerChoice}")

if __name__ == "__main__":
    play()