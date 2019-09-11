# Every function returns None by default. You can change that

def square(num):
    print(num*num)

#This will print 16 and "None"
print(square(4))


print("-------------------")

def square(num):
    return(num*num)

#This will print 16
print(square(4))
