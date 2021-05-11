import tkinter as tk
import getInfo as gi

bg = 'DeepSkyBlue3'
font_small = ('montserrat', 10)
font_med = ('montserrat', 12)
font_lrg = ('montserrat', 30)
font_xl = ('montserrat', 50, 'bold')
dg = u'\N{degree sign}'
SUNNY = ['Clear', 'Sunny', 'Fair']
RAIN = ['Rain']
PARTLY_CLOUDY = ["Mostly Cloudy", "Partly Cloudy"]
CLOUDS = ['Clouds', 'Cloudy']
SNOW = ['Snow']
STORM = ['Thunderstorm']

def submit():
  city = city_entry.get()
  city_parts = city.split()

  if len(city_parts) > 1:
    new_city_list = []
    for part in city_parts:
      new_city_list.append(part.capitalize())
      new_city = ' '.join(new_city_list)
  else: 
    new_city = city.capitalize()

  state = state_entry.get()
  state = state.upper()
  location.config(text = f'{new_city}, {state}')

  currentDict = gi.getCurrentWX(city, state)
  fill_current(currentDict)

  forecastDict = gi.getForecast(city, state)
  fill_forecast(forecastDict)

  city_entry.delete(0, 50)
  state_entry.delete(0, 20)

def fill_current(wx_dict):
  current, feels, date_time, wind_spd, condition, humidity, hi, lo = wx_dict['current'], wx_dict['feels'], wx_dict['dateTime'], wx_dict['windSpd'], wx_dict['condition'], wx_dict['humidity'], wx_dict['hi'], wx_dict['lo']

  c_temp.configure(text = f'{current}{dg}F')
  fl.configure(text = f'Feels: {feels}')
  time_date.configure(text = f'Last Updated {date_time}')
  winds.configure(text = f'{wind_spd} mph')
  cond.configure(text = f'{condition}')
  hum.configure(text= f'{humidity}%')
  hi_lo.configure(text = f'{hi}   |   {lo}')

def fill_forecast(wx_dict):
  icon1_day.configure(text=wx_dict['day'][0])
  icon2_day.configure(text=wx_dict['day'][1])
  icon3_day.configure(text=wx_dict['day'][2])
  icon4_day.configure(text=wx_dict['day'][3])

  icon1_hi.configure(text=wx_dict['hi'][0])
  icon2_hi.configure(text=wx_dict['hi'][1])
  icon3_hi.configure(text=wx_dict['hi'][2])
  icon4_hi.configure(text=wx_dict['hi'][3])
  
  icon1_lo.configure(text=wx_dict['lo'][0])
  icon2_lo.configure(text=wx_dict['lo'][1])
  icon3_lo.configure(text=wx_dict['lo'][2])
  icon4_lo.configure(text=wx_dict['lo'][3])

  icon1_cond.configure(text=wx_dict['wxDescr'][0])
  icon2_cond.configure(text=wx_dict['wxDescr'][1])
  icon3_cond.configure(text=wx_dict['wxDescr'][2])
  icon4_cond.configure(text=wx_dict['wxDescr'][3])

root = tk.Tk()
root.geometry('600x400')
root.title('Weather')

current = tk.Frame(root, bg = bg)
current.place(x=0, y=0, relwidth=0.7, relheight=0.75)

forecast = tk.Frame(root, bg = bg)
forecast.place(x=420, y=0, relwidth=0.3, relheight=1)

search = tk.Frame(root, bg = bg)
search.place(x=0, y=300, relwidth=0.7, relheight=0.25)

# Current Weather
location = tk.Label(current, text='--', fg='white', bg=bg, font=font_lrg, anchor=tk.W)
location.place(x=20, y=2, relwidth=0.9, relheight=0.15)

country = tk.Label(current, text='United States', fg='white', font=font_med, bg=bg)
country.place(x=23, y=52)

wx_icon = tk.Label(current, fg='white', bg='yellow')
wx_icon.place(x=25, y=80, relwidth=0.3, relheight=0.3)

hi_temp = '--'
lo_temp = '--'
temp = 45
hi_lo = tk.Label(current, text=f'{hi_temp}    |    {lo_temp}', bg=bg, fg='white', font=('montserrat', 10), anchor=tk.W)
hi_lo.place(x=185, y=80, relwidth=0.2, relheight=0.05)

c_temp = tk.Label(current, text=f'--', fg='white', bg=bg, font=font_xl, anchor=tk.W)
c_temp.place(x=175, y=95, relwidth=0.5, relheight=0.2)

fl_temp =  '--'
fl = tk.Label(current, text=f'Feels: {fl_temp}', bg=bg, fg='white', font=font_small, anchor=tk.W)
fl.place(x=185, y=155, relwidth=0.2, relheight=0.05)

time_date = tk.Label(current, text='Last Updated  ----', font=font_small, bg=bg, anchor=tk.W)
time_date.place(x=25, y=180)

condition_title = tk.Label(current, text='Condition', bg=bg, font=font_med)
condition_title.place(x=25, y=210)

cond = tk.Label(current, text='--', fg='goldenrod', bg=bg, font=font_med)
cond.place(x=160, y=210)

winds_title = tk.Label(current, text='Winds', bg=bg, font=font_med)
winds_title.place(x=25, y=240)

winds = tk.Label(current, text='--', fg='goldenrod', bg=bg, font=font_med)
winds.place(x=160, y=240)

hum_title = tk.Label(current, text='Humidity', bg=bg, font=font_med)
hum_title.place(x=25, y=270)

hum = tk.Label(current, text='--', fg='goldenrod', bg=bg, font=font_med)
hum.place(x=160, y=270)

# 5 Day Forecast
icon1 = tk.Label(forecast, bg='yellow')
icon1.place(x=0, y=70, relwidth=0.3, relheight=0.1)

icon1_day = tk.Label(forecast, text='---', fg='white', font=font_med, bg=bg)
icon1_day.place(x=60, y=70)

icon1_cond = tk.Label(forecast, text='--', font=font_small, bg=bg)
icon1_cond.place(x=60, y=90)

icon1_hi = tk.Label(forecast, text='--', fg='green4', font='bold', bg=bg)
icon1_hi.place(x=120, y=70)

icon1_lo = tk.Label(forecast, text='--', fg='red4', font='bold', bg=bg)
icon1_lo.place(x=120, y=90)

icon2 = tk.Label(forecast, bg='yellow')
icon2.place(x=0, y=140, relwidth=0.3, relheight=0.1)

icon2_day = tk.Label(forecast, text='---', fg='white', font=font_med, bg=bg)
icon2_day.place(x=60, y=140)

icon2_cond = tk.Label(forecast, text='--', font=font_small, bg=bg)
icon2_cond.place(x=60, y=160)

icon2_hi = tk.Label(forecast, text='--', fg='green4', font='bold', bg=bg)
icon2_hi.place(x=120, y=140)

icon2_lo = tk.Label(forecast, text='--', fg='red4', font='bold', bg=bg)
icon2_lo.place(x=120, y=160)

icon3 = tk.Label(forecast, bg='yellow')
icon3.place(x=0, y=210, relwidth=0.3, relheight=0.1)

icon3_day = tk.Label(forecast, text='---', fg='white', font=font_med, bg=bg)
icon3_day.place(x=60, y=210)

icon3_cond = tk.Label(forecast, text='--', font=font_small, bg=bg)
icon3_cond.place(x=60, y=230)

icon3_hi = tk.Label(forecast, text='--', fg='green4', font='bold', bg=bg)
icon3_hi.place(x=120, y=210)

icon3_lo = tk.Label(forecast, text='--', fg='red4', font='bold', bg=bg)
icon3_lo.place(x=120, y=230)

icon4 = tk.Label(forecast, bg='yellow')
icon4.place(x=0, y=280, relwidth=0.3, relheight=0.1)

icon4_day = tk.Label(forecast, text='---', fg='white', font=font_med, bg=bg)
icon4_day.place(x=60, y=280)

icon4_cond = tk.Label(forecast, text='--', font=font_small, bg=bg)
icon4_cond.place(x=60, y=300)

icon4_hi = tk.Label(forecast, text='--', fg='green4', font='bold', bg=bg)
icon4_hi.place(x=120, y=280)

icon4_lo = tk.Label(forecast, text='--', fg='red4', font='bold', bg=bg)
icon4_lo.place(x=120, y=300)
 
# Search Section
city2 = tk.Label(search, text='City:', fg='white', bg=bg, font=font_med)
city2.place(x=25, y=10)

city_entry = tk.Entry(search, width=15)
city_entry.place(x=65, y=10)

state = tk.Label(search, text='State:', fg='white', bg=bg, font=font_med)
state.place(x=25, y=35)

state_entry = tk.Entry(search, width=5)
state_entry.place(x=75, y=35)

submit_button = tk.Button(search, text='Show Weather', bg='goldenrod', command=submit)
submit_button.place(x=25, y=60)

root.mainloop()