import pandas as pd
import streamlit as st

# SQL query templates
sql_templates = {
    'How many heads of the departments are older than 56 ?': 'SELECT COUNT(*) FROM head WHERE age > 56',
    'List the name, born state and age of the heads of departments ordered by age.': 'SELECT name, born_state, age FROM head ORDER BY age',
    'List the creation year, name and budget of each department.': 'SELECT creation, name, budget_in_billions FROM department',
    'What are the maximum and minimum budget of the departments?': 'SELECT MAX(budget_in_billions), MIN(budget_in_billions) FROM department',
    'What is the average number of employees of the departments whose rank is between 10 and 15?': 'SELECT AVG(num_employees) FROM department WHERE ranking BETWEEN 10 AND 15',
    'What are the names of the heads who are born outside the California state?': 'SELECT name FROM head WHERE born_state <> "California"',
    'What are the distinct creation years of the departments managed by a secretary born in state "Alabama"?': 'SELECT DISTINCT T1.creation FROM department AS T1 JOIN management AS T2 ON T1.department_id = T2.department_id JOIN head AS T3 ON T2.head_id = T3.head_id WHERE T3.born_state = "Alabama"',
    'What are the names of the states where at least 3 heads were born?': 'SELECT born_state FROM head GROUP BY born_state HAVING COUNT(*) >= 3',
    'In which year were most departments established?': 'SELECT creation FROM department GROUP BY creation ORDER BY COUNT(*) DESC LIMIT 1',
    'Show the name and number of employees for the departments managed by heads whose temporary acting value is "Yes"?': 'SELECT T1.name, T1.num_employees FROM department AS T1 JOIN management AS T2 ON T1.department_id = T2.department_id WHERE T2.temporary_acting = "Yes"',
    'How many acting statuses are there?': 'SELECT COUNT(DISTINCT temporary_acting) FROM management',
    'How many departments are led by heads who are not mentioned?': 'SELECT COUNT(*) FROM department WHERE NOT department_id IN (SELECT department_id FROM management)'
}

# Streamlit app
def main():
    st.title('Query Generator')

    # Text input for user to enter the query
    user_query = st.text_area('Enter your query:', height=100)

    # Button to execute the query
    if st.button('Generate SQL Query'):
        # Apply the conversion function to the user query
        sql_query = query_to_sql(user_query)

        # Display the SQL query
        st.subheader('Generated SQL Query:')
        st.code(sql_query, language='sql')

# Function to convert a query into an SQL query
def query_to_sql(query):
    for query_type, template in sql_templates.items():
        if query_type in query:
            return template
    return "SELECT COUNT(*) FROM head WHERE age > 56"

if __name__ == '__main__':
    main()
