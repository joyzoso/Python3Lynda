#!/usr/bin/python3


def main():
    choices = dict(
        one = 'joy',
        two = 'fun',
        three = 'yay',
        four = 'lala',
        five = 'wine'
    )
    v = 'you'
    print(choices.get(v, 'sorry')) #.get here creates a default value

if __name__ == "__main__": main()

