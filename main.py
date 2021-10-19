import turtle as trtl
import math
import random as rand
import leaderboard as lb

#Initialize state variables
wn = trtl.Screen()
x_i = -200
y_i = -200
t0 = 0
t1 = 1
v0 = 12
a = -0.3
f_vel = 2
vp1 = 0
vp2 = 0
p1_shooting = False
p2_shooting = False
run = True
player_1_lost = False
player_2_lost = False
score1 = 0
score2 = 0

#bubble_size = [5, 2, 3, 1, 4]
#bubble_speed = [.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9, 9.5, 10]
#randcolor = ["red", "orange", "purple", "brown", "green", "black", "white", "yellow"]

CURSOR_SIZE = 20
FONT_SIZE = 20
FONT = ('Arial', FONT_SIZE, 'bold')


#Background
water = ("Water.gif")
wn.addshape(water)
water = trtl.Turtle(shape=water)

#Defining objects (Circle, player, etc.)
bubble = trtl.Turtle()
bubble.shape("circle")
bubble.penup()
bubble.goto(rand.randint(x_i, 200), y_i + 20)
bubble.shapesize(4)

arrow = trtl.Turtle()
arrow.shape("arrow")
arrow.hideturtle()
arrow.penup()
arrow.setheading(90)

arrow2 = trtl.Turtle()
arrow2.shape("arrow")
arrow2.hideturtle()
arrow2.penup()
arrow2.setheading(90)
arrow2.color("red")
arrow2.pencolor("red")

score_writer = trtl.Turtle()
score_writer.speed("fastest")
score_writer.hideturtle()
score_writer.penup()
score_writer.goto(160,220)
score_writer.pendown()
score_writer.write("Player 1 score: " + str(score1), font = FONT)

score_writer2 = trtl.Turtle()
score_writer2.speed("fastest")
score_writer2.hideturtle()
score_writer2.penup()
score_writer2.goto(160,190)
score_writer2.pendown()
score_writer2.write("Player 2 score: " + str(score2), font = FONT)

score_writert = trtl.Turtle()
score_writert.speed("fastest")
score_writert.hideturtle()
score_writert.penup()
score_writert.goto(160,160)
score_writert.pendown()
score_writert.write("Team score: " + str((score1 + score2)), font = FONT)

octopus_image_2 = ("player2.gif")
wn.addshape(octopus_image_2)
player_2 = trtl.Turtle(shape = octopus_image_2)
player_2.speed("fastest")
player_2.penup()
player_2.goto(0,-200)


octopus_image_1 = ("player1.gif")
wn.addshape(octopus_image_1)
player_1 = trtl.Turtle(shape = octopus_image_1)
player_1.penup()
player_1.goto(0,-200)
player_1.showturtle()

# leaderboard variables
leaderboard_file_name = "a122_leaderboard.txt"
leader_names_list = []
leader_scores_list = []
player_name = input ("Please enter your team name:")
 
# manages the leaderboard for top 5 scorers
def manage_leaderboard():
  global leader_scores_list
  global leader_names_list
  global score
  global spot
 
 # load all the leaderboard records into the lists
  lb.load_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list)
 
 # TODO
  if (len(leader_scores_list) < 5 or (score1 + score2) > leader_scores_list[4]):
   lb.update_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list, player_name, (score1 + score2))
   lb.draw_leaderboard(leader_names_list, leader_scores_list, True, player_1, (score1 + score2))
 
  else:
   lb.draw_leaderboard(leader_names_list, leader_scores_list, False, player_1, (score1 + score2))

#Game functions
def respawn():
  global score1, score2
  update_score()
  update_score2()
  update_scoret()
  bubble.hideturtle()
  bubble.speed("fastest")
  rx = rand.randint(-200,200)
  ry = rand.randint(-200,200)
  bubble.goto(rx,ry)
  bubble.showturtle()
  #bubble.color(randcolor)
  #bubble.shapesize(bubble_size)

def p1_up():
  space_deactivate()
  global p1_shooting
  p1_shooting = True
  arrow.goto(player_1.xcor(), player_1.ycor())
  arrow.showturtle()

def p2_up():
  space_deactivate2()
  global p2_shooting
  p2_shooting = True
  arrow2.goto(player_2.xcor(), player_2.ycor())
  arrow2.showturtle()
  
def p1_shoot():
  global p1_shooting, score1
  arrow.forward(10)
  if arrow.ycor() > 250:
    p1_shooting = False
    arrow.hideturtle()
    keys_activate()
  d_x = arrow.xcor() - bubble.xcor()
  d_y = arrow.ycor() - bubble.ycor()
  d = math.sqrt(d_x**2 + d_y**2)

  if d <= 30:
    p1_shooting = False
    arrow.hideturtle()
    score1 += 1
    respawn()
    keys_activate()

def p2_shoot():
  global p2_shooting, score2
  arrow2.forward(10)
  if arrow2.ycor() > 250:
    p2_shooting = False
    arrow2.hideturtle()
    keys_activate()
  d_x2 = arrow2.xcor() - bubble.xcor()
  d_y2 = arrow2.ycor() - bubble.ycor()
  d2 = math.sqrt(d_x2**2 + d_y2**2)

  if d2 <= 30:
    p2_shooting = False
    arrow2.hideturtle()
    bubble.hideturtle()
    score2 += 1
    respawn()
    keys_activate()
    
def ball_move():
  global t0, t1, v0, a, y_i, x_i, f_vel

  v = v0 + a * t0
  theta = math.atan2(v, f_vel) * 360 / (6.24)
  distance = math.sqrt(v**2 + f_vel**2)
  bubble.setheading(theta)
  bubble.forward(distance)
  t0 += 1 
  
  if bubble.ycor() <= y_i - v:
    t0 = 0
  
  if bubble.xcor() >= 320:
    f_vel = -2
  if bubble.xcor() <= -320:
    f_vel = 2

  return True

def player1_right():
  if player_1.xcor() < 320:
    player_1.forward(5)

def player1_left():
  if player_1.xcor() > -320:
    player_1.forward(-5)

def player2_right():
  if player_2.xcor() < 320:
    player_2.forward(5)

def player2_left():
  if player_2.xcor() > -320:
    player_2.forward(-5)

def update_score():
  score_writer.clear()
  score_writer.write("Player 1 score: " + str(score1), font = FONT)

def update_score2():
  score_writer2.clear()
  score_writer2.write("Player 2 score: " + str(score2), font = FONT)
  
def update_scoret():
  score_writert.clear()
  score_writert.write("Team score: " + str((score1 + score2)), font = FONT)

#User input
def keys_activate():
  wn.onkey(player1_left, "Left")
  wn.onkey(player1_right, "Right")
  wn.onkey(p1_up, "Up")
  wn.onkey(player2_left, "a")
  wn.onkey(player2_right, "d")
  wn.onkey(p2_up, "space")

def space_deactivate():
  wn.onkey(None,"Up")

def space_deactivate2():
  wn.onkey(None,"space")


keys_activate()
wn.listen()


#Where the game runs
while run:
  if p1_shooting:
    p1_shoot()
  if p2_shooting:
    p2_shoot()
  ball_move()
  collision_x = player_1.xcor() - bubble.xcor()
  collision_y = player_1.ycor() - bubble.ycor()
  collision_d = math.sqrt(collision_x**2 + collision_y**2)

  collision_x2 = player_2.xcor() - bubble.xcor()
  collision_y2 = player_2.ycor() - bubble.ycor()
  collision_d2 = math.sqrt(collision_x2**2 + collision_y2**2)

  if collision_d <= 40:
    player_1.hideturtle()
    player_1_lost = True
  
  if collision_d2 <= 40:
    player_2.hideturtle()
    player_2_lost = True

  if player_1_lost and player_2_lost:
    break

score_writer.clear()
score_writer2.clear()
score_writert.clear()

score_writer.penup()
score_writer.goto(-200, 260)
score_writer.write("You lost! Better luck next time", font = FONT)

manage_leaderboard()
    
  

wn.mainloop()