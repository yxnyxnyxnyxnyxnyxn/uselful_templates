import requests
import json

#Api url 
api_get_url = "https://jsonplaceholder.typicode.com/todos/1"
api_post_url = "https://jsonplaceholder.typicode.com/todos"
api_put_url = "https://jsonplaceholder.typicode.com/todos/10"
api_patch_url = "https://jsonplaceholder.typicode.com/todos/10"
api_delete_url = "https://jsonplaceholder.typicode.com/todos/10"

#Data
post_data = {"userId": 1, "title": "Buy milk", "completed": False}
put_data = {"userId": 1, "title": "Wash car", "completed": True}
patch_data = {"title": "Mow lawn"}

#Standard Header 
headers =  {"Content-Type":"application/json"}

#returns 200
def get_call(api_url):
	response = requests.get(api_url)
	return response


#returns 201
def post_call(api_url, data):
	"""
	using header + data combo gives you more control over the request.
	adding a header tells the REST API the type of data you send to request 
	use json.dump serialize the data to json format 
	same effect as response = requests.post(api_url, json=data)
	"""
	response = requests.post(api_url, data = json.dumps(data), headers = headers)
	return response



#returns 200 
def put_call(api_url,data):
	response = requests.put(api_url, data = json.dumps(data), headers = headers)
	return response


#returns 200
#unlike put, the patch call doesn't completely replace the existing resources but 
#only modifies the values set in the json sent with the request 
def patch_call(api_url,data):
	response = requests.patch(api_url, data = json.dumps(data), headers = headers)
	return response 

#returns 200
def delete_call(api_url):
	response = requests.delete(api_url)
	return response


print("--------GET CALL-----------")
get_response = get_call(api_get_url)
print(get_response.status_code)
print(get_response.json())


print("\n")


print("--------POST CALL-----------")
post_response = post_call(api_post_url,post_data)
print(post_response.status_code)
print(post_response.json())


print("\n")


print("--------PUT CALL-----------")
put_response = put_call(api_put_url,put_data)
print(put_response.status_code)
print(put_response.json())


print("\n")


print("--------PATCH CALL-----------")
patch_response = patch_call(api_patch_url,patch_data)
print(patch_response.status_code)
print(patch_response.json())

print("\n")

print("--------DELETE CALL-----------")
delete_response = delete_call(api_delete_url)
print(delete_response.status_code)
print(delete_response.json())
