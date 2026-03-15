def validate_length(response, min_length):

    if len(response) >= min_length:
        return True
    else:
        return False
    
def validate_keyword(response, keyword):

    if keyword.lower() in response.lower():
        return True
    else:
        return False