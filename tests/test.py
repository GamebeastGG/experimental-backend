import requests

url = 'https://experimental-backend.vercel.app/api/store_data'
data = [
    {"username": "GamebeastRblx", "message": "dude you're bad", "userId": 5439944669, "position": [-0.11967581370335638, -0.48464647358916437, -0.14027365453989497]},
    {"username": "GamebeastRblx", "message": "You didn't even try and then take my loot", "userId": 5439944669, "position": [-0.11967581370335638, -0.48464647358916437, -0.14027365453989497]},
    {"username": "GamebeastRblx", "message": "idk", "userId": 5439944669, "position": [-0.11967581370335638, -0.48464647358916437, -0.14027365453989497]},
    {"username": "GamebeastRblx", "message": "why?? camp", "userId": 5439944669, "position": [-0.1835979621591291, -0.48464647358916437, -0.07818210411960894]},
    {"username": "GamebeastRblx", "message": "trash", "userId": 5439944669, "position": [-0.21630919533382673, -0.48464647358916437, -0.044490686756439978]}
]

response = requests.post(url, json=data)
print(response.status_code)
print(response.json())