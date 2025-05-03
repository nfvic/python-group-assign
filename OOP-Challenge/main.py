from pet import Pet

# Create a pet
my_pet = Pet("Max")
print(f"Creating pet: {my_pet.name}")

# Perform actions
my_pet.eat()
my_pet.play()
my_pet.sleep()

# Display status
print()
my_pet.get_status()

# Train and show tricks
my_pet.train("roll over")
my_pet.train("play dead")
my_pet.show_tricks()
