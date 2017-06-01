.. _dev:

Development
===========

Installation
------------

Mongodb server is not in standard package repository of Linux distros, 
install it by hand here 
https://docs.mongodb.com/manual/administration/install-on-linux/.

Then follow instructions:

.. code-block:: shell-session

    # essential tools
    $ apt-get install python3 git

    # clone source code
    $ git clone https://github.com/kevin-leptons/leginx
    $ cd leginx

    # enter virtual environment
    $ ./env init
    $ . venv/bin/active

    # install dependency packages
    $ ./env install

    # create configuration
    # best choice is put it into ~/.bashrc
    $ export LEGINX_DBURL='mongodb://localhost'
    $ export LEGINX_DBNAME='leginx'
    $ export LEGINX_ROOT_EMAIL='root-mail@gmail.com'
    $ export LEGINX_ROOT_EMAIL_PWD='root-mail-pwd'
    $ export LEGINX_ROOT_EMAIL_SERVER='smtp.gmail.com:587'
    $ export LEGINX_JWT_KEY='json-web-token-key'

    # optional configuration, if it does not provided
    # default values will be use as below
    $ export LEGINX_ADDR='0'
    $ export LEGINX_PORT=8080

Develop
-------

.. code-block:: shell-session

    # build document
    $ ./ctl doc

    # view document
    $ ./ctl doc --view

    # test
    $ ./ctl test

    # build and push pip package to pypi
    # it required authentication
    $ ./ctl release
