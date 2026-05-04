import pandas as pd
import os
import re #regular expression
import datetime 

CSV_FILE = "user_data.csv"

#inititalizing csv file with columns

def init_csv():
    if not os.path.exists(CSV_FILE):
        df = pd.DataFrame(columns=[
            'user_id','full name','email','phone','password','registration_date','last_login'
        ])
        df.to_csv(CSV_FILE, index=False)


#validation funcation


def validate_email(email):
    """Email Validation Using Regex"""
    pattern= r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0_9._]+\.[a-zA-Z]{2,}$'
    if re.match(pattern,email):
        return True, "Valid Email"
    return False, "Invalid Email Format i.e user@domain.com"


def validate_phone(phone):
    """Phone Validation for Pakistani number format"""
    #Removing spaces and dashes from phone number

    phone = re.sub(r'[\s\-]','',phone)

#check different phone formats


def validation_phone(phone):
    pattern = [
        r'^03[0-9]{9}$',  #03XXXXXXXXXXXXX (Pakistan Mobile Number)
        r'^3[0-9]{9}$',    #3XXXXXXXXXX
        r'^\+923[0-9]{9}$',  #+923XXXXXXXX  
        r'^[0-9]{11}$',     #11 digits 
        r'^00923[0-9]{9}$'
    ]

    for pattern in pattern:
        if re.match(pattern,phone):
            return True, "Valid Phone Number"
    return False, "Invalid Phone Number"

def validate_password(password):
    """Password strength validation"""
    if len(password) < 8:
        errors.append("Password must be at least 8 characters long.")
    if len(password) > 20:
        errors.append("Password must be no less than 20 characters .")
    if not re.search(r'[A-Z]', password):
        errors.append("Password must contain at least one uppercase letter.")
    if not re.search(r'[a-z]', password):
        errors.append("Password must contain at least one lowercase letter.")
    if not re.search(r'[0-9]', password):
        errors.append("Password must contain at least one digit.")
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        errors.append("Password must contain at least one special character.")
    if errors:
        return False, f"Password mush have {", ".join(errors)}"
    return True, "Strong Password"
def validate_name(name,failed_name="Name"):
    """Name Validation for alphabets and spaces only"""
    if len(name) < 2:
        return False, f"{failed_name} must be at least 2 characters long."
    if len(name) > 50:
        return False, f"{failed_name} must be less than 50 characters long."
    if not re.match(r'^[a-zA-Z\s\-]+$', name):
        return False, f"{failed_name} must contain only alphabets and spaces."
def valudation_user_id(user_id):
    """User ID Validation for uniqueness and format"""
    if len(user_id) < 4:
        return False, "User ID must be at least 4 characters long."
    if len(user_id) > 20:
        return False, "User ID must be less than 20 characters long."
    if not re.match(r'^[a-zA-Z0-9_]+$', user_id):
        return False, "User ID must contain only alphanumeric characters and underscores."
    if os.path.exists(CSV_FILE):
        df = pd.read_csv(CSV_FILE)
        if user_id in df['user_id'].values:
            return False, "User ID already exists. Please choose a different one."
    return True, "Valid User ID"
def save_user(user_id, full_name, email, phone, password):
    """Save user data to CSV file"""
    init_csv()
    new_user =pd.DataFrame([{}])