paks = []
with open('./requirements.txt') as f:
    file = f.readlines()
    for line in file:
        if line in ['mysqlclient\n', '\n', 'xadmin-django\n']:
            continue
        pak, ver = line.split('==')
        paks.append(pak)
with open('./newrequirement.txt', 'w') as f:
    for pak in paks:
        f.write(pak+'\n')
    # print(file)