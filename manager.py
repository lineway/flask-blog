# coding:utf-8
__author__ = "piels"

import os
from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand
from webapp import create_app
from webapp.models import db, User, Post, Tag, Comment

# 默认使用dev配置

env = os.environ.get('WEBAPP_ENV', 'dev')
app = create_app('webapp.config.%sConfig' % env.capitalize())


migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command("server", Server())
manager.add_command("db", MigrateCommand)

@manager.shell
def make_shell_context():
    return dict(app=app, db=db, User=User, Tag=Tag, Post=Post, Comment=Comment)


if __name__ == '__main__':
    manager.run()

# from flask_migrate import Migrate, MigrateCommand
# from flask_script import Manager, Server
#
# from webapp import app
# from webapp.models import db, User, Post, Tag, Comment
#
#
# migrate = Migrate(app, db)
#
# manager = Manager(app)
# manager.add_command("server", Server())
# manager.add_command("db", MigrateCommand)
#
#
# @manager.shell
# def make_shell_context():
#     return dict(app=app, db=db, User=User, Tag=Tag)
#
#
# if __name__ == '__main__':
#     manager.run()
