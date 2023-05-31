from datetime import datetime

from peewee import DateTimeField, Model, MySQLDatabase, AutoField

from app.config.settings import CONFIG

mysql_config = CONFIG['mysql']

db = MySQLDatabase(mysql_config['database_name']['fastapi_quickstart'],
                   host=mysql_config['host'],
                   port=mysql_config['port'],
                   user=mysql_config['user'],
                   password=mysql_config['password'])


class BaseDatabaseModel(Model):
    class Meta:
        database = db

    id = AutoField()
    insert_time = DateTimeField(default=datetime.now, null=True)
    update_time = DateTimeField(null=True)

    def save(self, *args, **kwargs):
        self.update_time = datetime.now()
        return super(BaseDatabaseModel, self).save(*args, **kwargs)
