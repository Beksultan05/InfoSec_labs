rom itertools import product

name = "Belka"
surname = "Tumanov"
birth_date = "2005"

year = birth_date[-4:]
day_month = birth_date[:4]

words = [
    name.lower(),
    name.capitalize(),
    surname.lower(),
    surname.capitalize()
]

numbers = [
    year,
    day_month,
    birth_date
]

symbols = ["", "!", "@", "123"]

passwords = set()

for word, number, symbol in product(words, numbers, symbols):
    passwords.add(word + number + symbol)
    passwords.add(number + word + symbol)

with open("personalized_passwords.txt", "w") as file:
    for password in sorted(passwords):
        file.write(password + "\n")

print(f"Generated {len(passwords)} passwords")
