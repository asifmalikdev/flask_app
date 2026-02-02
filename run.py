
from .app import create_app
from flask_sqlalchemy import SQLAlchemy
from .app.extentions import db
from .app.models import User
from flask_migrate import Migrate

app = create_app()
migrate = Migrate(app, db)

if __name__ == '__main__':
    app.run(debug=True)