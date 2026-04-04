import mysql.connector as sql  
con = sql.connect(host='localhost', user='root', passwd='akshaya', database='T')  
cur = con.cursor() 
def show_place(place):
    cur.execute("SELECT * FROM TN WHERE PLACE=%s", (place,))
    d = cur.fetchall()

    print("PLACE \t\t\t HOTELS \t\t\t SIGHTSEEING")
    for i in d:
        print(i[0], i[1], i[2], sep='\t\t')

places = {
    1: "ARIYALUR", 2: "CHENGALPATTU", 3: "CHENNAI",
    4: "COIMBATORE", 5: "CUDDALORE", 6: "DHARMAPURI",
    7: "DINDIGUL", 8: "ERODE", 9: "KALLAKURICHI",
    10: "KANCHIPURAM", 11: "KANYAKUMARI", 12: "KARUR",
    13: "KRISHNAGIRI", 14: "MADURAI", 15: "MAYILADUTHURAI",
    16: "NAGAPATTINAM", 17: "NAMAKKAL", 18: "NILGIRIS",
    19: "PERAMBALUR", 20: "PUDUKKOTTAI", 21: "RAMANATHAPURAM",
    22: "RANIPET", 23: "SALEM", 24: "SIVAGANGAI",
    25: "TENKASI", 26: "THANJAVUR", 27: "THENI",
    28: "THOOTHUKUDI", 29: "TRICHY", 30: "TIRUNELVELI",
    31: "TIRUPATHUR", 32: "TIRUPPUR", 33: "TIRUVALLUR",
    34: "TIRUVANNAMALAI", 35: "TIRUVARUR", 36: "VELLORE",
    37: "VILUPPURAM", 38: "VIRUDHUNAGAR"
}

while True:
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
    
    try:
        ch = int(input('ENTER YOUR CHOICE: '))
        if ch == 39:
            break
        elif ch in places:
            show_place(places[ch])
        else:
            print("INVALID INPUT")

    except ValueError:
        print("Please enter a number!")
