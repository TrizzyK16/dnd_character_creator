from flask.cli import AppGroup
from .users import seed_users, undo_users
from .characters import seed_characters, undo_characters
from .backgrounds import seed_backgrounds, undo_backgrounds
from .char_classes import seed_char_classes, undo_char_classes
from .class_feats import seed_class_feat, undo_class_feats
from .races import seed_races, undo_races
from .subclass_feats import seed_subclass_feats, undo_subclass_feats
from .subclasses import seed_subclasses, undo_subclasses

from app.models.db import db, environment, SCHEMA

# Creates a seed group to hold our commands
# So we can type `flask seed --help`
seed_commands = AppGroup('seed')


# Creates the `flask seed all` command
@seed_commands.command('all')
def seed():
    if environment == 'production':
        # Before seeding in production, you want to run the seed undo 
        # command, which will  truncate all tables prefixed with 
        # the schema name (see comment in users.py undo_users function).
        # Make sure to add all your other model's undo functions below
        undo_users()
        undo_characters()
    seed_users()
    seed_characters()
    seed_backgrounds()
    seed_char_classes()
    seed_class_feat()
    seed_races()
    seed_subclass_feats()
    seed_subclasses()
    # Add other seed functions here


# Creates the `flask seed undo` command
@seed_commands.command('undo')
def undo():
    undo_users()
    undo_characters()
    undo_backgrounds()
    undo_char_classes()
    undo_class_feats()
    undo_races()
    undo_subclass_feats()
    undo_subclasses()
    # Add other undo functions here
