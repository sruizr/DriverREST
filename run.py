import falcon
import ujson


class DeviceCollection:
    devices = {}

    def on_get(self, req, resp):
        resp.body = ujosn'{"prueba": "Resultado" }'

    def on_post(self, req, resp):
        pass


class DeviceResource:

    def on_post(self, req, resp, key):
        pass

    def on_get(self, req, resp, key):
        pass

    def on_put(self, req, resp, key):
        pass


app = falcon.API()
devices = DeviceCollection()
device = DeviceResource()

app.add_route('/devices', devices)
app.add_route('/devices/{key}', device)
