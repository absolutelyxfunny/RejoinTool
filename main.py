import subprocess
import threading
import os
import json
import time
import keyboard


def logo():
    os.system("cls")
    print("\033[95;1m"+ """
\t\t██████╗ ███████╗     ██╗ ██████╗ ██╗███╗   ██╗████████╗ ██████╗  ██████╗ ██╗         ██╗   ██╗██████╗ 
\t\t██╔══██╗██╔════╝     ██║██╔═══██╗██║████╗  ██║╚══██╔══╝██╔═══██╗██╔═══██╗██║         ██║   ██║╚════██╗
\t\t██████╔╝█████╗       ██║██║   ██║██║██╔██╗ ██║   ██║   ██║   ██║██║   ██║██║         ██║   ██║ █████╔╝
\t\t██╔══██╗██╔══╝  ██   ██║██║   ██║██║██║╚██╗██║   ██║   ██║   ██║██║   ██║██║         ╚██╗ ██╔╝██╔═══╝ 
\t\t██║  ██║███████╗╚█████╔╝╚██████╔╝██║██║ ╚████║   ██║   ╚██████╔╝╚██████╔╝███████╗     ╚████╔╝ ███████╗
\t\t╚═╝  ╚═╝╚══════╝ ╚════╝  ╚═════╝ ╚═╝╚═╝  ╚═══╝   ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝      ╚═══╝  ╚══════╝
                                                                                                      
"""+ "\033[0m")



def menu():
    global choose
    os.system("cls")

    logo()
    print("\t\t\t\t\t\tdsc.gg/xHelper | t.me/xhelpper\n\n")
    print("\033[95;1m" + "\t\t\t\t[1] Info about RejoinTool \t[2] Info about DetectFreeze"+ "\033[0m\n"
          "\033[95;1m" + "\t\t\t\t[3] Connect RejoinTool \t\t[4] Credits" + "\033[0m\n")
    choose = int(input("\033[95;1m" + "\t\t\t\t\t\tRejoinTool | Choose option >> " + "\033[0m"))
menu()





def back_menu():
    try:

        print("\033[95;1m" + "RejoinTool | Click enter to exit >> " + "\033[0m")
        keyboard.wait("Enter")
        menu()
    except:
        menu()


if choose == 1:

    os.system("cls")
    logo()
    print("This programme open roblox everytime when it crashed")
    back_menu()

if choose == 2:
    os.system("cls")
    logo()

    print("This function close all roblox with choosen coodlown")
    back_menu()

if choose == 4:
    os.system("cls")
    logo()

    print("DiscordServer: dsc.gg/xHelper\nTelegram: t.me/xhelpper\nDonationAlerts: https://www.donationalerts.com/r/xfunny\n")
    back_menu()

    




def back_menu():
    try:

        print("\033[95;1m" + "RejoinTool | Click enter to exit >> " + "\033[0m")
        keyboard.wait("Enter")
        try:
            menu()
        except:
            menu()
    except:
        pass




#logo()


def get_ports():

    path = os.getenv("ProgramFiles")
    main_path = path + "\\Netease\\MuMuPlayerGlobal-12.0\\vms"


    folders = os.listdir(main_path)


    def running_ports():
        

        global inactive2_info, active2_info, active_names, inactive_names

        active_emulators = []
        inactive_emulators = []
        active2_info = []
        inactive2_info = []
        active_names = []
        inactive_names = []

        try:
            for log in folders:
                logs = os.path.join(main_path,log, "logs")
                info = os.listdir(logs)

                if "vboxmanager.log" in info:
                    vbmanager = logs + "\\VBox.log"
                    with open(vbmanager, "r") as file:
                        content = file.read()
                        if "stopped" in content:

                            inactive_emulators.append(log)
                            for inactiveport in inactive_emulators:

                                configs = os.path.join(main_path, inactiveport, "configs")
                                shell_cfg = os.path.join(configs, "vm_config.json")
                                extra_cfg = os.path.join(configs, "extra_config.json")

                            if os.path.exists(shell_cfg):

                                with open(shell_cfg, "r") as file:

                                    content = file.read()
                                    contentV2 = json.loads(content)
                                    vm = contentV2["vm"]
                                    nat = vm["nat"]
                                    port_frwrd = nat["port_forward"]
                                    adb = port_frwrd["adb"]
                                    host_ports = adb["host_port"]
                                    inactive2_info.append(host_ports)
                            if os.path.exists(extra_cfg):
                                with open(extra_cfg, "r") as fileplr:
                                    cont = fileplr.read()
                                    contV2 = json.loads(cont)
                
                                    plr_name = contV2["playerName"]
                                    inactive_names.append(plr_name)




                                
                        else:

                            active_emulators.append(log)
                            for activeport in active_emulators:

                                configs = os.path.join(main_path, activeport, "configs")
                                shell_cfg = os.path.join(configs, "vm_config.json")
                                extra_cfg = os.path.join(configs, "extra_config.json")

                            if os.path.exists(shell_cfg):
                                with open(shell_cfg, "r") as file:

                                    content = file.read()
                                    contentV2 = json.loads(content)
                                    vm = contentV2["vm"]
                                    nat = vm["nat"]
                                    port_frwrd = nat["port_forward"]
                                    adb = port_frwrd["adb"]
                                    host_ports = adb["host_port"]
                                    active2_info.append(host_ports)

                            if os.path.exists(extra_cfg):
                                with open(extra_cfg, "r") as fileplr:
                                    cont = fileplr.read()
                                    contV2 = json.loads(cont)
                
                                    plr_name = contV2["playerName"]
                                    active_names.append(plr_name)





        except:
            pass
                    

    running_ports()





def full_ports():

    global inports
    print("\t\t\t\t\t\t==EmulatorsList==\n")
    for actnames, actports, in zip(active_names, active2_info):
        print(f"\t\t\t\t\t{actnames} | {actports} | Status: " + "\033[92m" + "Active" + "\033[0m")
    for innames, inports in zip(inactive_names, inactive2_info):
        print(f"\t\t\t\t\t{innames} | {inports} | Status: "+ "\033[91m" "Inactive" + "\033[0m")


def check_emulator(emul):

    global adb

    path = os.getenv("ProgramFiles")
    adb = path + "\\Netease\\MuMuPlayerGlobal-12.0\\shell\\adb.exe"
    #try:
        #subprocess.run(f"{adb} kill-server")
    #except:
        #pass
    try:
        subprocess.run(f"{adb} connect 127.0.0.1:{emul}", stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    

        while True:
            command = [adb, '-s', f'127.0.0.1:{emul}', 'shell', 'ps']
            result = subprocess.run(command, capture_output=True, text=True, check=True)
        
            if "com.roblox.client" in result.stdout:
                pass
            else:
                time.sleep(10)
                subprocess.run(f"{adb} -s 127.0.0.1:{emul} shell am start -a android.intent.action.VIEW -d roblox://placeId={place_id}", stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except:
        pass

def detect_freeze(emul):

    time.sleep(cooldown)
    subprocess.run(f"{adb} -s 127.0.0.1:{emul} shell am force-stop com.roblox.client", stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    



def rejoiner():
    threads = []
    for emul in active2_info:

        thread = threading.Thread(target=check_emulator, args=(emul,))
        threads.append(thread)

        thread_detect = threading.Thread(target=detect_freeze, args=(emul,))
        threads.append(thread_detect)


        thread.start()
        if detect == "y":
            thread_detect.start()

    for thread in threads:
        thread.join() 

def rejoinerV2():
    check = threading.Thread(target=rejoiner)
    check.start()

if choose == 3:
    os.system("cls")
    logo()
    detect = input("Enable DetectFreeze? Y/N >> ").lower()
    if detect == "y":
        cooldown = int(input("Type DetetctFreeze cooldown (in seconds) >> "))
    place_id = int(input("Type PlaceID (to join) >> "))
    os.system("cls")

    logo()
    get_ports()
    full_ports()
    print("\t\t\t\t\t\t==RejoinInfo==\n")
    print(f"\t\t\t\t\tPlaceID: {place_id}")
    if detect == "y":
        print(f"\t\t\t\t\tDetectFreeze: " + "\033[92m" + "Enabled" + "\033[0m")
    else:
        print(f"\t\t\t\t\tDetectFreeze: " + "\033[91m" + "Disabled" + "\033[0m")
    rejoiner()


#rejoinerV2()