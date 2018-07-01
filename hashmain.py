from hashlib import sha256
from time import sleep

def main():
	targetString = "af6e56aacd8097c3fb7597b08ecb3d87a040f6ab58067a4b8ff9f5b747adb9be"
	
	with open("German_de_DE.dic", "r") as fh:
		content = fh.readlines()
		
	
	for element in content:
					
		if sha256(element.strip().split("/")[0]).hexdigest() == targetString:
			print "Uebereinstimmung gefunden bei dem Wort"
			print element 
			
		


if __name__ == "__main__":
	main()