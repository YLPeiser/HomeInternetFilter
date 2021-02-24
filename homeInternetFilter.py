# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 01:47:36 2020

@author: Yehuda Peiser

     Read: --- hosts --- file 
from path: --- C:\Windows\System32\drivers\etc

Copy it ito temp file in temp folder
Ask user via Gui which websites (symbolic names) they want unreachable by users of htis windows local account
Also ask user for an IP address to where they want that url redirected to
Append those lines to the temp txt file.
Rename hthe file WITHOUT the txt exxtention.
Copy the file over the original hosts file.

Things to check before starrting:
    -is the path accessable
    -is the file copyable?
    -can the temp file be saved without an extention without windows pop-ups
    -Finallyan d most NB, can the temp file be actually moved to the target 
      path assumming authorization is given and in teh presence of windows 
      security pop-ups. ie this is not meant as a stealth hack but to enable 
      the user to redirect the users of his machine away from certain sites.
"""

#%%
'''Working with escaping the escape character int eh Windows path.
There is teh r that makes teh string understood as a sring literal

path = r'C:\Windows\System32\drivers\etc'.replace(r"\\", '/')

'''
#%%

#%%
 
import admin
#if not admin.isUserAdmin():
#        admin.runAsAdmin()

url2bypass = input("Please enter the website (symbolic/alphabetic) url you want to bypass:")
mesg = "Please enter the IP address thwhere you want "+url2bypass+" redirected to \n For example '104.19.222.11' (which is chabad.org)>"
destIP = input(mesg)

srcPathFile  = r'C:\Windows\System32\drivers\etc\hosts'
destPathFile = r'C:\Users\owner\Documents\filter.txt' 
 #Text.txt" #r'C:hosts.txt'

import shutil

#original = r'original path where the file is currently stored\file name.file extension'
#target = r'target path where the file will be copied\file name.file extension'

print('before copying Original to "filter.txt" to Documents folder')
shutil.copy(srcPathFile, destPathFile)
input('filter.txt should be there now.')

print('openng FIlter.txt')
print('opening', destPathFile)
f = open(destPathFile,"a")
input("it's open")

line = '104.19.222.11 '+ url2bypass
f.write(line)
f.close()
input("Appended a line. Now it's closed")

#try:
srcPathFile  = r'C:\Windows\System32\drivers\etc\hostsBaam'
#if not admin.isUserAdmin():
try:
    admin.runAsAdmin([shutil.copy(destPathFile,srcPathFile)])
except AttributeError:
    pass
except PermissionError:
    print('Please run this script or open Command Prompt as Administrator.')
    
#except PermissionError:
#    print("How do we get permission?")
#    print("Perhaps run this very pthon program as Administrator?")
#    
#%%
