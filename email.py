# New class below for Email
class Email:
    # Creating the constructor for the Email class including the information attributes the Email will hold
    def __init__ (self, email_contents, from_address):
        self.has_been_read = False  # Has been read is also an attribute but is not included above, False as default
        self.email_contents = email_contents
        self.is_spam = False  # Same as has been read logic
        self.from_address = from_address

    # Output in String format for reading purposes
    def __str__(self):
        return f"From:              {self.from_address}\n" \
               f"Email Contents:    {self.email_contents}\n" \
               f"Read:              {self.has_been_read}\n" \
               f"Spam:              {self.is_spam}\n"
    # should the below method be called upon then the email will turn to being read/true
    def mark_as_read(self):
        self.has_been_read = True
    # as above if the below method is used then the email will now be True for Spam
    def mark_as_spam(self):
        self.is_spam = True

# First function is adding a new email, the user will input the attributes required for the email class
def add_email():
    email_contents = input("Enter email contents: ")
    from_address = input("Enter email address: ")
    return Email(email_contents, from_address)  # return/create the new email using the user's input

# This function will count the number of items in the inbox list, newly created below
def get_count():
    return print(len(inbox))

# Using the users chosen email index, the below function will locate the email and mark the read attribute to True
# Note the email will say unread on the first call of this function
def read_email():
    user_email_choice = int(input("What index email do you want? "))
    selected_email = inbox[user_email_choice]
    print(selected_email)
    selected_email.mark_as_read() # Using the mark_as_read() function to change the attibute

# This function loops through the inbox and will print each email which is not read yet
def get_unread_emails():
    for email in inbox:
        if email.has_been_read == False:
            print(email)

# Similarly to the mark as read function, this will mark the email as Spam and therefore change the attribute to True
def mark_spam():
    user_spam_choice = int(input("What index email do you want to mark as spam? "))
    selected_spam_email = inbox[user_spam_choice]
    selected_spam_email.mark_as_spam()
    print("Email now marked as spam")

# This function will loop through the email list and print each email which is Spam
def get_spam():
    for email in inbox:
        if email.is_spam:
            print(email)

# This function allows the user to delete emails using a index determined by the user
def delete_email():
    user_delete = int(input("What email index do you want to delete? "))
    inbox.pop(user_delete)

# Empty list below to be populated
inbox = []
# User's choice being set to empty before making a choice.
user_choice = ""

while user_choice != "quit":
    user_choice = input("What would you like to do - \nread (r) \nget unread emails (gue) \nemail count (ec) \nadd email (ae) \nmark-spam (ms) "
                        "\nget spam emails (gse)\ndelete (d) \nquit (q)? ")
    if user_choice == "r":
        read_email()
    elif user_choice == "gue":
        get_unread_emails()
    elif user_choice == "ec":
        get_count()
    elif user_choice == "ae":
        new_email = add_email()
        inbox.append(new_email)
    elif user_choice == "ms":
        mark_spam()
    elif user_choice == "gse":
        get_spam()
    elif user_choice == "d":
        delete_email()
    elif user_choice == "q":
        print("Goodbye")
    else:
        print("Oops - incorrect input")
