from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler

uuids = ["00000000-0000-0000-0000-000000000001",
	"00000000-0000-0000-0000-000000000002",
	"00000000-0000-0000-0000-000000000003"];

def runFilters(flnames, hids, vid, properties):
	# new response format
	# {
	# 	"result_code": int,
	# 	"result": [list of UUIDS],
	# 	"plugin_errors": { "plugin_name": ["errormsgs"] },
	# 	"errors": ["errormsgs"]
	# }
	ret = { "result_code":0,
		"result":uuids,
		"plugin_errors": {},
		"errors":[] };
	return ret;

def create_filter(filter_name):
	def filter_ret(p):
		return ["%s-%s"%(filter_name, x) for x in ["01", "02", "03"]];
	return filter_ret;

filters = {"f1":["df1", "rf1=1"], "f2":["df2", "rf2=2"], "f3":["df3", "rf3=3"]};
scores = {"s1":["ds1", "rs1=1"], "s2":["ds2", "rs2=2"], "s3":["ds3", "rs3=3"]};
balances = {"b1":["db1", "rb1=1"], "b2":["db3", "rb2=2"], "b3":["db3", "rb3=3"]};
discover_result = {"filters":filters, "scores":scores, "balance":balances};

class RequestHandler(SimpleXMLRPCRequestHandler):
	rpc_paths = ('/RPC2');

server = SimpleXMLRPCServer(("127.0.0.1", 8000), requestHandler = RequestHandler);

server.register_function(lambda x, y : x + y, 'add');
server.register_function(lambda : discover_result, 'discover'); 

#register filters
server.register_function(runFilters, "runFilters");

print "about to serve_forever()"
server.serve_forever();
