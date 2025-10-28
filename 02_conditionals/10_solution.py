pet_age = int(input("Enter your pet's age in years: "))
pet = input("Enter your pet type (dog/cat): ").strip().lower()

if pet_age <2 and pet == "dog":
    food = "puppy food"
elif pet_age > 5 and pet == "cat":
    food = "senior cat food"
print("Recommended food for your pet is:", food)
