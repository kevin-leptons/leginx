import waitress
from os import environ
from clink import App, AppConf, MongoConf, AuthConf, ctl as clink_ctl
from clink import Version
from leginx import ctl as leginx_ctl

class ServerConf():
    def __init__(
        self, dburl, dbname, 
        root_pwd, root_email, root_email_pwd, root_email_server,
        jwt_key, port=8080, addr='0',
    ):
        '''
        :param str dburl: mongodb url
        :param str dbname: name of database
        :param str root_pwd:
        :param str root_email:
        :param str root_email_pwd:
        :param str root_email_server:
        :param str jwt_key:
        :param int port:
        :param str addr:
        '''

        self.dburl = dburl
        self.dbname = dbname
        self.root_pwd = root_pwd
        self.root_email = root_email
        self.root_email_pwd = root_email_pwd
        self.root_email_server = root_email_server
        self.jwt_key = jwt_key
        self.port = port
        self.addr = addr


class Server():
    def __init__(self, conf=None):
        '''
        If conf is None, server scan system environment variables for
        configuration

            LEGINX_DBURL
            LEGINX_DBNAME
            LEGINX_ROOT_PWD
            LEGINX_ROOT_EMAIL
            LEGINX_ROOT_EMAIL_PWD
            LEGINX_ROOT_EMAIL_SERVER
            LEGINX_JWT_KEY
            LEGINX_PORT: optional
            LEGINX_ADDR: optional

        :param ServerConf conf:
        '''

        if conf is None:
            self._conf = self._env_conf()
        else:
            self._conf = conf

    def start(self):
        '''
        Bring application on network
        '''

        waitress.serve(
            self.new_app(), host=self._conf.addr, port=self._conf.port
        )

    def new_app(self):
        '''
        Create clink application
        '''

        app_conf = AppConf(
            'leginx', 'MIT License', Version(0, 1, 0), 
            'leginx org', 'Ha Noi, Viet Nam'
        )
        mongo_conf = MongoConf(self._conf.dburl, self._conf.dbname)
        auth_conf = AuthConf(
            self._conf.root_pwd, self._conf.root_email,
            self._conf.root_email_pwd, self._conf.root_email_server,
            self._conf.jwt_key
        )

        app = App(app_conf)
        app.add_prim(mongo_conf, auth_conf)
        app.add_ctls(clink_ctl)
        app.add_ctls(leginx_ctl)
        app.load()
        print('whattttttttttttttttttttttttttttttttttttt')

        return app

    def _env_conf(self):
        '''
        Scan system environment variables
        '''

        try:
            conf = ServerConf(
                environ['LEGINX_DBURL'],
                environ['LEGINX_DBNAME'],
                environ['LEGINX_ROOT_PWD'],
                environ['LEGINX_ROOT_EMAIL'],
                environ['LEGINX_ROOT_EMAIL_PWD'],
                environ['LEGINX_ROOT_EMAIL_SERVER'],
                environ['LEGINX_JWT_KEY']
            )
            if 'LEGINX_PORT' in environ:
                conf.port = environ['LEGINX_PORT']
            if 'LEGINX_ADDR' in environ:
                conf.addr = environ['LEGINX_ADDR']
            return conf
        except KeyError as e:
            raise RuntimeError('Missing environment variable %s' % e)
