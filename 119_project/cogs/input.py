# import themed tkinter, for nicer layout and import tkinter module (for window elements and customization)
import tkinter as tk
# for tkinter image display
from PIL import Image, ImageTk
import cogs.artist as artist_cog
import json
import random as ra

# NOTE(s):
# - Parts of this code have been copied and put here (from the cited source) for convenience.
# - Any tkinter reference to the function .place() means it will actually place with relative x and y positions on the screen.
# - Every function in all program files are equipped with docstrings to better inform the readers and other developers of the function's purpose and use.

# Example Docstring
'''
Desc: description of function
Args: argument; description of argument, argument 2...
Returns: any returned values; most cases None
'''

def rgb_to_hex(rgb_tuple):
  '''
  Desc: Converts a tuple of RGB values to a hexadecimal color code.
  Args: The rgb tuple of color.
  Returns: A usable hex code.
  '''
  return "#%02x%02x%02x" % rgb_tuple

def replace_json_line(key, value):
  '''
  Desc: Saves the given value to its specific key-value pair. 
  Args: Key (reference to the json-key), Value (reference to the value to be saved)
  Returns: None
  '''

  # opening the json file as a readable data structure
  ####################################################################################

  # EDIT THIS FILE PATH

  ####################################################################################
  with open("cogs/var.json", "r") as json_file:
    data=json.load(json_file)
    data[key]=value

  # saving the json file as a writable data structure
  ####################################################################################

  # EDIT THIS FILE PATH

  ####################################################################################
  with open("cogs/var.json", "w") as json_file:
    json.dump(data, json_file)

def reset_json_values():
  '''
  Desc: Resets all values of the json file to a default at the beginning of each run of the program
  Args: key; the key to be reset, value; the value to be reset
  Returns: None
  '''
  replace_json_line("color", 1)
  replace_json_line("school", "Dublin High")
  replace_json_line("ghost_num", 1)
  replace_json_line("ghost_facial_exp", "Happy")
  replace_json_line("pumpkin_facial_exp", "Happy")
  replace_json_line("tombstone", "Aahil Shaikh")

def window_resizer(root_name):
  '''
  Desc: Resizes the current window to the size of the canvas 
  Args: root_name (name of the current root/window)
  Returns: None
  '''
  width, height = root_name.winfo_screenwidth(), root_name.winfo_screenheight()
  root_name.geometry('%dx%d+0+0' % (width,height))

# Colorscheme class, works with the users input for colors of choice.
class Colors:
  # initializing class and its subsidiary functions.
  def __init__(self):
    pass
    
  def color_setup(self):
    '''
    Desc: Creates window displaying options for Color Scheme attributes/configuration, in this case only Type.
    Args: None
    Returns: None 
    '''
    # creates tkinter root, title, geometry, and background color.
    color_root = tk.Tk()
    color_root.title("Color Configuration")
    window_resizer(color_root)
    color_root.config(bg=rgb_to_hex((ra.randint(0,255), ra.randint(0,255), ra.randint(0,255))))
    # creates and configs the main window size, title, options, bg color.
    tk.Label(color_root, text="Which attribute you would like to edit?\n\nWhen you click, it saves automatically, eliminating the need\nto worry about whether it's saved or not.",font=("Rockwell 14"), padx=20, pady=20).place(relx=0.5, rely=0.15, anchor="center")
    tk.Button(color_root,
              text="Color Scheme Selection",
              font=("Rockwell 14"),
              command=lambda: [color_root.destroy(),
                               self.color_choice()]
              ).place(rely=0.3, relx=0.5, anchor="center")
    tk.Button(
      color_root,
      text="Back 🔙",
      font=("Rockwell 14"),
      command=lambda: [color_root.destroy(), color_root.quit(), start()]
      ).place(rely=0.4, relx=0.5, anchor="center")
    color_root.mainloop()

  def color_choice(self):
    '''
    Desc: Gets a name text entry from the user to display as the school's name.
    Args: None
    Returns: None
    '''

    def save_and_back():
      '''
      Desc: Saves the users input and then closes the current name() window and goes back to the previous (setup())
      Args: None
      Returns: None
      '''
      name_root.destroy()
      self.color_setup()

    # creates and configs the main window size, title, options, bg color.
    name_root = tk.Toplevel()
    name_root.title("Color Scheme Options")
    window_resizer(name_root)
    name_root.config(bg=rgb_to_hex((ra.randint(0,255), ra.randint(0,255), ra.randint(0,255))))
    global photo1, photo2
    # Load and display the first image

  ####################################################################################

  # EDIT THESE 2 FILE PATHS

  ####################################################################################
    image1 = Image.open("cogs/images/color1.png")
    photo1 = ImageTk.PhotoImage(image1)
  
    image2 = Image.open("cogs/images/color2.png")
    photo2 = ImageTk.PhotoImage(image2)
    
    def on_button_click(x):
      replace_json_line("color", x)

    tk.Label(name_root,
             text="Color Scheme 1:",
             font=('Rockwell 14'),
             padx=20,
             ).place(relx=0.5, rely=0.1, anchor="center")

    tk.Label(name_root, image=photo1).place(relx=0.5,
                                            rely=0.2,
                                            anchor="center")
    tk.Button(name_root,
      text="1",
      font=("Rockwell 14"),
      command=lambda: on_button_click(1),
      ).place(relx=0.5, rely=0.3, anchor="center")

    # Load and display the second image
    tk.Label(name_root,
             text="Color Scheme 2:",
             font=('Rockwell 14'),
             padx=20,
             ).place(relx=0.5, rely=0.4, anchor="center")

    tk.Label(name_root, image=photo2).place(relx=0.5,
                                            rely=0.5,
                                            anchor="center")
    tk.Button(name_root,
      text="2",
      font=("Rockwell 14"),
      command=lambda: on_button_click(2),
      ).place(relx=0.5, rely=0.6, anchor="center")
    
      
    tk.Button(name_root,
              text="Save and Back",
              font=("Rockwell 14"),
              command=save_and_back,
              ).place(relx=0.5, rely=0.7, anchor="center")

class School:
  # initializing variables
  def __init__(self):
    pass

  def school_setup(self):
    '''
    Desc: Creates window displaying options for School attributes/configuration, in this case only Name.
    Args: None
    Returns: None 
    '''
    # creates tkinter root
    school_setup_root = tk.Tk()
    school_setup_root.title("School Configuration")
    window_resizer(school_setup_root)
    school_setup_root.config(bg=rgb_to_hex((ra.randint(0,255), ra.randint(0,255), ra.randint(0,255))))
    # creates and configs the main window size, title, options, bg color.
    tk.Label(school_setup_root, text="Which attribute you would like to edit?\n\nWhen you click, it saves automatically, eliminating the need\nto worry about whether it's saved or not.",font=("Rockwell 14"), padx=20, pady=20).place(relx=0.5, rely=0.15, anchor="center")
    tk.Button(
      school_setup_root,
      text="Name of School",
      font=("Rockwell 14"),
      command=lambda: [school_setup_root.destroy(),
                       self.name_choice()]
      ).place(relx=0.5, rely=0.3, anchor="center")
    tk.Button(school_setup_root,
              text="Back 🔙",
              font=("Rockwell 14"),
              command=lambda: [school_setup_root.destroy(),
                               start()]
              ).place(relx=0.5, rely=0.4, anchor="center")
    school_setup_root.mainloop()

  def name_choice(self):
    '''
    Desc: Gets a name text entry from the user to display as the school's name.
    Args: None
    Returns: None
    '''

    def save_and_back():
      '''
      Desc: Saves the users input and then closes the current name() window and goes back to the previous (setup())
      Args: None
      Returns: None
      '''
      replace_json_line("school", f"{school_name_entry.get()}")
      name_root.destroy()
      self.school_setup()

    # creates and configs the main window size, title, options, bg color.
    name_root = tk.Tk()
    name_root.title("School Options")
    window_resizer(name_root)
    window_resizer(name_root)
    name_root.config(bg=rgb_to_hex((ra.randint(0,255), ra.randint(0,255), ra.randint(0,255))))
    # The worded question on the code.
    tk.Label(name_root,
             text="What name would you like to be displayed on the school?",
             font=('Rockwell 14'),
             padx=20,
             pady=20
             ).place(relx=0.5, rely=0.1, anchor="center")
    school_name_entry = tk.Entry(name_root, width=45)
    school_name_entry.place(relx=0.5, rely=0.2, anchor="center")
    tk.Button(name_root,
              text="Save and Back",
              font=("Rockwell 14"),
              command=save_and_back,
              ).place(relx=0.5, rely=0.3, anchor="center")
    name_root.mainloop()

class Ghost:
  # initializing variables
  def __init__(self):
    pass

  def ghost_setup(self):
    '''
    Desc: Creates window displaying options for Ghost attributes/configuration, in this case only Name.
    Args: None
    Returns: None 
    '''
    # creates tkinter root
    ghost_setup_root = tk.Tk()
    ghost_setup_root.title("Ghost Configuration")

    window_resizer(ghost_setup_root)
    ghost_setup_root.config(bg=rgb_to_hex((ra.randint(0,255), ra.randint(0,255), ra.randint(0,255))))
    # creates and configs the main window size, title, options, bg color.
    tk.Label(ghost_setup_root, text="Which attribute you would like to edit?\n\nWhen you click, it saves automatically, eliminating the need\nto worry about whether it's saved or not.",font=("Rockwell 14"), padx=20, pady=20).place(relx=0.5, rely=0.15, anchor="center")
    tk.Button(
      ghost_setup_root,
      text="Number of Ghosts",
      font=("Rockwell 14"),
      command=lambda: [ghost_setup_root.destroy(),
                       self.ghost_number_choice()]
      ).place(relx=0.5, rely=0.3, anchor="center")
    tk.Button(ghost_setup_root,
              text="Facial Expression of Ghosts",
              font=("Rockwell 14"),
              command=lambda:
              [ghost_setup_root.destroy(),
               self.facial_expression_choice()]
              ).place(relx=0.5, rely=0.4, anchor="center")
    tk.Button(ghost_setup_root,
              text="Back 🔙",
              font=("Rockwell 14"),
              command=lambda: [ghost_setup_root.destroy(),
                               start()]
              ).place(relx=0.5, rely=0.5, anchor="center")
    ghost_setup_root.mainloop()

  def ghost_number_choice(self):
    '''
    Desc: Gets a name text entry from the user to display as the school's name.
    Args: None
    Returns: None
    '''

    def save_and_back():
      '''
      Desc: Saves the users input and then closes the current name() window and goes back to the previous (setup())
      Args: None
      Returns: None
      '''

      ghost_number.destroy()
      self.ghost_setup()

    # creates and configs the main window size, title, options, bg color.
    ghost_number = tk.Tk()
    ghost_number.title("Number of Ghosts")
    window_resizer(ghost_number)
    ghost_number.config(bg=rgb_to_hex((ra.randint(0,255), ra.randint(0,255), ra.randint(0,255))))
    # The worded question on the code.
    tk.Label(ghost_number,
             text="How many ghosts would you like to be present?",
             font=('Rockwell 14'),
             padx=20,
             pady=20
             ).place(relx=0.5, rely=0.1, anchor="center")

    def on_button_click(x):
      '''
      Desc: Depending on which button the user clicks, the program saves a different number to the ghosts_number variable 
      Args: x (number of ghosts that will be drawn with turtle)
      Returns: None
      '''
      replace_json_line("ghost_num", x)

    tk.Button(ghost_number,
              text="1",
              font=("Rockwell 14"),
              command=lambda: on_button_click(1),
              ).place(relx=0.5, rely=0.2, anchor="center")
    tk.Button(ghost_number,
              text="2",
              font=("Rockwell 14"),
              command=lambda: on_button_click(2),
              ).place(relx=0.5, rely=0.3, anchor="center")
    tk.Button(ghost_number,
              text="3",
              font=("Rockwell 14"),
              command=lambda: on_button_click(3),
              ).place(relx=0.5, rely=0.4, anchor="center")
    tk.Button(ghost_number,
              text="Save and Back",
              font=("Rockwell 14"),
              command=save_and_back,
              ).place(relx=0.5, rely=0.5, anchor="center")
    ghost_number.mainloop()

  def facial_expression_choice(self):
    '''
    Desc: Gets a name text entry from the user to display as the school's name.
    Args: None
    Returns: None
    '''

    def save_and_back():
      '''
      Desc: Saves the users input and then closes the current name() window and goes back to the previous (setup())
      Args: None
      Returns: None
      '''

      facial_g_expression.destroy()
      self.ghost_setup()

    # creates and configs the main window size, title, options, bg color.
    facial_g_expression = tk.Tk()
    facial_g_expression.title("Ghost Facial Expressions")
    window_resizer(facial_g_expression)
    facial_g_expression.config(bg=rgb_to_hex((ra.randint(0,255), ra.randint(0,255), ra.randint(0,255))))
    # The worded question on the code.
    tk.Label(facial_g_expression,
             text="What do you want for the facial expression for all ghosts?",
             font=('Rockwell 14'),
             padx=20,
             pady=20
             ).place(relx=0.5, rely=0.1, anchor="center")

    facial_dict={
      1:"Sad",
      2:"Happy"
    }
    
    def on_button_click(x):
      replace_json_line("ghost_facial_exp", f"{facial_dict[x]}")
    
    tk.Button(facial_g_expression,
              text="Sad",
              font=("Rockwell 14"),
              command=lambda: on_button_click(1),
              ).place(relx=0.5, rely=0.2, anchor="center")
    tk.Button(facial_g_expression,
              text="Happy",
              font=("Rockwell 14"),
              command=lambda: on_button_click(2),
              ).place(relx=0.5, rely=0.3, anchor="center")
    tk.Button(facial_g_expression,
              text="Save and Back",
              font=("Rockwell 14"),
              command=save_and_back,
              ).place(relx=0.5, rely=0.4, anchor="center")
    facial_g_expression.mainloop()

class Pumpkin:
  # initializing variables
  def __init__(self):
    pass

  def pumpkin_setup(self):
    '''
    Desc: Creates window displaying options for Ghost attributes/configuration, in this case only Name.
    Args: None
    Returns: None 
    '''
    # creates tkinter root
    pumpkin_setup_root = tk.Tk()
    pumpkin_setup_root.title("Pumpkin Configuration")

    window_resizer(pumpkin_setup_root)
    pumpkin_setup_root.config(bg=rgb_to_hex((ra.randint(0,255), ra.randint(0,255), ra.randint(0,255))))
    # creates and configs the main window size, title, options, bg color.

    tk.Label(pumpkin_setup_root, text="Which attribute you would like to edit?\n\nWhen you click, it saves automatically, eliminating the need\nto worry about whether it's saved or not.",font=("Rockwell 14"), padx=20, pady=20).place(relx=0.5, rely=0.15, anchor="center")
    tk.Button(pumpkin_setup_root,
              text="Facial Expression of Pumpkin",
              font=("Rockwell 14"),
              command=lambda:
              [pumpkin_setup_root.destroy(),
               self.facial_expression_choice()]
              ).place(relx=0.5, rely=0.3, anchor="center")
    tk.Button(pumpkin_setup_root,
              text="Back 🔙",
              font=("Rockwell 14"),
              command=lambda: [pumpkin_setup_root.destroy(),
                               start()]
              ).place(relx=0.5, rely=0.4, anchor="center")
    pumpkin_setup_root.mainloop()

  def facial_expression_choice(self):
    '''
    Desc: Gets a name text entry from the user to display as the school's name.
    Args: None
    Returns: None
    '''

    def save_and_back():
      '''
      Desc: Saves the users input and then closes the current name() window and goes back to the previous (setup())
      Args: None
      Returns: None
      '''

      facial_p_expression.destroy()
      self.pumpkin_setup()

    # creates and configs the main window size, title, options, bg color.
    facial_p_expression = tk.Tk()
    facial_p_expression.title("Pumpkin Facial Expressions")

    window_resizer(facial_p_expression)
    facial_p_expression.config(bg='#57D0F3')
    # The worded question on the code.
    tk.Label(facial_p_expression,
             text="What do you want for the facial expression for the pumpkin?",
             font=('Rockwell 14'),
             padx=20,
             pady=20
             ).place(relx=0.5, rely=0.1, anchor="center")
    
    facial_dict={
      1:"Sad",
      2:"Happy"
    }
    
    def on_button_click(x):
      '''
      Desc: Saves the value which determines the pumpkin's expression to its respective json line
      Args: x (key for facial_dict dictionary)
      Returns: None
      '''
      replace_json_line("pumpkin_facial_exp", f"{facial_dict[x]}")

    tk.Button(facial_p_expression,
              text="Sad",
              font=("Rockwell 14"),
              command=lambda: on_button_click(1),
              ).place(relx=0.5, rely=0.2, anchor="center")
    tk.Button(facial_p_expression,
              text="Happy",
              font=("Rockwell 14"),
              command=lambda: on_button_click(2),
              ).place(relx=0.5, rely=0.3, anchor="center")
    tk.Button(facial_p_expression,
              text="Save and Back",
              font=("Rockwell 14"),
              command=save_and_back,
              ).place(relx=0.5, rely=0.4, anchor="center")
    facial_p_expression.mainloop()

class Tombstone:
  # initializing variables
  def __init__(self):
    pass

  def tombstone_setup(self):
    '''
    Desc: Creates window displaying options for School attributes/configuration, in this case only Name.
    Args: None
    Returns: None 
    '''
    # creates tkinter root
    tombstone_setup_root = tk.Tk()
    tombstone_setup_root.title("Tombstone Configuration")

    window_resizer(tombstone_setup_root)
    tombstone_setup_root.config(bg=rgb_to_hex((ra.randint(0,255), ra.randint(0,255), ra.randint(0,255))))
    # creates and configs the main window size, title, options, bg color.
    tk.Label(tombstone_setup_root, text="Which attribute you would like to edit?\n\nWhen you click, it saves automatically, eliminating the need\nto worry about whether it's saved or not.",font=("Rockwell 14"), padx=20, pady=20).place(relx=0.5, rely=0.15, anchor="center")
    tk.Button(
      tombstone_setup_root,
      text="Name",
      font=("Rockwell 14"),
      command=lambda: [tombstone_setup_root.destroy(),
                       tombstone_setup_root.quit(),self.name_choice()]
      ).place(relx=0.5, rely=0.3, anchor="center")
    tk.Button(tombstone_setup_root,
              text="Back 🔙",
              font=("Rockwell 14"),
              command=lambda: [tombstone_setup_root.destroy(),tombstone_setup_root.quit(),
                               start()]
              ).place(relx=0.5, rely=0.4, anchor="center")
    tombstone_setup_root.mainloop()

  def name_choice(self):
    '''
    Desc: Gets a name text entry from the user to display as the school's name.
    Args: None
    Returns: None
    '''

    def save_and_back():
      '''
      Desc: Saves the users input and then closes the current name_choice() window and goes back to the previous (tombstone_setup())
      Args: None
      Returns: None
      '''

      replace_json_line("tombstone", f"{tomb_entry.get()}")
      name_root.destroy()
      name_root.quit()
      self.tombstone_setup()

    # creates and configs the main window size, title, options, bg color.
    name_root = tk.Tk()
    name_root.title("Tombstone Options")

    window_resizer(name_root)
    name_root.config(bg=rgb_to_hex((ra.randint(0,255), ra.randint(0,255), ra.randint(0,255))))
    # The worded question on the code.
    tk.Label(name_root,
             text="What name would you like to be displayed on the Tombstone?",
             font=('Rockwell 14'),
             padx=20,
             pady=20
             ).place(relx=0.5, rely=0.1, anchor="center")
    tomb_entry = tk.Entry(name_root, width=45)
    tomb_entry.place(relx=0.5, rely=0.2, anchor="center")
    tk.Button(name_root,
              text="Save and Back",
              font=("Rockwell 14"),
              command=save_and_back,
              ).place(relx=0.5, rely=0.3, anchor="center")
    name_root.mainloop()

def start():
  '''
  Desc: This is the run function for the input program.
  Args: None
  Returns: None
  '''
  artist_cog.resetcanvas()
  menu = tk.Tk()
  menu.title("Main Menu")
  window_resizer(menu)
  menu.config(bg=rgb_to_hex((ra.randint(0,255), ra.randint(0,255), ra.randint(0,255))))
  # default_json_values()
  global school_inst, colors_inst, ghost_inst, tombstone_inst, pumpkin_inst
  school_inst = School()
  colors_inst = Colors()
  ghost_inst = Ghost()
  pumpkin_inst = Pumpkin()
  tombstone_inst = Tombstone()
  tk.Label(menu, text="Welcome to the Scary School Creator!\n\nThis menu is for choosing the sections of the scary school that you want to create!\n\nClick these buttons to edit these items to your liking!",font=("Rockwell 14"), padx=20, pady=20).place(relx=0.5, rely=0.15, anchor="center")
  tk.Button(
            menu,
            text="Colors",
            font=("Rockwell 14"),
            command=lambda: [menu.destroy(), 
                             colors_inst.color_setup()]).place(rely=0.3, 
                                                               relx=0.5, 
                                                               anchor="center")
  tk.Button(menu,
            text="School",
            font=("Rockwell 14"),
            command=lambda: [menu.destroy(),
                             school_inst.school_setup()]).place(rely=0.4,
                                                                relx=0.5,
                                                                anchor="center")
  tk.Button(
            menu,
            text="Ghost",
            font=("Rockwell 14"),
            command=lambda: [menu.destroy(), 
                             ghost_inst.ghost_setup()]).place(rely=0.5,
                                                              relx=0.5,
                                                              anchor="center")
  tk.Button(
            menu,
            text="Pumpkin",
            font=("Rockwell 14"),
            command=lambda: [menu.destroy(), 
                             pumpkin_inst.pumpkin_setup()]).place(rely=0.6, 
                                                                  relx=0.5, 
                                                                  anchor="center")
  tk.Button(
            menu,
            text="Tombstone",
            font=("Rockwell 14"),
            command=lambda: [menu.destroy(), 
                             tombstone_inst.tombstone_setup()]).place(rely=0.7, 
                                                                      relx=0.5, 
                                                                      anchor="center")
  tk.Button(
            menu,
            text="Save and Close",
            font=("Rockwell 14"),
            command=lambda: [menu.destroy(), menu.quit(), run()]).place(rely=0.8, 
                                                                        relx=0.5, 
                                                                        anchor="center")
  menu.mainloop()

def restart():
  '''
  Desc: This is the run function for the input program.
  Args: None
  Returns: None
  '''
  restart_window = tk.Tk()
  restart_window.title("Restart?")
  restart_window.geometry("500x500")
  restart_window.config(bg="#E7E058")
  tk.Label(restart_window, text="Would you like to create another image?",font=("Rockwell 14"), bg="#E7E058", padx=20, pady=20).place(relx=0.5, rely=0.15, anchor="center")
  tk.Button(
            restart_window,
            text="Yes",
            font=("Rockwell 14"),
            command=lambda: [restart_window.destroy(), 
                             start(),replace_json_line("restart", "yes")]).place(rely=0.3, 
                                                               relx=0.5, 
                                                               anchor="center")
  tk.Button(
            restart_window,
            text="No",
            font=("Rockwell 14"),
            command=lambda: [restart_window.destroy(), restart_window.quit(), replace_json_line("restart", "no")]).place(rely=0.8, 
                                                                        relx=0.5, 
                                                                        anchor="center")
  restart_window.mainloop()
  
def run():
  '''
  Desc: This runs all the previous code so that full program can be used
  Args: None
  Returns: None
  '''
  ####################################################################################

  # EDIT THIS FILE PATH

  ####################################################################################
  with open("cogs/var.json", "r") as json_file:
    data=json.load(json_file)
  global color, school_name, ghost_number, ghost_facial_expression, pumpkin_facial_expression, tomb_name
  color=data["color"]
  school_name=data["school"]
  ghost_number=data["ghost_num"]
  ghost_facial_expression=data["ghost_facial_exp"]
  pumpkin_facial_expression=data["pumpkin_facial_exp"]
  tomb_name=data["tombstone"]
  print(f"{color}\n{school_name}\n{ghost_number}\n{ghost_facial_expression}\n{pumpkin_facial_expression}\n{tomb_name}")
  artist_cog.school_select_draw()
  artist_cog.ghost_select_draw()
  artist_cog.pumpkin_select_draw()
  artist_cog.tombstone_select_draw()
  artist_cog.flag_painter()
  if data["ticker"] == 10:
    restart()
    if data["restart"]=="no":
      artist_cog.flag_painter()
    else:
      print("broken 2")
  else:
    print("broken 3")