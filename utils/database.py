import psycopg2
from .database_connection import Database

database_name = "password_manager"
user = "postgres"
password = "postgres"


database = Database(database_name, user, password)


def create_table():
    with database as cur:
        query = """
        create table if not exists passwords(
            pw_id serial primary key,
            url varchar(100) not null,
            application_name varchar(100) not null,
            username varchar(100) not null,
            sec_password varchar(200) not null
        )
        """
        try:
            cur.execute(query)
            print("Table created.")
        except psycopg2.Error as err:
            raise err


def insert_into_table(url, application_name, username, password):
    query = """
    insert into passwords(url, application_name, username, sec_password)
    values (%s,%s,%s,%s)
    """
    with database as cur:
        try:
            cur.execute(query, (url, application_name, username, password))
            print("Inserted into db.")
        except psycopg2.Error as err:
            raise err


def get_all():
    query = """
    select * from passwords
    """
    with database as cur:
        try:
            cur.execute(query)
            results = cur.fetchall()
            return results
        except psycopg2.Error as err:
            raise err


def get_one(application_name=None, url=None):
    query = """
    select * from passwords
    where application_name = (%s)
    or url = (%s)
    """
    with database as cur:
        try:
            cur.execute(query, (application_name, url))
            result = cur.fetchall()
            return result
        except psycopg2.Error as err:
            raise err


def remove_application(application_name=None, url=None):
    query = """
    delete from passwords
    where application_name = (%s)
    or url = (%s)
    """
    with database as cur:
        try:
            cur.execute(query, (application_name, url))
            print("Application deleted")
        except psycopg2.Error as err:
            raise err
