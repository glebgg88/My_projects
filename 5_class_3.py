dictionary = {"cat" : "chat" , "dog" : "chien" , "horse" : "cheval"}
phone_num = {
    'boss' : 23467829692876,
    'Suzy' : 287289890288278
}

print(dictionary["cat"])
print(phone_num["Suzy"])



dict1 = {
    "cat" : 'chat' , 
    "dog" : 'chien',
    "horse" : "cheval"
}

words = ['cat', 'lion' , 'horse']

for word in words:
    if word in dict1:
        print(word, '->' , dict1[word])
    else: 
        print(word, 'is not in dictionary')

