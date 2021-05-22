# mipt_battles

This is an educational project in 4 semester at  DCAM MIPT.

## Environment 

PyCharm (our OS is Windows)

## Authors

Maria Zharova and Maria Tikhonova

## Breef description of rules

This game is a duel between 2 players:

1). At the beginning of the round, each player is given a certain amount of health, and a timer starts;

2). Within the allotted time, players must make their move (there are 3 options for strikes: top, bottom and middle);

3). When the turn time expires, the timer counter is reset to its original value, and the fighters on the screen perform the action specified by the players during the course.
four). Depending on the result of the actions of each player, the following options are possible:

- the first player chooses the top hit, and the second - middle; a hit on the second player is counted, and he loses one point of health;
- the first player chooses the top kick, and the second - the bottom one; the hit on the first player is counted, and he loses one point of health;
- the first player chooses the middle blow, and the second - the bottom one; a hit on the second player is counted, and he loses one point of health;
- up to redesignations :)
- if both players have chosen the same hit, then the first and second players lose one health point.

After completing one of the above actions, players are given the opportunity to make a new choice, or leave the previous one. When the turn time has elapsed, the action, which depends on the new choices, takes place on the screen again. The game continues until one of the players has zero health. In the event that the health of the first player becomes empty, the victory will be awarded to the second player, and if the health of the second player is empty, then the first one. A possible outcome is that the health of both players will become equal to zero at the same time, in which case a draw is declared. 

## Control

Immediately after starting the game, the user will be offered a menu in which you can select the game mode, or exit it.

In order to start the battle mode against the computer, you must press W; to fight against another player - D, to exit the game - S.

In the combat mode against the computer, the WSD keys are also responsible for strikes: W - top, D - middle, S - bottom. In the battle mode against another player, the control of the first player remains the same, and the second player makes a choice using the arrows: the upper arrow ☝ is the top strike, the lower 👇 is the bottom, and the left 👈 is the middle one. 

## Playing with the computer

The computer player has three difficulty levels: low, normal, and high.

On normal difficulty, the AI player simply randomly chooses three hits. The probability of each hit is one in three.

At the low difficulty level, the same random selection occurs, but already from four options: the fourth is added to the three hits - a miss. Having made a mistake, the computer opponent gets hit regardless of the choice made by the player, and does not damage the player himself. The probability of each choice is one in four, with the likelihood that the computer will choose to miss, giving the player a big advantage.

Of greatest interest is the high level of complexity. Our game has a Nash equilibrium. If players make random choices all the time, the game will end up being a draw. But the choice of a person, as a rule, is not completely random, so you can try to beat him. Assuming that the player's current move depends on the results of his previous moves, subroutines will be created that store the statistics of previous moves, as well as make a weighted random choice depending on the history of the duel. 
