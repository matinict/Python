
def trafficLightSignal():
	trafficLight = input("Please Input Traffic Light- red, green, yellow: ")
	if trafficLight=="red":
		print(trafficLight.upper()+" Light - The Signal To STOP ")
	elif trafficLight=="green":
		print(trafficLight.upper()+" Light - The Signal To Go-Ahead /Proceed ")
	elif trafficLight=="yellow":
		print(trafficLight.upper()+" Light - The Signal To Proceed With Caution")
	else:
		print("Sorry!! Wrong Signal Input ")

		
## >>> trafficLightSignal()
## Please Input Traffic Light- red, green, yellow: green
## GREEN Light - The Signal To Go-Ahead /Proceed 
## >>> 
