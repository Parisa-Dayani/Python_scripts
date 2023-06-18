import os
import time


choice=input("Please select one of the following:\nA.shutdown\nB.Restart\nC.Cancel\n")

if choice == "A":
    def shutdown():
      os.system("shutdown /s /t 1")
    set_time =input("Please insert your desire time (based on minutes) ")
    set_time =int(set_time)
    sec = 60
    print("Computer Will Now Shutdown in " + str(set_time) + "Minutes")
    time.sleep(set_time * sec)
    print("\n")
    print("Computer Will Now Shutdown!")
    time.sleep(3)
    shutdown()
elif choice == "B":
    def Restart():
      os.system("shutdown /r /t 1")
    set_time =input("Please insert your desire time (based on minutes) ")
    set_time =int(set_time)
    sec = 60
    print("Computer Will Now Restart in " + str(set_time) + "Minutes")
    time.sleep(set_time * sec)
    print("\n")
    print('Computer Will Now Restart!')
    time.sleep(3)
    Restart()
elif choice == "C":
    print("Canceled!")
    exit()
else:
    print("Wrong choice!")
    
