# Example 2: Multiple default parameters
def create_profile(name, age=18, country="Unknown"):
    """Creates a user profile with default values"""
    print(f"Profile: {name}, Age: {age}, Country: {country}")

print("Multiple default parameters:")
create_profile("Alice")  # All defaults
create_profile("Bob", 25)  # Age specified
create_profile("Charlie", 30, "USA")  # All specified
print()