import os
from flask import Flask, render_template, request, session, redirect
from flask_cors import CORS
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect, generate_csrf
from flask_login import LoginManager
from .models import db, User
from .api.user_routes import user_routes
from .api.auth_routes import auth_routes
from .api.character_routes import character_routes
from .api.char_class_routes import char_class_routes
from .api.background_routes import background_routes
from .api.feat_routes import feat_routes
from .api.race_routes import race_routes
from .api.item_routes import item_routes
from .api.class_feat_routes import class_feat_routes
from .api.race_trait_routes import race_traits_routes
from .api.skill_routes import skill_routes
from .api.spell_routes import spell_routes
from .api.subclass_feat_routes import subclass_feat_routes
from .api.subclass_routes import subclass_routes
from .api.subrace_routes import subrace_routes
from .api.subrace_trait_routes import subrace_trait_routes
from .seeds import seed_commands
from .config import Config

app = Flask(__name__, static_folder='../react-vite/dist', static_url_path='/')

if os.environ.get('FLASK_ENV') == 'production':
    app.config.update(
        SESSION_COOKIE_SAMESITE='None',
        SESSION_COOKIE_SECURE=True,
    )
else:
    # Dev environment settings: less strict so cookies work on localhost HTTP
    app.config.update(
        SESSION_COOKIE_SAMESITE='Lax',
        SESSION_COOKIE_SECURE=False,
    )

# Setup login manager
login = LoginManager(app)
login.login_view = 'auth.unauthorized'


@login.user_loader
def load_user(id):
    return User.query.get(int(id))


# Tell flask about our seed commands
app.cli.add_command(seed_commands)

app.config.from_object(Config)
app.register_blueprint(user_routes, url_prefix='/api/users')
app.register_blueprint(auth_routes, url_prefix='/api/auth')
app.register_blueprint(character_routes, url_prefix='/api/characters')
app.register_blueprint(race_routes, url_prefix='/api/races')
app.register_blueprint(char_class_routes, url_prefix='/api/classes')
app.register_blueprint(background_routes, url_prefix='/api/backgrounds')
app.register_blueprint(feat_routes, url_prefix='/api/feats')
app.register_blueprint(item_routes, url_prefix='/api/items')
app.register_blueprint(class_feat_routes, url_prefix='/api/class_feats')
app.register_blueprint(race_traits_routes, url_prefix='/api/race_traits')
app.register_blueprint(skill_routes, url_prefix='/api/skills')
app.register_blueprint(spell_routes, url_prefix='/api/spells')
app.register_blueprint(subclass_feat_routes, url_prefix='/api/subclass_feats')
app.register_blueprint(subclass_routes, url_prefix='/api/subclasses')
app.register_blueprint(subrace_routes, url_prefix='/api/subraces')
app.register_blueprint(subrace_trait_routes, url_prefix='/api/subrace_traits')
db.init_app(app)
Migrate(app, db)

# Application Security
CORS(app, resources={r"/api/*": {"origins": "http://localhost:5173"}}, supports_credentials=True)

# HTTPS redirect for production
@app.before_request
def https_redirect():
    if os.environ.get('FLASK_ENV') == 'production':
        if request.headers.get('X-Forwarded-Proto') == 'http':
            url = request.url.replace('http://', 'https://', 1)
            code = 301
            return redirect(url, code=code)

# CSRF token injection
@app.after_request
def inject_csrf_token(response):
    response.set_cookie(
        'csrf_token',
        generate_csrf(),
        secure=True if os.environ.get('FLASK_ENV') == 'production' else False,
        samesite='Strict' if os.environ.get('FLASK_ENV') == 'production' else 'Lax',
        httponly=False)  # Changed to False so JavaScript can access it
    return response

# CSRF token endpoint
@app.route("/api/csrf/restore", methods=["GET"])
def restore_csrf():
    return {"csrf_token": generate_csrf()}


@app.route("/api/docs")
def api_help():
    """
    Returns all API routes and their doc strings
    """
    acceptable_methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
    route_list = { rule.rule: [[ method for method in rule.methods if method in acceptable_methods ],
                    app.view_functions[rule.endpoint].__doc__ ]
                    for rule in app.url_map.iter_rules() if rule.endpoint != 'static' }
    return route_list


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def react_root(path):
    """
    This route will direct to the public directory in our
    react builds in the production environment for favicon
    or index.html requests
    """
    if path == 'favicon.ico':
        return app.send_from_directory('public', 'favicon.ico')
    return app.send_static_file('index.html')


@app.errorhandler(404)
def not_found(e):
    return app.send_static_file('index.html')
