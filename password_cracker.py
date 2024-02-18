import hashlib

def crack_sha1_hash(sha1_hash, use_salts=False):
    # Read passwords from file
    with open('top-10000-passwords.txt', 'r') as f:
        passwords = f.read().splitlines()

    if use_salts:
        # Read salts from file
        with open('known-salts.txt', 'r') as f:
            salts = f.read().splitlines()

        # Try combinations of password and salt
        for password in passwords:
            for salt in salts:
                salted_password = salt + password
                hashed = hashlib.sha1(salted_password.encode()).hexdigest()
                if hashed == sha1_hash:
                    return password

                salted_password = password + salt
                hashed = hashlib.sha1(salted_password.encode()).hexdigest()
                if hashed == sha1_hash:
                    return password
    else:
        # Try plain passwords
        for password in passwords:
            hashed = hashlib.sha1(password.encode()).hexdigest()
            if hashed == sha1_hash:
                return password

    # Password not found
    return "PASSWORD NOT IN DATABASE"
