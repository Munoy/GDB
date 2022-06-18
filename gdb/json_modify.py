import json

file = open('gdb/static/json/all-cards.json', encoding='UTF-8')
jsonObject = json.load(file)

print(jsonObject[0]['oracle_id'])

oracle_name = {}


for card in jsonObject:
    oracle = {}
    o = str(card.get('name'))
    if card['name'] in oracle_name:
        a = oracle_name[o]['card_id']
        a.append(card['id'])
        print(a)
        oracle_name[o]['card_id'] = a
        a = ''
    else:
        oracle.setdefault('name', card['name'])
        oracle.setdefault('card_id', [card['id']])
        oracle_name.setdefault(card.get('name'), oracle)
    if 'printed_name' in card:
        oracle_name[o].setdefault('printed_name', card['printed_name'])

file_path = "gdb/static/json/oracle_name.json"

with open(file_path, 'w', encoding='UTF-8') as f:
    json.dump(oracle_name, f, ensure_ascii=False)
