from httpslurp.config import Config
from httpslurp.handler import requestdump
from sanic import Sanic
from sanic.log import logger
from sanic.response import json

app = Sanic()
cfg = Config()


@app.route("/")
async def test(request):
    dumpfile = requestdump(request, cfg.conf['base']['dumpdir'])
    logger.info("Dumped %s" % dumpfile)
    return json({"status": "ok"})


def main():
    app.run(host="0.0.0.0", port=int(cfg.conf['base']['port']))
