from pydantic import BaseModel


class GetTasks(BaseModel):
    """Schema bookingdates."""

    checkin: date
    checkout: date