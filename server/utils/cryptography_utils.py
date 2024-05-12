import hashlib

# hashing, not encrypt, a string value using the sha256 algorithm
def hash_sha256 (input_value):
    lib = hashlib.sha256()
    converted_byte_value = bytearray(input_value, 'utf-8')
    lib.update(converted_byte_value)
    return lib.hexdigest()