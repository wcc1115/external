from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler

from logger import simple_logged_method
from service import service

class  proxy():
	def __init__(self, url="localhost", port=18781):
		class RequestHandler(SimpleXMLRPCRequestHandler):
			rpc_paths = ('/RPC2');
		self.__server = SimpleXMLRPCServer((url, port), requestHandler = RequestHandler);

	@simple_logged_method
	def register_functions(self, service):
		self.__server.register_function(lambda x, y : x + y, 'add')
		self.__server.register_function(service.run_discover, 'discover')
		self.__server.register_function(service.run_filters, "runFilters")
		self.__server.register_function(service.run_cost_functions, "runCostFunctions")
		self.__server.register_function(service.run_load_balancing, "runLoadBalancing")
		return self

	@simple_logged_method
	def start(self):
		self.__server.serve_forever();

	def __repr__(self):
		return id(self)


if __name__ == "__main__":
	proxy().register_functions(service()).start()
