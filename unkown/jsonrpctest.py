__author__ = 'sswy'
__author__ = 'sswy'
import functools
import jsonrpclib

HOST = 'localhost'
PORT = 8069
DB = 'odoo'
USER = 'admin'
PASS = '1'
url = 'http://%s:%d/jsonrpc/' % (HOST, PORT)
server = jsonrpclib.Server(url)

# 1.log in the given database
uid = server.call(service="common", method="login", args=[DB, USER, PASS])
print uid


# 2.helper function for invoking model methods
def invoke(model, method, *args):
    args = [DB, uid, PASS, model, method] + list(args)
    print args
    return server.call(service="object", method="execute", args=args)


# 3.create a new note
args = {
    'color': 8,
    'memo': 'This is another note',
    'create_uid': uid,
}
note_id = invoke('note.note', 'create', args)
print note_id
