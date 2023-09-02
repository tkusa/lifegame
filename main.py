import config
from lifegame import LifeGame

def main():
    lg = LifeGame()
    lg.shuffle()
    lg.print()
    while True:
        i = input()
        lg.update()
        lg.print()

if __name__ == "__main__":
    main()