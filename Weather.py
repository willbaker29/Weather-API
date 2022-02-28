from tkinter import *
from tkinter import messagebox
import requests
import time

  
key = '<KEY>' # API Key
loc_id = 3809 #MET Office Location ID (RNAS Couldrose)

api_request = 'http://datapoint.metoffice.gov.uk/public/data/val/wxobs/all/json/3809?res=hourly&key=<KEY>' # Request

def get_weather():
    """Performs an API request 

    Returns:
        List: Wind direction, speed, visability, temperature
    """    
    response = requests.get(api_request) 
    if response:
        json = response.json()
        wind_dir = json['SiteRep']['DV']['Location']['Period'][1]['Rep'][0]['D']
        wind_speed = json['SiteRep']['DV']['Location']['Period'][1]['Rep'][0]['S']
        visability = json['SiteRep']['DV']['Location']['Period'][1]['Rep'][0]['V']
        temp = json['SiteRep']['DV']['Location']['Period'][1]['Rep'][0]['T']
        pressure = json['SiteRep']['DV']['Location']['Period'][1]['Rep'][0]['P']
        final = (wind_dir, wind_speed, visability, temp)
        return final

    else:
        return None

#Configure GUI Display    
root = Tk() 
root.title("Weather")
root.geometry("400x700")
root['background'] = "white"

#Create Heading
head = Label(root, text = "Will's Weather App", font = ("Helvetica", 30), fg='red', bg='white') 
head.place(x=30, y=20)

#Configure Data Labels
temp_label = Label(root, text='Error')
temp_label.pack()
temp_label.place(x=50, y=100)

wind_label = Label(root, text='Error')
wind_label.pack()
wind_label.place(x=50, y=150)

vis_label = Label(root, text='Error')
vis_label.pack()
vis_label.place(x=50, y=200)

time_tag = Label(root, text='Error')
time_tag.pack()
time_tag.place(x=50, y=250)

#Populate data labels from get_weather function
weather = get_weather()
if weather:
    time_tag['text'] = '{}'.format(time.ctime())
    temp_label['text'] = 'Temperature: {}C'.format(weather[3])
    wind_label['text'] = 'Wind: {}, {} mph'.format(weather[0], weather[1])
    vis_label['text']= 'Visability: {}m'.format(weather[2])
    
else:
    messagebox.showerror('Cannot find weather')

root.mainloop()
