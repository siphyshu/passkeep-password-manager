import hashlib

def get_hashed_password(plain_text_password):
    # Hash a password for the first time
    # Using bcrypt, the salt is saved into the hash itself
    return hashlib.sha1(plain_text_password.encode()).hexdigest()

def check_password(plain_text_password, hashed_password):
    # Check if given password is same as hashed password.
    if hashlib.sha1(plain_text_password.encode()).hexdigest() == hashed_password:
        return True

    else:
        return False
