for i in range(10):
    print("number is {:02}".format(i))

pi = 3.141592
print("pi value is {:.3f}".format(pi))

sentence = "Big numnber seprated by comma {:,}".format(1000 ** 2)
print(sentence)
sentence = "Big numnber seprated by comma and two decimal places{:,.2f}".format(
    1000 ** 2
)
print(sentence)


import datetime

my_date = datetime.datetime(2019, 9, 21, 12, 55, 3)
sentence = "formatted date : {:%B %d, %y}".format(my_date)
print(sentence)


sentence = "{0:%B %d, %y} fell on {0:%A} and was the {0:%j} day of the year".format(
    my_date
)
print(sentence)
