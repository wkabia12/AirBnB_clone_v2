from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base, BaseModel
from os import getenv
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import models


class DBStorage:
    """This class manages storage of hbnb models using SQLAlchemy"""

    __engine = None
    __session = None

    def __init__(self):
        """Creates the engine and links to the MySQL database"""

        usr = getenv("HBNB_MYSQL_USER")
        pwd = getenv("HBNB_MYSQL_PWD")
        ht = getenv("HBNB_MYSQL_HOST")
        db = getenv("HBNB_MYSQL_DB")
        env = getenv("HBNB_ENV")
        self.__engine = create_engine(f'mysql+mysqldb://{usr}:{pwd}@{ht}/{db}',
                                      pool_pre_ping=True)

        if env == "test":
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """Query on the current database session and return a dictionary"""

        objects_dict = {}

        if cls is not None:
            if cls in [User, State, City, Amenity, Place, Review]:
                for obj in self.__session.query(cls).all():
                    key = f"{obj.__class__.__name__}.{obj.id}"
                    objects_dict[key] = obj
        else:
            for c in [User, State, City, Amenity, Place, Review]:
                for obj in self.__session.query(c).all():
                    key = f"{obj.__class__.__name__}.{obj.id}"
                    objects_dict[key] = obj

        return objects_dict

    def new(self, obj):
        """Add the object to the current database session"""
        session = self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session"""

        self.__session.commit()

    def delete(self, obj=None):
        """Delete from the current database session obj if not None"""

        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables in the database and create a session"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """
        calls remove() method on the pricate session attribute
        """
        if self.__session:
            self.__session.close()
