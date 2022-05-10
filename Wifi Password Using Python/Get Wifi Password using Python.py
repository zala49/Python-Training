# Get Wifi Password using Python

# import subprocess 
import subprocess

# store profiles data in "data" variable by using subprocess.check_output
data = subprocess.check_output(['netsh','wlan','show','profiles']).decode('utf-8').split('\n')

# store profile by converting them to list
profile = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]

#using for loop in python checking & printing the wifi passwords if available
for i in profile:
    # check password
    results = subprocess.check_output(['netsh','wlan','show','profile',i, 'key=clear']).decode('utf-8').split('\n')

    #Storing password and converting them to list
    results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
    try:
        print("{:<30}|  {:<}".format(i, results[0]))
    except IndexError:
            print("{:<30}|  {:<}".format(i, ""))