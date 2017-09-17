import waitress
from os import environ
from clink import App, AppConf, MongoConf, AuthConf, ctl as clink_ctl
from leginx import ctl as leginx_ctl


class ServerConf():
    def __init__(
        self, app_name, license, version, owner, owner_addr,
        dburl, dbname,
        root_pwd, root_email, root_email_pwd, root_email_server,
        root_email_server_port, jwt_key, port=8080, addr='0',
    ):
        '''
        :param str app_name:
        :param str license:
        :param str version:
        :param str owner:
        :param str owner_addr:
        :param str dburl: mongodb url
        :param str dbname: name of database
        :param str root_pwd:
        :param str root_email:
        :param str root_email_pwd:
        :param str root_email_server:
        :param int root_email_server_port:
        :param str jwt_key:
        :param int port:
        :param str addr:
        '''

        self.app_name = app_name
        self.license = license
        self.version = version
        self.owner = owner
        self.owner_addr = owner_addr
        self.dburl = dburl
        self.dbname = dbname
        self.root_pwd = root_pwd
        self.root_email = root_email
        self.root_email_pwd = root_email_pwd
        self.root_email_server = root_email_server
        self.root_email_server_port = root_email_server_port
        self.jwt_key = jwt_key
        self.port = port
        self.addr = addr


class Server():
    def __init__(self, conf):
        '''
        :param ServerConf conf:
        '''

        self._wsgi_app = None
        self._conf = conf

    def start(self):
        '''
        Bring application on network
        '''

        print('Starting...')
        app = self.wsgi_app()
        print('Load components: Done')
        print('Bring application to network...')
        waitress.serve(
            self.wsgi_app(), host=self._conf.addr, port=self._conf.port
        )

    def wsgi_app(self):
        if self._wsgi_app is None:
            self._wsgi_app = self._mk_app()
        return self._wsgi_app

    def _mk_app(self):
        '''
        Create clink application
        '''

        app_conf = AppConf(
            self._conf.app_name, self._conf.license, self._conf.version,
            self._conf.owner, self._conf.owner_addr
        )
        mongo_conf = MongoConf(self._conf.dburl, self._conf.dbname)
        auth_conf = AuthConf(
            self._conf.root_pwd, self._conf.root_email,
            self._conf.root_email_pwd, self._conf.root_email_server,
            self._conf.root_email_server_port, self._conf.jwt_key
        )

        app = App(app_conf)
        app.add_prim(mongo_conf, auth_conf)
        app.add_ctls(clink_ctl)
        app.add_ctls(leginx_ctl)
        app.load()

        return app

