from faker import Faker

print("_"*80, "\nFAKE USER\n")

fake = Faker()

print("-"*80)

print(fake.name())
print(fake.email())
print(fake.country())
print(fake.profile())

print("-"*80)
