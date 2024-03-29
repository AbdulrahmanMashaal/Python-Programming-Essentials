"""
Testing template for number_to_name()
"""

###################################################
# Copy and paste your definition of number_to_name() here

def number_to_name(number):
    """
    Take string name as input (rock-Spock-paper-lizard-scissors)
    and returns integer (0-1-2-3-4)
    """
    if number == 0:
        return("rock")
    elif number == 1:
        return("Spock")
    elif number == 2:
        return("paper")
    elif number == 3:
        return("lizard")
    elif number == 4:
        return("scissors")


###################################################
# Test calls to number_to_name()
print(number_to_name(0))
print(number_to_name(1))
print(number_to_name(2))
print(number_to_name(3))
print(number_to_name(4))



###################################################
# Output to the console should have the form:
# rock
# Spock
# paper
# lizard
# scissors
