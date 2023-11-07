
from Exceptions.apiExceptions import *



def validate_input(input_field,required_field,is_body = True):
    # input fied: the field that the user inputs
    # required_field: the arguments that are needed for the function to be called correctly
    # is_body: just whether we should be checking the body or the params(soley for exceptions)
    
    input_field = set(input_field)
    missing = []
    for field in required_field:
        if field not in input_field:
            missing.append(field)
    if missing:
        if is_body:
            raise MissingArgumentException(missing_body_parts=missing)
        else:
            raise MissingParameterException
    return True
            
    