import string
import random


class SupportTicket:
    id: str
    customer: str
    issue: str

    def generate_id(self,lenght=8):
        return ''.join(random.choices(string.ascii_uppercase, k=lenght))

    def __init__(self, customer, issue):
        self.id = self.generate_id()
        self.customer = customer
        self.issue = issue

