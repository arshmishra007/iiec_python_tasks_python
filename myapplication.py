import os

print("____________________________________________Hello Arsh This Is Cortana Here!____________________________________________")
print()
while True:   
    print("___________________________________________What Program would you like to open?_________________________________________")
    p = input()
    if("run" in p) and (("browser" in p) or ("explorer" in p)):
        print("Opening a Browser!")
        os.system("iexplore")
    elif("run" in p) and (("mediaplayer" in p) or ("songplayer" in p)):
        print("Opening Media Player!")
        os.system("wmplayer")
    elif("run" in p) and (("notepad" in p)or("editor" in p)):
        print("Opening Text Editor! ")
        os.system("notepad")
    elif("calculator" in p):
        print("Opening Calculator")
        os.system("calc")    
    elif("run" in p) and (("jupyter" in p)or("IDE" in p)):
        print("Opening Jupyter IDE")
        os.system("jupyter notebook")
    elif("run" in p) and (("paint" in p) or ("drawing software" in p)):
        print("Opening Paint Software!")
        os.system("mspaint")
    elif("run" in p) and ("gitbash" in p):
        print("Opening Git Bash")
        os.system("git bash")
    elif("run" in p) and ("chrome" in p):
        print("Opening the Chrome Browser")
        os.system("chrome")
    elif("run" in p) and ("putty" in p):
        print("Opening Putty Software....")
        os.system("putty")
    elif("run" in p) and("kubernetes" in p):
        print("Opening the Kubernetes Cluster in VM....Might Take some time.....")      
        os.system("minikube.exe start")              
    elif("exit" in p):
        print("We are closing the program!")
        print("________________________________________________________________________________________________________________________")
        os.system(exit())
        break
    
                   


