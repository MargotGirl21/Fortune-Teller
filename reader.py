import csv

print('Welcome to your daily horoscope!')

user_month = input("First, tell me the month you were born in (1-12)")
user_day = input("What day is your birthday?" )

def csv_reader(file):
    filtered_data = []
    with open(file, 'r') as csvfile:
        csv_reader = csv.reader(csvfile)
        next(csv_reader)
        for row in csv_reader:
            month, day, star_sign, fortune = row
            filtered_data.append((month,day,star_sign,fortune))
    return filtered_data

def sign_reader(user_month, user_day, horoscope_data):
    user_month, user_day= str(user_month), str(user_day)
    for month, day, star_sign, fortune in horoscope_data:
        if day == user_day and month == user_month:
            print(f'Your star sign is {star_sign}')
            return star_sign, fortune
    return None, None

def fortune_teller(star_sign, horoscope_data):
    ask_fortune = input("Would you like to hear your daily fortune? (y/n)")
    if ask_fortune == "y":
        print(f"Your daily fortune: {fortune}")
    elif ask_fortune == "n":
        print("Thanks for using the fortune teller!")
    else:
        print("Error: please enter y/n")


data = csv_reader("horoscope_dates.csv")
sign, fortune = sign_reader(user_month, user_day, data)
fortune_teller = fortune_teller(sign, fortune)


    

