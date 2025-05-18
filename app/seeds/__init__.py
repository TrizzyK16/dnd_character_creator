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
        undo_subclass_feats()
        undo_subclasses()
        undo_races()
        undo_class_feats()
        undo_char_classes()
        undo_backgrounds()
        undo_characters()
        undo_users()

    # Seed in the correct order
    seed_users()
    seed_characters()
    seed_backgrounds()
    seed_char_classes()
    seed_class_feat()
    seed_races()
    seed_subclasses()         # Seed subclasses first
    seed_subclass_feats()    # Then subclass_feats, which depend on them



# Creates the `flask seed undo` command
@seed_commands.command('undo')
def undo():
    undo_subclass_feats()
    undo_subclasses()
    undo_races()
    undo_class_feats()
    undo_char_classes()
    undo_backgrounds()
    undo_characters()
    undo_users()
