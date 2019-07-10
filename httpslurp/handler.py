import aiohttp
import json
import os.path
import time
import uuid


def requestdump(request, dumpdir):
    '''dump a request to disk'''
    reqtime = str(time.time())
    filename = os.path.join(dumpdir,
                            "%s-%s" % (reqtime, str(uuid.uuid4())))
    with open(filename, 'w') as logfile:
        dumpdict = {"time": reqtime,
                    "args": request.args,
                    "headers": dict(request.headers),
                    "url": request.url,
                    "query_string": request.query_string}
        if request.cookies != {}:
            # add cookies if there are any
            dumpdict["cookies"] = request.cookies
        logfile.write(json.dumps(dumpdict))
    return filename, dumpdict


async def proxy(request, backend):
    '''proxy request back'''
    proxy_url = backend + request.path
    if request.query_string != '':
        proxy_url += '?' + request.query_string
    async with aiohttp.ClientSession() as session:
        async with session.get(proxy_url) as r:
            response = await r.text()
            return response
