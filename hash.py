import hashlib
#The first part depends on the framework you are using
#Let's say you get a password in clear format from the request:
password = "MD5Online"

# #The second part depends on the database you are using
# #But your password is hashed in the database, 
# #so you get a string like:
# db_password = "d49019c7a78cdaac54250ac56d0eda8a"

# #Finally, validate that the two passwords are the same
# if (hashlib.md5(password.encode()).hexdigest() == db_password):
#    print("Authentication success")
# else:
#    print("Bad login or password")
#    #Probably redirect or display again the login form

print(hashlib.md5("alicepassword".encode()).hexdigest())
print(password)

print(hashlib.md5("bobpassword".encode()).hexdigest())
print(password)

print(hashlib.md5("tompassword".encode()).hexdigest())
print(password)