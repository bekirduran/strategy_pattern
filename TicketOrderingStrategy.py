from abc import ABC, abstractmethod
from typing import List
from SupportTicket import SupportTicket


class TicketOrderingStrategy(ABC):
    @abstractmethod
    def create_ordering(self, ticket_list: List[SupportTicket]) -> List[SupportTicket]:
        pass
