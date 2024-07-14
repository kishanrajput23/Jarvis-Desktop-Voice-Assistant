#import necessary functions
from jarvis_actions import takecommand
from evaluate_query import evaluate_query


#listen to user input and process query
def listen():
    query = takecommand().lower()
    evaluate_query(query)