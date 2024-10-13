#Random number function (random number method)
import random
print("Random number in range of 100: ", random.choice(range(100)))

#number shuffle( method e)
list= [20,16,19,12]
random.shuffle(list)
print("Shuffled list", list)

random.shuffle(list)
print("reshuffled list",list)

#number uniform method example
print("Float uniform is: ", random.uniform(5,10))