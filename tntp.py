import mysql.connector as sql
import tkinter as tk
from tkinter import ttk

con = sql.connect(host='localhost',user='root',passwd='password',database='T')
cur = con.cursor()
def clean_hotel(name):
    if not name:
        return None
    name = name.strip()
    return name if name != "" else None

def show_place():
    place = combo.get().strip().upper()
    cur.execute("SELECT * FROM TN WHERE DISTRICT=%s", (place,))
    data = cur.fetchall()
    text.delete("1.0", tk.END)
    if not data:
        text.insert(tk.END, "No data found")
        return
    for row in data:
        district = row[0]
        hotels = row[1:]
        text.insert(tk.END, f"\n📍 {district}\n")
        text.insert(tk.END, "-" * 35 + "\n")
        seen = set()
        count = 1
        for hotel in hotels:
            hotel = clean_hotel(hotel)
            if hotel and hotel not in seen:
                text.insert(tk.END, f"{count}. {hotel}\n")
                seen.add(hotel)
                count += 1
        if count == 1:
            text.insert(tk.END, "No hotels available\n")

root = tk.Tk()
root.title("Tamil Nadu Tourism App")
root.geometry("520x460")
districts = [
    "ARIYALUR","CHENGALPATTU","CHENNAI","COIMBATORE","CUDDALORE",
    "DHARMAPURI","DINDIGUL","ERODE","KALLAKURICHI","KANCHIPURAM",
    "KANYAKUMARI","KARUR","KRISHNAGIRI","MADURAI","MAYILADUTHURAI",
    "NAGAPATTINAM","NAMAKKAL","NILGIRIS","PERAMBALUR","PUDUKKOTTAI",
    "RAMANATHAPURAM","RANIPET","SALEM","SIVAGANGAI","TENKASI",
    "THANJAVUR","THENI","THOOTHUKUDI","TRICHY","TIRUNELVELI",
    "TIRUPATHUR","TIRUPPUR","TIRUVALLUR","TIRUVANNAMALAI",
    "TIRUVARUR","VELLORE","VILUPPURAM","VIRUDHUNAGAR"
]

combo = ttk.Combobox(root, values=districts, width=35)
combo.set("Select District")
combo.pack(pady=12)
btn = tk.Button(root, text="Show Hotels", command=show_place)
btn.pack(pady=5)
frame = tk.Frame(root)
frame.pack(pady=10)
scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
text = tk.Text(frame, width=60, height=18, yscrollcommand=scrollbar.set)
text.pack()
scrollbar.config(command=text.yview)
root.mainloop()
