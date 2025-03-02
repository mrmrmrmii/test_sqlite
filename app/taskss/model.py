from datetime import datetime, timezone
from sqlalchemy import Column, String, Integer, DateTime
from app.database import Base
import pytz

msk_timezone = pytz.timezone('Europe/Moscow')

class tasks(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(255))
    description = Column(String(1024), nullable=True)
    created_at = Column(DateTime, default=lambda: datetime.now(msk_timezone))
    updated_at = Column(DateTime, default=lambda: datetime.now(msk_timezone), onupdate=datetime.now(timezone.utc))


