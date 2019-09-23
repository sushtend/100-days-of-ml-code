from collections import namedtuple

Color = namedtuple("Color", ["red", "green", "blue"])
color = Color(55, 155, 255)

print(color.red)
print(color.green)


# print("Red color is {0[0]:04} and green is {0[1]:04}".format(color))
