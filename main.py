import tkinter as tk
import tkinter as ttk
from tkinter import filedialog, messagebox
from cryptography.fernet import Fernet
import string
import hashlib
import random
import math
encryption_algorithms = {
    "Caesar Cipher": 1,
    "Reverse Cipher": 2,
    "Autokey": 3,
    "Vigenere": 4,
    "Hashing": 5,
    "Transfer encrypt key": 6,
    "Transfer encrypt not key": 7,
    "One-Time Pad": 8,
    "Custom Algorithm": 9,
    "Merge Encryption/Decryption": 10,
}
fontstyle=("Georgia",14,"bold italic")
fontstyl=("Georgia",20,"bold italic")

def encrypt_password(password, algorithm):
    if algorithm == "Caesar Cipher":
        return caesar_cipher_encrypt(password, 3)
    elif algorithm == "Reverse Cipher":
        return reverse_cipher_encrypt(password)
    elif algorithm == "Transfer encrypt key":
        return transfer_encrypt(password)
    elif algorithm == "Transfer encrypt not key":
        return transfer_encrypt_not_key(password)
    elif algorithm == "Custom Algorithm":
        return custom_algorithm_encrypt(password)
    elif algorithm == "Autokey":
        return autokey_encrypt(password)
    elif algorithm == "Vigenere":
        return vigenere_encrypt(password)
    elif algorithm == "Hashing":
        return hashing_encrypt(password)
    elif algorithm == "One-Time Pad":
        key = generate_random_key(len(password))
        return one_time_pad_encrypt(password, key)
    elif algorithm == "Merge Encryption/Decryption":
        key = generate_random_key(len(password))
        return merge_encrypt_decrypt(password, key)
    else:
        return password
def generate_random_key(length):
    key = ""
    for _ in range(length):
        key += random.choice(string.ascii_letters)
    return key
def caesar_cipher_encrypt(plan_txte, key):
    cipher_txte = ""
    for i in range(len(plan_txte)):
        if plan_txte[i].islower():
            cipher_txte += chr((ord(plan_txte[i]) - 97 + key) % 26 + 97)
        elif plan_txte[i].isupper():
            cipher_txte += chr((ord(plan_txte[1]) - 65 + key) % 26 + 65)
    return (cipher_txte)
def caesar_cipher_dicrption(plan_txte, key):
    cipher_txte = ""
    for i in range(len(plan_txte)):
        if plan_txte[i].islower():
            cipher_txte += chr((ord(plan_txte[i]) - 97 - key) % 26 + 97)
        elif plan_txte[i].isupper():
            cipher_txte += chr((ord(plan_txte[1]) - 65 - key) % 26 + 65)
    return (cipher_txte)
def reverse_cipher_encrypt(text):
    return text[::-1]
def reverse_cipher_Decrypt(text):
    return text[::-1]
def custom_algorithm_encrypt(text):
    # Your custom algorithm implementation here
    return text
def autokey_encrypt(plan_text):
    key = "RLOmliki"
    cipher_text = ""
    for i in range(len(plan_text)):
        if plan_text[i].islower():
            cipher_text += chr((ord(plan_text[i]) - 97 + ord(key[i]) - 97) % 26 + 97)
        elif plan_text[i].isupper():
            cipher_text += chr((ord(plan_text[i]) - 65 + ord(key[i]) - 65) % 26 + 65)
    return cipher_text
def autokey_Decrypt(plan_text):
    key = "secretkey"
    cipher_text = ""
    for i in range(len(plan_text)):
        if plan_text[i].islower():
            cipher_text += chr((ord(plan_text[i])  - ord(key[i]) ) % 26 + 97)
        elif plan_text[i].isupper():
            cipher_text += chr((ord(plan_text[i]) - ord(key[i])) % 26 + 65)
    return cipher_text
def vigenere_encrypt(plan_text):
    key = "almliki"
    cipher_text = ""
    for i in range(len(plan_text)):
        if plan_text[i].islower():
            cipher_text += chr((ord(plan_text[1]) - 97 + ord(key[i]) - 97) % 26 + 97)
        elif plan_text[1].isupper():
            cipher_text += chr((ord(plan_text[1]) - 65 + ord(key[i]) - 65) % 26 + 65)
    return cipher_text
def vigenere_Decrypt(plan_text):
    key = "secretkey"
    cipher_text = ""
    for i in range(len(plan_text)):
        if plan_text[i].islower():
            cipher_text += chr((ord(plan_text[1])  - ord(key[i])) % 26 + 97)
        elif plan_text[1].isupper():
            cipher_text += chr((ord(plan_text[1]) - ord(key[i])) % 26 + 65)
    return cipher_text
def hashing_encrypt(text):
    hashed_text = hashlib.sha256(text.encode()).hexdigest()
    return hashed_text
def transfer_encrypt(plain):
    col = "231"
    num = str(col)
    w = len(num)
    n_row = math.ceil(len(plain) / w)
    aa = w * n_row
    d_free = w * n_row - len(plain)
    for i in range(d_free):
        plain += "z"
    x = 0
    cipher1 = ""
    while x != aa:
        cipher = ""
        for i in range(w):
            cipher += plain[x]
            x += 1
        for i in range(w):
            cipher1 += cipher[int(num[i]) - 1]
    return cipher1
def transfer_decrypt(cipher):
    col = "231"
    num = str(col)
    w = len(num)
    n_row = math.ceil(len(cipher) / w)
    aa = w * n_row
    plain = ""
    x = 0
    while x != aa:
        block = ""
        for i in range(w):
            block += cipher[x]
            x += 1
        for i in range(w):
            index = num.index(str(i + 1))
            plain += block[index]
    return plain
def transfer_encrypt_not_key(message):
    plaintext = message
    num_columns = 3
    num_rows = math.ceil(len(plaintext) / num_columns)
    remaining_chars = num_columns * num_rows - len(plaintext)
    for i in range(remaining_chars):
        plaintext += "x"
    matrix = [[0] * num_columns for _ in range(num_rows)]
    index = 0
    for i in range(num_rows):
        for j in range(num_columns):
            matrix[i][j] = plaintext[index]
            index += 1
    ciphertext = ""
    for i in range(num_columns):
        for j in range(num_rows):
            ciphertext += matrix[j][i]
    return ciphertext
def transfer_decrypt_not_key(ciphertext):
    num_columns = 3
    num_rows = len(ciphertext) // num_columns
    matrix = [[0] * num_columns for _ in range(num_rows)]
    index = 0
    for i in range(num_columns):
        for j in range(num_rows):
            matrix[j][i] = ciphertext[index]
            index += 1
    plaintext = ""
    for i in range(num_rows):
        for j in range(num_columns):
            if matrix[i][j] != "x":
                plaintext += matrix[i][j]
    return plaintext
def one_time_pad_encrypt(plaintext, key):
    encrypted_text = ""
    for i in range(len(plaintext)):
        char = plaintext[i]
        key_char = key[i % len(key)]
        encrypted_char = chr(ord(char) ^ ord(key_char))
        encrypted_text += encrypted_char
    return encrypted_text
def merge_encrypt_decrypt(plaintext, key):
    merged_text = ""
    for i in range(len(plaintext)):
        char = plaintext[i]
        key_char = key[i % len(key)]
        merged_char = chr(ord(char) ^ ord(key_char))
        merged_text += merged_char
    return merged_text

root = tk.Tk()
root.configure(bg="#330000")
root.geometry("800x800")
root.title("تطبيق التشفير")

def encrypt_file(filetype):

    filepath = filedialog.askopenfilename(initialdir="/", title="Select File",
                                              filetypes=((filetype, "*.jpg" + filetype),))
    key = b'F2Uaj6R5Gl2OQDg9p1FQF8YH2gK0poYX2c2XlZq9L1E='
    cipher = Fernet(key)
    with open(filepath, 'rb') as file:
        file_data = file.read()
    encrypted_data = cipher.encrypt(file_data)
    with open('rakan.pdf', 'wb') as file:
        file.write(encrypted_data)
    messagebox.showinfo("Encryption", f"{filetype} encrypted successfully!")
def encrypt_image():
    filepath = filedialog.askopenfilename(initialdir="/", title="Select File",)
    key=100
    with open(filepath,'rb')  as image:
        data_img=image.read()
    imgby=bytearray(data_img)
    for index,value in enumerate(imgby):
       imgby[index]=(value^key)
    with open('rakan.jpg', 'wb') as file:
        file.write(imgby)
    messagebox.showinfo("Encryption", f"{filepath} encrypted successfully!")
def encrypt_pdf():
    key = Fernet.generate_key()
    k = Fernet((key))
    filepath = filedialog.askopenfilename(initialdir="/", title="Select File")
    with open(filepath, 'rb') as file:
        file_data = file.read()
    ciphertext = k.encrypt(file_data)
    with open('rakan.pdf', 'wb') as file:
        file.write(ciphertext)
    messagebox.showinfo("Encryption", f"{filepath} encrypted successfully!")
def encrypt_audio():
    key = Fernet.generate_key()
    k = Fernet((key))
    filepath = filedialog.askopenfilename(initialdir="/", title="Select Audio",
                                              filetypes=(("Audio Files", "*.mp3"),))
    with open(filepath, 'rb') as audio:
       audio_data = audio.read()
    enc = k.encrypt(audio_data)
    with open('rakan.mp3', 'wb') as file:
        file.write(enc)
    messagebox.showinfo("Encryption", f"{filepath} Audio encrypted successfully!")
def encrypt_video():
        # اختيار ملف الفيديو
    filepath = filedialog.askopenfilename(initialdir="/", title="Select Video",
                                              filetypes=(("Video Files", "*.mp4"),))
    key = Fernet.generate_key()
    k = Fernet((key))
    with open(filepath, 'rb') as video:
        video_data = video.read()
    encrypted_data = k.encrypt(video_data)
    with open('rakan.mp4', 'wb') as file:
        file.write(encrypted_data)
    messagebox.showinfo("Encryption", f"{filepath}Video encrypted successfully!")
def process_data():
    plain_text = plaintext_entry.get()
    cipher_text=ciphertext_entry.get()
    algorithm = algorithm_var.get()
    if algorithm == "Caesar Cipher":
        encrypted_text = caesar_cipher_encrypt(plain_text,  7)
        messagebox.showinfo("Encrypted Text", encrypted_text)
        cipher_text1 = caesar_cipher_dicrption(cipher_text,7)
        messagebox.showinfo("Decription Text", cipher_text1)

    elif algorithm == "Reverse Cipher":
        encrypted_text = reverse_cipher_encrypt(plain_text)
        messagebox.showinfo("Encrypted Text", encrypted_text)
        d = reverse_cipher_Decrypt(cipher_text)
        messagebox.showinfo("Decription Text", d)
    elif algorithm == "Custom Algorithm":
        encrypted_text = custom_algorithm_encrypt(plain_text)
        messagebox.showinfo("Encrypted Text", encrypted_text)
    elif algorithm == "Transfer encrypt key":
         e= transfer_encrypt(plain_text)
         messagebox.showinfo("Encrypted Text", e)
         d = transfer_decrypt(cipher_text)
         messagebox.showinfo("Decription Text", d)
    elif algorithm == "Transfer encrypt not key":
         e = transfer_encrypt_not_key(plain_text)
         messagebox.showinfo("Encrypted Text", e)
         d = transfer_decrypt_not_key(cipher_text)
         messagebox.showinfo("Decription Text", d)
    elif algorithm == "Autokey":
         e = autokey_encrypt(plain_text)
         messagebox.showinfo("Encrypted Text", e)
         d = autokey_Decrypt(cipher_text)
         messagebox.showinfo("Decription Text", d)

    elif algorithm == "Vigenere":
         encrypted_text= vigenere_encrypt(plain_text)
         messagebox.showinfo("Encrypted Text", encrypted_text)
         Decrypted_text = vigenere_Decrypt(plain_text)
         messagebox.showinfo("Decrypted Text", Decrypted_text)

    elif algorithm == "Hashing":
        encrypted_text= hashing_encrypt(plain_text)
        messagebox.showinfo("Encrypted Text", encrypted_text)
    elif algorithm == "One-Time Pad":
        key = generate_random_key(len(plain_text))
        encrypted_text= one_time_pad_encrypt(plain_text, key)
        messagebox.showinfo("Encrypted Text", encrypted_text)

    elif algorithm == "Merge Encryption/Decryption":
        key = generate_random_key(len(plain_text))
        encrypted_text= merge_encrypt_decrypt(plain_text, key)
        messagebox.showinfo("Encrypted Text", encrypted_text)

    else:
        return " "
header = tk.Label(root, text="R ^_^ Welcome  Program The Encrption   ^_^ L", font=("Arial", 16),bg="black",fg="#330000")
header["font"]=fontstyl
header.pack(pady=15)
plaintext_label = tk.Label(root, text="Enter Plain Text:",bg='black',fg="#330000",font=("Georgia", 18,"bold italic"))
plaintext_label["font"]=fontstyle
plaintext_label.pack()
plaintext_entry = tk.Entry(root,font=("Arial", 12),bg='black',fg="#330000")
plaintext_entry["font"]=fontstyle
plaintext_entry.pack()

ciphertext_label = tk.Label(root, text="Cipher Text:",bg="black",fg="#330000",font=("Georgia", 18,"bold italic"))
ciphertext_label["font"]=fontstyle
ciphertext_label.pack()
ciphertext_entry = tk.Entry(root,font=("Arial", 12),bg='black',fg="#330000")
ciphertext_entry["font"]=fontstyle
ciphertext_entry.pack()
algorithm_label = tk.Label(root, text="Encription Algorithm:",bg="black",fg="#330000",font=("Georgia", 18,"bold italic"))
algorithm_label["font"]=fontstyle
algorithm_label.pack()

algorithm_var = tk.StringVar(root)
algorithm_var.set("Caesar Cipher")
Combobox = tk.OptionMenu(root, algorithm_var,*encryption_algorithms)

Combobox.config(width=14,height=1,bg="#330000",borderwidth=3,relief='solid',padx=20,pady=5,font=("Georgia", 12,"bold italic"))
Combobox["menu"].config(borderwidth=5)
Combobox.configure(highlightthickness=5)
Combobox["highlightbackground"]="black"
Combobox.pack(pady=10)

process_button = tk.Button(root, text="Encription && Decription", command=process_data,bg='black',fg="#330000",font=("Georgia", 16,"bold italic"))
process_button.pack()

btnImage = tk.Button(root, text="Encrypt Image", command=encrypt_image,bg='black',fg="#330000",font=("Georgia", 18,"bold italic"))
btnImage.pack(pady=10)

btnPDF = tk.Button(root, text="Encrypt PDF", command=encrypt_pdf,bg='black',fg="#330000",font=("Georgia", 18,"bold italic"))
btnPDF.pack(pady=10)

btnAudio = tk.Button(root, text="Encrypt Audio", command=encrypt_audio,bg='black',fg="#330000",font=("Georgia", 18,"bold italic"))
btnAudio.pack(pady=10)

btnVideo = tk.Button(root, text="Encrypt Video", command=encrypt_video,bg='black',fg="#330000",font=("Georgia", 18,"bold italic"))
btnVideo.pack(pady=10)

root.mainloop()



