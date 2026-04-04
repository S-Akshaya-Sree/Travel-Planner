import mysql.connector as sql
import tkinter as tk
from tkinter import ttk

con = sql.connect(host='localhost', user='root', passwd='password', database='T')
cur = con.cursor()

def show_place():
    place = combo.get()
    cur.execute("SELECT * FROM TN WHERE PLACE=%s", (place,))
    data = cur.fetchall()
    text.delete("1.0", tk.END)
    text.insert(tk.END, "PLACE\t\tHOTELS\t\tSIGHTSEEING\n\n")
    for row in data:
        text.insert(tk.END, f"{row[0]}\t\t{row[1]}\t\t{row[2]}\n")

root = tk.Tk()
root.title("Tamil Nadu Tourism App")
root.geometry("600x400")
places = [
    "ARIYALUR", "CHENGALPATTU", "CHENNAI", "COIMBATORE",
    "CUDDALORE", "DHARMAPURI", "DINDIGUL", "ERODE",
    "KALLAKURICHI", "KANCHIPURAM", "KANYAKUMARI", "KARUR",
    "KRISHNAGIRI", "MADURAI", "MAYILADUTHURAI", "NAGAPATTINAM",
    "NAMAKKAL", "NILGIRIS", "PERAMBALUR", "PUDUKKOTTAI",
    "RAMANATHAPURAM", "RANIPET", "SALEM", "SIVAGANGAI",
    "TENKASI", "THANJAVUR", "THENI", "THOOTHUKUDI",
    "TRICHY", "TIRUNELVELI", "TIRUPATHUR", "TIRUPPUR",
    "TIRUVALLUR", "TIRUVANNAMALAI", "TIRUVARUR", "VELLORE",
    "VILUPPURAM", "VIRUDHUNAGAR"
]

combo = ttk.Combobox(root, values=places, width=30)
combo.set("Select a place")
combo.pack(pady=10)
btn = tk.Button(root, text="Show Details", command=show_place)
btn.pack(pady=5)
text = tk.Text(root, width=70, height=15)
text.pack(pady=10)
root.mainloop()
