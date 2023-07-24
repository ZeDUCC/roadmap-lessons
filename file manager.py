import os

print(os.getcwd())

os.chdir("C:/Documents/test photos")

print(os.getcwd())

#os.rename('C:/Documents/test photos/folder 1/Screenshot 2023-06-13 212405.png', 'C:/Documents/test photos/Screenshot 2023-06-13 212405.png')

#os.mkdir("C:/Documents/test photos/folder 2")

#print(os.listdir())

# for i in os.listdir():
#     if i.__contains__('folder'):
#         pass
#     else:
#         if i.__contains__("1"):
#             os.rename(i, 'C:/Documents/test photos/folder 1/type 1.png')
#         elif i.__contains__("2"):
#             os.rename(i, 'C:/Documents/test photos/folder 2/type 2.png')

# for i in os.listdir():
#     j = i.replace('IMG-', '')
#     j = j.replace('Copy', '')
#     a = j.split('-')
#     print([a])
#     os.rename(i, (a[0] + '.png'))

for i in os.listdir():
    if i.__contains__('folder'):
        pass
    else:
        year = i[0:4]
        month = i[4:6]
        day = i[6:8]
        
        if month == '01':
            month = 'January'
        elif month == '02':
            month = 'February'
        elif month == '03':
            month = 'March'
        elif month == '04':
            month = 'April'
        elif month == '05':
            month = 'May'
        elif month == '06':
            month = 'June'
        elif month == '07':
            month = 'July'
        elif month == '08':
            month = 'August'
        elif month == '09':
            month = 'September'
        elif month == '10':
            month = "October"
        elif month == '11':
            month = 'November'
        else:
            month = 'December'

        os.rename(i, 'C:/Documents/test photos/' + month + ' ' + day + ', ' + year + '/' +  i + '.png')