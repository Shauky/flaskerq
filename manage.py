#!usr/bin/env python

# export FLASK_APP=app/app declared through line 8
# export FLASK_ENV=development declared in config and
import os
from app import create_app

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
print(app)

if __name__ == '__main__':
    app.run()
