from dataclasses import dataclass

@dataclass
class UserClaimDto:
    typ: str
    val: str
