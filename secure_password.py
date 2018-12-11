import random as rd
import string as s


sym = s.ascii_letters + s.digits + s.punctuation

secure_random = rd.SystemRandom()
password = "".join(secure_random.choice(sym) for i in range(14))

print password
