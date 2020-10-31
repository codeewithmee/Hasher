import hashlib
import pyfiglet
import sys

hash_list = ['sha384', 'sha512', 'sha256', 'sha1', 'blake2b', 'sha224', 'sha3_256', 'md5', 'sha3_384', 'sha3_224', 'sha3_512', 'blake2s','exit']

class Hasher(object):
	"""docstring for Hasher"""
	def __init__(self):
		self.Banner("Hasher")
		self.Hash_List()


	def Banner(self,name):
		banner = pyfiglet.figlet_format(name, font = "bulbhead" )
		print(banner)

	def Hash_List(self):
		global hash_list
		for i in range(len(hash_list)):
			print(f'{i}. {hash_list[i]}')
	
		print("---------------------------")

	def get_input_string(self,en):
		a = str(input(f"Enter the string to {en} : "))
		return a

	def get_hash_select(self):
		a = int(input("Enter the hash number : "))
		return a

	def exit(self):
		self.Banner("Bye")
		sys.exit()
		

	def hash_checker(self,hash_name):
		if hash_name == "sha384":
			return hashlib.sha384(), hash_name

		elif hash_name == "sha512":
			return hashlib.sha512(), hash_name

		elif hash_name == "sha256":
			return hashlib.sha256(), hash_name

		elif hash_name == "sha1":
			return hashlib.sha1(), hash_name

		elif hash_name == "blake2b":
			return hashlib.blake2b(), hash_name

		elif hash_name == "sha224":
			return hashlib.sha224(), hash_name

		elif hash_name == "sha3_256":
			return hashlib.sha3_256(), hash_name

		elif hash_name == "md5":
			return hashlib.md5(), hash_name

		elif hash_name == "sha3_384":
			return hashlib.sha3_384(), hash_name

		elif hash_name == "sha3_224":
			return hashlib.sha3_224(), hash_name

		elif hash_name == "sha3_512":
			return hashlib.sha3_512(), hash_name

		elif hash_name == "blake2s":
			return hashlib.blake2s(), hash_name

		elif hash_name == "exit":
			self.exit()

		else:
			print("Select the valid hash")
			self.exit()

	def hash_encoder(self,hash_obj,input_string,hash_name):
		hash_obj.update(input_string.encode())
		output = hash_obj.hexdigest()
		print(f"Your encoded {hash_name} hash is : {output}" )

	def hasher(self,hash_selected):
		hash_obj, hash_name = self.hash_checker(hash_selected)
		input_string = self.get_input_string("encode")
		self.hash_encoder(hash_obj,input_string,hash_name)

	def main(self):
		global hash_list
		hash_selected = self.get_hash_select()
		if hash_selected < len(hash_list):
			hash_selected = hash_list[hash_selected]
		else:
			print("---------- Enter the valid hash number ----------------")
			self.main()
		self.hasher(hash_selected)
		self.main()




a = Hasher()
a.main()
