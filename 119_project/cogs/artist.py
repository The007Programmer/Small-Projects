import turtle as trt
import json
import time

# SP is the school-painter turtle instance for drawing the school itself.
sp = trt.Turtle()
sp.shape("turtle")
sp.speed(0)
# GP is the ghost-painter
gp = trt.Turtle()
gp.shape("circle")
gp.speed(0)
# PP is the pumpkin painter
pp = trt.Turtle()
pp.shape("triangle")
pp.speed(0)
# TP is the tombstone painter
tp = trt.Turtle()
tp.shape("square")
tp.speed(0)
# FP is the flag painter
fp = trt.Turtle()
fp.speed(0)


wn = trt.Screen()
wn.screensize(800, 800)
wn.title("Scary School")

def resetcanvas():
  wn.clearscreen()
  go_to(sp,0,0)
  go_to(gp,0,0)
  go_to(pp,0,0)
  go_to(tp,0,0)
  go_to(fp,0,0)
  sp.seth(0)
  gp.seth(0)
  pp.seth(0)
  tp.seth(0)
  fp.seth(0)

####################################################################################

# EDIT THESE 11 FILE PATHS

####################################################################################

# a list of each frame for the moving image
flag_sections = [
  "cogs/images/flags/flag1-0.gif",
  "cogs/images/flags/flag1-1.gif",
  "cogs/images/flags/flag1-2.gif",
  "cogs/images/flags/flag1-3.gif",
  "cogs/images/flags/flag1-4.gif",
  "cogs/images/flags/flag1-5.gif",
  "cogs/images/flags/flag1-6.gif",
  "cogs/images/flags/flag1-8.gif",
  "cogs/images/flags/flag1-9.gif",
  "cogs/images/flags/flag1-10.gif",
  "cogs/images/flags/flag1-11.gif",
]

# adding/registering each shape to the screen
for i in flag_sections:
  wn.addshape(i)
  
# setting 2 colorschemes
colorschemes = [
  # color scheme 1: light purple, purple, black, sun-yellow, orange
  ["#44355B", "#31263E", "#221E22", "#ECA72C", "#EE5622"],
  # color scheme 2: black, dark purple, gray, green-gray, mint-green
  ["#1A090D", "#4A314D", "#6B6570", "#A8BA9A", "#ACE894"]
]

def go_to(tturtle, x, y):
  '''
  Desc: Moves a specific turtle to a given spot without drawing a line.
  Args: tturtle; turtle of choice, x, y
  Returns: None
  '''
  tturtle.up()
  tturtle.goto(x, y)
  tturtle.down()


# Most liked colorscheme selctions in order of (colorscheme_number, which section)
# school=(1;2)(2;3)
# ghost=(1;4)(2;5)
# pumpkin=(1;5)(2;2)
# tombstone=(1;1)(2;2)

def replace_json_line(key, value):
  '''
  Desc: Saves the given value to its specific key-value pair. 
  Args: Key (reference to the json-key), Value (reference to the value to be saved)
  Returns: None
  '''
  ####################################################################################

  # EDIT THESE 2 FILE PATHS

  ####################################################################################
  # opening the json file as a readable data structure
  with open("cogs/var.json", "r") as json_file:
    data=json.load(json_file)
    data[key]=value

  # saving the json file as a writable data structure
  with open("cogs/var.json", "w") as json_file:
    json.dump(data, json_file)


def flag_painter():
  '''
  Desc: This function paints the flag of the school
  Args: None
  Returns: None
  '''
  
  ticker=0
  while ticker <= 10:
    go_to(fp, 50, 150)
    for i in flag_sections:
      fp.shape(i)
      time.sleep(0.07)
      wn.update()
    print(ticker)
    replace_json_line("ticker", ticker)
    ticker+=1
    
def school_select_draw():
  '''
  Desc: This is the final function called in the input file to draw the school and its attributes.
  Args: None
  Returns: None
  '''
  ####################################################################################

  # EDIT THIS FILE PATH

  ####################################################################################
  with open("cogs/var.json", "r") as json_file:
    data = json.load(json_file)

  def school_draw(building_col, door_col, knob_col, word_col):
    '''
    Desc: This function draws the school itself with its attributes.
    Args: Color of the building, door, doorknob, and wording colors
    Returns: None
    '''

    def school(fd1, fd2):
      '''
      Desc: The physical school itself, no colors or anything, this is called twice depending on colorscheme.
      Args: fd1; dimension for the x, fd2; dimension for the y
      Returns: None
      '''
      sp.fd(fd1)
      sp.rt(90)
      sp.fd(fd2)
      sp.rt(90)
      sp.fd(fd1)
      sp.rt(90)
      sp.fd(fd2)

    def door(first_rt):
      '''
      Desc: Draws a individual door, called 4 times because 2 doors and 2 colorschemes; drawn with selected door color.
      Args: first_rt; rotation of the door
      Returns: None
      '''
      sp.fillcolor(door_col)
      sp.begin_fill()
      sp.rt(first_rt)
      sp.fd(115)
      sp.rt(90)
      sp.fd(60)
      sp.rt(90)
      sp.fd(115)
      sp.end_fill()

    def knob():
      '''
      Desc: Draw a individual doorknob, called 4 times because 2 knobs and 2 colorschemes; drawn with selected knob color.
      Args: None
      Returns: None
      '''
      sp.fillcolor(knob_col)
      sp.begin_fill()
      sp.circle(10, 360)
      sp.end_fill()

    def write():
      '''
      Desc: Writes the user's chosen text on the school; drawn with selected wording color.
      Args: None
      Returns: None
      '''
      sp.color(word_col)
      sp.write(data["school"], font=("Rockwell", 20, "bold"))

    go_to(sp, -200, -200)
    sp.fillcolor(building_col)
    sp.begin_fill()
    sp.lt(90)
    school(300, 450)
    sp.end_fill()
    go_to(sp, -40, -200)
    door(90)
    go_to(sp, 24, -200)
    door(180)
    go_to(sp, -5, -142.5)
    knob()
    go_to(sp, 30, -142.5)
    knob()
    go_to(sp, -80, -35)
    write()
    go_to(sp, -80, -35)
    write()
    go_to(sp, 5, 150)
    sp.shape("arrow")
    sp.color("black")
    sp.pensize(5)
    sp.fd(50)
    go_to(sp, 48, 160)
    sp.hideturtle()

  if data["color"] == 1:
    school_draw(colorschemes[0][1], colorschemes[0][0], colorschemes[0][2],
                colorschemes[0][3])
  if data["color"] == 2:
    school_draw(colorschemes[1][1], colorschemes[1][0], colorschemes[1][2],
                colorschemes[1][3])

def ghost_select_draw():
  '''
  Desc: This is the final function called in the input file to draw the selected number of ghosts with correct attributes.
  Args: None
  Returns: None
  '''
  ####################################################################################

  # EDIT THIS FILE PATH

  ####################################################################################
  with open("cogs/var.json", "r") as json_file:
    data = json.load(json_file)

  def ghost_drawer(color_selected_scheme):
    '''
    Desc: Draws a individual ghost, with the selected color scheme
    Args: color_selected_scheme; just the choice for color scheme
    Returns: None
    '''
    gp.fillcolor(color_selected_scheme)
    gp.begin_fill()
    gp.rt(90)
    gp.circle(40, -270)
    gp.rt(180)
    gp.circle(40, 90)
    gp.lt(90)
    gp.end_fill()
    gp.color("black")

  def ghosts(num, color, exp):
    '''
    Desc: Essentially creates a conditional flow chart of sorts, checking multiple conditions based on the user inputs.
    Args: num; number of ghosts. color; which is the chosen colorscheme colors to use, exp; then chosen face expressison
    Returns: None
    '''

    def ghost_exp(expression, x1, x2, y1, y2):
      '''
      Desc: Draws an individual ghost's expression.
      Args: expression; happy or sad, x1, x2, y1, y2
      Returns: None
      '''
      if expression == "sad":
        go_to(gp, x1, y1)
        gp.pensize(3)
        gp.stamp()
        go_to(gp, x2, y1)
        gp.stamp()
        go_to(gp, x1, y2 - 10)
        gp.rt(90)
        gp.circle(15, -180)
        gp.setheading(0)
      if expression == "happy":
        go_to(gp, x1, y1)
        gp.pensize(3)
        gp.stamp()
        go_to(gp, x2, y1)
        gp.stamp()
        go_to(gp, x1, y2)
        gp.rt(90)
        gp.circle(15, 180)
        gp.setheading(0)

    if num == 1:
      go_to(gp, 250, 100)
      ghost_drawer(color)
      ghost_exp(exp, 275, 305, 105, 85)

    if num == 2:
      go_to(gp, 250, 100)
      ghost_drawer(color)
      go_to(gp, 250, 15)
      ghost_drawer(color)
      ghost_exp(exp, 275, 305, 105, 85)
      ghost_exp(exp, 275, 305, 20, 0)

    if num == 3:
      go_to(gp, 250, 100)
      ghost_drawer(color)
      go_to(gp, 250, 15)
      ghost_drawer(color)
      go_to(gp, 250, -70)
      ghost_drawer(color)
      ghost_exp(exp, 275, 305, 105, 85)
      ghost_exp(exp, 275, 305, 20, 0)
      ghost_exp(exp, 275, 305, -65, -85)

  def full_ghost_selection():
    '''
    Desc: An organized/structured layout of the code in order, to be called after colorscheme selection.
    Args: None
    Returns: None
    '''
    if data["ghost_facial_exp"] == "Happy":
      if data["ghost_num"] == 1:
        ghosts(1, chosen_color_ghost, "happy")
      if data["ghost_num"] == 2:
        ghosts(2, chosen_color_ghost, "happy")
      if data["ghost_num"] == 3:
        ghosts(3, chosen_color_ghost, "happy")

    if data["ghost_facial_exp"] == "Sad":
      if data["ghost_num"] == 1:
        ghosts(1, chosen_color_ghost, "sad")
      if data["ghost_num"] == 2:
        ghosts(2, chosen_color_ghost, "sad")
      if data["ghost_num"] == 3:
        ghosts(3, chosen_color_ghost, "sad")
    gp.hideturtle()

  if data["color"] == 1:
    chosen_color_ghost = colorschemes[0][3]
    full_ghost_selection()

  if data["color"] == 2:
    chosen_color_ghost = colorschemes[1][4]
    full_ghost_selection()

def pumpkin_select_draw():
  '''
  Desc: This is the final function called in the input file to draw the pumpkin with correct attributes.
  Args: None
  Returns: None
  '''
  ####################################################################################

  # EDIT THIS FILE PATH

  ####################################################################################
  with open("cogs/var.json", "r") as json_file:
    data = json.load(json_file)
    
  def pumpkin_exp(expression, x1, x2, y1, y2,facecolor):
    '''
    Desc: Draws the pumpkins facial expression.
    Args: expression; happy or angry or sad, x1, x2, y1, y2
    Returns: None
    '''
    if expression == "sad":
      pp.fillcolor(facecolor)
      go_to(pp, x1, y1)
      pp.stamp()
      go_to(pp, x2, y1)
      pp.stamp()
      go_to(pp, x1, y2-15)
      pp.pensize(5)
      pp.begin_fill()
      pp.circle(-20, 180)
      pp.setheading(0)
      pp.lt(180)
      pp.fd(40)
      pp.end_fill()
      pp.hideturtle()
    if expression == "happy":
      pp.color("black")
      pp.fillcolor(facecolor)
      go_to(pp, x1, y1)
      pp.stamp()
      go_to(pp, x2, y1)
      pp.stamp()
      go_to(pp, x1, y2)
      pp.lt(180)
      pp.begin_fill()
      pp.pensize(5)
      pp.circle(20, 180)
      pp.setheading(0)
      pp.lt(180)
      pp.fd(40)
      pp.end_fill()
      pp.hideturtle()
      
  def pumpkin_drawer(pcolor):
    '''
    Desc: Draws the pumpkins body.
    Args: color; red or orange or yellow or green or blue or purple
    Returns: None
    '''
    go_to(pp,-225,-250)
    pp.fillcolor(pcolor)
    pp.begin_fill()
    pp.circle(40, 360)
    pp.end_fill()
    go_to(pp,-175,-250)
    pp.fillcolor(pcolor)
    pp.begin_fill()
    pp.circle(40, 360)
    pp.end_fill()
    go_to(pp,-200,-260)
    pp.fillcolor(pcolor)
    pp.begin_fill()
    pp.circle(45, 360)
    pp.end_fill()
    go_to(pp,-200,-170)
    pp.pensize(15)
    pp.lt(90)
    pp.color(colorschemes[1][0])
    pp.fd(25)
    pp.pensize(1)

  def full_pumpkin_selection():
    '''
    Desc: An organized/structured layout of the code in order, to be called after colorscheme selection.
    Args: None
    Returns: None
    '''
    
    if data["pumpkin_facial_exp"] == "Happy":
      pumpkin_drawer(pumpkin_color)
      pumpkin_exp("happy", -220, -180, -200, -220, pumpkin_face_color)
    
    if data["pumpkin_facial_exp"] == "Sad":
      pumpkin_drawer(pumpkin_color)
      pumpkin_exp("sad", -220, -180, -200, -220, pumpkin_face_color)

    
  if data["color"]==1:
    pumpkin_color=colorschemes[0][4]
    pumpkin_face_color=colorschemes[0][2]
    full_pumpkin_selection()
  if data["color"]==2:
    pumpkin_color=colorschemes[1][3]
    pumpkin_face_color=colorschemes[1][0]
    full_pumpkin_selection()

def tombstone_select_draw():
  '''
  Desc: This is the final function that will be called in the input file for drawing the tombstone.
  Args: None
  Returns: None
  '''
  ####################################################################################

  # EDIT THIS FILE PATH

  ####################################################################################
  with open("cogs/var.json", "r") as json_file:
    data = json.load(json_file)
    
  def tombstone_drawer(color):
    '''
    Desc: Draws the physical tombstone itself, with colors.
    Args: color; the chosen color based on colorscheme choice.
    Returns: None
    '''
    go_to(tp, 190, -270)
    tp.lt(90)
    tp.fillcolor(color)
    tp.begin_fill()
    tp.pensize(5)
    tp.fd(60)
    tp.circle(-80, 180)
    tp.fd(60)
    tp.end_fill()
    tp.rt(90)
    tp.fd(160)

  def tombstone_writer(word_color):
    '''
    Desc: Writes the user's words on the tombstone.
    Args: word_color, based on the user's colorscheme choice.
    Returns: None
    '''
    go_to(tp, 230, -210)
    tp.color(word_color)
    tp.write(f'R.I.P\n\n{data["tombstone"]}', font=("Rockwell", 10, "bold"))
    tp.hideturtle()

  if data["color"]==1:
    tombstone_drawer(colorschemes[0][2])
    tombstone_writer(colorschemes[0][3])
  if data["color"]==2:
    tombstone_drawer(colorschemes[1][2])
    tombstone_writer(colorschemes[1][3])