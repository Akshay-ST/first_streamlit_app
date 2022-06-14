import streamlit as s
import pandas as pd
import requests as r
import snowflake.connector as sf
from urllib.error import URLError

s.title('My Parents New Healthy Diner')
s.header('Breakfast FAvourites')
s.text('🥣 Omega 3 & Blueberry Oatmeal')
s.text('🥗 Kale, Spinach & Rocket Smoothie')
s.text('🐔 Hard-Boiled Free-Range')
s.text('🥑🍞 Avocado Toast')

s.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')


#my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = pd.read_csv("fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

#s.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado', 'Strawberries'])
fruits_selected = s.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado', 'Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

#s.dataframe(my_fruit_list)
s.dataframe(fruits_to_show)

#New Section to import FruityVice API response
s.header('Fruityvice Fruit Advice!')
#fruit_choice = s.text_input('What fruit would you like information about?', 'Kiwi')
#s.write('The user entered', fruit_choice)
try:
    fruit_choice = s.text_input('What fruit would you like information about?')
    if not fruit_choice:
        s.error('Please select a fruit to get information.')
     else:
        fruityvice_response = r.get("https://Fruityvice.com/api/fruit/" + fruit_choice)
        fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
        s.dataframe(fruityvice_normalized)

#s.text(fruityvice_response.json()) 
#fruityvice_response = r.get("https://Fruityvice.com/api/fruit/" + fruit_choice)
#fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
#s.dataframe(fruityvice_normalized)

except URLError as e:
  s.error()

my_cnx = sf.connect(**s.secrets["snowflake"])
my_cur = my_cnx.cursor()
#my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_cur.execute("SELECT * from fruit_load_list")
my_data_row = my_cur.fetchall()
s.header("The fruit list contains:")
s.dataframe(my_data_row)

s.stop() 
  
add_my_fruit = s.text_input('What fruit would you like to add?')
if (add_my_fruit != ''):
  input_qur = "insert into fruit_load_list values (\'" + add_my_fruit + "\');"
  my_cur.execute(input_qur)
  s.write('Thanks for adding ',add_my_fruit)
