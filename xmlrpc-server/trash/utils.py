class RpcUtils:
	@classmethod
	def make_simple_message(cls, result):
		# new response format
		# {
		# 	"result_code": int,
		# 	"result": [list of UUIDS],
		# 	"plugin_errors": { "plugin_name": ["errormsgs"] },
		# 	"errors": ["errormsgs"]
		# }

		ret = { "result_code":0, "result":result, "plugin_errors": {}, "errors":[] };
		return ret;

class PrintUtils:
	@classmethod
	def print_run_cost_functions_params(cls, scorename_and_weight, hids, vid, properties):
		print "cost functions and their weights:"
		try:
			for (score, weight) in scorename_and_weight:
				print "%s: %d"%(score, weight);
		except:
			pass;

		print "vid: ",
		cls.__try_print(vid);
		cls.__try_print_hids_and_properties(hids, properties);

	@classmethod
	def print_run_load_balancing_params(cls, name, hids, properties):
		print "balancing name: ",
		cls.__try_print(name);
		cls.__try_print_hids_and_properties(hids, properties);

	@classmethod
	def __try_print_hids_and_properties(cls, hids, properties):
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

	@classmethod
	def __try_print(cls, x):
		try:
			print x;
		except:
			print "__try_print() exception";
			pass;
