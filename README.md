Control Raspberry Pi LED with Webpage  Using Python and Flask




To Run in Your Raspberry Pi 

Follow the commandments in raspberry pi cmd


1 --
  
  
  sudo apt-get update
 
2--
  
  
  sudo apt-get upgrade

3--
  
  
  sudo apt-get install python3
  
4--
  
  
  sudo pip install flask
  
5--
  
  
  sudo apt-get install git
  
6--
  
  
  git clone https://github.com/Tony-Vaniya/FlaskPi.git
  
7--
  
  
  cd FlaskPi
  
8--
  
  
  sudo python3 main.py
  



 
#Start On Boot
##Follow The Command In cmd

1 --
  
  
  
  sudo nano /etc/profile
   
   
   ####In Last Add Line
   
      sudo python3 /home/pi/FlaskPi/main.py
    
   
