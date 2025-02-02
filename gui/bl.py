#import evdev
from evdev import InputDevice, categorize, ecodes
gamepad = InputDevice('/dev/input/event0')
aBtn = 304
bBtn = 305
yBtn = 308
xBtn = 307
up = 115
down = 114
left = 165
right = 163
playpause = 164
key_axis = []
value = 0
class xboxOne:
    def __init__(self):
        self.key_axis = ""
        self.value    = 0
    #     super().__init__(self,*args)
        # print(self.pushButton_Home)
    #creates object 'gamepad' to store the data
    #you can call it whatever you like
    #prints out device info at start
    print(gamepad)    
    
    #evdev takes care of polling the controller in a loop
    def testButtonCodes(self):
        for event in gamepad.read_loop():
            print(categorize(event))
    #star(left) = 158
    #select(right) =315
    #rb=311
    #rt
    # 
    def readXboxInput(self):
        # key_axis = ""
        for event in gamepad.read_loop():        
            self.key_axis = []
            self.value = 0
            if event.type == ecodes.EV_KEY:
                # print(ecodes)
                if event.value == 1:
                    if event.code == aBtn:
                        self.key_axis = "A"
                        # print("A")
                        # return self.key_axis
                    elif event.code == bBtn:
                        self.key_axis = "B"
                        # print("B")
                    elif event.code == playpause:
                        self.key_axis = "A"
                        # print("Play/Pause")
                    elif event.code == up:
                        self.key_axis = "A"
                        # print("up")
                    elif event.code == down:
                        self.key_axis = "A"
                        # print("down")
                    elif event.code == left:
                        self.key_axis = "A"
                        # print("left")
                    elif event.code == right:
                        self.key_axis = "A"
                        # print("right")
                    elif event.code == yBtn:
                        self.key_axis = "Y"
                        # print("Y")
                    elif event.code == xBtn:
                        self.key_axis = "X"
                        # print("X")
                    return self.key_axis
            elif event.type == ecodes.EV_ABS:
                if not event.value == 0:
                    absevent = categorize(event)
                    #print(absevent.event)
                    print(ecodes.bytype[absevent.event.type][absevent.event.code], absevent.event.value)
                    a = (ecodes.bytype[absevent.event.type][absevent.event.code], absevent.event.value)           
                    #print(a[1])
                    if a[0] == "ABS_BRAKE":
                        self.key_axis ="Brake"
                        self.value    = a[1]
                        # print("Brake")

                    elif a[0] == "ABS_GAS":
                        self.key_axis ="Gas"
                        self.value    = a[1]
                        # print("Gas")

                    elif a[0] == "ABS_HAT0X" and a[1] == -1:
                        self.key_axis ="Left"
                        self.value    = a[1]
                        # print("Hat0 Left")

                    elif a[0] == "ABS_HAT0X" and a[1] == 1:
                        self.key_axis ="Right"
                        self.value    = a[1]                    
                        # print("Hat0 Right")

                    elif a[0] == "ABS_HAT0Y" and a[1] == -1:
                        self.key_axis ="Up"
                        self.value    = a[1]
                        # print("Hat0 UP")

                    elif a[0] == "ABS_HAT0Y" and a[1] == 1:
                        self.key_axis ="Down"
                        self.value    = a[1]
                        # print("Hat0 Down")

                    elif a[0] == "ABS_Y":
                        self.key_axis ="JoyY"
                        self.value    = a[1]
                        print("joy Up/Down")

                    elif a[0] == "ABS_X":
                        self.key_axis ="JoyX"
                        self.value    = a[1]
                        print("joy Left/Right")
                    
                    elif a[0] == "ABS_RZ":
                        self.key_axis ="JoyRZ"
                        self.value    = a[1]
                        print("joyZ Left/Right")

                    elif a[0] == "ABS_Z":
                        self.key_axis ="JoyZ"
                        self.value    = a[1]
                        print("joyZ Up/Down")

                    if not self.key_axis == []:
                        return self.key_axis, self.value
            #print(key_axis)
            
            # return self.key_axis, self.value
#readXboxInput()