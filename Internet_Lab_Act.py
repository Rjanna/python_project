def get_customer_input():
    print("Welcome to your local internet provider! To proceed, kindly enter the following information:")
    complete_details = False

    while not complete_details:
        print("-" * 50)
        name = input("Customer Name: ")

        # Validate name input
        if not name.isalpha():
            print("Invalid. Please enter letters only.")
            name = input("Customer Name: ")

        account_number = input("Account Number: ")

        # Validate account number
        if not account_number.isnumeric() or int(account_number) < 0:
            print("Invalid input. Please enter a positive number.")
            account_number = input("Account Number: ")

        phone_number = input("Phone Number: ")

        # Validate phone number
        if not phone_number.isnumeric() or int(phone_number) < 0:
            print("Invalid input. Please enter a positive number.")
            phone_number = input("Phone Number: ")

        email_address = input("Email Address: ")

        # Validate email address
        email_address = input("Email Address: ")
        # Use a regular expression to check if the email address is valid
        if "@" not in email_address:
            print("Invalid input. Please enter a valid email address.")


        internet_plan = input("Internet Plan (Standard, Pro, Business): ").lower()

        # Validate internet plan
        valid_plans = ["standard", "pro", "business"]
        if internet_plan not in valid_plans:
            print("Invalid input. Please choose a valid internet plan.")
            internet_plan = input("Internet Plan: ").lower()
            continue

        bandwidth_consumed = input("Bandwidth used for a month (MB): ")

        # Validate bandwidth
        if not bandwidth_consumed.isnumeric() or int(bandwidth_consumed) < 0:
            print("Invalid input. Please enter a positive number.")
            bandwidth_consumed = input("Bandwidth used for a month (MB): ")

        # Data is complete
        complete_details = True
        print("-" * 50)

    # Define constants
    STANDARD = 1000
    PRO = 2000
    BUSINESS = 3500
    STANDARD_EXCESS = 0.05
    PRO_EXCESS = 0.15
    BUSINESS_EXCESS = 0.5
    GBtoMB = 1024

 
    if internet_plan == "standard":
        # Check if bandwidth exceeded limit
        if int(bandwidth_consumed) > 30 * GBtoMB:
            excess_bandwidth_mb = int(bandwidth_consumed) - 30 * GBtoMB
            excess_charges = excess_bandwidth_mb * STANDARD_EXCESS

        total_bill = STANDARD + excess_charges

    elif internet_plan == "pro":
        # Check if bandwidth exceeded limit
        if int(bandwidth_consumed) > 60 * GBtoMB:
            excess_bandwidth_mb = int(bandwidth_consumed) - 60 * GBtoMB
            excess_charges = excess_bandwidth_mb * PRO_EXCESS

        total_bill = PRO + excess_charges

    elif internet_plan == "business":
        # Check if bandwidth exceeded limit
        if int(bandwidth_consumed) > 120 * GBtoMB:
            excess_bandwidth_mb = int(bandwidth_consumed) - 120 * GBtoMB
            excess_charges = excess_bandwidth_mb * BUSINESS_EXCESS

        total_bill = BUSINESS + excess_charges
    else:
        return


# Example usage:
name, account_number, phone_number, email_address, internet_plan, bandwidth_consumed = get_customer_input()
total_bill = calculate_total_bill(internet_plan, bandwidth_consumed)

# Print or use the obtained information as needed
print("Name:", name)
print("Account Number:",account_number)
print("Phone Number:", phone_number)
print("Email Address:",email_address)
print("Internet Plan:",internet_plan)
print("Bandwidth Consumed",bandwidth_consumed,"MB")
print("Total Bill:",total_bill,"Php")
