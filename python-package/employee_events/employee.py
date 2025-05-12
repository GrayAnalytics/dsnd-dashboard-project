# Import the QueryBase class
#from query_base import QueryBase
from employee_events.query_base import QueryBase

# Import dependencies needed for sql execution
# from the `sql_execution` module
from sqlite3 import connect
from pathlib import Path
from functools import wraps
import pandas as pd
#from sql_execution import QueryMixin
from employee_events.sql_execution import QueryMixin

# Define a subclass of QueryBase
# called Employee

class Employee(QueryBase):


    # Set the class attribute `name`
    # to the string "employee"
    name = 'employee'
    #id = 'employee_id'

    #def event_counts(self):
    #    return super().event_counts(id = self.id)
    
    #def notes(self):
    #    return super().notes(id = self.id)


    # Define a method called `names`
    # that receives no arguments
    # This method should return a list of tuples
    # from an sql execution
    def names(self):
        # Query 3
        # Write an SQL query
        # that selects two columns 
        # 1. The employee's full name
        # 2. The employee's id
        # This query should return the data
        # for all employees in the database
        return self.query(f'''select
                            first_name || ' ' || last_name as full_name,
                            employee_id
                            from employee ''')

    # Define a method called `username`
    # that receives an `id` argument
    # This method should return a list of tuples
    # from an sql execution
    def username(self, id):
        
        # Query 4
        # Write an SQL query
        # that selects an employees full name
        # Use f-string formatting and a WHERE filter
        # to only return the full name of the employee
        # with an id equal to the id argument
        #### YOUR CODE HERE
        return self.query(f'''select
                            first_name || ' ' || last_name as full_name
                            from employee 
                            where employee_id = {id}''')
        


    # Below is method with an SQL query
    # This SQL query generates the data needed for
    # the machine learning model.
    # Without editing the query, alter this method
    # so when it is called, a pandas dataframe
    # is returns containing the execution of
    # the sql query
    #### YOUR CODE HERE
    def model_data(self, id):

        return self.pandas_query(  f"""
                    SELECT SUM(positive_events) positive_events
                         , SUM(negative_events) negative_events
                    FROM {self.name}
                    JOIN employee_events
                        USING({self.name}_id)
                    WHERE {self.name}.{self.name}_id = {id}
                """)


