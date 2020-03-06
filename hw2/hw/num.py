import requests

API_URL = 'http://127.0.0.1:5000' #need to change for assignement

item_name = 'test-item' #item to get to the server
endpoint = '{}/{}'.format(API_URL, item_name)

if __name__ == '__main__':
    response = requests.get(endpoint)  #get data from server
    if not response.ok:                #when you first run it there is no item 
        print('item does not exist')   #cause todos in server is empty so 404 is gonna return

    response = requests.put(endpoint, data={'content': 'Design 2nd Assignment'}) #item to put into todo send server
    if response.ok:
        print('item created')

    response = requests.get(endpoint)  #get data from server
    if response.ok:
        content = response.json()
        print('item content: {}'.format(content))
