from dataclasses import dataclass
from typing import Optional
from datetime import datetime


@dataclass
class CompanyBean:
    id: str
    name: str
    domain: Optional[str]
    industry: Optional[str]
    logo_url: Optional[str]
    location: Optional[str]
    state: Optional[str]
    created_at: datetime
    updated_at: datetime
