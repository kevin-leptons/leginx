from pytest import fixture
from subprocess import Popen
from time import sleep

from lib.invoker import Invoker


@fixture(scope='module')
def leginx_server(request):
    port = 8080
    p = Popen(['leginx', 'start'])
    sleep(1)

    def free():
        p.terminate()

    request.addfinalizer(free)

    return Invoker('http://localhost:%i' % port)
