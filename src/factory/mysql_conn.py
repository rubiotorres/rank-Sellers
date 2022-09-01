from sqlalchemy import create_engine, pool, desc, inspect
from sqlalchemy.orm import sessionmaker

from src.exception.process_exception import ProcessSystemException
from src.factory.base import Base
from src.factory.db_config import DbConfig
from src.factory.db_connection import DbConnection
from src.model.seller import Seller


class MysqlConn:  # pragma: no cover

    def __init__(self):
        self.__engine = None
        self.__session = None

    def get_engine(self, config: DbConfig):
        engine = create_engine(
            config.connection_string.format(config.user, config.password, config.host, config.port),
            poolclass=pool.QueuePool)
        inspect_engine = inspect(engine).get_schema_names()

        if config.database not in inspect_engine:
            engine.execute(f"CREATE DATABASE {config.database}")
        return create_engine(
            config.connection_string.format(config.user, config.password, config.host,
                                            config.port) + f"/{config.database}",
            poolclass=pool.QueuePool)

    def connect(self, config: DbConfig) -> DbConnection:
        try:
            self.__engine = self.get_engine(config)
            self.__session = sessionmaker(bind=self.__engine)
            self.__session.configure(bind=self.__engine)

        except Exception as e:
            raise ProcessSystemException(e)

    def create_session(self):
        session = sessionmaker(bind=self.__engine)
        session.configure(bind=self.__engine)

        self.__session = session()
        return self.__session

    def close(self):
        if self.__session:
            self.__session.close()
        if self.__engine:
            self.__engine.dispose()

    def create_all(self):
        self.create_session()
        Base.metadata.create_all(self.__engine)
        self.__session.close()

    def find_all(self, model):
        self.create_session()
        query = self.__session.query(model).all()
        self.__session.close()
        return query

    def find_filter(self, model, attr, value):
        self.create_session()
        query = self.__session.query(model)
        query = query.filter(getattr(model, attr) == value).one_or_none()
        self.__session.close()
        return query

    def count_rows(self, model):
        self.create_session()
        query = self.__session.query(model).count()
        self.__session.close()
        return query

    def commit_element(self):
        self.__session.commit()

    def add_element(self, element):
        self.create_session()
        self.__session.add(element)
        sess = self.__session
        self.__session.commit()
        self.__session.refresh(element)

        self.__session.close()
        return element.get_dict_model()

    def find_all_desc(self, model, col):
        self.create_session()
        query = self.__session.query(model).order_by(desc(col)).all()
        self.__session.close()
        return query

    def update_element_seller(self, element, sales):

        self.create_session()
        result = self.__session.query(Seller).filter(Seller.id == element.id).update({"sales": sales})
        self.__session.commit()
        self.__session.close()

        if result:
            return element
        else:
            return None

    def create_table(self, table):
        if not inspect(self.__engine).has_table(table.name):
            table.create(self.__engine)

    def delete_row(self, model, attr, value):
        self.create_session()
        query = self.__session.query(model)
        query = query.filter(getattr(model, attr) == value).delete()
        self.__session.commit()

        self.__session.close()
        return query
