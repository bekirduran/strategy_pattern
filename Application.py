from typing import List

from RandomOrderingStrategy import RandomOrderingStrategy
from SupportTicket import SupportTicket
from TicketOrderingStrategy import TicketOrderingStrategy


class CustomerSupport:
    tickets: List[SupportTicket] = []

    def create_ticket(self, customer, issue):
        self.tickets.append(SupportTicket(customer, issue))

    def process_tickets(self, processing_strategy: TicketOrderingStrategy):
        ticket_list = processing_strategy.create_ordering(self.tickets)

        if len(ticket_list) == 0:
            print("There are no tickets to process. Well Done!")
            return

        for ticket in ticket_list:
            self.process_ticket(ticket)

    def process_ticket(self, ticket: SupportTicket):
        print("============Ticket==============")
        print(f"Processing ticket id: {ticket.id}")
        print(f"Customer: {ticket.customer}")
        print(f"Issue: {ticket.issue}")
        print("============Ticket==============\n")

if __name__ == '__main__':
    app = CustomerSupport()

    app.create_ticket("Bekir DURAN", "Bilgisayardan garip sesler geliyor")
    app.create_ticket("Lenanard Luis", "I can't upload and remove the images, Can you help me please")
    app.create_ticket("Akin Mihaloğlu", "Klavyede bazı tuşlar basmıyor, bazılarıda bastıktan sonra kalkmıyor")

    app.process_tickets(RandomOrderingStrategy())
