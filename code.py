import pandas as pd

def email_slicer(email):
    # Split the email address into username and domain
    username, domain = email.split('@')
    
    # Initialize first name and last name
    first_name = ""
    last_name = ""
    
    # Check if there are any delimiters in the username
    delimiters = ['.', '-', '_']
    delimiter_found = False
    for delimiter in delimiters:
        if delimiter in username:
            first_name, last_name = username.split(delimiter)
            delimiter_found = True
            break
    
    # If no delimiter found, consider the full username as the first name
    if not delimiter_found:
        first_name = username
    
    # Capitalize the first letter of first name and last name
    first_name = first_name.capitalize()
    last_name = last_name.capitalize()
    
    return username, domain, first_name, last_name

def main():
    # Read the Excel file
    df = pd.read_excel("./src/emails.xlsx")

    # Extract email addresses from the DataFrame
    email_list = df["Email"].tolist()

    # Loop through the list and slice each email
    for email in email_list:
        username, domain, first_name, last_name = email_slicer(email)
        print("Email:", email)
        print("Username:", username)
        print("Domain:", domain)
        print("First Name:", first_name)
        print("Last Name:", last_name)
        print()  # Add a blank line between email addresses

if __name__ == "__main__":
    main()
