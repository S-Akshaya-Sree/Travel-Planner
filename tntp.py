
import mysql.connector as sql  
con=sql.connect(host='localhost',user='root',passwd='akshaya',database='T')  
cur=con.cursor() 

def ARIYALUR(): 
    cur.execute("SELECT * FROM TN WHERE PLACE='ARIYALUR'") 
    d=cur.fetchall() 
    print("PLACE \t\t\t HOTELS \t\t\t SIGHTSEEING") 
    for i in d: 
        print(i[0],i[1],i[2],sep='\t\t') 

def CHENGALPATTU():  
    cur.execute("SELECT * FROM TN WHERE PLACE='CHENGALPATTU'") 
    d=cur.fetchall() 
    print("PLACE \t\t\t HOTELS \t\t\t SIGHTSEEING")  
    for i in d:  
        print(i[0],i[1],i[2],sep='\t\t')  

def CHENNAI():  
    cur.execute("SELECT * FROM TN WHERE PLACE='CHENNAI'") 
    d=cur.fetchall()  
    print("PLACE \t\t\t HOTELS \t\t\t SIGHTSEEING")  
    for i in d:  
        print(i[0],i[1],i[2],sep='\t\t') 

def COIMBATORE(): 
    cur.execute("SELECT * FROM TN WHERE PLACE='COIMBATORE'") 
    d=cur.fetchall() 
    print("PLACE \t\t\t HOTELS \t\t\t SIGHTSEEING")  
    for i in d: 
        print(i[0],i[1],i[2],sep='\t\t') 
 
def CUDDALORE():  
    cur.execute("SELECT * FROM TN WHERE PLACE='CUDDALORE'")  
    d=cur.fetchall()  
    print("PLACE \t\t\t HOTELS \t\t\t SIGHTSEEING")  
    for i in d: 
        print(i[0],i[1],i[2],sep='\t\t') 

def DHARMAPURI():  
    cur.execute("SELECT * FROM TN WHERE PLACE='DHARMAPURI'")  
    d=cur.fetchall()  
    print("PLACE \t\t\t HOTELS \t\t\t SIGHTSEEING")  
    for i in d:  
        print(i[0],i[1],i[2],sep='\t\t')  

def DINDIGUL():  
    cur.execute("SELECT * FROM TN WHERE PLACE='DINDIGUL'")  
    d=cur.fetchall()  
    print("PLACE \t\t\t HOTELS \t\t\t SIGHTSEEING")  
    for i in d:  
        print(i[0],i[1],i[2],sep='\t\t') 

def ERODE():  
    cur.execute("SELECT * FROM TN WHERE PLACE='ERODE'")  
    d=cur.fetchall()  
    print("PLACE \t\t\t HOTELS \t\t\t SIGHTSEEING") 
    for i in d:  
        print(i[0],i[1],i[2],sep='\t\t') 
 
def KALLAKURICHI():  
    cur.execute("SELECT * FROM TN WHERE PLACE='KALLAKURICHI'") 
    d=cur.fetchall() 
    print("PLACE \t\t\t HOTELS \t\t\t SIGHTSEEING") 
    for i in d: 
        print(i[0],i[1],i[2],sep='\t\t') 
 
def KANCHIPURAM(): 
    cur.execute("SELECT * FROM TN WHERE PLACE='KANCHIPURAM'") 
    d=cur.fetchall() 
    print("PLACE \t\t\t HOTELS \t\t\t SIGHTSEEING") 
    for i in d: 
        print(i[0],i[1],i[2],sep='\t\t') 
 
def KANYAKUMARI():  
    cur.execute("SELECT * FROM TN WHERE PLACE='KANYAKUMARI'")  
    d=cur.fetchall()  
    print("PLACE \t\t\t HOTELS \t\t\t SIGHTSEEING")  
    for i in d:  
        print(i[0],i[1],i[2],sep='\t\t') 
 
def KARUR(): 
    cur.execute("SELECT * FROM TN WHERE PLACE='KARUR'") 
    d=cur.fetchall() 
    print("PLACE \t\t\t HOTELS \t\t\t SIGHTSEEING") 
    for i in d: 
        print(i[0],i[1],i[2],sep='\t\t') 
 
def KRISHNAGIRI(): 
    cur.execute("SELECT * FROM TN WHERE PLACE='KRISHNAGIRI'") 
    d=cur.fetchall() 
    print("PLACE \t\t\t HOTELS \t\t\t SIGHTSEEING") 
    for i in d: 
        print(i[0],i[1],i[2],sep='\t\t') 

def MADURAI(): 
    cur.execute("SELECT * FROM TN WHERE PLACE='MADURAI'") 
    d=cur.fetchall() 
    print("PLACE \t\t\t HOTELS \t\t\t SIGHTSEEING") 
    for i in d: 
        print(i[0],i[1],i[2],sep='\t\t') 
 
def MAYILADUTHURAI(): 
    cur.execute("SELECT * FROM TN WHERE PLACE='MAYILADUTHURAI'") 
    d=cur.fetchall()  
    print("PLACE \t\t\t HOTELS \t\t\t SIGHTSEEING") 
    for i in d: 
        print(i[0],i[1],i[2],sep='\t\t') 
 
def NAGAPATTINAM(): 
    cur.execute("SELECT * FROM TN WHERE PLACE='NAGAPATTINAM'") 
    d=cur.fetchall() 
    print("PLACE \t\t\t HOTELS \t\t\t SIGHTSEEING") 
    for i in d: 
        print(i[0],i[1],i[2],sep='\t\t') 
 
def NAMAKKAL(): 
    cur.execute("SELECT * FROM TN WHERE PLACE='NAMAKKAL'") 
    d=cur.fetchall() 
    print("PLACE \t\t\t HOTELS \t\t\t SIGHTSEEING") 
    for i in d: 
        print(i[0],i[1],i[2],sep='\t\t') 
 
def NILGIRIS(): 
    cur.execute("SELECT * FROM TN WHERE PLACE='NILGIRIS'") 
    d=cur.fetchall() 
    print("PLACE \t\t\t HOTELS \t\t\t SIGHTSEEING") 
    for i in d: 
        print(i[0],i[1],i[2],sep='\t\t') 
 
def PERAMBALUR(): 
    cur.execute("SELECT * FROM TN WHERE PLACE='PERAMBALUR'") 
    d=cur.fetchall() 
    print("PLACE \t\t\t HOTELS \t\t\t SIGHTSEEING") 
    for i in d: 
        print(i[0],i[1],i[2],sep='\t\t') 
 
def PUDUKKOTTAI(): 
    cur.execute("SELECT * FROM TN WHERE PLACE='PUDUKKOTTAI'")  
    d=cur.fetchall()  
    print("PLACE \t\t\t HOTELS \t\t\t SIGHTSEEING")  
    for i in d:  
        print(i[0],i[1],i[2],sep='\t\t') 
 
def RAMANATHAPURAM():  
    cur.execute("SELECT * FROM TN WHERE PLACE='RAMANATHAPURAM'") 
    d=cur.fetchall()  
    print("PLACE \t\t\t HOTELS \t\t\t SIGHTSEEING")  
    for i in d:  
        print(i[0],i[1],i[2],sep='\t\t') 
 
def RANIPET(): 
 
    cur.execute("SELECT * FROM TN WHERE PLACE='RANIPET'")  
    d=cur.fetchall() 
    print("PLACE \t\t\t HOTELS \t\t\t SIGHTSEEING") 
    for i in d: 
        print(i[0],i[1],i[2],sep='\t\t') 
 
def SALEM():  
    cur.execute("SELECT * FROM TN WHERE PLACE='SALEM'")  
    d=cur.fetchall() 
    print("PLACE \t\t\t HOTELS \t\t\t SIGHTSEEING") 
    for i in d: 
        print(i[0],i[1],i[2],sep='\t\t') 
 
def SIVAGANGAI(): 
    cur.execute("SELECT * FROM TN WHERE PLACE='SIVAGANGAI'") 
    d=cur.fetchall() 
    print("PLACE \t\t\t HOTELS \t\t\t SIGHTSEEING") 
    for i in d: 
        print(i[0],i[1],i[2],sep='\t\t') 
 
def TENKASI(): 
    cur.execute("SELECT * FROM TN WHERE PLACE='TENKASI'") 
    d=cur.fetchall() 
    print("PLACE \t\t\t HOTELS \t\t\tSIGHTSEEING") 
    for i in d: 
        print(i[0],i[1],i[2],sep='\t\t') 
 
def THANJAVUR(): 
    cur.execute("SELECT * FROM TN WHERE PLACE='THANJAVUR'") 
    d=cur.fetchall() 
    print("PLACE \t\t\t HOTELS \t\t\t SIGHTSEEING") 
    for i in d: 
        print(i[0],i[1],i[2],sep='\t\t') 
 
def THENI(): 
    cur.execute("SELECT * FROM TN WHERE PLACE='THENI'") 
    d=cur.fetchall()
    print("PLACE \t\t\t HOTELS \t\t\t SIGHTSEEING") 
    for i in d:  
        print(i[0],i[1],i[2],sep='\t\t') 
 
def THOOTHUKUDI(): 
    cur.execute("SELECT * FROM TN WHERE PLACE='THOOTHUKUDI'") 
    d=cur.fetchall() 
    print("PLACE \t\t\t HOTELS \t\t\t SIGHTSEEING") 
    for i in d: 
        print(i[0],i[1],i[2],sep='\t\t') 
 
def TRICHY(): 
    cur.execute("SELECT * FROM TN WHERE PLACE='TRICHY'") 
    d=cur.fetchall() 
    print("PLACE \t\t\t HOTELS \t\t\t SIGHTSEEING") 
    for i in d: 
        print(i[0],i[1],i[2],sep='\t\t') 
 
def TIRUNELVELI(): 
    cur.execute("SELECT * FROM TN WHERE PLACE='TIRUNELVELI'") 
    d=cur.fetchall() 
    print("PLACE \t\t\t HOTELS \t\t\t SIGHTSEEING") 
    for i in d: 
        print(i[0],i[1],i[2],sep='\t\t') 
 
def TIRUPATHUR(): 
    cur.execute("SELECT * FROM TN WHERE PLACE='TIRUPATHUR'") 
    d=cur.fetchall() 
    print("PLACE \t\t\t HOTELS \t\t\t SIGHTSEEING") 
    for i in d: 
        print(i[0],i[1],i[2],sep='\t\t') 
 
def TIRUPPUR(): 
    cur.execute("SELECT * FROM TN WHERE PLACE='TIRUPPUR'") 
    d=cur.fetchall() 
    print("PLACE \t\t\t HOTELS \t\t\t SIGHTSEEING") 
    for i in d: 
        print(i[0],i[1],i[2],sep='\t\t') 
 
def TIRUVALLUR(): 
    cur.execute("SELECT * FROM TN WHERE PLACE='TIRUVALLUR'") 
    d=cur.fetchall() 
    print("PLACE \t\t\t HOTELS \t\t\t SIGHTSEEING") 
    for i in d: 
        print(i[0],i[1],i[2],sep='\t\t') 
 
def TIRUVANNAMALAI(): 
    cur.execute("SELECT * FROM TN WHERE PLACE='TIRUVANNAMALAI'") 
    d=cur.fetchall() 
    print("PLACE \t\t\t HOTELS \t\t\t SIGHTSEEING") 
    for i in d: 
        print(i[0],i[1],i[2],sep='\t\t') 
 
def TIRUVARUR(): 
    cur.execute("SELECT * FROM TN WHERE PLACE='TIRUVARUR'")
    d=cur.fetchall() 
    print("PLACE \t\t\t HOTELS \t\t\t SIGHTSEEING") 
    for i in d: 
        print(i[0],i[1],i[2],sep='\t\t') 
 
def VELLORE(): 
    cur.execute("SELECT * FROM TN WHERE PLACE='VELLORE'") 
    d=cur.fetchall() 
    print("PLACE \t\t\t HOTELS \t\t\t SIGHTSEEING") 
    for i in d: 
        print(i[0],i[1],i[2],sep='\t\t') 
 
def VILUPPURAM(): 
    cur.execute("SELECT * FROM TN WHERE PLACE='VILUPPURAM'") 
    d=cur.fetchall() 
    print("PLACE \t\t\t HOTELS \t\t\t SIGHTSEEING") 
    for i in d: 
        print(i[0],i[1],i[2],sep='\t\t') 
 
def VIRUDHUNAGAR(): 
    cur.execute("SELECT * FROM TN WHERE PLACE='VIRUDHUNAGAR'") 
    d=cur.fetchall() 
    print("PLACE \t\t\t HOTELS \t\t\t SIGHTSEEING") 
    for i in d: 
        print(i[0],i[1],i[2],sep='\t\t') 
 
while(1):
    print('''MENU 

            1.ARIYALUR          2.CHENGALPATTU  3.CHENNAI 
            4.COIMBATORE        5.CUDDALORE     6.DHARMAPURI 
            7.DINDIGUL          8.ERODE         9.KALLAKURICHI 
            10.KANCHIPURAM     11.KANYAKUMARI  12.KARUR 
            13.KRISHNAGIRI     14.MADURAI      15.MAYILADUTHURAI 
            16.NAGAPATTINAM    17.NAMAKKAL     18.NILGIRIS 
            19.PERAMBALUR      20.PUDUKKOTTAI  21.RAMANATHAPURAM 
            22.RANIPET         23.SALEM        24.SIVAGANGAI 
            25.TENKASI         26.THANJAVUR    27.THENI 
            28.THOOTHUKUDI     29.TRICHY       30.TIRUNELVELI 
            31.TIRUPATHUR      32.TIRUPPUR     33.TIRUVALLUR 
            34.TIRUVANNAMALAI  35.TIRUVARUR    36.VELLORE 
            37.VILUPPURAM      38.VIRUDHUNAGAR 
            39.EXIT\n''') 
 
    ch=int(input('ENTER YOUR CHOICE:'))
    if(ch==1): 
        ARIYALUR() 
    elif(ch==2): 
        CHENGALPATTU() 
    elif(ch==3): 
        CHENNAI() 
    elif(ch==4): 
        COIMBATORE() 
    elif(ch==5): 
        CUDDALORE() 
    elif(ch==6):  
        DHARMAPURI() 
    elif(ch==7): 
        DINDIGUL()
    elif(ch==8): 
        ERODE() 
    elif(ch==9): 
        KALLAKURICHI() 
    elif(ch==10): 
        KANCHIPURAM()  
    elif(ch==11):  
        KANYAKUMARI()  
    elif(ch==12):  
        KARUR()  
    elif(ch==13):  
        KRISHNAGIRI()  
    elif(ch==14):  
        MADURAI()  
    elif(ch==15):  
        MAYILADUTHURAI() 
    elif(ch==16):  
        NAGAPATTINAM()  
    elif(ch==17):  
        NAMAKKAL()  
    elif(ch==18):  
        NILGIRIS() 
    elif(ch==19): 
        PERAMBALUR() 
    elif(ch==20): 
        PUDUKKOTTAI() 
    elif(ch==21):  
        RAMANATHAPURAM() 
    elif(ch==22):  
        RANIPET()  
    elif(ch==23): 
        SALEM()  
    elif(ch==24):  
        SIVAGANGAI()  
    elif(ch==25):  
        TENKASI()  
    elif(ch==26): 
        THANJAVUR() 
    elif(ch==27): 
        THENI() 
    elif(ch==28): 
        THOOTHUKUDI() 
    elif(ch==29): 
        TRICHY()  
    elif(ch==30):  
        TIRUNELVELI()  
    elif(ch==31): 
        TIRUPATHUR()  
    elif(ch==32): 
        TIRUPPUR()  
    elif(ch==33):  
        TIRUVALLUR()  
    elif(ch==34):  
        TIRUVANNAMALAI()  
    elif(ch==35):  
        TIRUVARUR()  
    elif(ch==36):  
        VELLORE()  
    elif(ch==37):  
        VILUPPURAM()  
    elif(ch==38):  
        VIRUDHUNAGAR()  

    elif(ch==39): 
        break  

    else: 
        print('INVALID INPUT')

