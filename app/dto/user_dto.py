from dataclasses import dataclass
from typing import List
from dto.user_claim_dto import UserClaimDto

@dataclass
class UserDto:
    access_token: str
    expires_on: str
    id_token: str
    provider_name: str
    user_claims: List[UserClaimDto]
    user_id: str