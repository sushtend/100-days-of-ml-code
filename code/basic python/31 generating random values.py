import random

for i in range(5):
    print(random.randint(1,10)) 


names=['Abdul','Vikram Sarabhai','Satish Dhawan']

#Randomly pick items from list
print(random.choice(names))


#Write an algo to print output of dice

dice=[1,2,3,4,5,6]

print(f'({random.choice(dice)},{random.choice(dice)})')