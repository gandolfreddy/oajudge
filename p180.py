# input
year = input()

# process
zodiac_dt = {"4":  "Rat", "5": "Ox", "6": "Tiger", "7": "Rabbit",  "8": "Dragon",
                          "9": "Snake", "10": "Horse", "11": "Goat",  "0": "Monkey",  "1": "Rooster",
             "2": "Dog", "3": "Pig"}
zodiac = zodiac_dt[str(int(year) % 12)]

# output
print(zodiac)
