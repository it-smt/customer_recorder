from datetime import datetime

from ninja import Schema


class RecordBodySchema(Schema):
    """Схема записи клиента."""
    service: int  # id услуги
    master: int  # id мастера
    date: datetime
    first_name: str
    last_name: str
    middle_name: str
    phone: str
    email: str
