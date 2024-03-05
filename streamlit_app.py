import streamlit
import snowflake.connector
import pandas
import snowflake.connector 
from urllib.error import URLError 

streamlit.title('My Praents New Healty Diner')
streamlit.header('Breakfast Menu') 
streamlit.text('Omega 3 * Blueberry Oatmeal')
streamlit.text('Kale, Spniach & Rocket Snoothie')
streamlit.text('Hard-Boiled Free-Range Egg')


import pandas 
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
fruits_selected= streamlit.multiselect("Pick some fruits" ,list(my_fruit_list.index), ['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)

#Create the repeatable code block ( Called a function)
def get_fruityvice_data(this_fruit_choice):
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + this_fruit_choice)
    fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
    return fruityvice_normalized 
    
#New Section to display fruityvice api response
streamlit.header("Fruityvice Fruit Advice!")
try:
    fruit_choice = streamlit.text_input('What fruit would you like information about?')
    #streamlit.write('The user entered ', fruit_choice)
    if not fruit_choice:
        #import requests
        streamlit.error("Please select a fruit to get information")
    else:
        back_from_function = get_fruityvice_data(fruit_choice)
        streamlit.dataframe(back_from_function)
except URLError as e:
    streamlit.error() 
    
streamlit.stop()
import streamlit
import snowflake.connector
import pandas
import snowflake.connector 
from urllib.error import URLError 

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
# Function to insert a new fruit into the database
def add_fruit_to_list(fruit_name):
    my_cur.execute("INSERT INTO fruit_load_list (fruit_name) VALUES (%s)", (fruit_name,))
    my_cnx.commit()   
my_cur.execute("SELECT * from fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.header("The fruit load list contains:")
streamlit.dataframe(my_data_rows)

# Allow the user to add a new fruit
add_new_fruit = streamlit.text_input("What fruit would you like to add?")
add_fruit_to_list(add_new_fruit)
streamlit.success(f"Thanks for adding {add_new_fruit}")


