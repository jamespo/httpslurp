from httpslurp.config import Config
from httpslurp.handler import requestdump, proxy
from sanic import Sanic
from sanic.log import logger
from sanic.response import json, text

app = Sanic()
cfg = Config()

# retrieve reqs over /httpslurp URL
app.static('/httpslurp', cfg.conf['base']['dumpdir'])


@app.route("/")
@app.route('/<path:path>')
async def catch_all(request, path=''):
    '''catch-all hander to dump requests'''
    dumpfile, dumpdict = requestdump(request, cfg.conf['base']['dumpdir'])
    logger.info("Dumped %s" % dumpfile)
    # proxy if backend set up
    if cfg.conf.has_section('proxy'):
        proxy_response = await proxy(request, cfg.conf['proxy']['backend'])
        return text(proxy_response)
    else:
        return json(dumpdict)


def main():
    app.run(host="0.0.0.0", port=int(cfg.conf['base']['port']))
