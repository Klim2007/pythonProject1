import json
import datetime
ap = open('C:\\Users\\User\\Desktop\\apls2.json', 'a')
# bin_list = open('bin.txt','r')
# list = {bin.txt.read())
bin_list = {'851129350443', '810708300434', '120340017336', '040240002456'}
username = input("Enter your name:")
userage = input("Enter your age:")
tax_number = input("Enter your tax number:")
def find_bin(tax_number):
    if tax_number in bin_list:
        print("Ok!")
    else:
        print("You cannot apply! Sorry!")
find_bin(tax_number)
application_date = datetime.datetime.now()
date = application_date.strftime("%d") + "." + application_date.strftime("%m") + "." + application_date.strftime("%Y")
application_text = """
I am: {},
i am: {} years old,
My tax id: {},
application date:""" + date+ ","
print(application_text.format(username, userage, tax_number))
if tax_number in bin_list:
    ap.write(application_text.format(username, userage, tax_number))
ap.close()
