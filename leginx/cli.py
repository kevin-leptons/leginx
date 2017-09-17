import click
import yaml

from leginx import Server, ServerConf


def _read_conf(conf_file):
    '''
    Read configuration file in YAML format.
    '''

    try:
        f = open(conf_file)
        raw_conf = yaml.load(f.read())
        f.close()
        conf = ServerConf(
            raw_conf['app_name'],
            raw_conf['license'],
            raw_conf['version'],
            raw_conf['owner'],
            raw_conf['owner_addr'],
            raw_conf['dburl'],
            raw_conf['dbname'],
            raw_conf['root_pwd'],
            raw_conf['root_email'],
            raw_conf['root_email_pwd'],
            raw_conf['root_email_server'],
            int(raw_conf['root_email_server_port']),
            raw_conf['jwt_key']
        )
        if 'port' in raw_conf:
            conf.port = int(raw_conf['port'])
        if 'addr' in raw_conf:
            conf.addr = raw_conf['addr']
        return conf
    except KeyError as e:
        raise RuntimeError('Missing configuration: %s' % e)

@click.group()
@click.version_option(version='0.1.0')
def cli():
    pass


@cli.command(help='Start service')
@click.argument('conf_file')
def start(conf_file):
    conf = _read_conf(conf_file)
    print('Reading configuration: Done')
    server = Server(conf)
    server.start()
