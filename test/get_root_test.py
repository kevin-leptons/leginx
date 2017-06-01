from leginx.model import root


def test_get_root(leginx_server):
    res_schema = {
        'body': root.get_root
    }
    leginx_server.test_get('/', res_schema=res_schema)


def test_http404(leginx_server):
    leginx_server.test_get('/not/exist/path', res_status=404)
