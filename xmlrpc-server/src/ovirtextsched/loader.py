def load_filters():
	from filters import noop

	filters = {}
	filters["noop1"] = noop.noop_filter("noop1", "description of noop1")
	filters["noop2"] = noop.noop_filter("noop2", "description of noop2")
	filters["noop3"] = noop.noop_filter("noop3", "description of noop3")

	info = {}
	for key in filters:
		info[key] = filters[key].get_rpc_attributes()

	return filters, info

def load_scores():
	from scores import noop

	scores = {}
	scores["noop4"] = noop.noop_score("noop4", "description of noop4")
	scores["noop5"] = noop.noop_score("noop5", "description of noop5")
	scores["noop6"] = noop.noop_score("noop6", "description of noop6")

	info = {}
	for key in scores:
		info[key] = scores[key].get_rpc_attributes()

	#info = {"s1":["ds1", "rs1=1"], "s2":["ds2", "rs2=2"], "s3":["ds3", "rs3=3"]};

	return scores, info;

def load_balances():
	from balances import noop

	balances = {};
	balances["noop7"] = noop.noop_balance("noop7", "description of noop7")
	balances["noop8"] = noop.noop_balance("noop8", "description of noop8")
	balances["noop9"] = noop.noop_balance("noop9", "description of noop9")

	info = {}
	for key in balances:
		info[key] = balances[key].get_rpc_attributes()
	
	##info = {"b1":["db1", "rb1=1"], "b2":["db3", "rb2=2"], "b3":["db3", "rb3=3"]};

	return balances, info;

if __name__ == "__main__":
	filters, info = load_filters()
	print filters
	print filters["noop1"];
	print filters["noop1"].get_rpc_attributes()
	print info

	scores, info = load_scores()
	print info

	balances, info = load_balances()
	print info
	
