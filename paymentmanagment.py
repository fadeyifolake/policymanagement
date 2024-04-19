class PaymentManagement:
    def __init__(self):
        self.payments = {}  # Dictionary to store payment information

    def process_payment(self, policy_number, amount):
        if policy_number in self.payments:
            self.payments[policy_number].append(amount)
        else:
            self.payments[policy_number] = [amount]
        return True

    def send_reminder(self, policy_number):
        if policy_number in self.payments:
            total_payments = sum(self.payments[policy_number])
            if total_payments < 0:
                print("Reminder sent: Please make a payment to avoid policy suspension.")
                return True
            else:
                print("No reminder needed: Payments are up to date.")
                return False
        else:
            print("Policyholder not found.")
            return False

    def apply_penalty(self, policy_number, penalty_amount):
        if policy_number in self.payments:
            self.payments[policy_number].append(-penalty_amount)  # Negative amount indicates penalty
            return True
        else:
            print("Policyholder not found.")
            return False

    def display_payment_details(self, policy_number=None):
        if policy_number is None:
            return self.payments
        else:
            if policy_number in self.payments:
                return {policy_number: self.payments[policy_number]}
            else:
                return None
