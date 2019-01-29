#
#   BFH Demo Project for an Weather Station realised by Tinkerforge Bricklets
#   29.01.2019 by patrik.marti@bfh.ch
#   BFH Wirtschaftsingenieure Roadshow
#
# **************************************************************************

from tkinter import *
import tf

root = Tk()

altitude = 50000

#Images
photo_rain = PhotoImage(file="png\_rain_150_150.png" )
photo_partly_sunny = PhotoImage(file="png\_Partly_Sunny_150x150.png")
photo_sunny = PhotoImage(file="png\_sunny_150_150.png")
photo_storm = PhotoImage(file="png\storm_150_150.png")
photo_scattered_shower = PhotoImage(file="png\_scattered-shower_150_150.png")

#Set Windon Size and Title
root.title("BFH Wirtschaftsingenieure Roadshow")
root.iconbitmap(r"png\bfhlogo_icon.ico")
window_width=root.winfo_screenwidth() 
window_heigt=root.winfo_screenheight()

if window_width > 1280: root.geometry("800x480+20+20") 
else: root.geometry("%dx%d+20+20" % (window_width, window_heigt))

#Labels Objects 
space = Label(root, text="                         ", font='arial 24')
temp        = Label(root, text="0", font='arial 24')
temp_unit   = Label(root, text="° C", font='arial 24')
baro        = Label(root, text="0", font='arial 24')
baro_unit   = Label(root, text="mPa", font='arial 24')
humi        = Label(root, text="0", font='arial 24')
humi_unit   = Label(root, text="%", font='arial 24')
ambi        = Label(root, text="0", font='arial 24')
ambi_unit   = Label(root, text="lux", font='arial 24')

#Image
weatherConditions = Label(root)

#Set Layout and Font
space.grid(row=0, sticky=E)
space.grid(row=0, column=1)
weatherConditions.grid(row=1,column=2, rowspan = 4)
temp.grid(row=1, sticky=E)
temp_unit.grid(row=1, column=1, sticky=W)
baro.grid(row=2, sticky=E)
baro_unit.grid(row=2, column=1, sticky=W)
humi.grid(row=3, sticky=E)
humi_unit.grid(row=3, column=1, sticky=W)
ambi.grid(row=4, sticky=E)
ambi_unit.grid(row=4, column=1, sticky=W)

def update_status():

    # Get the current Data from Tinkerforge Sensors
    temperature, pressure, humidity, illuminance = tf.getAllData()
    pressureTot = pressure + altitude

    if pressureTot < 965000: weatherConditions.config(image=photo_storm)
    elif pressureTot >= 965000 and pressureTot < 990000: weatherConditions.config(image=photo_rain)
    elif pressureTot >= 990000 and pressureTot < 1010000: weatherConditions.config(image=photo_scattered_shower)
    elif pressureTot >= 1010000 and pressureTot < 1035000: weatherConditions.config(image=photo_partly_sunny)
    else: weatherConditions.config(image=photo_sunny)

    temp["text"] = str(round(temperature/100.0,1))
    baro["text"] = str(round(pressure/1000.0,1))
    humi["text"] = str(round(humidity/100.0,1))
    ambi["text"] = str(round(illuminance/100.0,1))

    # After 1 second, update the status
    root.after(1000, update_status)

# Launch the status message after 1 millisecond (when the window is loaded)
root.after(1, update_status)
root.mainloop()
