import tkinter as tk
from urllib.parse import quote, urlsplit, urlunsplit

import pyperclip

HEADING_FONT = ('TkDefaultFont', 18)
FONT = ('TkDefaultFont', 12)

root = tk.Tk()
root.title("Affiliate Link Tool")
root.geometry("500x300")

TRACKING_LINK = 'https://prf.hn/click/camref:1100l8rZZ/destination:'
DEFAULT_PADDING = {"pady": 2, "padx": 10}

label = tk.Label(root, text="Affiliate Link", font=HEADING_FONT)
label.pack(anchor='w')

output_text = tk.StringVar()
output_label = tk.Entry(root, textvariable=output_text, state='readonly', width=900, font=FONT)

def remove_query_params(url:str)->str:
    parts = urlsplit(url)
    return urlunsplit((parts.scheme, parts.netloc, parts.path, '', ''))



def on_input_update(*args):
    input_link = input_text.get()

    if "chewy" in input_link:
        output = TRACKING_LINK + quote(input_link, safe='')
        output_text.set(output)
        copytoclip()
    elif "amazon" in input_link:
        output = remove_query_params(input_link)
        output_text.set(output)
        copytoclip()
    else:
        output_text.set('unknown input')


input_text = tk.StringVar()
input_text.trace("w", on_input_update)
input_field = tk.Entry(root, textvariable=input_text, width=900, font=FONT)
input_field.pack(**DEFAULT_PADDING)

label2 = tk.Label(root, text="Formatted Link", font=HEADING_FONT)
label2.pack(anchor='w')

output_label.pack(**DEFAULT_PADDING)

def copytoclip():
    pyperclip.copy(output_text.get())
    copy_button.config(text="Copied!")
    root.after(1500, lambda: copy_button.config(text="Copy to Clipboard"))

def pastetoinput():
    input_text.set(pyperclip.paste())
    paste_button.config(text="Pasted!")
    root.after(1500, lambda: paste_button.config(text="Paste from Clipboard"))

paste_button = tk.Button(root, text="Paste from Clipboard", command=pastetoinput)
paste_button.pack(**DEFAULT_PADDING)

copy_button = tk.Button(root, text="Copy to Clipboard", command=copytoclip)
copy_button.pack(**DEFAULT_PADDING)

root.mainloop()
