import calendar

print("-"*80, "\nCALENDAR\n")

print("."*80)
year =int( input("Enter year :"))
month = int( input("Enter month :"))
print("."*80)

print("-"*80)
print(calendar.month(year,month))
print("-"*80)
