spam_amount = 0
print(spam_amount)

spam_amount = spam_amount + 4

if spam_amount > 0:
    print("But I don't want ANY spam!")

viking_song = "Spam " * spam_amount
print(viking_song)

# help(round(-2.01))

def least_difference(a, b, c):
    """ Return the smallest difference between any two numbers among a, b and c.  
    >>> least_difference(1, 5, -5)
    4
    """
    diff1 = abs(a - b)
    diff2 = abs(b - c)
    diff3 = abs(a - c)
    return min(diff1, diff2, diff3)

# print(
#     least_difference(1, 10, 100),
#     least_difference(1, 10, 10),
#     least_difference(5, 6, 7)
# )

def greet(who="Colin"):
    print("Hello,", who)

greet()
greet(who="Kaggle")
greet("world")

def mult_by_five(x):
    return 5 * x

def call(fn, arg):
    """Call fn on arg"""
    return fn(arg)

def squared_call(fn, arg):
    """Call fn on the result of calling fn on arg"""
    return fn(fn(arg))

# print(
#     call(mult_by_five,  1),
#     squared_call(mult_by_five, 1),
#     sep='\n'
# )

def mod_5(x):
    """Return the remainder oof x after dividing by 5"""
    return x % 5

print(
    'which number is biggest?',
    max(100, 51, 14),
    'Which number is the biggest modulo 5?',
    max(100, 51, 14, key=mod_5),
    sep="\n"
)


def can_run_for_president(age):
    """Can someone of the given agae for president in the US?"""
    return age >= 35

print("Can a 19-year-old run for president?",can_run_for_president(19))
print("Can a 45-year-old run for president?", can_run_for_president(45))
# help(least_difference)

