def simple_logged_method(method, param = True, retval = True):
	def wrapped(ins, *args, **kwargs):
		print "\nINVOKE: %s"%method.func_name + ": %s, %s"%(args.__repr__(), kwargs.__repr__()) if param else ""
		ret = method(ins, *args, **kwargs);
		print "RETURN: %s"%method.func_name + ": %s\n"%ret.__repr__() if retval else "\n"
		return ret

	return wrapped

