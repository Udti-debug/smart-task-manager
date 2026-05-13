import streamlit as st

st.title("Smart Task Manager")

# Store tasks
if "tasks" not in st.session_state:
    st.session_state.tasks = []

task = st.text_input("Enter your task")

if st.button("Add Task"):
    if task:
        # Category logic
        if "study" in task.lower():
            category = "Study"
        elif "project" in task.lower():
            category = "Work"
        else:
            category = "Personal"

        # Priority logic
        if "urgent" in task.lower():
            priority = "High"
        elif "later" in task.lower():
            priority = "Low"
        else:
            priority = "Medium"

        st.session_state.tasks.append((task, category, priority))
        st.success("Task Added!")

if st.button("Show Tasks"):
    for t in st.session_state.tasks:
        st.write(f"Task: {t[0]}")
        st.write(f"Category: {t[1]}")
        st.write(f"Priority: {t[2]}")
        st.write("---")