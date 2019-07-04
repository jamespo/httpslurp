from httpslurp.config import Config
from sanic import Sanic
from sanic.response import json

app = Sanic()
cfg = Config()


@app.route("/")
async def test(request):
    return json({"hello": "world"})


def main():
    app.run(host="0.0.0.0", port=int(cfg.conf['base']['port']))
