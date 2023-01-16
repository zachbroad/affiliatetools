import tkinter as tk
from urllib.parse import quote, urlsplit, urlunsplit

import pyperclip

HEADING_FONT = ('System', 18)

root = tk.Tk()
root.title("Affiliate Link Tool")
root.geometry("500x300")

TRACKING_LINK = 'https://prf.hn/click/camref:1100l8rZZ/destination:'

label = tk.Label(root, text="Affiliate Link", font=HEADING_FONT)
label.pack(anchor='w')

output_text = tk.StringVar()
output_label = tk.Entry(root, textvariable=output_text, state='readonly', width=900)

def remove_query_params(url:str)->str:
    parts = urlsplit(url)
    return urlunsplit((parts.scheme, parts.netloc, parts.path, '', ''))

def on_input_update(*args):
    input_link = input_text.get()

    if "chewy" in input_link:
        output = TRACKING_LINK + quote(input_link, safe='')
        output_text.set(output)
    elif "amazon" in input_link:
        output = remove_query_params(input_link)
        output_text.set(output)
    else:
        output_text.set('unknown input')


input_text = tk.StringVar()
input_text.trace("w", on_input_update)
input_field = tk.Entry(root, textvariable=input_text, width=900)
input_field.pack()

label2 = tk.Label(root, text="Formatted Link", font=HEADING_FONT)
label2.pack(anchor='w')

output_label.pack()

def copytoclip():
    pyperclip.copy(output_text.get())
    copy_button.config(text="Copied!")
    root.after(1500, lambda: copy_button.config(text="Copy to Clipboard"))

copy_button = tk.Button(root, text="Copy to Clipboard", command=copytoclip)
copy_button.pack()

root.mainloop()
