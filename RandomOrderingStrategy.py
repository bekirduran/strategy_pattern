
from typing import List
import random

from SupportTicket import SupportTicket
from TicketOrderingStrategy import TicketOrderingStrategy


class RandomOrderingStrategy(TicketOrderingStrategy):
    def create_ordering(self, ticket_list: List[SupportTicket]) -> List[SupportTicket]:
        random_list = ticket_list.copy()
        random.shuffle(random_list)
        return random_list
