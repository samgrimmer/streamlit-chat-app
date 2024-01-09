from dataclasses import dataclass
from typing import Optional

@dataclass
class UserInfoDto:
    username: Optional[str]
    email: Optional[str]
    
    def clean_username(self) -> str:
        return self.username.replace(' ', '-')
