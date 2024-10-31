"""                       """
""" SoundPad Protocol     """
"""            in Soundux """
"""                       """

import sys
import re
import json

# DearPyGui | UI | Addons 
import dearpygui.dearpygui as dpg  
import libs.dpg_animations as dpg_animations  
import libs.dpg_animator.dearpygui_animate as dpg_animator 
import libs.dpg_markdown as dpg_markdown  
import libs.dpg_theme as dpg_theme  
from libs.dpg_addons.cyr_support import init_font_with_cyr_support, to_cyr
from libs.dpg_markdown.setup import init_dpg_markdown
from libs.dpg_addons.dpg_blur import WindowsWindowEffect, get_hwnd, MARGINS   

# Python Libraries
from datetime import datetime    
import time as time    
from requests_html import HTMLSession # type: ignore
from fake_useragent import UserAgent # type: ignore 
import threading    
import shutil
import os
import tempfile
import subprocess
from tkinter import filedialog
import tkinter as tk
from tkinter import messagebox

is_unlocker_run = False
is_update_available = False
update_text = ""
temp_file_path = ""

dpg.create_context() 

def extract_url(url):
    pattern = r'soundpad://sound/url/(.+)'
    match = re.search(pattern, url)
    if match:
        return match.group(1)
    else:
        return None

is_url_extracted = False
extracted_url = ""

if __name__ == "__main__":
    if len(sys.argv) > 1:
        url = sys.argv[1]
        print(url)
        extracted_url = extract_url(url)
        if extracted_url:
            is_url_extracted = True
            
def load_data(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)

def find_value_by_name(data, name):
    for item in data:
        if item['name'] == name:
            return item['value']
    return None

def get_data_folder():
    if getattr(sys, 'frozen', False):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.dirname(os.path.abspath(__file__))
    data_folder_path = os.path.join(base_path, 'data')
    return data_folder_path

data = []
try:
    data = load_data(os.path.join(os.path.dirname(sys.executable), 'data.json'))
except:pass
version = '1'

def get_exe_directory():
    exe_path = sys.executable
    exe_dir = os.path.dirname(exe_path)
    return exe_dir

data_folder = get_data_folder()
window_effect = WindowsWindowEffect()
def close(): dpg.destroy_context(); sys.exit(0)
with dpg.font_registry() as font_registry:
  with dpg.font(os.path.join(data_folder,"Fonts","base.ttf"), 17) as default_font:
    dpg.add_font_range_hint(dpg.mvFontRangeHint_Default)
    dpg.add_font_range_hint(dpg.mvFontRangeHint_Cyrillic)
init_dpg_markdown(dpg,dpg_markdown,font_registry,  17 ,os.path.join(data_folder,"Fonts","base.ttf"),os.path.join(data_folder,"Fonts","bold.ttf"),os.path.join(data_folder,"Fonts","italic.ttf"),os.path.join(data_folder,"Fonts","bolditalic.ttf"))

is_menu_bar_clicked = False
    
def select_folder():
    root = tk.Tk()
    root.withdraw() 
    root.iconbitmap(os.path.join(data_folder,"logo","logo.ico")) 
    folder_path = filedialog.askdirectory()  
    dpg.set_value("Path-to-folder_input", folder_path)

def update_combo():
    file_path = "data.json"
    if os.path.exists(file_path):
        try:
            with open(file_path, 'r') as file:
                data = json.load(file)
        except:pass
        else:
            dpg.set_value("element_selector", "")
            dpg.configure_item("element_selector", items=[] if data is None else [item['name'] for item in data])

def add_element():
    global data
    file_path = "data.json"
    name = dpg.get_value("Name_input")
    value = dpg.get_value("Path-to-folder_input")
    if name == "":
        messagebox.showerror("SPP-IN-Soundux", "Error: The name is empty!")
        return
    if value == "":
        messagebox.showerror("SPP-IN-Soundux", "Error: The path-to-folder is empty!")
        return
    if os.path.exists(file_path):
        try:
            with open(file_path, 'r') as file:
                data = json.load(file)
        except:pass
    data.append({"name": name, "value": value})
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)
    update_combo()

def remove_element():
    global data
    file_path = "data.json"
    name = dpg.get_value("element_selector")
    data = []
    if os.path.exists(file_path):
        try:
            with open(file_path, 'r') as file:
                data = json.load(file)
        except:pass
    data = [item for item in data if item['name'] != name]
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)
    update_combo()
 
def mouse_drag_callback(_, app_data):
    if is_menu_bar_clicked:
        _, drag_delta_x, drag_delta_y = app_data
        viewport_pos_x, viewport_pos_y = dpg.get_viewport_pos()
        new_pos_x = viewport_pos_x + drag_delta_x
        new_pos_y = viewport_pos_y + drag_delta_y
        dpg.set_viewport_pos([new_pos_x, new_pos_y])
def mouse_click_callback():
    global is_menu_bar_clicked
    mouse_pos_temp = dpg.get_mouse_pos(local=False)
    if mouse_pos_temp[1] < 35 and mouse_pos_temp[0] <= 370:is_menu_bar_clicked = True   
    else: is_menu_bar_clicked = False   
with dpg.handler_registry():
    dpg.add_mouse_drag_handler(button=0, threshold=0, callback=mouse_drag_callback)
    dpg.add_mouse_click_handler(button=0, callback=mouse_click_callback)
def move_viewport_to_desktop():
    dpg.set_viewport_pos([100, 10])

script_path = os.path.abspath(__file__)
reg_path = r"Soundpad"
current_path = os.path.abspath(__file__)
new_path = os.path.join(os.path.dirname(current_path), "tools.exe")
exe_dir = os.path.join(os.path.dirname(sys.executable), os.path.basename(sys.executable))

def check_and_modify_registry():
    if os.path.isfile(new_path):
        program_path = new_path
        parameters = ["check", f"\"{exe_dir}\""]
        subprocess.run([program_path] + parameters)
    else:
        print(True)
        root = tk.Tk()
        root.withdraw() 
        messagebox.showerror("SPP-IN-Soundux", "Error: SPP-IN-Soundux Tool (tools.exe) not found!\nReinstall SPP-IN-Soundux!")
        root.destroy()

def check_registry():
    if os.path.isfile(new_path):
        program_path = new_path
        parameters = ["test", f"\"{exe_dir}\""]
        subprocess.run([program_path] + parameters)
    else:
        root = tk.Tk()
        root.withdraw() 
        messagebox.showerror("SPP-IN-Soundux", "Error: SPP-IN-Soundux Tool (tools.exe) not found!\nReinstall SPP-IN-Soundux!")
        root.destroy()

def unsetup_registry():
    if os.path.isfile(new_path):
        program_path = new_path
        parameters = ["unsetup", f"\"{exe_dir}\""]
        subprocess.run([program_path] + parameters)
    else:
        root = tk.Tk()
        root.withdraw() 
        messagebox.showerror("SPP-IN-Soundux", "Error: SPP-IN-Soundux Tool (tools.exe) not found!\nReinstall SPP-IN-Soundux!")
        root.destroy()

def download_file(url):
    global temp_file_path
    file_extension = os.path.splitext(url)[-1]
    temp_dir = tempfile.gettempdir()
    temp_file_path = os.path.join(temp_dir, f"temp_file_from_spp-in-soundux{file_extension}")
    session = HTMLSession()
    ua = UserAgent()
    headers = {'User-Agent': ua.random}
    response = session.get(url, headers=headers, stream=True)
    file_size = int(response.headers.get('Content-Length', 0))
    chunk_size = 1024
    downloaded_size = 0

    with open(temp_file_path, 'wb') as file:
        for chunk in response.iter_content(chunk_size=chunk_size):
            if chunk:
                file.write(chunk)
                downloaded_size += len(chunk)
                progress = downloaded_size / file_size
                dpg.set_value("progress_bar", progress)

    dpg.enable_item("save_soundux")
    return temp_file_path

def move_file_to_destination(temp_file_path, dest_folder, new_name=None):
    os.makedirs(dest_folder, exist_ok=True)
    file_extension = os.path.splitext(temp_file_path)[-1]
    destination_path = os.path.join(dest_folder, (new_name or "downloaded_file") + file_extension)
    shutil.move(temp_file_path, destination_path)

def soundux_button():
    
    file_name = to_cyr(dpg.get_value("select_name"))
    file_path = find_value_by_name(data, dpg.get_value("select_folder"))
    move_file_to_destination(temp_file_path, file_path, file_name)
    close()
    
def soundpad_button():
    with open('cfg.json', 'r') as config_file:
        config = json.load(config_file)
    program_path = config["SoundPad_Path"]
    if program_path == "user_dont_have_soundpad":
        messagebox.showerror("SPP-IN-Soundux", "Error: не удалось найти SoundPad или до установки плагина SoundPad не был установлен!")
    parameters = ["-c", extracted_url]
    subprocess.run([program_path] + parameters)

def _help(message):
    last_item = dpg.last_item()
    group = dpg.add_group(horizontal=True)
    dpg.move_item(last_item, parent=group)
    dpg.capture_next_item(lambda s: dpg.move_item(s, parent=group))
    t = dpg.add_text("[i]", color=[255, 255, 255])
    with dpg.tooltip(t):
        dpg.add_text(message)
def Init_Before_UI_Init(): 
    window_effect.setRoundedCorners(get_hwnd(), 10)
    input_font = init_font_with_cyr_support(dpg=dpg, font_path=os.path.join(data_folder,"Fonts","base.ttf"), font_registry=font_registry) 
    if is_url_extracted:
        download_thread = threading.Thread(target=download_file, args=(extracted_url,))
        download_thread.start()

lw,lh,lc,ld = dpg.load_image(os.path.join(data_folder,"assets","soundux.png"))
dw,dh,dc,dd = dpg.load_image(os.path.join(data_folder,"assets","soundpad.png"))
with dpg.texture_registry(show=False):
    dpg.add_static_texture(width=lw, height=lh, default_value=ld, tag="soundux")
    dpg.add_static_texture(width=dw, height=dh, default_value=dd, tag="soundpad")
with dpg.theme() as transparent_button_for_text_in_center:
        with dpg.theme_component():
            dpg.add_theme_color(dpg.mvThemeCol_Button, [0, 0, 0, 0])
            dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, [0, 0, 0, 0])
            dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, [0, 0, 0, 0])
with dpg.theme() as border_with_transparent_button_for_text_element:
        with dpg.theme_component():
            dpg.add_theme_style(dpg.mvStyleVar_FrameBorderSize, 1, category=dpg.mvThemeCat_Core)
            dpg.add_theme_color(dpg.mvThemeCol_Button, [11,11,11,90])
            dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, [11,11,11,90])
            dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, [11,11,11,90])
with dpg.theme() as main_button:
        with dpg.theme_component():
            dpg.add_theme_color(dpg.mvThemeCol_Button, [63, 136, 108, 255])
            dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, [80, 174, 138, 255])
            dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, [90, 184, 148, 255])
with dpg.theme() as second_button:
        with dpg.theme_component():
            dpg.add_theme_color(dpg.mvThemeCol_Button, [137, 30, 30, 255])
            dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, [154, 68, 60, 255])
            dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, [164, 78, 70, 255])
with dpg.theme() as progress_bar:
        with dpg.theme_component():
            dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 0, category=dpg.mvThemeCat_Core)
            dpg.add_theme_color(dpg.mvThemeCol_FrameBg, [11,11,11,11])
            dpg.add_theme_color(dpg.mvThemeCol_PlotHistogram, [99,99,99,130])
with dpg.theme() as close_button:
        with dpg.theme_component():
            dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 0, category=dpg.mvThemeCat_Core)
            dpg.add_theme_color(dpg.mvThemeCol_Button, [99,99,99,130])
            dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, [154, 68, 60,130])
            dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, [164, 78, 70,130])
with dpg.theme() as transparent_child_window:
        with dpg.theme_component():
            dpg.add_theme_color(dpg.mvThemeCol_ChildBg, [0,0,0,0])
with dpg.theme() as border_to_element:
        with dpg.theme_component():
            dpg.add_theme_style(dpg.mvStyleVar_FrameBorderSize, 1, category=dpg.mvThemeCat_Core)

link_for = extracted_url.replace("https://", "")
link_for_program = link_for.replace("http://", "")
name = extracted_url.replace("%20", " ")
name_for = name.rsplit('/', 1)[-1]
name_for_file = name_for.split('.')[0]
if is_url_extracted:
    with dpg.window(width=410, height=179, pos=(-5,0), no_title_bar=True, no_move=True, no_resize=True, tag="protocol"):
        
        with dpg.child_window(pos=(0,0),height=35,width=410, tag="nav_bar", no_scroll_with_mouse=True, no_scrollbar=True):
            dpg.bind_item_theme(dpg.last_item(), transparent_child_window)
            dpg.add_progress_bar(default_value=1, width=365, height=35, pos=(5,0), tag="progress_bar"); dpg.bind_item_theme("progress_bar", progress_bar)
            dpg.add_button(label="",width=35, height=35, pos=(370,0), callback=close); dpg.bind_item_theme(dpg.last_item(), close_button)
            dpg.add_text("x", pos=(383, 5))
            pass
        
        dpg.add_input_text(enabled=False, default_value=f"{link_for_program}", width=383, pos=(13,43))
        dpg.add_input_text(default_value=f"{name_for_file}", width=383, pos=(13,74), tag="select_name")
        dpg.add_combo([item['name'] for item in data],default_value=1, width=384, pos=(13,105), tag="select_folder")
        dpg.set_value("select_folder", "-")
        dpg.add_button(label="", width=35, height=35, pos=(13,136),callback=soundpad_button); dpg.bind_item_theme(dpg.last_item(), second_button)
        dpg.add_image("soundpad", width=25, height=25 , pos=(18,141))
        dpg.add_button(label="", width=342, height=35, pos=(55,136), tag="save_soundux", enabled=False, callback=soundux_button); dpg.bind_item_theme(dpg.last_item(), main_button)
        dpg.add_text("save to soundux", pos=(165,141))
        dpg.add_image("soundux", width=25, height=25 , pos=(60,141))
else:
    with dpg.window(width=410, height=179, pos=(-5,0), no_title_bar=True, no_move=True, no_resize=True, no_scroll_with_mouse=True, no_scrollbar=True):
        
        with dpg.child_window(pos=(0,0),height=35,width=410, tag="nav_bar", no_scroll_with_mouse=True, no_scrollbar=True):
            dpg.bind_item_theme(dpg.last_item(), transparent_child_window)
            dpg.add_progress_bar(default_value=1, width=365, height=35, pos=(5,0), tag="progress_bar"); dpg.bind_item_theme("progress_bar", progress_bar)
            dpg.add_button(label="",width=35, height=35, pos=(370,0), callback=close); dpg.bind_item_theme(dpg.last_item(), close_button)
            dpg.add_text("x", pos=(383, 5))
            pass
        
        dpg.add_text(""" SPP-IN-Soundux""", pos=(9,6))
        dpg_markdown.add_text("""<font size=10 color="(155, 155, 155)">by Agzes</font>""", pos=(133,4))
        
        dpg.add_combo([] if data is None else [item['name'] for item in data], tag="element_selector", width=300, pos=(13,45))
        dpg.add_button(label="Delete", width=79, pos=(319,45),callback=remove_element)
        
        dpg.add_input_text(hint="Name", pos=(13,75), tag="Name_input", width=300)
        dpg.add_input_text(hint="C:/Path/To/Folder", tag="Path-to-folder_input", pos=(13,105), width=345)
        dpg.add_button(label="[/]", pos=(364,105), callback=select_folder)
        dpg.add_button(label="Add", width=79, pos=(319,75), callback=add_element)
        
        with dpg.child_window(pos=(0,139),height=35,width=410, no_scroll_with_mouse=True, no_scrollbar=True): 
            dpg.add_separator()
            
            t = dpg.add_button(label="Check Plugin", callback=check_registry, pos=(12,8))
            with dpg.tooltip(t):
                dpg.add_text("[!] Administrator rights are required [!]", color=(134, 27, 45))
            t = dpg.add_button(label="Setup/Fix Plugin", callback=check_and_modify_registry, width=146, pos=(124,8))
            with dpg.tooltip(t):
                dpg.add_text("[!] Administrator rights are required [!]", color=(134, 27, 45))
            t = dpg.add_button(label="UnSetup Plugin", callback=unsetup_registry, pos=(276,8))
            with dpg.tooltip(t):
                dpg.add_text("[!] Administrator rights are required [!]", color=(134, 27, 45))
            
        
            

           
        
    
    

dpg.bind_theme(dpg_theme.initialize())
dpg.bind_font(default_font)
dpg.set_frame_callback(5, Init_Before_UI_Init)
icon_path = os.path.join(data_folder,"logo","logo.ico")
dpg.create_viewport(title="SPP-IN-Soundux", width=400, height=179, large_icon=icon_path, small_icon=icon_path, decorated=False, resizable=False, clear_color=[0, 0, 0, 0]) 
dpg.setup_dearpygui() 
dpg.show_viewport() 
program_start = datetime.now() 
dpg_animator.run() 
dpg_animations.update() 
while dpg.is_dearpygui_running():
    dpg_animator.run() 
    dpg_animations.update() 
    dpg.render_dearpygui_frame()  
dpg.destroy_context()
