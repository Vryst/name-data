import datetime as dt

red = '\033[91m'
green = '\033[92m'
blue = '\033[94m'
bold = '\033[1m'
bg = '\033[3m'
underline = '\033[4m'
end = '\033[0m'



arrowr = 20*"→"
arrowl = 20*"←"
arr2 = 31*"→"
arl2 = 31*"←"
sp1 = 15*"—"



name = input(bold + "Enter your name = " + bold + bg + end)

print(f"{bold}{blue}{arr2}\n{arl2}{end}")

print(f"""\n\n{bold}Please enter your date,
Month,
And year of birth.{end}
""")

print(f"{bold}{blue}{arr2}\n{arl2}{end}")


date = int(input(bold + "\n\nDate = " + end))
month = int(input(bold + "Month \t= " + end))
year = int(input(bold + "Year \t= " + end))

today = dt.date.today()
print(21*"—")

print(f"{bold}Current date is = {bg}{today}{end}")

print(21*"—")


date_of_birth = dt.date(year,month,date)

print(f"\n{bold}Your date of birth is = {green}{date_of_birth}{end}")

day_of_birth = f"{date_of_birth:%A}"

print(f"Your birthday is = {day_of_birth}")

age = today - date_of_birth
age1 = age // 365
age_m = (age.days % 365) // 30
print(f"{bold}Your age is = {green}{age1.days} year and {age_m} months {end}")

print(f"""\n\n{bold}Thank you {green}{nama}'s{end} {bold}for using this program{end}

{bold}{blue}{underline}{sp1}/End of the program\{sp1}{end}
""")
