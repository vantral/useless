def nice():
    items = []
    path = os.path.abspath('.')
    for root, dirs, files in os.walk(path):
        for file in files:
            items.append((root, file))
    print('-' * 60)
    print('{0:<31}{1}{2}'.format('Folder', ' \ ', 'Filename'))
    print('-' * 60)
    for line in items:
        x = line[0]
        #print(len(x))
        if len(x) > 31:
            #print(line[:10])
            x = line[0][:9] + '...' + line[0][-19:]
        print('{0:<30}{1}{2}'.format(x, ' \ ', line[1]))

nice()
