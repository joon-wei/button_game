import random

class ButtonGame:
    def __init__(self):
        self.score = 0
        self.scores = []
        self.reset_chance = 0
        self.high_score = 0

    def press_button(self):
        if random.randint(1, 100) <= self.reset_chance:
            print("-----------------------------")
            print("Oops! You've been reset to 0.\n-----------------------------")
            if self.score > 0:
                self.scores.append(self.score)
            self.score = 0
            self.reset_chance = 0
        else:
            self.score += 1
            self.reset_chance += 1

        if self.score > self.high_score:
            self.high_score = self.score

        #print(f"Current score: {self.score} | High score: {self.high_score} | Reset chance: {self.reset_chance}%")
        print(f"{self.score}")

    def get_current_score(self):
        return self.score

    def get_average_score(self):
        if not self.scores:
            return 0
        return "{:.2f}".format(sum(self.scores) / len(self.scores))
    
    def press_button_100_times(self):
        for _ in range(100):
            self.press_button()


def main():
    game = ButtonGame()
    print("Press <enter> to gain 1 point, or input '100' to press the button 100 times.\n('q': Quit, 'h': View highscores)")
    while True:
        user_input = input()
        if user_input.lower() == 'q':
            print("Thanks tor playing!")
            print(f"You are {game.get_average_score()}% lucky today.")
            break
        elif user_input.lower() == 'h':
            print(game.scores)
        elif user_input.lower() == '100':
            game.press_button_100_times()
        else:
            game.press_button()

if __name__ == "__main__":
    main()

