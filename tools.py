"""                       """
""" SoundPad Protocol     """
"""            in Soundux """
"""                       """

"""      TOOLS V1         """


import winreg
import json
import sys
import os
import ctypes
import subprocess

class messagebox():
    def showinfo(title, text):
        return ctypes.windll.user32.MessageBoxW(0, text, title, 0x40)
    def showerror(title, text):
        return ctypes.windll.user32.MessageBoxW(0, text, title, 0x10)
    def showsuccessfully(title, text):
        return ctypes.windll.user32.MessageBoxW(0, text, title, 0x40)

data = ""
for i in range(len(sys.argv)):
    if sys.argv[i] == 'check' or sys.argv[i] == 'unsetup' or sys.argv[i] == 'test':
        data = sys.argv[i] 
        script_path = sys.argv[i+1]
if data == "":
    messagebox.showinfo("SPP-IN-Soundux Tool", "SPP-IN-Soundux Tool v.1.0\nPath of SPP-IN-Soundux\n\nNeed for setup/fix/unsetup SPP-IN-Soundux\n\nYou can find source of this file in:\nhttps://github.com/Agzes/SPP-IN-Soundux")
    sys.exit()
    
def load_data(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)
    
reg_path = r"Soundpad"

def delete_registry_key():
    key_path = r"HKEY_CLASSES_ROOT\Soundpad"
    try:
        result = subprocess.run(
            ["reg", "delete", key_path, "/f"],
            capture_output=True, 
            text=True            
        )
        if result.returncode == 0:
            return 0
        else:
            return result.stderr
    except Exception as e:
        return e

def check_and_modify_registry():
    if sys.maxsize > 2**32: 
        reg_access = winreg.KEY_WOW64_64KEY
    else:  
        reg_access = winreg.KEY_WOW64_32KEY

    try:
        
        try:
            with winreg.OpenKey(winreg.HKEY_CLASSES_ROOT, reg_path, 0, reg_access | winreg.KEY_ALL_ACCESS) as key:
                winreg.SetValue(key, None, winreg.REG_SZ, "SPP-IN-Soundux")
        except FileNotFoundError:
            with winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, reg_path) as key:
                winreg.SetValue(key, None, winreg.REG_SZ, "SPP-IN-Soundux")
        
        
        status = delete_registry_key()
        print(status)
        if status == 0:
            pass
        else:
            raise ValueError(status)
        
        
        try:
            with winreg.OpenKey(winreg.HKEY_CLASSES_ROOT, reg_path, 0, reg_access | winreg.KEY_ALL_ACCESS) as key:
                winreg.SetValue(key, None, winreg.REG_SZ, "SPP-IN-Soundux")
        except FileNotFoundError:
            with winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, reg_path) as key:
                winreg.SetValue(key, None, winreg.REG_SZ, "SPP-IN-Soundux")
        
        try:
            icon_key_path = r"Soundpad\DefaultIcon"
            with winreg.OpenKey(winreg.HKEY_CLASSES_ROOT, icon_key_path, 0, reg_access | winreg.KEY_ALL_ACCESS) as icon_key:
                winreg.SetValue(icon_key, None, winreg.REG_SZ, f"\"{script_path}\",0")
        except FileNotFoundError:
            with winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, icon_key_path) as icon_key:
                winreg.SetValue(icon_key, None, winreg.REG_SZ, f"\"{script_path}\",0")

        
        try:
            command_key_path = r"Soundpad\shell\open\command"
            with winreg.OpenKey(winreg.HKEY_CLASSES_ROOT, command_key_path, 0, reg_access | winreg.KEY_ALL_ACCESS) as command_key:
                default_command = winreg.QueryValueEx(command_key, None)[0]
                if '-c' in default_command:
                    path_before_s = default_command.split(' -c')[0]
                    new_command = f"\"{script_path}\" \"%1\""
                    try:
                        temp_data = load_data('output.json')
                        if temp_data['SoundPad_Path']:pass
                    except:
                        json_data = {"WARNING": "DON'T DELETE THIS FILE! PATH OF FUNCTION SPP-IN-SOUNDUX", "SoundPad_Path": path_before_s}
                        with open('cfg.json', 'w') as json_file:
                            json.dump(json_data, json_file)
                    winreg.SetValue(command_key, None, winreg.REG_SZ, new_command)
        except FileNotFoundError:
            with winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, command_key_path) as command_key:
                new_command = f"\"{script_path}\" \"%1\""
                winreg.SetValue(command_key, None, winreg.REG_SZ, new_command)
                json_data = {"WARNING": "DON'T DELETE THIS FILE! PATH OF FUNCTION SPP-IN-SOUNDUX", "SoundPad_Path": "user_dont_have_soundpad"}
                with open('cfg.json', 'w') as json_file:
                    json.dump(json_data, json_file)
                   
                    
        try:
            with winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, reg_path) as key:
                winreg.SetValueEx(key, "URL Protocol", 0, winreg.REG_SZ, "")
        except: pass
    except Exception as e:
        if isinstance(e, OSError) and e.winerror == 5:
            pass
        else:
            messagebox.showerror("SPP-IN-Soundux Tool", f"An error occurred: {str(e)}")
    else:
        messagebox.showsuccessfully("SPP-IN-Soundux Tool", "SPP-IN-Soundux successfully tuned!")

def unsetup_registry():
    temp_data = load_data('output.json')
    script_path = temp_data["SoundPad_Path"]
    if sys.maxsize > 2**32: 
        reg_access = winreg.KEY_WOW64_64KEY
    else:  
        reg_access = winreg.KEY_WOW64_32KEY
    
    
    
    try:
        
        try:
            with winreg.OpenKey(winreg.HKEY_CLASSES_ROOT, reg_path, 0, reg_access | winreg.KEY_ALL_ACCESS) as key:
                winreg.SetValue(key, None, winreg.REG_SZ, "SPP-IN-Soundux")
        except FileNotFoundError:
            with winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, reg_path) as key:
                winreg.SetValue(key, None, winreg.REG_SZ, "SPP-IN-Soundux")
        
        status = delete_registry_key()
        if status == 0:
            pass
        else:
            raise ValueError(status)
            
        temp_data = load_data('output.json')
        if temp_data['SoundPad_Path'] == "user_dont_have_soundpad": raise ValueError(0)
        
  
        try:
            with winreg.OpenKey(winreg.HKEY_CLASSES_ROOT, reg_path, 0, reg_access | winreg.KEY_ALL_ACCESS) as key:
                winreg.SetValue(key, None, winreg.REG_SZ, "URL:Soundpad Protocol")  
        except FileNotFoundError:
            with winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, reg_path) as key:
                winreg.SetValue(key, None, winreg.REG_SZ, "URL:Soundpad Protocol")
        
        try:
            with winreg.OpenKey(winreg.HKEY_CLASSES_ROOT, reg_path, 0, reg_access | winreg.KEY_ALL_ACCESS) as key: 
                pass
        except: 
            with winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, reg_path) as key:
                winreg.SetValueEx(key, "URL Protocol", 0, winreg.REG_SZ, "")
            
        
        icon_key_path = r"Soundpad\DefaultIcon"
        try:
            with winreg.OpenKey(winreg.HKEY_CLASSES_ROOT, icon_key_path, 0, reg_access | winreg.KEY_ALL_ACCESS) as icon_key:
                winreg.SetValue(icon_key, None, winreg.REG_SZ, f"\"{script_path}\",0")
        except FileNotFoundError:
            with winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, icon_key_path) as icon_key:
                winreg.SetValue(icon_key, None, winreg.REG_SZ, f"\"{script_path}\",0")

        
        shell_key_path = r"Soundpad\shell"
        
        
        
        
        
        
        
        command_key_path = r"Soundpad\shell\open\command"
        try:
            with winreg.OpenKey(winreg.HKEY_CLASSES_ROOT, command_key_path, 0, reg_access | winreg.KEY_ALL_ACCESS) as command_key:
                default_command = winreg.QueryValueEx(command_key, None)[0]
                if '-c' in default_command:
                    path_before_s = default_command.split(' -c')[0]
                    new_command = f"\"{script_path}\" -c \"%1\""
                    json_data = {"WARNING": "DON'T DELETE THIS FILE! PATH OF FUNCTION SPP-IN-SOUNDUX!", "SoundPad_Path": path_before_s}
                    with open('cfg.json', 'w') as json_file:
                        json.dump(json_data, json_file)
                    winreg.SetValue(command_key, None, winreg.REG_SZ, new_command)
                    
                    
                else:
                    json_data = {"WARNING": "DON'T DELETE THIS FILE! PATH OF FUNCTION SPP-IN-SOUNDUX", "SoundPad_Path": "user_dont_have_soundpad"}
                    with open('cfg.json', 'w') as json_file:
                        json.dump(json_data, json_file)
                        
                        
        except FileNotFoundError:
            with winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, command_key_path) as command_key:
                new_command = f"\"{script_path}\" -c \"%1\""
                winreg.SetValue(command_key, None, winreg.REG_SZ, new_command)
                json_data = {"WARNING": "DON'T DELETE THIS FILE! PATH OF FUNCTION SPP-IN-SOUNDUX", "SoundPad_Path": "user_dont_have_soundpad"}
                with open('cfg.json', 'w') as json_file:
                    json.dump(json_data, json_file)
    except Exception as e:
        if str(e) == "0": 
            messagebox.showsuccessfully("SPP-IN-Soundux", "SPP-IN-Soundux successfully unsetup!")   
        else: 
             messagebox.showerror("SPP-IN-Soundux", f"An error occurred: {str(e)}")
    else:messagebox.showsuccessfully("SPP-IN-Soundux", "SPP-IN-Soundux successfully unsetup!")

def check():
    if sys.maxsize > 2**32: 
        reg_access = winreg.KEY_WOW64_64KEY
    else:  
        reg_access = winreg.KEY_WOW64_32KEY
    
    is_checked = False
    
    try:
        try:
            with winreg.OpenKey(winreg.HKEY_CLASSES_ROOT, reg_path, 0, reg_access | winreg.KEY_ALL_ACCESS) as key:
                value, _ = winreg.QueryValueEx(key, None)
                if value == "SPP-IN-Soundux":
                    pass
                else: is_checked = True
        except FileNotFoundError:is_checked = True
            
        icon_key_path = r"Soundpad\DefaultIcon"
        try:
            with winreg.OpenKey(winreg.HKEY_CLASSES_ROOT, icon_key_path, 0, reg_access | winreg.KEY_ALL_ACCESS) as icon_key:
                icon_value, _ = winreg.QueryValueEx(icon_key, None)
                if icon_value == f"\"{script_path}\",0":
                    pass
                else: is_checked = True
        except FileNotFoundError:is_checked = True

        command_key_path = r"Soundpad\shell\open\command"
        try:
            with winreg.OpenKey(winreg.HKEY_CLASSES_ROOT, command_key_path, 0, reg_access | winreg.KEY_ALL_ACCESS) as command_key:
                command_value, _ = winreg.QueryValueEx(command_key, None)
                if command_value == f"\"{script_path}\" \"%1\"":
                    pass
                else: is_checked = True
        except FileNotFoundError:is_checked = True
        
        try:
            with winreg.OpenKey(winreg.HKEY_CLASSES_ROOT, reg_path, 0, reg_access | winreg.KEY_ALL_ACCESS) as key:
                url_protocol, _ = winreg.QueryValueEx(key, "URL Protocol")
        except FileNotFoundError:is_checked = True

    except Exception as e:
        if isinstance(e, OSError) and e.winerror == 5:
            messagebox.showsuccessfully("SPP-IN-Soundux Tool", "SPP-IN-Soundux setup!\n")
        else:
            messagebox.showerror("SPP-IN-Soundux Tool", "SPP-IN-Soundux not setup :(\nClick to Setup/Fix button to fix!\nError: {e}")
    else:
        if is_checked:
            messagebox.showerror("SPP-IN-Soundux Tool", "SPP-IN-Soundux not setup :(\nClick to Setup/Fix button to fix!")
        else:
            messagebox.showsuccessfully("SPP-IN-Soundux Tool", "SPP-IN-Soundux setup!")

if data == "check":
    if ctypes.windll.shell32.IsUserAnAdmin():
       check_and_modify_registry()
    else:
       ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
if data == "unsetup":
    if ctypes.windll.shell32.IsUserAnAdmin():
        unsetup_registry()
    else:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
if data == "test":
    if ctypes.windll.shell32.IsUserAnAdmin():
        check()
    else:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
