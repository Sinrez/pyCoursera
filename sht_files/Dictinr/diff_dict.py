import sys

k = sys.argv[1].strip()
v = sys.argv[2].strip()

user = {
    "first_name": "Егор",
    "last_name": "Михеев",
    "sex": "m"
}
user.update( {k : v})


print(user)