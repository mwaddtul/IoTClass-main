# Module Controller.py
#Autheur Youssef Miri

########## Programme Arduino: Sur votre espace Arduino Ide vous allez sur File-> Examples-> Firmata->Standard Firmata puis upload.
### Les pins 9 10 11 12 et 13 sont reliés à la cathode (longue patte) et GND et relié à l'anode.

### Bonne lecture :)


import pyfirmata # Importe le module pyfirmata pour communiquer avec Arduino

comport='/dev/cu.usbmodem112201' 

# Initialise une connexion avec Arduino sur le port spécifié
board=pyfirmata.Arduino(comport)
# Initialise les broches de sortie sur lesquelles sont connectées les LED
led_1=board.get_pin('d:13:o')
led_2=board.get_pin('d:12:o')
led_3=board.get_pin('d:11:o')
led_4=board.get_pin('d:10:o')
led_5=board.get_pin('d:9:o')
# Définit une fonction pour contrôler les LED en fonction du nombre total de doigts levés
def led(total):
    if total==0: # Nombre de doigts 0
        led_1.write(0)
        led_2.write(0)
        led_3.write(0)
        led_4.write(0)
        led_5.write(0)
    elif total==1:# Nombre de doigts 1
        led_1.write(1)
        led_2.write(0)
        led_3.write(0)
        led_4.write(0)
        led_5.write(0)
    elif total==2:
        led_1.write(1)
        led_2.write(1)
        led_3.write(0)
        led_4.write(0)
        led_5.write(0)
    elif total==3:# Nombre de doigts 3
        led_1.write(1)
        led_2.write(1)
        led_3.write(1)
        led_4.write(0)
        led_5.write(0)
    elif total==4:# Nombre de doigts 4
        led_1.write(1)
        led_2.write(1)
        led_3.write(1)
        led_4.write(1)
        led_5.write(0)
    elif total==5: # Nombre de doigts 5
        led_1.write(1)
        led_2.write(1)
        led_3.write(1)
        led_4.write(1)
        led_5.write(1)

