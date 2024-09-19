name = input("Please enter your name: ")

def prettyGreeting(name):
    text = f"Welcome to INF201, {name}!"
    nrChar = len(text) + 4  

    dynLine = '*' * nrChar  

    print(dynLine)
    print(f"* {text} *")
    print(dynLine)

prettyGreeting(name)
