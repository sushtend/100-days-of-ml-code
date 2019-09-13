names = ["KAbdul", "Vikram", "Satish"]

# Old programming style
# found = False
# for name in names:
#     if name.startswith("A"):
#         found = True
#         print("Found")
#         pass

# if not found:
#     print("Not found")

# New style
for name in names:
    if name.startswith("A"):
        print("Found")
        pass

else:
    print("Not found")
