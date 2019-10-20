
def error_handling(status):
    if (status=="ZERO_RESULTS"):
        raise ZeroResultError()
    elif (status=="OVER_QUERY_LIMIT"):
        raise OverQueryError()
    elif (status=="REQUEST_DENIED"):
        raise RequestDeniedError()
    elif (status=="INVALID_REQUEST"):
        raise InvalidRequestError()
    elif (status=="UNKNOWN_ERROR"):
        raise UnknownError()
    elif (status=="NOT_FOUND"):
        raise NotFoundError() 
    else:
        pass

class ZeroResultError(Exception):

    def __init__(self,status="ZERO_RESULTS",msg="There is no result from the query."):
        self.msg=msg
        self.status=status

class OverQueryError(Exception):

    def __init__(self,status="OVER_QUERY_LIMIT",msg="Your Google Maps quota is over. Please wait for a moment and do it again"):
        self.msg=msg
        self.status=status

class RequestDeniedError(Exception):
    
    def __init__(self,status="REQUEST_DENIED",msg="Your request is denied. Please use a valid Google API Key"):
        self.msg=msg
        self.status=status

class InvalidRequestError(Exception):

    def __init__(self,status="INVALID_REQUEST",msg="The required query parameter is missing"):
        self.msg=msg
        self.status=status

class UnknownError(Exception):

    def __init__(self,status="UNKNOWN_ERROR",msg="Please try again"):
        self.msg=msg
        self.status=status

class NotFoundError(Exception):

    def __init__(self,status="NOT_FOUND",msg="The referenced location was not found in the Place database"):
        self.msg=msg
        self.status=status

