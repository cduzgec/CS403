import requests

API_URL = 'http://10.36.54.157:5000' #need to change for assignement


guess = 2**63-1 #item to get to the server
numpoint = '{}/{}/{}'.format(API_URL, 'number_game', guess)
bigger = 2**64-1
smaller = 0

if __name__ == '__main__':

	while True:
	
		response = requests.get(numpoint)
		print(response)
		serverguess = response.json()
        
		if serverguess == "greater":
			smaller= guess
			guess=(bigger-smaller)/2
			print("greater")
		   
			numpoint = '{}/{}/{}'.format(API_URL, 'number_game', guess)
       
		if serverguess == "smaller":
			bigger = guess
			guess = (bigger-smaller)/2
			print("smaller")
        
			numpoint = '{}/{}/{}'.format(API_URL, 'number_game', guess)
		
		if serverguess == "success":
			print(response,"found it", guess)
			break
		    
