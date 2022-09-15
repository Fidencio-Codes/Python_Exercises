# Building an email slicer
# takes an email and slices into username, domain and extension 

# Collect email from user
# splt email using '@' symbol 
# save first part as username, second part as domain
# split domain using '.' symbol 


def main():
    print("Welcome to my email slicer\n")
    print("")
     
    email_input = input("Input your email address: ")

    (username, domain) = email_input.split("@")
    (domain, extension) = domain.split(".")

    print("Username: ", username)
    print("Domain :", domain)
    print("Extension:", extension)

while True:
    main()