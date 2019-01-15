import RPi.GPIO as GPIO

# set up GPIO pins as outputs
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
LED1 = 21
BUZZ = 20
MOT = 16

GPIO.setup(LED1, GPIO.OUT, initial = False)# Output set 
GPIO.setup(BUZZ, GPIO.OUT, initial = False)# Output set
GPIO.setup(MOT, GPIO.OUT, initial = False)# Output set

MonAMOn = ()
MonPMOn = ()
TueAMOn = ()
TuePMOn = ()
WedAMOn = ()
WedPMOn = ()
ThuAMOn = ()
ThuPMOn = ()
FriAMOn = ()
FriPMOn = ()
SatAMOn = ()
SatPMOn = ()
SunAMOn = ()
SunPMOn = ()

class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

# import date and time modules
import datetime
import time


def verify_pin(pin):    
    if pin == '1234' :     #pin is set as 1234
            return True
    else :
         return false

def log_in( ):
        tries = 0
        while tries < 4:            #gives the user 4 tries 
            pin = input('Please Enter Your 4 Digit Pin:  ')
            if verify_pin(pin) :
                print ('Pin accepted!')     #if correctpin is entered then say 'accepted'
                return True
        else:
                print('Invalid pin')            #if anything else print invalid
                tries+= 1
        print('Too many incorrect tries. Could not log in')
        return False

def start_menu( ):
        print("Welcome To Oscar's Pill Dispenser")
        if log_in( ) :
            print ('Program loading......')      
start_menu( )

person = input("\n"" Enter your name: ")             #asks for the user to enter their name and labels it as 'person'
greeting = 'Hello, {}!'.format(person)
print (greeting)
print ("\n" * 4)

def main_menu():
    print ("\t""__________________________________________")
    print ("\t"" Main Menu ")
    print ("\t"" Option 1 set Monday's time")
    print ("\t"" Option 2 set Tuesday's time")
    print ("\t"" Option 3 set Wednesday's time")
    print ("\t"" Option 4 set Thursday's time")
    print ("\t"" Option 5 set Friday's time")
    print ("\t"" Option 6 set Saturday's time")
    print ("\t"" Option 7 set Sunday's time")
    print ("\t"" Option 8 Manually cycle Pill dispenser")
    print ("\t"" Option 9 to exit program")
    print("\t""-------------------------------------------------------------------------")

loop = 1 #sets loop
number = 0 #sets menu choice to zero
while loop == 1: #starts loop
        number = main_menu()
        number  = int(input ("\n""Please enter your option from 1-9 "))
# while True:
            #try:

            #except ValueError:
                    #print ("Not an integer, please try again with value between 1 to 9 ")
                    #continue
            #if number <= 9:
                    #break         
   
        if number == 1:         # Monday
            while True:
                try:
                   MonAMOn  = int(input ('What hour (0 to 12) would you like your Monday AM pills to be dispensed ?    '))
                except ValueError:
                        print ("Not an integer, please try again with value between 0 and 12")
                        continue
                if MonAMOn <= 12:
                        break
            while True:
                try:
                   MonPMOn  = int(input ('What hour (13 to 23) would you like your Monday PM pills to be dispensed ?    '))
                except ValueError:
                        print ("Not an integer, please try again with value between 13 and 23")
                        continue
                if MonPMOn >= 13 and MonPMOn <=23:
                        break
            print ('Okay, your morning pills will dispense at', MonAMOn)
            time.sleep(1)
            print ('And your evening pills will dispensed at', MonPMOn)


        elif number == 2:         # Tuesday
            while True:
                try:
                   TueAMOn  = int(input ('What hour (0 to 12) would you like your Tuesday AM pills to be dispensed ?    '))
                except ValueError:
                        print ("Not an integer, please try again with value between 0 and 12")
                        continue
                if TueAMOn <= 12:
                        break

            while True:
                try:
                   TuePMOn  = int(input ('What hour (13 to 23) would you like your Tuesday PM pills to be dispensed ?    '))
                except ValueError:
                        print ("Not an integer, please try again with value between 13 and 23")
                        continue
                if TuePMOn >= 13 and TuePMOn <=23:
                        break
            print ('Okay, your morning pills will dispense at', TueAMOn)
            time.sleep(1)
            print ('And your evening pills will dispensed at', TuePMOn)

        elif number == 3:
        # Wednesday
          
            while True:
                try:
                    WedAMOn  = int(input ('What hour (0 to 12) would you like your Wednesday AM pills to be dispensed ?    '))
                except ValueError:
                        print ("Not an integer, please try again with value between 0 and 12")
                        continue
                if WedAMOn <= 12:
                        break

            while True:
                try:
                   WedPMOn  = int(input ('What hour (13 to 23) would you like your Wednesday PM pills to be dispensed ?    '))
                except ValueError:
                        print ("Not an integer, please try again with value between 13 and 23")
                        continue
                if WedPMOn >= 13 and WedPMOn <=23:
                        break
            print ('Okay, your morning pills will dispense at', WedAMOn)
            time.sleep(1)
            print ('And your evening pills will dispensed at', WedPMOn)

        elif number == 4:
        # Thursday
           
            while True:
                try:
                    ThuAMOn  = int(input ('What hour (0 to 12) would you like your Thursday AM pills to be dispensed ?    '))
                except ValueError:
                        print ("Not an integer, please try again with value between 0 and 12")
                        continue
                if ThuAMOn <= 12:
                        break

            while True:
                try:
                    ThuPMOn  = int(input ('What hour (13 to 23) would you like your Thursday PM pills to be dispensed ?    '))
                except ValueError:
                        print ("Not an integer, please try again with value between 13 and 23")
                        continue
                if ThuPMOn >= 13 and ThuPMOn <=23:
                        break
            print ('Okay, your morning pills will dispense at', ThuAMOn)
            time.sleep(1)
            print ('And your evening pills will dispensed at', ThuPMOn)

        elif number == 5:
        # Friday
           
            while True:
                try:
                    FriAMOn  = int(input ('What hour (0 to 12) would you like your Friday AM pills to be dispensed ?    '))
                except ValueError:
                        print ("Not an integer, please try again with value between 0 and 12")
                        continue
                if FriAMOn <= 12:
                        break

            while True:
                try:
                    FriPMOn  = int(input ('What hour (13 to 23) would you like your Friday PM pills to be dispensed ?    '))
                except ValueError:
                        print ("Not an integer, please try again with value between 13 and 23")
                        continue
                if FriPMOn >= 13 and FriPMOn <=23:
                        break
            print ('Okay, your morning pills will dispense at', FriAMOn)
            time.sleep(1)
            print ('And your evening pills will dispensed at', FriPMOn)

        elif number == 6:
        # Saturday
            
            while True:
                try:
                    SatAMOn  = int(input ('What hour (0 to 12) would you like your Saturday AM pills to be dispensed ?    '))
                except ValueError:
                        print ("Not an integer, please try again with value between 0 and 12")
                        continue
                if SatAMOn <= 12:
                       break

            while True:
                try:
                    SatPMOn  = int(input ('What hour (13 to 23) would you like your Saturday PM pills to be dispensed ?    '))
                except ValueError:
                        print ("Not an integer, please try again with value between 13 and 23")
                        continue
                if SatPMOn >= 13 and SatPMOn <=23:
                        break
            print ('Okay, your morning pills will dispense at', SatAMOn)
            time.sleep(1)
            print ('And your evening pills will dispensed at', SatPMOn)

        elif number == 7:         # Sunday
            
            while True:
                try:
                    SunAMOn  = int(input ('What hour (0 to 12) would you like your Sunday AM pills to be dispensed ?    '))
                except ValueError:
                        print ("Not an integer, please try again with value between 0 and 12")
                        continue
                if SunAMOn <= 12:
                        break

            while True:
                try:
                    SunPMOn  = int(input ('What hour (13 to 23) would you like your Sunday PM pills to be dispensed ?    '))
                except ValueError:
                        print ("Not an integer, please try again with value between 13 and 23")
                        continue
                if SunPMOn >= 13 and SunPMOn <=23:
                        break
            print ('Okay, your morning pills will dispense at', SunAMOn)
            time.sleep(1)
            print ('And your evening pills will dispensed at', SunPMOn)

        elif number == 8:         # System Override
            print ("System test running ")
            
        elif number == 9: # Exit
            print (" Goodbye")
            loop = 0
            exit()         


    #get the current time in hours, minutes and seconds
        currTime = datetime.datetime.now()
    #get the current day of the week (0=Monday, 1=Tuesday, 2=Wednesday...)
        currDay = datetime.date.today().weekday()

   #Check to see if it's time to run the appliance for the AM hours
        while (currTime.hour == MonAMOn and currDay == 0 or currTime.hour == TueAMOn and currDay == 1 or currTime.hour == WedAMOn and currDay == 2 or currTime.hour == ThuAMOn and currDay == 3 or currTime.hour == FriAMOn and currDay == 4 or currTime.hour == SatAMOn and currDay == 5 or currTime.hour == SunAMOn and currDay == 6 or currTime.hour == SunAMOn and currDay == 6 or number == 8):   #and currTime.hour <= OffTimeAM[currDay].hour):
            # set GPIO outputs 
             print ('Appliance On AM')
             GPIO.output(LED1, True)      #Turns LED on and off every second
             GPIO.output(BUZZ, True) 
             time.sleep(1)
             GPIO.output(LED1,False)
             GPIO.output(BUZZ, False)
             time.sleep(1)
             GPIO.output(LED1,True)
             GPIO.output(BUZZ, True)
             time.sleep(1)
             GPIO.output(LED1,False)
             GPIO.output(BUZZ, False)
             time.sleep(1)
             GPIO.output(LED1,True)
             GPIO.output(BUZZ, True)
             time.sleep(1)
             GPIO.output(LED1,False)   #LED stop flashing
             GPIO.output(BUZZ,False)
             time.sleep(1)
             GPIO.output(LED1,True)
             GPIO.output(BUZZ, True)
             time.sleep(1)
             GPIO.output(LED1,False)   #LED stop flashing
             GPIO.output(BUZZ,False)
             GPIO.output(MOT, True)
             time.sleep(9.1) #Motor running time
             GPIO.output(LED1, False)
             GPIO.output(BUZZ, False)
             GPIO.output(MOT, False)
             print ('Pill dispenser Off AM')
             GPIO.cleanup()
             time.sleep(6) #checks every hour
             
     
    #Check to see if it's time to run the appliance for the PM hours
        while (currTime.hour == MonPMOn and currDay == 0 or currTime.hour == TuePMOn and currDay == 1 or currTime.hour == WedPMOn and currDay == 2 or currTime.hour == ThuPMOn and currDay == 3 or currTime.hour == FriPMOn and currDay == 4 or currTime.hour == SatPMOn and currDay == 5 or currTime.hour == SunPMOn and currDay == 6):#OnTimePM
            print ('Pill dispenser On PM')
            GPIO.output(LED1, True)      #Turns LED on and off every second
            GPIO.output(BUZZ, True) 
            time.sleep(1)
            GPIO.output(LED1,False)
            GPIO.output(BUZZ, False)
            time.sleep(1)
            GPIO.output(LED1,True)
            GPIO.output(BUZZ, True)
            time.sleep(1)
            GPIO.output(LED1,False)
            GPIO.output(BUZZ, False)
            time.sleep(1)
            GPIO.output(LED1,True)
            GPIO.output(BUZZ, True)
            time.sleep(1)
            GPIO.output(LED1,False)   #LED stop flashing
            GPIO.output(BUZZ,False)
            time.sleep(1)
            GPIO.output(LED1,True)
            GPIO.output(BUZZ, True)
            time.sleep(1)
            GPIO.output(LED1,False)   #LED stop flashing
            GPIO.output(BUZZ,False)
            GPIO.output(MOT, True)
            time.sleep(9.1) #Motor running time
            GPIO.output(LED1, False)
            GPIO.output(BUZZ, False)
            GPIO.output(MOT, False)
            print ('Pill dispenser Off PM')
            GPIO.cleanup()
            time.sleep(6) #checks every hour


  

            

