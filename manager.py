# coding:utf-8
__author__ = "piels"

from main import app, db, User, Post, Tag

from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand



migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command("server", Server())
manager.add_command("db", MigrateCommand)


@manager.shell
def make_shell_context():
    return dict(app=app, db=db, User=User, Tag=Tag)


if __name__ == '__main__':
    manager.run()
