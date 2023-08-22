#!/usr/bin/python3

class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        self.__engine = create_engine('mysql+mysqldb://{}:{}@HBNB_MYSQL_HOST/{}'\
                .format(HBNB_MYSQL_DB, HBNB_MYSQL_USER, HBNB_MYSQL_PWD, pool_pre_ping=True)
        if HBNB_ENV == test:
            Session = sessionmaker(bind=engine)
            DBStorage.__session = Session()
            DBStorage.__session.query("DROP TABLE *)
