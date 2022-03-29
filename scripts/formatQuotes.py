filename = 'test.txt'

with open(filename, 'r+', encoding="utf8") as f:
        lines=f.readlines()
        for i, line in enumerate(lines):
                lines[i] = '>*' + lines[i].strip() + '*\n>\n' #two new lines to leave a space between each
        f.seek(0) # go back to start
        for line in lines:
                f.write(line) #write the modified lines
        
