fh = open('mbox.txt')
for line in fh:
    ly = line.rstrip()
    print(ly.upper())
    