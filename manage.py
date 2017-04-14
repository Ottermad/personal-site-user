"""Managment File."""
import logging

from flask_script import Manager

from flask_migrate import Migrate, MigrateCommand, upgrade, migrate

from sqlalchemy import create_engine
from sqlalchemy.exc import ProgrammingError

from app import create_app, db
from app.main.models import User
from config import DATABASE_NAME

app = create_app()

migrater = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

logging.basicConfig(level=logging.INFO, format='[%(levelname)s] - %(message)s')


@manager.command
def create_database():
    """Create database."""
    logging.info("Creating database")
    engine = create_engine("postgresql://postgres:postgres@db/postgres")
    conn = engine.connect()
    conn.execute("commit")

    try:
        conn.execute("create database {}".format(DATABASE_NAME))
        logging.info("Created database")
    except ProgrammingError:
        logging.info("Database already existed, continuing")
    finally:
        conn.close()


@manager.command
def create_admin():
    logging.info("creating admin")
    user = User("Charles", "Thomas", "charlie.thomas@attwoodthomas.net", "Password")
    db.session.add(user)
    db.session.commit()


@manager.command
def run():
    """Run the app."""
    create_database()
    migrate()
    upgrade()
    app.run(host="0.0.0.0", port=80)

if __name__ == "__main__":
    manager.run()
