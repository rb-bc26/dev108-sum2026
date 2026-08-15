# this is DEV 108
# [07/26/2026]
# [Reecha Bharali]# This is where you will code your three functions 
# Be sure to write documentation for this module. Refer to your book chapter for instructions on how to do this.

# sayHello() ex: Hello Tony!
def sayHello(firstName):
    """Takes a first name and returns a greeting string with an
    exclamation point. Example: sayHello("Tony") returns "Hello Tony!"
    """
    return "Hello " + firstName + "!"

# fullName() ex: Tony Stark
def fullName(firstName, lastName):
    """Takes a first name and a last name and returns them joined
    together with a space in between. Example: fullName("Tony", "Stark")
    returns "Tony Stark"
    """
    return firstName + " " + lastName


# lastNameFirst() ex: Stark, Tony
def lastNameFirst(firstName, lastName):
    """Takes a first name and a last name and returns the last name
    first, followed by a comma, a space, and the first name.
    Example: lastNameFirst("Tony", "Stark") returns "Stark, Tony"
    """ 
    return lastName + ", " + firstName