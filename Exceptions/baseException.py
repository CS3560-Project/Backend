class baseException(Exception):
    # base Exception case
    error_code = 400
    message = "Error occurred"
    def __init__(self,message = None, error_code =None):
        if message:
            self.message = message
        if error_code:
            self.error_code = error_code 
        super().__init__(self.message)
