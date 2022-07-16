from termcolor import cprint

def try_me():

    while True:
        val = (input("How big is your package?\n" ))
        try:
            val = float(val)
            if val > 1:
                print("Sorry... your package is too big")
                print("you need a tinier package\n")
            elif val < 0:
                print("Woah that package is too negative for me")
                print("We can only work with positive (tiny) packages\n")
            else:
                print("That's a tiny package!")
                cprint("Nice!", 'yellow', attrs=['blink', 'reverse'])
                break
        except ValueError:
            cprint('Your package size has to be a number!\n', 'red')


if __name__ == '__main__':
    try_me()
