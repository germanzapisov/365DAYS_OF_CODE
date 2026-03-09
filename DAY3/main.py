import random
import string

letters = string.ascii_letters
integers = string.digits
special_symbols = string.punctuation

password = [
    random.choice(letters),
    random.choice(integers),
    random.choice(special_symbols)]

password += [random.choice(letters) for _ in range(10)]
password += [random.choice(integers) for _ in range(5)]
random.shuffle(password)
