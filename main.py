def equalsTen(x):
    if x > 10:
        return "x is greater than 10"

    elif x == 10:
        return "x equals 10"
    
    else: 
        return "x is not greater than 10"

print(equalsTen(10))

if "cat" < "dog":
    print("wow I can't believe this worked")
else:
    print("wow I still can't believe this worked")


def login(password):
    if password == "OsowskiR00lz":
        return "ACCESS GRANTED"
    else:
        return "ACCESS DENIED"

print(login("OsowskiR00lz"))


def trivia(answer):
    if answer.lower() == "gerald":
        return "Bingo!!"
    else:
        return "git gud lol"

print(trivia("gerald"))

def fiveSauces(sauce):

    if sauce == "Tomato":
        return "Bingo!"

    elif sauce == "Mayonaise":
        return "Bingo!"

    elif sauce == "Espagnole":
        return "Bingo!"

def define(definition):
    definition = definition.lower()
    definition = definition.upper()
    if definition == "Tomato":
        return "Red fruit used to make various foods"
    
    elif definition == "Mayonaise":
        return "White sauce used for many recipes and  foods"

    elif definition == "Fortnite":
        return "Fortnite is a battle royale video game focus on building, fighting, and dancing"

    elif definition == "Squash":
        return "A squash is a plant in the gourd family, cooked for human consumption"

    elif definition == "Pain":
        return "A signal sent to the brain in response to self-harmful real world events"

    elif definition == "Carrot":
        return "Carrots are a root vegetable that are known for improving eyesight"
    
    elif definition == "Potato":
        return "Root vegetable commonly grown in colder climates underground"

    elif definition == "YouTube":
        return "YouTube is a website where you can watch videos uploaded by people all over the world"

    elif definition == "Minecraft":
        return "Minecarft is a sandbox game that is known for its distinct art style"

    elif definition == "Guitar":
        return "Musical string instrument"

    else:
         return "word not in dictionary"

print(define("definition"))
    

