import requests

res=requests.get('http://192.168.41.235:8000/Employee/')
res=requests.get('http://192.168.41.235:8000/Employee/id/')
res=requests.post('http://192.168.41.235:8000/Employee/') # with data
res=requests.put('http://192.168.41.235:8000/Employee/id/') #with data
res=requests.patch('http://192.168.41.235:8000/Employee/id/') #with data
res=requests.delete('http://192.168.41.235:8000/Employee/id/') #with data

data=res.text
print(data)


# data={
#     'name':'Rahul',
#     'f_name':'Raj',
#     'm_name':'Rani',
#     'roll_no':101,
#     'city':'Delhi',
# }

# res=requests.post('http://192.168.41.156:8000/student/',data=data)

# print(res.text)