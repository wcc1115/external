from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler

filters = {"f1":["df1", "rf1=1"], "f2":["df2", "rf2=2"], "f3":["df3", "rf3=3"]};
scores = {"s1":["ds1", "rs1=1"], "s2":["ds2", "rs2=2"], "s3":["ds3", "rs3=3"]};
balances = {"b1":["db1", "rb1=1"], "b2":["db3", "rb2=2"], "b3":["db3", "rb3=3"]};
discover_result = {"filters":filters, "scores":scores, "balance":balances};

class RequestHandler(SimpleXMLRPCRequestHandler):
	rpc_paths = ('/RPC2');

server = SimpleXMLRPCServer(("127.0.0.1", 8000), requestHandler = RequestHandler);

server.register_function(lambda x, y : x + y, 'add');
server.register_function(lambda : discover_result, 'discover'); 

print "about to serve_forever()"
server.serve_forever();
