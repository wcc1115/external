class ovirtapi:
	ovirt = None

	@classmethod
	def get_connection(cls):
		if cls.ovirt == None:
			cls.connect()
		return cls.ovirt

	@classmethod
	def connect(cls):
		from ovirtsdk.api import API
		cls.ovirt = API(url="127.0.0.1:8080/ovirt-engine/api/", username="admin@internal", password="qwe123")
		return None

if __name__ == "__main__":
	print "hello"
	print "init"
	ovirtapi.connect()
	print "first"
	ovirtapi.get_connection()
	print "sceond"
	ovirtapi.get_connection()
	print "third"
	ovirtapi.get_connection()
