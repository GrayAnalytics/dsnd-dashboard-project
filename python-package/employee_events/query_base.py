# Import any dependencies needed to execute sql queries
from sqlite3 import connect
from pathlib import Path
from functools import wraps
import pandas as pd
#from sql_execution import QueryMixin
from employee_events.sql_execution import QueryMixin

# Define a class called QueryBase
# Use inheritance to add methods
# for querying the employee_events database.

class QueryBase(QueryMixin):

    # Create a class attribute called `name`
    # set the attribute to an empty string
    name = ''

    # Define a `names` method that receives
    # no passed arguments
    def names(self):
        
        # Return an empty list
        return []


    # Define an `event_counts` method
    # that receives an `id` argument
    # This method should return a pandas dataframe
    def event_counts(self,id):

        # QUERY 1
        # Write an SQL query that groups by `event_date`
        # and sums the number of positive and negative events
        # Use f-string formatting to set the FROM {table}
        # to the `name` class attribute
        # Use f-string formatting to set the name
        # of id columns used for joining
        # order by the event_date column
        result = self.pandas_query(f''' 
                             select 
                                event_date,
                                sum(positive_events	) as positive_events,
                                sum(negative_events) as negative_events
                             from employee_events
                             inner join {self.name} on employee_events.{self.name}_id = {self.name}.{self.name}_id
                             and employee_events.{self.name}_id = {id}
                             group by event_date
                             order by event_date
                             ''')
        

        return result
    
## blag = QueryMixin()
## print( blag.pandas_query(''' select * from notes''').head()  )



    # Define a `notes` method that receives an id argument
    # This function should return a pandas dataframe
    def notes(self, id):

        # QUERY 2
        # Write an SQL query that returns `note_date`, and `note`
        # from the `notes` table
        # Set the joined table names and id columns
        # with f-string formatting
        # so the query returns the notes
        # for the table name in the `name` class attribute
        result = self.pandas_query(f''' 
                                select distinct
                                    note_date, note 
                                from notes
                                inner join {self.name} on notes.{self.name}_id = {self.name}.{self.name}_id
                                       and {self.name}.{self.name}_id = {id}
                             ''')
        return result




## blag = QueryBase()
## blag.name = 'team'
## blig = blag.notes(id = 'team_id')
## print(blig.head() )



## blig = Employee()
## print( blig.notes().head() ) 
## print( blig.event_counts().head() )


## blag = Team()
## print( blag.notes().head())
## print( blag.event_counts().head() ) 


