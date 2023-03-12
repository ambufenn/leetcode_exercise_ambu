'''
collect email from user
split the email with? @, user name, save by domain
ect


'''

def main():
    print("welkam to email slicer")
    print("")

    email_input = input("input your email address:")

    (username, domain) = email_input.split("@")
    (domain, extention)= domain.split(".")

    print("username:", username)
    print("domain:", domain)
    print("extention:", extention)

while True:
    main()



