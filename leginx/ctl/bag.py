from clink import stamp, mapper, Controller


@stamp()
@mapper.path('bag')
class BagCtl(Controller):
    @mapper.get('item')
    def get_items(self, req, res):
        res.body = []
