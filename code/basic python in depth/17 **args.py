def user(**args):
    print(f"{args['id']}  {args['name']}")


# Use keyword arguments. Function will read them as dictionary

user(id=1, name="Abdul")

