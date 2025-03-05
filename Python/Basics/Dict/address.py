address = {
    'flat' : 601,
    'location' : 'sr nagar',
    'Area' : 'ameerpet'
    }
print(address)
print(type(address))
for item in address:
    print(item)
for item in address.values():
    print(item)
for name,value in address.items():
    print(f"{name }={value}")