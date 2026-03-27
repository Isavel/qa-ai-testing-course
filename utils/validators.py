def validate_length(response, min_length):
    """
    Validate length of response
    """

    if len(response) >= min_length:
        return True
    else:
        return False
    
def validate_keyword(response, keyword):
    """
    Validate keyword exists in response
    """
    
    if keyword.lower() in response.lower():
        return True
    else:
        return False
    
def validate_field_exists(data, field):
    """
    Validata field is in data
    """
    return field in data

def validate_is_valid(value):
    """
    Validate value is valid
    """
    if value > 0:
        return True
    else:
        return False
    
def validate_fields_exist(data, required_fields):
    """
    Validate response has required fields 
    """
    missing_fields = []
  
    for field in required_fields:
        if field not in data:
            missing_fields.append(field)

    return missing_fields

def validate_type(value, expected_type):
    """
    Validate data type 
    """
    return isinstance(value, expected_type)
   

def validate_not_empty(value):
    """
    Validate fields are not empty
    """
    return bool(value)

def validate_greater_than(value, threshold):
    """
    Validate value versus threshold
    """
    return value > threshold
