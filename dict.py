dict = {
    "name": "Shubham",
    "age": 21,
    "place": "Phaltan",
    "subject": ["python", "AIT", "ADBMS"]
}

print(dict.keys())
print(dict.items())
dict2 = {"new":1}
dict.update(dict2)
print(dict.get("age"))
