import hashlib
import string
import random
import time




challenge_string = 'ADHFUIF3384HCNFIF'

def generate_random(size = 30, challenge = challenge_string):

    nounce = ''.join(random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits) for x in range(size))
    return nounce
                     
nounce_data = generate_random()

def hasher(nounce = nounce_data):

    attempt = challenge_string + nounce

    sha256 = hashlib.sha256()
    sha256.update(attempt)
    digest = sha256.hexdigest()

    return digest




found = False
start_time = time.time()

while (found == False):
    nounce_data = generate_random()
    sha256val = hasher(nounce =nounce_data)

    if sha256val.startswith('00000'):

        time_spent = time.time() - start_time

        print 'Nounce Data :- ', nounce_data
        print 'Challenge :- ', challenge_string
        print 'Hasher :- ', sha256val
        print 'Time Spent :- ', time_spent
        found = True





