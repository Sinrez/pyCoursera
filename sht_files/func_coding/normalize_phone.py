def normalize_phone(phone):
    return "".join(filter(str.isdigit, phone))