from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler

def make_simple_rpc_result(result):
	# new response format
	# {
	# 	"result_code": int,
	# 	"result": [list of UUIDS],
	# 	"plugin_errors": { "plugin_name": ["errormsgs"] },
	# 	"errors": ["errormsgs"]
	# }

	ret = { "result_code":0, "result":result, "plugin_errors": {}, "errors":[] };
	return ret;


single_uuid = "00000000-0000-0000-0000-000000000000";
three_uuids = ["00000000-0000-0000-0000-000000000001",
	"00000000-0000-0000-0000-000000000002",
	"00000000-0000-0000-0000-000000000003"];

def try_print_hids_and_properties(hids, properties):
	print "host guids:";
	try:
		for hid in hids:
			print hid;
	except:
		print "hids exception";
		pass;

	print "properties:";
	try:
		for (key, value) in properties:
			print "%s: %s"%(key, value);
	except:
		print "properties exception"
		pass;

def try_print(x):
	try:
		print x;
	except:
		print "try_print() exception";
		pass;

def run_filters(flnames, hids, vid, properties):
	return make_simple_rpc_result(three_uuids);

def run_cost_functions(scorename_and_weight, hids, vid, properties):
	print_run_cost_functions_params(scorename_and_weight, hids, vid, properties);
	guid_score_pairs = [(x, 119) for x in three_uuids];
	return make_simple_rpc_result(guid_score_pairs);

def run_load_balancing(blcname, hids, properties):
	print_run_load_balancing_params(blcname, hids, properties);
	return make_simple_rpc_result((single_uuid, three_uuids));

def print_run_cost_functions_params(scorename_and_weight, hids, vid, properties):
	print "cost functions and their weights:"
	try:
		for (score, weight) in scorename_and_weight:
			print "%s: %d"%(score, weight);
	except:
		pass;

	print "vid: ",
	try_print(vid);
	try_print_hids_and_properties(hids, properties);

def print_run_load_balancing_params(name, hids, properties):
	print "balancing name: ",
	try_print(name);
	try_print_hids_and_properties(hids, properties);

filters = {"f1":["df1", "rf1=1"], "f2":["df2", "rf2=2"], "f3":["df3", "rf3=3"]};
scores = {"s1":["ds1", "rs1=1"], "s2":["ds2", "rs2=2"], "s3":["ds3", "rs3=3"]};
balances = {"b1":["db1", "rb1=1"], "b2":["db3", "rb2=2"], "b3":["db3", "rb3=3"]};
discover_result = {"filters":filters, "scores":scores, "balance":balances};

class RequestHandler(SimpleXMLRPCRequestHandler):
	rpc_paths = ('/RPC2');

server = SimpleXMLRPCServer(("localhost", 18781), requestHandler = RequestHandler);
server.register_function(lambda x, y : x + y, 'add');
server.register_function(lambda : discover_result, 'discover'); 
server.register_function(run_filters, "runFilters");
server.register_function(run_cost_functions, "runCostFunctions");
server.register_function(run_load_balancing, "runLoadBalancing");

print "about to serve_forever()"
server.serve_forever();
