firstname = str(input('First name: '))
lastname = str(input('Last name: '))
shortname = firstname[0] + '.' + " "+lastname[0:4]
print('Short name: ' + shortname)