import hashlib

# Small issue here but 6 characters might be a bit too short
# since after enough shorts urls are stored, we can
# have identical short ids (collisions)
def generate_short_id(url):
    return hashlib.sha256(url.encode()).hexdigest()[:6]
