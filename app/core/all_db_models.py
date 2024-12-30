
"""
Import all db models here to be registered with the metadata object and to be created in the database
if they do not exist.
"""

from app.models.db.base import (
    SQLBase
)
from app.models.db.doctors import (
    Doctor
)
from app.models.db.patients import (
    Patient
)
from app.models.db.reservations import (
    Reservation
)
from app.models.db.branches import (
Branch
)
# from app.models.db.users import (
#     User
# )
