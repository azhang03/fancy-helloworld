import random
import time

# Build Hello World! by picking a random character until it matches
def rando():
    str = ""
    world = list("Hello World!")
    while(str != "Hello World!"):
        time.sleep(0.0005)
        attempt = chr(random.randint(32, 127))
        if attempt == world[0]:
            world.remove(attempt)
            str += attempt
            print(str)
        else:
            print(str + attempt)

def scrambled():
    world = "Hello World"
    display = [" "]*len(world)
    while "".join(display) != world:
        for i in range(len(world)):
            if display[i] != world[i]:
                display[i] = chr(random.randint(32, 127))
        time.sleep(0.005)
        print("".join(display))

def matrix_rain():
    text = "Hello World!"
    for char in text:
        print(" " * random.randint(0, 40) + char)
        time.sleep(0.009)

def colorful_hello():
    text = "Hello World!"
    colors = [
        "\033[91m", "\033[92m", "\033[93m", "\033[94m", "\033[95m", "\033[96m"
    ]
    reset = "\033[0m"
    for char in text:
        color = random.choice(colors)
        print(f"{color}{char}{reset}", end='', flush=True)
    print()

def main():
    funcs = ["rando", "scrambled", "rain", "colorful", 'exit']
    print("Hello World!\n\nWait... that's boring. Here's some fun ways to say it!")
    for i in funcs:
        print("--"+i)

    choice= input("Which one would you like? 'exit' to exit ").lower().strip()
    while choice not in funcs:
        choice = input("That's not a valid choice. Try again! ").lower().strip()

    while choice != 'exit':
        if choice == "rando":
            rando()

        elif choice == "scrambled":
            scrambled()

        elif choice == "rain":
            matrix_rain()

        elif choice == "colorful":
            colorful_hello()

        choice = input("Which one would you like? 'exit' to exit ").lower().strip()
        while choice not in funcs:
            choice = input("That's not a valid choice. Try again! ").lower().strip()


if __name__ == '__main__':
    main()