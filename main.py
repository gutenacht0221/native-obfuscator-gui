import os, requests, tkinter, tkinter.filedialog, customtkinter as ctk, shutil, threading, zipfile, plyer
from tkinter import *

window = ctk.CTk()
window.title('Native Obfuscator GUI')
window.geometry("750x500")
window.set_appearance_mode("dark")
ctk.set_default_color_theme("green")
window.resizable(False, False)

cwd = os.getcwd()
filename = ""
files = ["https://cdn.discordapp.com/attachments/1052369601259909251/1052369737067274280/native.jar"]

def no_file_selected():
    plyer.notification.notify(
        title = 'No File Selected',
        message = 'Please select a file to obfuscate.',
        app_icon = None,
        timeout = 3,
    )

def notify(started):
    if started:
        plyer.notification.notify(
            title = 'Started Obfuscating',
            message = 'Your file is being obfuscated, please wait a little while.',
            app_icon = None,
            timeout = 3,
        )
    else:
        plyer.notification.notify(
            title = 'Finished Obfuscating',
            message = 'Your file has been obfuscated, you can find it in the output folder.',
            app_icon = None,
            timeout = 3,
        )

def SetupFolder():
    for url in files:
        r = requests.get(url)
        name = url.split("/")[-1]
        try:
            with open(f'{cwd}\\Native\\{name}', 'wb') as f:
                    f.write(r.content)
        except:
            print("Error Downloading File")

def CreateFolder():
    if not os.path.exists(f'{cwd}\\Native'):
        os.makedirs(f'{cwd}\\Native')
    SetupFolder()

def init():
    if not os.path.exists(f'{cwd}\\Native\\out'):
        os.makedirs(f'{cwd}\\Native\\out')
    if not os.path.exists(f'{cwd}\\Native'):
        os.makedirs(f'{cwd}\\Native\\out\\cpp\\out\\cpp')

def browseFiles():
    global filename
    filename = tkinter.filedialog.askopenfilename(initialdir="/", title="Select a File", filetypes=(("Java Files", "*.jar"), ("All Files", "*.*")))
    print(filename)
    init()

def Finish():
    shutil.rmtree(f"{cwd}\\Native\\out")
    print("Done")

def StartObfuscating():
    threading.Thread(target=obfuscate).start()

def obfuscate():
    notify(True)
    if (filename == ""):
        no_file_selected()
        return
    name = filename.split("/")[-1]
    os.system(f'java -jar "{cwd}\\Native\\native.jar" "{filename}" Native\\out')
    os.chdir("Native\\out\\cpp")
    os.system("cmake .")
    os.system("cmake --build . --config release")
    os.chdir(f"{cwd}\\Native\\out\\cpp\\build\\lib")
    shutil.copy("native_library.dll", "x64-windows.dll")
    shutil.copy("native_library.dll", "x86-windows.dll")
    shutil.copy("native_library.dll", "x64-macos.dylib")
    os.chdir(cwd)

    x64macos = f"{cwd}\\Native\\out\\cpp\\build\\lib\\x64-macos.dylib"
    x64windows = f"{cwd}\\Native\\out\\cpp\\build\\lib\\x64-windows.dll"
    x86windows = f"{cwd}\\Native\\out\\cpp\\build\\lib\\x86-windows.dll"

    with zipfile.ZipFile(f"{cwd}\\Native\\out\\{name}", "a") as jar:
        jar.write(x64macos, "native0/x64-macos.dylib")
        jar.write(x64windows, "native0/x64-windows.dll")
        jar.write(x86windows, "native0/x86-windows.dll")

    if not os.path.exists(f"{cwd}\\output"):
        os.mkdir(f"{cwd}\\output")
    shutil.move(f"{cwd}\\Native\\out\\{name}", f"{cwd}\\output\\{name}")
    Finish()
    notify(False)

CreateFolder()
      
button_explore = ctk.CTkButton(window, text = "Browse Files 📦", command = browseFiles)
  
button_explore.place(relx=0.5, rely=0.1, anchor=CENTER)

obfuscate_button = ctk.CTkButton(window, text="Obfuscate 😍", command=StartObfuscating)
obfuscate_button.place(relx=0.5, rely=0.2, anchor=CENTER)

github_button = ctk.CTkButton(window, text="Github", command=lambda: os.system("start chrome.exe https://github.com/radioegor146/native-obfuscator"))
github_button.place(relx=0.5, rely=0.6, anchor=CENTER)

window.mainloop()