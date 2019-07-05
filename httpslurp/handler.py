import json
import os.path
import time
import uuid


def requestdump(request, dumpdir):
    '''dump a request to disk'''
    filename = os.path.join(dumpdir,
                            "%s-%s" % (time.time(), str(uuid.uuid4())))
    with open(filename, 'w') as logfile:
        logfile.write(json.dumps({"parsed": True, "args": request.args,
                                  "url": request.url,
                                  "query_string": request.query_string}))
    return filename
