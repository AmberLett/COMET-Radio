import tkinter as tk
import serial

ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)

def send_coordinates():
	ra = ra_entry.get()
	dec = dec_entry.get()

	message = f"RA,{ra},{dec}\n"
	ser.write(message.encode())
	print (f"Sent: {message.strip()}")

root = tk.Tk()
root.title("Telescope Motor Control")

tk.Label(root, text="Right Ascension (RA):").grid(row=0)
tk.Label(root, text="Declination (Dec):").grid(row=1)

ra_entry = tk.Entry(root)
dec_entry = tk.Entry(root)

ra_entry.grid(row=0, column=1)
dec_entry.grid(row=1, column=1)

send_button = tk.Button(root, text="Send", command=send_coordinates)
send_button.grid(row=2, columnspan=2)

root.mainloop()
