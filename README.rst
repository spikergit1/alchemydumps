AlchemyDumps
------------

Do you use `Flask <http://flask.pocoo.org>`_ with `SQLAlchemy <http://www.sqlalchemy.org/>`_  and `Flask-Script <http://flask-script.readthedocs.org/en/latest/>`_ ? Wow, what a coincidence!

This package let you backup and restore all your data using `SQLALchemy dumps() method <http://docs.sqlalchemy.org/en/latest/core/serializer.html>`_.

It is an easy way (one singe command, I mean it) to save **all** the data stored in your database.

Examples
--------

Considering you have these *models* (`SQLAlchemy mapped classes <http://docs.sqlalchemy.org/en/latest/orm/mapper_config.html>`_):

::

    class User(Model):
        id = db.Column(db.Integer, primary_key=True)
        email = db.Column(db.String(140), index=True, unique=True)
        ...
    
    class Post(Model):
        id = db.Column(db.Integer, primary_key=True)
        title = db.Column(db.String(140))
        content = db.Column(db.UnicodeText)
        ...

You can **backup all your data**:

::

    $ python manage.py alchemydumps create

Output:

::

    ==> 3 rows from User post saved as /vagrant/alchemydumps/db-bkp-20141115172107-User.gz
    ==> 42 rows from Post saved as /vagrant/alchemydumps/db-bkp-20141115172107-Post.gz

You can **list the backups you have already created**:

::

    $ python manage.py alchemydumps history

Output:
	
::

    ==> ID: 20141114203949 (from Nov 15, 2014 at 17:21:07)
        /vagrant/alchemydumps/db-bkp-20141115172107-User.gz
        /vagrant/alchemydumps/db-bkp-20141115172107-Post.gz

    ==> ID: 20141115140629 (from Nov 15, 2014 at 14:06:29)
        /vagrant/alchemydumps/db-bkp-20141115140629-User.gz
        /vagrant/alchemydumps/db-bkp-20141115140629-Post.gz

And, surely, you can **restore backuped data**:

::

    $ python manage.py alchemydumps restore -d 20141115172107

Output:

::

    ==> /vagrant/alchemydumps/db-bkp-20141115172107-User.gz totally restored.
    ==> /vagrant/alchemydumps/db-bkp-20141115172107-Post.gz totally restored.

Install
-------

First install the package: `$ pip install Flask-AlchemyDumps`

Then configure it in your Flask application:

::

    from alchemydumps import AlchemyDumps, AlchemyDumpsCommand
    from flask import Flask
    from flask.ext.script import Manager
    from flask.ext.sqlalchemy import SQLAlchemy

    app = Flask(__name__)
    db = SQLAlchemy(app)
    manager = Manager(app)

    alchemydumps = AlchemyDumps(app, db)
    manager.add_command('alchemydumps', AlchemyDumpsCommand)

The first line import the methods from the package, the last two lines instantiate and add AlchemyDumps to the *Flask-Script manager*).

You might want to add `alchemydumps` to yout `.gitignore`. It is the folder where **AlchemyDumps** save the backup files.

Requirements
------------

As **AlchemyDumps** was designed to work together with `Flask <http://flask.pocoo.org>`_ applications that uses `SQLAlchemy <http://www.sqlalchemy.org/>`_. And it runs within the `Flask-Script <http://flask-script.readthedocs.org/en/latest/>`_ manager. Thus, be sure to have these packages installed and in use. **AlchemyDumps** also uses `Unipath <https://github.com/mikeorr/Unipath>`_ package.

In sum, if your `requirements.txt` looks something like this, probably you will be fine:

::

    Flask>=0.10.1
    Flask-Script>=2.0.5
    Flask-SQLAlchemy>=0.16
    SQLAlchemy>=0.7.9
    Unipath>=1.0

License
-------

Copyright (c) 2014 Eduardo Cuducos.

Licensed under the `MIT License <http://opensource.org/licenses/MIT>`_.