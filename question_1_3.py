def URLify(str):
    str = str.replace(" ", "%20", 3)
    return str

print(URLify("I am Zlatan"))