import random

#user inputs the number of sides they want the dice to have
faces = input('Please select the number of faces for the dice: ')


#a random number is generated in the range of faces on the dice 
value = random.randint(1, int(faces))


#print face value
print(value)
