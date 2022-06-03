filename = 'hans.md'

replacements = {
    'ā':'a',
    'ē':'e',
    'ī':'i',
    'ō':'o',
    'ū':'u',
    'ȳ':'y',
    'ÿ':'y',
    'Ā':'A',
    'Ē':'E',
    'Ī':'I',
    'Ō':'O',
    'Ū':'U',
    'Ȳ':'Y',
}


with open(filename, encoding="utf8") as f:
    data = f.read()
    text = ''.join([replacements.get(c,c) for c in data])

with open(filename, "w", encoding="utf8") as f:
    f.write(text)
