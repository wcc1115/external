class noop_balance():
	__default_name = "noop_balance_instance"
	__default_description = "Return what it recives as hosts and the first of hosts as vm"
	def __init__(self, name=__default_name, description=__default_description):
		self.name = name
		self.description = description

	def __call__(self, units):
		print self.__str__()
		for u in units:
			try:
				print "host: %s: %s"%(u.get_name(), u.get_description())
			except AttributeError:
				print "!!! AttributeError"
				pass
		return (units[0], units)

	def get_rpc_attributes(self):
		return [self.description, ""]

	def __str__(self):
		return "noop_balance: %s: %s"%(self.name, self.description)

	def __repr__(self):
		return u"noop_balance('%s', '%s')"%(self.name, self.description)

if __name__ == "__main__":
	import sys;
	sys.path.append("..")

	from ovirtapi import ovirtapi

	clusters = ovirtapi.get_connection().clusters.list()
	hosts = clusters

	ret = noop_balance("wcc", "the lord")(hosts)
	print ret.__repr__()
