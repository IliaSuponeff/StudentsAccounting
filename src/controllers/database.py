"""
Contains class implementing a sqlite-database connection

version: 0.0.2

versions-list:  0.0.1 - setup standard db functions(execution sql scripts and get their results)
                0.0.2 - adding external control functions

author: Ilia Suponev GitHub: https://github.com/ProgKalm
"""
import sqlite3
from settings import RuntimeSettings
from jinja2 import Template
from models.student import Student, Currency, StudentState


class DataBase:
    NONE_RESULT = 0
    ONE_RESULT = 1
    ALL_RESULTS = -1

    def __init__(self, settings: RuntimeSettings):
        self.settings = settings

        # build connection to db
        self._connection = sqlite3.connect(self.settings.get_resource_filepath('db.sqlite'))
        self._cursor = self._connection.cursor()

        # try to initialize db
        self._execute_script('init_db')

    def close(self):
        self.save()
        self._cursor.close()
        self._connection.close()

    def add_student(self, student: Student):
        self._execute_script('add_student')
        self.save()

    def _execute_script(self, script_name: str, **kwargs):
        script_data = self.settings.get_sql_script_filedata(f'{script_name}.sql')
        script_template = Template(script_data)
        script = script_template.render(kwargs)
        self._cursor.execute(script)

    def _get_results(self, count: int = 0):
        if count == self.NONE_RESULT:
            return ()

        if count == self.ONE_RESULT:
            return self._cursor.fetchone()

        if count <= self.ALL_RESULTS:
            return self._cursor.fetchall()

        return self._cursor.fetchmany(count)

    def save(self):
        self._connection.commit()
