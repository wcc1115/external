class noop_filter():
	__default_name = "noop_filter_instance"
	__default_description = "Return what it recives"
	def __init__(self, name=__default_name, description=__default_description):
		self.name = name
		self.description = description

	def __call__(self, units, unit):
		print "%s:"%self.__str__()
		for u in units:
			try:
				print "host: %s: %s"%(u.get_name(), u.get_description())
			except AttributeError:
				print "!!! AttributeError"
				pass
		print "vm: %s: %s"%(unit.get_name(), unit.get_description())
		return units

	def get_rpc_attributes(self):
		return [self.description, ""]

	def __str__(self):
		return "noop_filter: %s: %s"%(self.name, self.description)

	def __repr__(self):
		return u"noop_filter('%s', '%s')"%(self.name, self.description)

if __name__ == "__main__":
	class unit:
		def __init__(self, name, description):
			self.name = name
			self.description = description
		def get_name(self):
			return self.name
		def get_description(self):
			return self.description
	units = [unit(name, dsc) for (name, dsc) in zip(["unit1", "unit2", "unit3"], ["dsc1", "dsc2", "dsc3"])];
	unt = unit("vm", "vmdsc")
	noop_filter()(units, unt);
	print noop_filter("wcc", "wccccccc");
