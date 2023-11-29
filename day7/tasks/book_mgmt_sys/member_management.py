class LibraryMember:
    def __init__(self):
        self.members_list = []

    def add_member(self, member_id, name, address, contact):
        new_member = {'member_id': member_id, 'name': name, 'address': address, 'contact': contact}
        self.members_list.append(new_member)
        print(f"Member '{name}' added to the list.")

    def update_member(self, member_id, name=None, address=None, contact=None):
        for member in self.members_list:
            if member['member_id'] == member_id:
                if name is not None:
                    member['name'] = name
                if address is not None:
                    member['address'] = address
                if contact is not None:
                    member['contact'] = contact
                print(f"Member details updated for ID {member_id}.")
                return
        print(f"Member with ID {member_id} not found in the list.")

    def remove_member(self, member_id):
        for member in self.members_list:
            if member['member_id'] == member_id:
                self.members_list.remove(member)
                print(f"Member '{member['name']}' removed from the list.")
                return
        print(f"Member with ID {member_id} not found in the list.")

    def display_members(self):
        print("\nLibrary Members:")
        for member in self.members_list:
            print(f"ID: {member['member_id']}, Name: {member['name']}, Address: {member['address']}, Contact: {member['contact']}")
