from sqlalchemy import Date, cast
from datetime import datetime

created_at = datetime.now().date()
print(created_at)