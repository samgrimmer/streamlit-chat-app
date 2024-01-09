from dataclasses import dataclass

@dataclass
class RecentHistoryDto:
    session_id: str
    question: str
