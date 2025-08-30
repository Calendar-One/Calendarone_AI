def get_attribute_as_string(obj, attr_name) -> str | None:
    """
    Get an attribute value from an object and ensure it's returned as a string.

    Parameters:
        obj: The object to get the attribute from
        attr_name (str): The name of the attribute to retrieve

    Returns:
        str: The attribute value converted to string, or None if attribute doesn't exist
    """
    try:
        value = getattr(obj, attr_name)
        if value is None:
            return None
        return str(value)
    except AttributeError:
        return None
