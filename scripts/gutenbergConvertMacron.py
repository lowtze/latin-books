filename = 'ritchie.txt'

replacements = {
    'á':'ā',
    'é':'ē',
    'í':'ī',
    'ó':'ō',
    'ú':'ū',
    'ý':'ȳ',
    'Á':'Ā',
    'É':'Ē',
    'Í':'Ī',
    'Ó':'Ō',
    'Ú':'Ū',
    'Ý':'Ȳ',
}


with open(filename, encoding="utf8") as f:
    data = f.read()
    text = ''.join([replacements.get(c,c) for c in data])

with open(filename, "w", encoding="utf8") as f:
    f.write(text)
