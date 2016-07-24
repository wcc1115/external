class noop_score():
	__default_name = "noop_score_instance"
	__default_description = "Mark every host with score 47"
	def __init__(self, name=__default_name, description=__default_description):
		self.name = name
		self.description = description

	def __call__(self, units, unit):
		print self.__str__()
		for u in units:
			try:
				print "host: %s: %s"%(u.get_name(), u.get_description())
			except AttributeError:
				print "!!! AttributeError"
				pass
		print "vm: %s: %s"%(unit.get_name(), unit.get_description())
		return [(unit, 47) for unit in units]

	def get_rpc_attributes(self):
		return [self.description, ""]

	def __str__(self):
		return "noop_score: %s: %s"%(self.name, self.description)

	def __repr__(self):
		return u"noop_score('%s', '%s')"%(self.name, self.description)

if __name__ == "__main__":
	import sys;
	sys.path.append("..")

	from ovirtapi import ovirtapi

	clusters = ovirtapi.get_connection().clusters.list()
	vm, hosts = clusters[0], clusters[1:]

	ret = noop_score("wcc", "the lord")(hosts, vm)
	print ret.__repr__()
