from Exceptions.baseException import baseException

class MissingArgumentException(baseException):
    # this should be use for any api calls through the body
    error_code = 400
    message = "Missing one or more argument in body"
    def __init__(self,missing_body_parts= None):
        if missing_body_parts:
            
            super().__init__(f"Missing {','.join([parts for parts in missing_body_parts])} in body")

class MissingParameterException(Exception):
    # this should be used exclusively for get methods (or any that passes through the params)
    error_code = 400
    message = "Missing one or more paramter"
    def __init__(self,missing_param= None):
        if missing_params:
            
            super().__init__(f"Missing {','.join([params for params in missing_params])} in parameter")