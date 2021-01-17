import time

#This will be my first attempt at a web blocker 

#initialize path, redirect, and websitelist variables
hostPath = r"C:\Windows\System32\drivers\etc\hosts"
redirect= "127.0.0.1"
websiteList = ["www.youtube.com", "www.facebook.com", "www.instagram.com"]

#this code shall run infinitely which is fun
while True:
  #this time sleep will keep the program from making the program explode your computer
  time.sleep(5)
  #open the ost file
  file = open(hostPath, 'r+')
  #read the host file
  fileContent = file.read()
  #add websites to host file
  for website in websiteList:
    if website in fileContent:
      pass
    else:
        file.write(redirect + " " + website + "\n")

  #close file(SUPER IMPORTANT)
  file.close()
