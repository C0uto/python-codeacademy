import random
import string
def generate_key(groups, group_length):
    characters = string.ascii_uppercase + string.digits
    key = '-'.join(''.join(random.choice(characters) for _ in range(group_length)) for _ in range(groups))
    return key
key_groups = 5
group_length = 5
generated_key = generate_key(key_groups, group_length)
print(generated_key)