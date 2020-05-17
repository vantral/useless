import json

notebook = json.load(open('search.ipynb'))

code = []
for cell in notebook['cells']:
    if cell['cell_type'] == 'code':
        code.append(cell['source'])
        
with open('py.py', 'w', encoding='utf-8') as f:
    f.write('\n\n'.join([''.join(x) for x in code]))
