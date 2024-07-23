import random
import keyboard
import pydirectinput
import pyautogui

def moveAround():
    # If the chat message is "left", then hold down the A key for 2 seconds
    if msg == "left": 
        HoldAndReleaseKey(A, 2)

    # If the chat message is "right", then hold down the D key for 2 seconds
    if msg == "right": 
        HoldAndReleaseKey(D, 2)

    # If message is "drive", then permanently hold down the W key
    if msg in ["forward", "drive", "forwards"]: 
        ReleaseKey(S) #release brake key first
        HoldKey(W) #start permanently driving

    # If message is "reverse", then permanently hold down the S key
    if msg in ["back", "reverse", "backward", "backwards"]: 
        ReleaseKey(W) #release drive key first
        HoldKey(S) #start permanently reversing

    if msg in ["ult", "ultimate"]:
        HoldAndReleaseKey(Q, 1)

    if msg == "jump":
        HoldAndReleaseKey(SPACE, 1)

    if msg in ["jump left", "lump"]:
        HoldKey(SPACE)
        HoldKey(A)
        time.sleep(0.5)
        ReleaseKey(SPACE)
        time.sleep(0.5)
        ReleaseKey(A)

    if msg in ["jump right", "rump"]:
        HoldKey(SPACE)
        HoldKey(D)
        time.sleep(0.5)
        ReleaseKey(SPACE)
        time.sleep(0.5)
        ReleaseKey(D)

    # Release both the "drive" and "reverse" keys
    if msg == "stop": 
        ReleaseKey(W)
        ReleaseKey(S)
        ReleaseKey(LEFT_SHIFT)

    if msg == "reload":
        HoldAndReleaseKey(R, 0.5)

    if msg == "crouch":
        HoldAndReleaseKey(LEFT_CONTROL, 1)

    if msg == "punch":
        HoldAndReleaseKey(J, 1)

    if msg == "interact"
        HoldAndReleaseKey(G, 1)

def lookAround():
    # Aim the mouse by a little bit
    if msg == "aim up":
        pydirectinput.moveRel(0, -150, relative=True)
    if msg == "aim down":
        pydirectinput.moveRel(0, 150, relative=True)
    if msg == "aim right":
        pydirectinput.moveRel(150, 0, relative=True)
    if msg == "aim left":
        pydirectinput.moveRel(-150, 0, relative=True)

    # Look the camera around at a 45 degree angle-ish
    if msg == "look up":
        pydirectinput.moveRel(0, -600, relative=True)
    if msg == "look down":
        pydirectinput.moveRel(0, 600, relative=True)
    if msg == "look right":
        pydirectinput.moveRel(1500, 0, relative=True)
    if msg == "look left":
        pydirectinput.moveRel(-1500, 0, relative=True)

    # Turn completely around
    if msg == "turn around":
        pydirectinput.moveRel(6000, 0, relative=True)

    # Turn 90 degrees-ish
    if msg == "turn right":
        pydirectinput.moveRel(3000, 0, relative=True)
    if msg == "turn left":
        pydirectinput.moveRel(-3000, 0, relative=True)



######################################
# TANK HEROES
######################################
def dva():
    # This is the LEFT_SHIFT ability
    if msg in ["ab1", "shift"]:
        HoldAndReleaseKey(LEFT_SHIFT, 3)
    # This is the E ability
    if msg in ["ab2", "e"]:
        HoldAndReleaseKey(E, 1)
    # This is the RIGHT CLICK ability
    if msg in ["ab3", "right click"]:
        pydirectinput.mouseDown(button="right")
        time.sleep(2)
        pydirectinput.mouseUp(button="right")
    # This is the SHOOT
    if msg == "shoot": 
        pydirectinput.mouseDown(button="left")
        time.sleep(2)
        pydirectinput.mouseUp(button="left")

def doomfist():
    # This is the LEFT_SHIFT ability
    if msg in ["ab1", "shift"]:
        HoldAndReleaseKey(LEFT_SHIFT, 1)
    # This is the E ability
    if msg in ["ab2", "e"]:
        HoldAndReleaseKey(E, 1)
    # This is the RIGHT CLICK ability
    if msg in ["ab3", "right click"]:
        pydirectinput.mouseDown(button="right")
        time.sleep(3)
        pydirectinput.mouseUp(button="right")
    # Press the left mouse button down for 1 second, then release it
    if msg == "shoot": 
        pydirectinput.mouseDown(button="left")
        time.sleep(2)
        pydirectinput.mouseUp(button="left")

def junkerqueen():
    # This is the LEFT_SHIFT ability
    if msg in ["ab1", "shift"]:
        HoldAndReleaseKey(LEFT_SHIFT, 1)
    # This is the E ability
    if msg in ["ab2", "e"]:
        HoldAndReleaseKey(E, 1)
    # This is the RIGHT CLICK ability
    if msg in ["ab3", "right click"]:
        pydirectinput.mouseDown(button="right")
        time.sleep(0.5)
        pydirectinput.mouseUp(button="right")
    # Press the left mouse button down for 1 second, then release it
    if msg == "shoot": 
        pydirectinput.mouseDown(button="left")
        time.sleep(1)
        pydirectinput.mouseUp(button="left")

def mauga():
    # This is the LEFT_SHIFT ability
    if msg in ["ab1", "shift"]:
        HoldAndReleaseKey(LEFT_SHIFT, 0.5)
    # This is the E ability
    if msg in ["ab2", "e"]:
        HoldAndReleaseKey(E, 0.5)
    # Press the left mouse button down for 1 second, then release it
    if msg == "shoot": 
        pydirectinput.mouseDown(button="left")
        pydirectinput.mouseDown(button="right")
        time.sleep(2)
        pydirectinput.mouseUp(button="left")
        pydirectinput.mouseUp(button="right")

def orisa():
    # This is the LEFT_SHIFT ability
    if msg in ["ab1", "shift"]:
        HoldAndReleaseKey(LEFT_SHIFT, 0.5)
    # This is the E ability
    if msg in ["ab2", "e"]:
        HoldAndReleaseKey(E, 0.5)
    # This is the RIGHT CLICK ability
    if msg in ["ab3", "right click"]:
        pydirectinput.mouseDown(button="right")
        time.sleep(0.5)
        pydirectinput.mouseUp(button="right")
    # Press the left mouse button down for 1 second, then release it
    if msg == "shoot": 
        pydirectinput.mouseDown(button="left")
        time.sleep(2)
        pydirectinput.mouseUp(button="left")

def ramattra():
    # This is the LEFT_SHIFT ability
    if msg in ["ab1", "shift"]:
        HoldAndReleaseKey(LEFT_SHIFT, 0.5)
    # This is the E ability
    if msg in ["ab2", "e"]:
        HoldAndReleaseKey(E, 0.5)
    # This is the RIGHT CLICK ability
    if msg in ["ab3", "right click"]:
        pydirectinput.mouseDown(button="right")
        time.sleep(0.5)
        pydirectinput.mouseUp(button="right")
    # Press the left mouse button down for 1 second, then release it
    if msg == "shoot": 
        pydirectinput.mouseDown(button="left")
        time.sleep(2)
        pydirectinput.mouseUp(button="left")
    # This is for BLOCKING
    if msg == "block":
        pydirectinput.mouseDown(button="right")
        time.sleep(2)
        pydirectinput.mouseUp(button="right")

def reinhardt():
    # This is the LEFT_SHIFT ability
    if msg in ["ab1", "shift"]:
        HoldAndReleaseKey(LEFT_SHIFT, 0.5)
    # This is the E ability
    if msg in ["ab2", "e"]:
        HoldAndReleaseKey(E, 0.5)
    # This is the RIGHT CLICK ability
    if msg == "shield up":
        pydirectinput.mouseDown(button="right")
    if msg == "shield down":
        pydirectinput.mouseUp(button="right")
    # Press the left mouse button down for 1 second, then release it
    if msg == "shoot": 
        pydirectinput.mouseDown(button="left")
        time.sleep(2)
        pydirectinput.mouseUp(button="left")

def roadhog():
    # This is the LEFT_SHIFT ability
    if msg in ["ab1", "shift"]:
        HoldAndReleaseKey(LEFT_SHIFT, 0.5)
    # This is the E ability
    if msg in ["ab2", "e"]:
        HoldAndReleaseKey(E, 0.5)
    # This is the RIGHT CLICK ability
    if msg in ["ab3", "right click"]:
        pydirectinput.mouseDown(button="right")
        time.sleep(2)
        pydirectinput.mouseUp(button="right")
    # Press the left mouse button down for 1 second, then release it
    if msg == "shoot": 
        pydirectinput.mouseDown(button="left")
        time.sleep(2)
        pydirectinput.mouseUp(button="left")

def sigma():
    # This is the LEFT_SHIFT ability
    if msg in ["ab1", "shift"]:
        HoldAndReleaseKey(LEFT_SHIFT, 0.5)
    # This is the E ability
    if msg in ["ab2", "e"]:
        HoldAndReleaseKey(E, 0.5)
    # This is the RIGHT CLICK ability
    if msg in ["ab3", "right click"]:
        pydirectinput.mouseDown(button="right")
        time.sleep(1)
        pydirectinput.mouseUp(button="right")
    # Press the left mouse button down for 1 second, then release it
    if msg == "shoot": 
        pydirectinput.mouseDown(button="left")
        time.sleep(2)
        pydirectinput.mouseUp(button="left")

def winston():
    # This is the LEFT_SHIFT ability
    if msg in ["ab1", "shift"]:
        HoldAndReleaseKey(LEFT_SHIFT, 0.5)
    # This is the E ability
    if msg in ["ab2", "e"]:
        HoldAndReleaseKey(E, 0.5)
    # This is the RIGHT CLICK ability
    if msg in ["ab3", "right click"]:
        pydirectinput.mouseDown(button="right")
        time.sleep(2)
        pydirectinput.mouseUp(button="right")
    # Press the left mouse button down for 1 second, then release it
    if msg == "shoot": 
        pydirectinput.mouseDown(button="left")
        time.sleep(2)
        pydirectinput.mouseUp(button="left")

def wreckingball():
    # This is the LEFT_SHIFT ability
    if msg in ["ab1", "shift"]:
        HoldAndReleaseKey(LEFT_SHIFT, 0.5)
    # This is the E ability
    if msg in ["ab2", "e"]:
        HoldAndReleaseKey(E, 0.5)
    # This is the RIGHT CLICK ability
    if msg == "attach":
        pydirectinput.mouseDown(button="right")
    if msg == "detach":
        pydirectinput.mouseUp(button="right")
    # Press the left mouse button down for 1 second, then release it
    if msg == "shoot": 
        pydirectinput.mouseDown(button="left")
        time.sleep(2)
        pydirectinput.mouseUp(button="left")

def zarya():
    # This is the LEFT_SHIFT ability
    if msg in ["ab1", "shift"]:
        HoldAndReleaseKey(LEFT_SHIFT, 0.5)
    # This is the E ability
    if msg in ["ab2", "e"]:
        HoldAndReleaseKey(E, 0.5)
    # This is the RIGHT CLICK ability
    if msg in ["ab3", "right click"]:
        pydirectinput.mouseDown(button="right")
        time.sleep(0.5)
        pydirectinput.mouseUp(button="right")
    # Press the left mouse button down for 1 second, then release it
    if msg == "shoot": 
        pydirectinput.mouseDown(button="left")
        time.sleep(2)
        pydirectinput.mouseUp(button="left")


######################################
# DAMAGE HEROES
######################################
def ashe():
    # This is the LEFT_SHIFT ability
    if msg in ["ab1", "shift"]:
        HoldAndReleaseKey(LEFT_SHIFT, 0.5)
    # This is the E ability
    if msg in ["ab2", "e"]:
        HoldAndReleaseKey(E, 0.5)
    # This is the RIGHT CLICK ability
    if msg == "aim down":
        pydirectinput.mouseDown(button="right")
    if msg == "aim out":
        pydirectinput.mouseUp(button="right")
    # Press the left mouse button down for 1 second, then release it
    if msg == "shoot": 
        pydirectinput.mouseDown(button="left")
        time.sleep(2)
        pydirectinput.mouseUp(button="left")

def bastion():
    # This is the LEFT_SHIFT ability
    if msg in ["ab1", "shift"]:
        HoldAndReleaseKey(LEFT_SHIFT, 0.5)
    # This is the RIGHT CLICK ability
    if msg in ["ab3", "right click"]:
        pydirectinput.mouseDown(button="right")
        time.sleep(0.5)
        pydirectinput.mouseUp(button="right")
    # Press the left mouse button down for 1 second, then release it
    if msg == "shoot": 
        pydirectinput.mouseDown(button="left")
        time.sleep(2)
        pydirectinput.mouseUp(button="left")

def cassidy():
    # This is the LEFT_SHIFT ability
    if msg in ["ab1", "shift"]:
        HoldAndReleaseKey(LEFT_SHIFT, 0.5)
    # This is the E ability
    if msg in ["ab2", "e"]:
        HoldAndReleaseKey(E, 0.5)
    # This is the RIGHT CLICK ability
    if msg in ["ab3", "right click"]:
        pydirectinput.mouseDown(button="right")
        time.sleep(0.5)
        pydirectinput.mouseUp(button="right")
    # Press the left mouse button down for 1 second, then release it
    if msg == "shoot": 
        pydirectinput.mouseDown(button="left")
        time.sleep(1)
        pydirectinput.mouseUp(button="left")

def echo():
    # This is the LEFT_SHIFT ability
    if msg in ["ab1", "shift"]:
        HoldAndReleaseKey(LEFT_SHIFT, 0.5)
    # This is the E ability
    if msg in ["ab2", "e"]:
        HoldAndReleaseKey(E, 0.5)
    # This is the RIGHT CLICK ability
    if msg in ["ab3", "right click"]:
        pydirectinput.mouseDown(button="right")
        time.sleep(0.5)
        pydirectinput.mouseUp(button="right")
    # Press the left mouse button down for 1 second, then release it
    if msg == "shoot": 
        pydirectinput.mouseDown(button="left")
        time.sleep(1.5)
        pydirectinput.mouseUp(button="left")

def genji():
    # This is the LEFT_SHIFT ability
    if msg in ["ab1", "shift"]:
        HoldAndReleaseKey(LEFT_SHIFT, 0.5)
    # This is the E ability
    if msg in ["ab2", "e"]:
        HoldAndReleaseKey(E, 0.5)
    # This is the RIGHT CLICK ability
    if msg in ["ab3", "right click"]:
        pydirectinput.mouseDown(button="right")
        time.sleep(0.5)
        pydirectinput.mouseUp(button="right")
    # Press the left mouse button down for 1 second, then release it
    if msg == "shoot": 
        pydirectinput.mouseDown(button="left")
        time.sleep(0.5)
        pydirectinput.mouseUp(button="left")

def hanzo():
    # This is the LEFT_SHIFT ability
    if msg in ["ab1", "shift"]:
        HoldAndReleaseKey(LEFT_SHIFT, 0.5)
    # This is the E ability
    if msg in ["ab2", "e"]:
        HoldAndReleaseKey(E, 0.5)
        pydirectinput.mouseDown(button="left")
        time.sleep(2.5)
        pydirectinput.mouseUp(button="left")
    if msg == "double jump":
        HoldAndReleaseKey(SPACE, 0.5)
        HoldAndReleaseKey(SPACE, 0.5)
    # Press the left mouse button down for 1 second, then release it
    if msg == "shoot": 
        pydirectinput.mouseDown(button="left")
        time.sleep(2)
        pydirectinput.mouseUp(button="left")

def junkrat():
    # This is the LEFT_SHIFT ability
    if msg in ["ab1", "shift"]:
        HoldAndReleaseKey(LEFT_SHIFT, 0.5)
    # This is the E ability
    if msg in ["ab2", "e"]:
        HoldAndReleaseKey(E, 0.5)
    # This is the RIGHT CLICK ability
    if msg in ["ab3", "right click"]:
        pydirectinput.mouseDown(button="right")
        time.sleep(0.5)
        pydirectinput.mouseUp(button="right")
    # Press the left mouse button down for 1 second, then release it
    if msg == "shoot": 
        pydirectinput.mouseDown(button="left")
        time.sleep(2)
        pydirectinput.mouseUp(button="left")

def mei():
    # This is the LEFT_SHIFT ability
    if msg in ["ab1", "shift"]:
        HoldAndReleaseKey(LEFT_SHIFT, 0.5)
    # This is the E ability
    if msg in ["ab2", "e"]:
        HoldAndReleaseKey(E, 0.5)
    # This is the RIGHT CLICK ability
    if msg in ["ab3", "right click"]:
        pydirectinput.mouseDown(button="right")
        time.sleep(0.5)
        pydirectinput.mouseUp(button="right")
    # Press the left mouse button down for 1 second, then release it
    if msg == "shoot": 
        pydirectinput.mouseDown(button="left")
        time.sleep(2)
        pydirectinput.mouseUp(button="left")

def pharah():
    # This is the LEFT_SHIFT ability
    if msg in ["ab1", "shift"]:
        HoldAndReleaseKey(LEFT_SHIFT, 0.5)
    # This is the E ability
    if msg in ["ab2", "e"]:
        HoldAndReleaseKey(E, 0.5)
    # This is the RIGHT CLICK ability
    if msg in ["ab3", "right click"]:
        pydirectinput.mouseDown(button="right")
        time.sleep(0.5)
        pydirectinput.mouseUp(button="right")
    # Press the left mouse button down for 1 second, then release it
    if msg == "shoot": 
        pydirectinput.mouseDown(button="left")
        time.sleep(2)
        pydirectinput.mouseUp(button="left")
    # Start FLYING
    if msg == "fly":
        HoldAndReleaseKey(SPACE, 3)

def reaper():
    # This is the LEFT_SHIFT ability
    if msg in ["ab1", "shift"]:
        HoldAndReleaseKey(LEFT_SHIFT, 0.5)
    # This is the E ability
    if msg in ["ab2", "e"]:
        HoldAndReleaseKey(E, 0.5)
    # This is the RIGHT CLICK ability
    if msg in ["ab3", "right click"]:
        pydirectinput.mouseDown(button="right")
        time.sleep(0.5)
        pydirectinput.mouseUp(button="right")
    # Press the left mouse button down for 1 second, then release it
    if msg == "shoot": 
        pydirectinput.mouseDown(button="left")
        time.sleep(2)
        pydirectinput.mouseUp(button="left")

def sojourn():
    # This is the LEFT_SHIFT ability
    if msg in ["ab1", "shift"]:
        HoldAndReleaseKey(LEFT_SHIFT, 0.5)
    # This is the E ability
    if msg in ["ab2", "e"]:
        HoldAndReleaseKey(E, 0.5)
    # This is the RIGHT CLICK ability
    if msg in ["ab3", "right click"]:
        pydirectinput.mouseDown(button="right")
        time.sleep(0.5)
        pydirectinput.mouseUp(button="right")
    # Press the left mouse button down for 1 second, then release it
    if msg == "shoot": 
        pydirectinput.mouseDown(button="left")
        time.sleep(2)
        pydirectinput.mouseUp(button="left")

def soldier():
    # This is the LEFT_SHIFT ability
    if msg in ["ab1", "shift", "run"]:
        HoldKey(SHIFT)
        HoldKey(W)
    # This is the E ability
    if msg in ["ab2", "e"]:
        HoldAndReleaseKey(E, 0.5)
    # This is the RIGHT CLICK ability
    if msg in ["ab3", "right click"]:
        pydirectinput.mouseDown(button="right")
        time.sleep(0.5)
        pydirectinput.mouseUp(button="right")
    # Press the left mouse button down for 1 second, then release it
    if msg == "shoot": 
        pydirectinput.mouseDown(button="left")
        time.sleep(2)
        pydirectinput.mouseUp(button="left")

def sombra():
    # This is the LEFT_SHIFT ability
    if msg in ["ab1", "shift"]:
        HoldAndReleaseKey(LEFT_SHIFT, 1.5)
    # This is the E ability
    if msg in ["ab2", "e"]:
        HoldAndReleaseKey(E, 0.5)
    # This is the RIGHT CLICK ability
    if msg in ["ab3", "right click"]:
        pydirectinput.mouseDown(button="right")
        time.sleep(2)
        pydirectinput.mouseUp(button="right")
    # Press the left mouse button down for 1 second, then release it
    if msg == "shoot": 
        pydirectinput.mouseDown(button="left")
        time.sleep(2)
        pydirectinput.mouseUp(button="left")

def symmetra():
    # This is the LEFT_SHIFT ability
    if msg in ["ab1", "shift"]:
        HoldAndReleaseKey(LEFT_SHIFT, 0.5)
    # This is the E ability
    if msg in ["ab2", "e"]:
        HoldAndReleaseKey(E, 0.5)
    # This is the RIGHT CLICK ability
    if msg in ["ab3", "right click"]:
        pydirectinput.mouseDown(button="right")
        time.sleep(1.5)
        pydirectinput.mouseUp(button="right")
    # Press the left mouse button down for 1 second, then release it
    if msg == "shoot": 
        pydirectinput.mouseDown(button="left")
        time.sleep(2)
        pydirectinput.mouseUp(button="left")

def torbjorn():
    # This is the LEFT_SHIFT ability
    if msg in ["ab1", "shift"]:
        HoldAndReleaseKey(LEFT_SHIFT, 0.5)
    # This is the E ability
    if msg in ["ab2", "e"]:
        HoldAndReleaseKey(E, 0.5)
    # This is the RIGHT CLICK ability
    if msg in ["ab3", "right click"]:
        pydirectinput.mouseDown(button="right")
        time.sleep(0.5)
        pydirectinput.mouseUp(button="right")
    # Press the left mouse button down for 1 second, then release it
    if msg == "shoot": 
        pydirectinput.mouseDown(button="left")
        time.sleep(2)
        pydirectinput.mouseUp(button="left")