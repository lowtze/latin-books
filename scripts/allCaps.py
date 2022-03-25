filename = 'test.txt' # put in same directory as file and change name

with open(filename, encoding="utf8") as f:
    data = f.read()
    text = data.upper().replace(' ','') # replace removes all spaces between letters

with open(filename, "w", encoding="utf8") as f:
    f.write(text)

''' to do:

replace punctuation with no space as well

def a(text):
    chars = "&#"
    for c in chars:

'''
