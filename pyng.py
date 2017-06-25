import platform
import os
import argparse

def ping(host):
	
	"""Returns true if the host responds to a ping request"""
	
	paramaters = "-n 1" if platform.system().lower()=="windows" else "-c 1"
	
	return os.system("ping " + paramaters + " " + host)
	
def main():
	descStr = """ Ping a store and tell if its up with given arguements
	
	C: Device your'e wanting to ping (Rest, Ret, SCCB, SWCB01, SWCB02, SWCB03)

	S: three digit store number
	
	Ex. python pyng.py --C Rest --S 395
	
	"""
	parser = argparse.ArgumentParser(description=descStr)

	parser.add_argument("--C", type = str, dest="comp", required = True, help="Enter in the computer youre wanting to check as online")
	parser.add_argument("--S", type = str, dest="store", required = True, help="Enter in the three digit store number")
	
	args = parser.parse_args()
	
	if args.comp == "Rest":
		host = "rscb0"+args.store+".crackerbarrel.com"
	
	elif args.comp == "Ret":
		host = "rtcb0"+args.store+".crackerbarrel.com"
		
	elif args.comp == "SCCB":
		host = "sccb0"+args.store+".crackerbarrel.com"
		
	elif args.comp == "SWCB01":
		host = "swcb010"+args.store+".crackerbarrel.com"
		
	elif args.comp == "SWCB03":
		host = "swcb030"+args.store+".crackerbarrel.com"
		
	elif args.comp == "SWCB02":
		host = "swcb020"+args.store+".crackerbarrel.com"
	
	if ping(host):
		print "Device: "+args.comp+" at store: "+args.store+" is currently pinging"
	
	else:
		print "Unable to connect to Device: "+args.comp+" as store: "+args.store
		
if __name__ == "__main__":
	main()