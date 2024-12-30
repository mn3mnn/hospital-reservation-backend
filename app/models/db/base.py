from sqlalchemy.ext.declarative import declarative_base

_Base = declarative_base()


class SQLBase(_Base):
    """
    Base class for all SQL models
    """
    __abstract__ = True

    # id: int
    # created_at: datetime
    # updated_at: datetime
    # deleted_at: datetime
    # created_by: str
    # updated_by: str
    # deleted_by: str
    # is_deleted: bool
    # is_active: bool
    #
    # def __repr__(self):
    #     return f"<{self.__name__} id={self.id}>"

