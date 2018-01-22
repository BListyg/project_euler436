# project_euler436
Simulation code to Project Euler #436 along with an extension that allows for any two values of S can be used.

*The problem: 

  Julie proposes the following wager to her sister Louise.
  She suggests they play a game of chance to determine who will wash the dishes.
  For this game, they shall use a generator of independent random numbers uniformly distributed between 0 and 1.
  The game starts with S = 0.
  The first player, Louise, adds to S different random numbers from the generator until S > 1 and records her last random number 'x'.
  The second player, Julie, continues adding to S different random numbers from the generator until S > 2 and records her last random number 'y'.
  The player with the highest number wins and the loser washes the dishes, i.e. if y > x the second player wins.

  For example, if the first player draws 0.62 and 0.44, the first player turn ends since 0.62+0.44 > 1 and x = 0.44.
  If the second players draws 0.1, 0.27 and 0.91, the second player turn ends since 0.62+0.44+0.1+0.27+0.91 > 2 and y = 0.91. Since y > x, the second player wins.

  Louise thinks about it for a second, and objects: "That's not fair".
  What is the probability that the second player wins?
  Give your answer rounded to 10 places behind the decimal point in the form 0.abcdefghij
  
*The solution:

  Louise is right that this game isn't fair. The second player will always have a greater probability of winning the game compared to the first player (specific values depend on the number of simulations you run). The part I'm particularly proud of is that this code will allow you to use any two values for the sums the random uniform draws have to hit. The cool thing is that regardless of what values Louise or Julie pick, the second value being higher than the first will always guarentee that the second player wins in the long run.
