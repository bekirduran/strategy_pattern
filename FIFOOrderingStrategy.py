from SupportTicket import SupportTicket
from TicketOrderingStrategy import TicketOrderingStrategy
from typing import List


class FIFOOrderingStrategy(TicketOrderingStrategy):
    def create_ordering(self, ticket_list: List[SupportTicket]) -> List[SupportTicket]:
        return ticket_list.copy()