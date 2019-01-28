from tkinter import *
import tf

root = Tk()
#Creat a Layout

#Images
photo = PhotoImage(file="png\_rain_150_150.png" )
weatherConditions = Label(root, image=photo)

#Set Window
root.title("BFH WeatherStation")
root.geometry("800x480+250+250")

#Label Objects 
space = Label(root, text="                         ", font='arial 24')
temp = Label(root, text="0", font='arial 24')
baro = Label(root, text="0", font='arial 24')
humi = Label(root, text="0", font='arial 24')
ambi = Label(root, text="0", font='arial 24')

#Set Layout and Font
space.grid(row=0, sticky=E)
weatherConditions.grid(row=1,column=1)
temp.grid(row=1, sticky=E)
baro.grid(row=2, sticky=E)
humi.grid(row=3, sticky=E)
ambi.grid(row=4, sticky=E)

def update_status():

    # Get the current message
    temperature, pressure, humidity, illuminance = tf.getAllData()

    current_temp = temp["text"]
    current_baro = baro["text"]
    current_humi = humi["text"]
    current_ambi = ambi["text"]

    current_temp = str(temperature/100.0)+"° C"
    current_baro = str(pressure/1000.0)+" mPa"
    current_humi = str(humidity/100.0)+"%"
    current_ambi = str(illuminance/100.0)+" lux"

    # Update the message
    temp["text"] = current_temp
    baro["text"] = current_baro
    humi["text"] = current_humi
    ambi["text"] = current_ambi


    # After 1 second, update the status
    root.after(1000, update_status)

# Launch the status message after 1 millisecond (when the window is loaded)
root.after(1, update_status)
root.mainloop()

#    print("humidity    = "+ str(humidity/100.0)+"%")
#    print("illuminance = "+ str(illuminance/100.0)+" lux")