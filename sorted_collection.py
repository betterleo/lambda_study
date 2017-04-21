collection = [{'score': 2, 'name': 'a'}, {'score': 1, 'name': 'c'}, {'score': 3, 'name': 'b'}]
print sorted(collection, key=lambda x: x.get('score'), reverse=True)
print sorted(collection, key=lambda x: x.get('name'), reverse=True)


