# The Button Game
The rules of the game is simple: Press a button to increase your score by 1. Everytime your score increases, the chance of failing and having your score reset increases by 1%. The objective of the game is to get the highest score as possible, up to a maximum of 100. 

When you end the game (enter 'q' into the termial), it calculates the average of your highscores, giving you an overview of your luck (or since that is the score which you failed at,  it calculates your bad luck?🤔)

## Manual
'Enter' - Button

'h' - View highscores from current session

'q' - Quit the game

'100' - If you are feeling lucky and think you will reach 100 in one go, I have coded a function to press the button 100 times automatically, saving you the hassle. 

Give it a try! Its harder than it looks.


## Backgound
After playing the game for a while, you may notice that it is rare to achieve a score of more than around 25-ish. That can seem a bit low, since getting past a score of 25 only comes with a 25% chance of failure, or a 75% success rate.

In truth, the probability of passing 25 is not 75% chance. Rather to get to 25, you would have needed to pass the previous 24 button presses in succession. The probability of that happening can be calculated with the product rule, which states the probability of two or more independent events occuring together can be calculated by multiplying the individual probabilities of each event occuring alone.

The probabilty of getting to a score of 3 is 1 * 0.99 * 0.98, and the probability of getting to 25 would be: 

`1 * 0.99 * 0.98 * ... * 0.75`

To demonstrate this, I coded another script [button_game_stats.py](button_game_stats.py) which calculates the actual probability to get to a certain score. This, in essence, caculates your **actual** luck that you had to get to that highscore.

By using the script we can deduce the probability to get to a score of 25 is actually 3.76%. You would notice the chances of getting to 100 decreases exponentially.

Will you be able to hit 100?
