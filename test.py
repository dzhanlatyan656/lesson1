users = {
	"Маша": {"city": "Moscow", "temperature":"25" ,"wind":"north"},
	"Паша": {"city":"SPb", "temperature":"30", "wind":"east"},
	"Саша": {"city":"Voronezh", "temperature":"29", "wind":"south"}
}

user_reply = input("your name? ")


user = users.get(user_reply)

if user:
	print(user["city"],user["temperature"],user["wind"])
else:
	print("Not found")