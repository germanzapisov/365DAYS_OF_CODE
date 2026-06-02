import json
data = {"name": "German",
        "age": 30}

s = json.dumps(data,
               ensure_ascii=False,
               indent=1)

new_s = json.loads(s)

print(s)
print(type(new_s))

# with open (data.json, 'w') as file:
#         json.dump(data)
#
