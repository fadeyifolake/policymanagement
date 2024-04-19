class PolicyHolderManagement:
    def __init__(self):
        self.policyholders = {}  # Dictionary to store policyholders

    def register_policyholder(self, name, policy_number):
        if policy_number not in self.policyholders:
            self.policyholders[policy_number] = {"name": name, "status": "Active"}
            return True
        else:
            print("Policyholder with the same policy number already exists.")
            return False

    def suspend_policyholder(self, policy_number):
        if policy_number in self.policyholders:
            if self.policyholders[policy_number]["status"] == "Active":
                self.policyholders[policy_number]["status"] = "Suspended"
                return True
            else:
                print("Policyholder is already suspended.")
                return False
        else:
            print("Policyholder not found.")
            return False

    def reactivate_policyholder(self, policy_number):
        if policy_number in self.policyholders:
            if self.policyholders[policy_number]["status"] == "Suspended":
                self.policyholders[policy_number]["status"] = "Active"
                return True
            else:
                print("Policyholder is already active.")
                return False
        else:
            print("Policyholder not found.")
            return False

    def display_policyholder_details(self, policy_number=None):
        if policy_number is None:
            return self.policyholders
        else:
            if policy_number in self.policyholders:
                return self.policyholders[policy_number]
            else:
                return None




