# Customer Service Bot


# Customer Service Bot Function
def cs_service_bot():
    print("""Hello! Welcome to the DNS Cable Company's Service Portal. Are you a new or existing customer?)
            [1] New Customer
            [2] Existing Customer""")
    response = int(input("Please enter the number corresponding to your choice: "))
    if response == 1:
        new_customer()
    elif response == 2:
        existing_customer()
    else:
        print("Sorry, we didn't understand your selection. Please try again.")
        cs_service_bot()


# New Customer Function
def new_customer():
    print("""Welcome!
            [1] Sign up for service.
            [2] Schedule a home visit.
            [3] Speak to a sales representative.""")
    response = int(input("Please enter the number corresponding to your choice: "))
    if response == 1:
        sign_up()
    elif response == 2:
        home_visit("new install")
    elif response == 3:
        live_rep()
    else:
        print("Sorry, we didn't understand your selection. Please try again.")
        new_customer()


# Existing Customer Function
def existing_customer():
    print("""What kind of support do you need?
            [1] Television Support
            [2] Internet Support
            [3] Speak to a support representative""")
    response = int(input("Please enter the number corresponding to your choice: "))
    if response == 1:
        television_support()
    elif response == 2:
        internet_support()
    elif response == 3:
        live_rep()
    else:
        print("Sorry, we didn't understand your selection. Please try again.")
        existing_customer()


# Television Support Function
def television_support():
    print("""What is the nature of your problem?
            [1] I can't access certain channels.
            [2] My picture is blurry.
            [3] I keep losing service.
            [4] Other issues.""")
    response = int(input("Please enter the number corresponding to your choice: "))
    if response == 1:
        print(""""Please check the channel lists at DefinitelyNotSinister.com. 
                If the channel you cannot access is there, please contact a live representative.""")
        did_that_help()
    elif response == 2:
        print("Try adjusting the antenna above your television set.")
        did_that_help()
    elif response == 3:
        print("Is it raining outside? If so, wait until it is not raining and then try again.")
        did_that_help()
    elif response == 4:
        live_rep()
    else:
        print("Sorry, we didn't understand your selection. Please try again.")
        television_support()


# Internet Support Function
def internet_support():
    print("""What is the nature of your problem?
            [1] I can't connect to the internet.
            [2] My connection is very slow.
            [3] I can't access certain sites.
            [4] Other issues.""")
    response = int(input("Please enter the number corresponding to your choice: "))
    if response == 1:
        print("Unplug your router, then plug it back in, then give it a good whack, like the Fonz.")
        did_that_help()
    elif response == 2:
        print("""Make sure that all cell phones and other peoples computers are not connected to the internet,"
                so that you can have all the bandwidth.""")
        did_that_help()
    elif response == 3:
        print("Move to a different region or install a VPN. Some areas block certain sites.")
        did_that_help()
    elif response == 4:
        live_rep()
    else:
        print("Sorry, we didn't understand your selection. Please try again.")
        internet_support()


# "Did That Help?" Function
def did_that_help():
    print("""Did the provided solution solve your problem?
            [1] Yes
            [2] No""")
    response = int(input("Please enter the number corresponding to your choice: "))
    if response == 1:
        print("Thank you for choosing DNS Company, have a great day!")
    elif response == 2:
        print("""Would you like to talk with a live representative or schedule a home visit?
                [1] Speak to a live representative
                [2] Schedule a home visit
                [3] Neither""")
        response2 = int(input(" Please enter the number corresponding to your choice: "))
        if response2 == 1:
                live_rep()
        elif response2 == 2:
                home_visit("support")
        elif response2 == 3:
            print("""We are sorry we were unable to help you today.
                    We will be here should you need additional assistance.""")
            # Escape?
        else:
            print("Sorry, we didn't understand your selection. Please try again.")
            did_that_help()
            # Fix to route back to sub menu instead of start of function did_that_help
    else:
        print("Sorry, we didn't understand your selection. Please try again.")
        did_that_help()


# Sign-Up Function
def sign_up():
    print("""Great choice, friend! We're excited to have you join the DNS family!
            Please select the package you are interested in signing up for.
            [1] Bundle Deal (Internet + Cable)
            [2] Internet
            [3] Cable""")
    response = int(input("Please enter the number corresponding to your choice: "))
    if response == 1:
        print("""You've selected the Bundle Package! 
                Please schedule a home visit and our technician will come and set up your new service.""")
        home_visit("new install")
    elif response == 2:
        print("""You've selected the Internet Only Package!
                Please schedule a home visit and our technician will come and set up your new service.""")
        home_visit("new install")
    elif response == 3:
        print("""You've selected the Cable Only Package!
                Please schedule a home visit and our technician will come and set up your new service.""")
        home_visit("new install")
    else:
        print("Sorry, we didn't understand your selection. Please try again.")
        sign_up()


# Home Visit Function
def home_visit(purpose):
    if purpose == "new install" or purpose == "support":
        visit_date = input("""Please enter a date when you are available for a technician to come to your home"
                             and {}""".format(purpose))
        print("""Wonderful! A technician will come visit you on {}.
               Please be available between the hours of 1:00am and 11:00pm.""".format(visit_date))
    else:
        print("""Please specify what the purpose of this home visit will be for:
                [1] New service installation.
                [2] Existing service repair.
                [3] Location scouting for unserviced region.""")
        response = int(input("Please enter the number corresponding to your choice: "))
        if response == 1:
            home_visit("new_install")
        elif response == 2:
            home_visit("support")
        elif response == 3:
            home_visit("scout")
        else:
            print("Sorry, we didn't understand your selection. Please try again.")
            home_visit("none")


# Live Rep Function
def live_rep():
    print("""Please hold while we connect you with a live sales representative.
            The wait time will be between two minutes and six hours.
            We thank you for your patience.""")
    # Future functionality to connect to representative called here.


# Start Bot
cs_service_bot()
