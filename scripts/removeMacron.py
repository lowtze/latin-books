filename = 'test.txt' # put in same directory as file and rename appropriately

replacements = {
    'ā':'a',
    'ē':'e',
    'ī':'i',
    'ō':'o',
    'ū':'u',
    'ȳ':'y',
    'Ā':'A',
    'Ē':'E',
    'Ī':'I',
    'Ō':'O',
    'Ū':'U',
    'Ȳ':'Y',
} # can change to adjust any other common errors by adding additional keys and values


with open(filename, encoding="utf8") as f:
    data = f.read()
    text = ''.join([replacements.get(c,c) for c in data]) # find keys above in target text and replace with corresponding values

with open(filename, "w", encoding="utf8") as f:
    f.write(text) # update the original doc; may want to make a back up as there is no going back after this...
