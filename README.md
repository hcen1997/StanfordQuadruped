# StanfordQuadruped    
## joystick replacement  
### html and phone  
after the  calibration  i'm sure the dog is ok to go.  
but i don't have a joystick and i'm a happy coder.  
so i'm planning to do use my android touch screen and  
some web code to simulate a joystick.  
  
### code explanation  
here is some structure.    
controller.html is for android app or browser.  
WebInterface.py is the web-server.    
they two get human command and translate to machine code for JoystickInterface.py  
  
   
### diagram  
  ||  
        |--> ps4 joystick    --> PupperCommand   --|  
human --|                                          |--> JoystickInterface.py  
        |--> controller.html --> WebInterface.py --|    

  
### other  
do-what-ever-you-like  
