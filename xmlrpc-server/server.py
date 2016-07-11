from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler

filters = {"f1":"None", "f2":"None", "f3":"None"};
scores = {"s1":"None", "s2":"None", "s3":"None"};
balances = {"b1":"None", "b2":"None", "b3":"None"};
discover_result = {"filters":filters, "scores":scores, "balance":balances};

class RequestHandler(SimpleXMLRPCRequestHandler):
	rpc_paths = ('/RPC2');

server = SimpleXMLRPCServer(("127.0.0.1", 8000), requestHandler = RequestHandler);

server.register_function(lambda x, y : x + y, 'add');
server.register_function(lambda : discover_result, 'discover'); 

print "about to serve_forever()"
server.serve_forever();
