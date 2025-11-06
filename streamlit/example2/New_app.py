import streamlit as st,requests

rolenames=[]
st.markdown("Title")
mydata= requests.get(f'http://10.0.38.88:8001/api/Region').json()
for item in mydata:
    rolenames.append(item['rolename'])
selected=st.selectbox('Select an Rolename', rolenames)

tupledata=()
mydataintuple= requests.get(f'http://10.0.38.88:8001/api/Region').json()
for item in mydataintuple:
    tupledata=(item['rolename'])

selecteddata=st.selectbox('Select an Rolename tuple', tupledata)

dataforcheckbox=st.checkbox('Checkbox')

st.spinner('Spinner')
if st.checkbox('Balloons', False):
        st.balloons()
        st.camera_input("test")

st.header('Pokemon Images')
mypokemon=['charizard','pikachu','eevee','snorlax','garchomp','lucario']
pokemon=st.selectbox('Select a Pokemon', mypokemon)
if pokemon:
    requests=requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon}').json()
for img in requests['sprites'].values():
    if img is not None:
        if str(img)[-4:]=='.png':
            st.image(img)


if st.checkbox('Snow', False):
            st.snow()
