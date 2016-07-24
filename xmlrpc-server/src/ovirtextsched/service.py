from logger import simple_logged_method
from ovirtapi import ovirtapi

import loader

class service():
	def __init__(self):
		self.__filters, self.__filters_info = {}, {}
		self.__scores, self.__scores_info = {}, {}
		self.__balances, self.__balances_info = {}, {}
		self.__load_policy_units();

	@simple_logged_method
	def run_discover(self):
		discover_result = { "filters":self.__filters_info,
				"scores":self.__scores_info,
				"balance":self.__balances_info };
		return discover_result

	@simple_logged_method
	def run_filters(self, filter_names, hids, vid, properties):
		hosts = [ovirtapi.get_connection().clusters.get(id = x) for x in hids];
		vm = ovirtapi.get_connection().clusters.get(id=vid);

		for filter_name in filter_names:
			hosts = self.__filters.get(filter_name)(hosts, vm)

		hids = [host.get_id() for host in hosts]
		return self.__make_simple_message(hids);

	@simple_logged_method
	def run_cost_functions(self, scorename_and_weight, hids, vid, properties):
		#PrintUtils.print_run_cost_functions_params(scorename_and_weight, hids, vid, properties);

		hosts = [ovirtapi.get_connection().clusters.get(id = x) for x in hids];
		vm = ovirtapi.get_connection().clusters.get(id = vid);

		guid_score_pairs = [(x, 119) for x in hids];
		return self.__make_simple_message(guid_score_pairs);

	@simple_logged_method
	def run_load_balancing(self, blcname, hids, properties):
		#PrintUtils.print_run_load_balancing_params(blcname, hids, properties);

		ovirt = ovirtapi.get_connection()
		hosts = [ovirt.clusters.get(id=x) for x in hids];

		return self.__make_simple_message((hids[0], hids));

	def __make_simple_message(self, result):
		# new response format
		# {
		# 	"result_code": int,
		# 	"result": [list of UUIDS],
		# 	"plugin_errors": { "plugin_name": ["errormsgs"] },
		# 	"errors": ["errormsgs"]
		# }

		ret = { "result_code":0, "result":result, "plugin_errors": {}, "errors":[] };
		return ret;


	def __load_policy_units(self):
		print "loading filters ..."
		self.__filters, self.__filters_info = loader.load_filters()
		print self.__filters_info

		print "loading scores ..."
		self.__scores, self.__scores_info = loader.load_scores()
		print self.__scores_info

		print "loading balances ..."
		self.__balances, self.__balances_info = loader.load_balances()
		print self.__balances_info

		return self

if __name__ == "__main__":
	cids = [cluster.get_id() for cluster in ovirtapi.get_connection().clusters.list()]
	vid, hids = cids[0], cids[1:]
	names = ["noop1", "noop2"]

	s = service()
	s.run_filters(names, hids, vid, None)
	s.run_cost_functions(names, hids, vid, None)
	s.run_load_balancing(names, hids, None)
	s.run_discover()
