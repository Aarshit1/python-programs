def shutdown():
    switch=input("do you want to shut down the system? YES/NO : ")
    if(switch=="yes" or switch=="YES"):
        print("system shutting down")
    elif(switch=="no" or switch=="NO"):
        print("system shutdown aborted")
    else:
        print("sorry... what?")

shutdown()