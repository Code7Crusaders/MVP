from datetime import datetime
from pydantic import BaseModel

class SupportMessageDTO(BaseModel):
    id: int
    user_id: int
    description: str
    status: bool
    subject: str
    created_at: datetime = datetime.now()

