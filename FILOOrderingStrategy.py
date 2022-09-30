from SupportTicket import SupportTicket
from TicketOrderingStrategy import TicketOrderingStrategy
from typing import List


class FILOOrderingStrategy(TicketOrderingStrategy):
    def create_ordering(self, ticket_list: List[SupportTicket]) -> List[SupportTicket]:
        list_copied = ticket_list.copy()
        list_copied.reverse()
        return list_copied