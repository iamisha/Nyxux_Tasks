
class InvalidISBNError(Exception):
    def __init__(self, isbn):
        super().__init__(f"Invalid ISBN: {isbn}. ISBN must be a positive integer.")

class NegativeQuantityError(Exception):
    def __init__(self, quantity):
        super().__init__(f"Invalid quantity: {quantity}. Quantity must be a non-negative integer.")

class MemberNotFoundError(Exception):
    def __init__(self, member_id):
        super().__init__(f"Member not found with ID: {member_id}.")

def validate_isbn(isbn):
    if not isinstance(isbn, int) or isbn <= 0:
        raise InvalidISBNError(isbn)

def validate_quantity(quantity):
    if not isinstance(quantity, int) or quantity < 0:
        raise NegativeQuantityError(quantity)

def validate_member(member_id, members_list):
    if not any(member['member_id'] == member_id for member in members_list):
        raise MemberNotFoundError(member_id)