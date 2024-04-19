from policyholder import PolicyHolderManagement
from productmanagment import ProductManagement
from paymentmanagment import PaymentManagement


# Create instances of management classes
policyholder_manager = PolicyHolderManagement()
product_manager = ProductManagement()
payment_manager = PaymentManagement()

# Demonstration logic (same as before)
product_manager.create_product("P001", "Car Insurance", "Insurance for cars", 200)
policyholder_manager.register_policyholder("Alice", "PH001")
policyholder_manager.register_policyholder("Bob", "PH002")
payment_manager.process_payment("PH001", 200)

# Display account details for Alice and Bob
def display_account_details(policyholder_id):
    # Implementation of display_account_details function
    details = policyholder_manager.display_policyholder_details(policyholder_id)
    if details:
        print(f"\nAccount Details for {policyholder_id}:")
        print(f"Name: {details['name']}")
        print(f"Policy Number: {policyholder_id}")
    else:
        print(f"Policyholder {policyholder_id} not found.")

# Call the function to display account details for Alice and Bob
display_account_details("PH001")
display_account_details("PH002")