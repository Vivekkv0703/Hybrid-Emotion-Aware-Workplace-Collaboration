from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class EmployeeBean:
    id: str
    first_name: str
    last_name: str
    email: str
    role: Optional[str]
    is_active: bool
    company_id: str
    created_at: datetime
    updated_at: datetime
    manager_id: Optional[str] = None
