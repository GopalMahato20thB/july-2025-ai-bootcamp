"""
1. Probablity
--------------
Probablity means:
"How likely something is to happen."

Example1: 
If i flip a coin: 
. heads or tails | there are 2 outcomes | Only 1 is Heads 
So, P(Heads) = 1 / 2 = 0.5 = 50 %
it means: If you flip 100 times, you'll likely get 50 heads.

Example2: 
Dice has numbers: 1, 2, 3, 4, 5, 6
What is the probablity of getting a 4?
P(4) = 4 / 6 =  1/ 6 =  16.7 % 

2. Types of Probability Distribution (very basic)
-----------------------------------------------
Distribution tell us how values are spread.

#>>> Uniform Distribution
All values have equal chances. like dice: Each face (1 - 6) has same chance 1 / 6

#>>> Normal distribution
Bell-shaped curve.
Most values are near average, like human  height:
>> Some people are very short/tall
>> Most are medium height
>> 
"""
import numpy as np
import matplotlib.pyplot as plt
#### trying this is Python
## lets simulate a dice roll 1000 times:
dice_rolls = np.random.randint(1, 7, 1000)
plt.hist(dice_rolls, bins=6, edgecolor="black")
plt.title("Simulated Dice Rolls (Uniform Distribution)")
plt.xlabel("Dice Face")
plt.ylabel("Count")
plt.show()
