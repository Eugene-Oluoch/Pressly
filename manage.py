#imports
from app import create_app, db
from flask_script import Manager, Server
from app.models import User, Post
from flask_migrate import Migrate,MigrateCommand


#Selection of the app state
app = create_app('production')
manager = Manager(app)

#Migration set Commands
migrate = Migrate(app,db)
manager.add_command('db',MigrateCommand)


#App Shell for the Database
@manager.shell
def make_shell_context():
    return dict(app = app, db = db, User = User, Post = Post)


#This handles the app run state
manager.add_command('server',Server)
if __name__ == '__main__':
    manager.run()