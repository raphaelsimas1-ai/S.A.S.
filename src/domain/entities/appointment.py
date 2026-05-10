from dataclasses import dataclass
from datetime import datetime
@dataclass
class appointment:
    id: str
    client_name: str
    service_type: str
    start_time: datetime
    end_time: datetime
    is_confirmed: bool = False
