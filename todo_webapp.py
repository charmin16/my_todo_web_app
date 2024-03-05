import streamlit as st
import functions

todo_list = functions.get_todos()
def add_todo():
    todo = st.session_state['new_todo'] + "\n"
    todo_list.append(todo)
    functions.write_todos(todo_list)

st.title('Todo App')

st.subheader('This is my todo app')
st.write('This app is to increase your productivity')


for index, item in enumerate(todo_list):
    checkbox = st.checkbox(item, key=item)
    if checkbox:
        #todo_list.pop(index)
        todo_list.remove(item)
        functions.write_todos((todo_list))
        del st.session_state[item]
        st.rerun()

st.text_input(label='', placeholder='Enter a todo', on_change=add_todo, key='new_todo')

#st.session_state

