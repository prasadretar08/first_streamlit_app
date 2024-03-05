import streamlit

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

streamlit.header("Fruityvice Fruit Advice!")

fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)

streamlit.text(fruityvice_response.json())
# write your own comment -what does the next line do? 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
streamlit.dataframe(fruityvice_normalized)

import snowflake.connector

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
    streamlit.success(f"Thanks for adding {add_new_fruit}!")


