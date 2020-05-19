import os

### Leave alone if default location
gam_alias = "~/bin/gam/gam"

gam_task = ["1", "2", "3", "4", "5", "6", "7", "8"]

print('-' * 35)
options = """1 - Search Users, Groups, or Alias'
2 - Create an Alias
3 - Add Member to a Group
4 - Remove Member from Group
5 - Show User Delegates
6 - Add Delegate
7 - Remove Delegate
8 - Quit Program"""
print(options)
print('-' * 35)

create_alias = """Create an alias for either a user or a group."""

chosen_task = ""

while chosen_task not in gam_task:
    print("Enter the number corresponding to the action you'd like to take.")
    chosen_task = input("Please select a task: ")

### 1 Search whatis

    if chosen_task == "1":
        info_search_target = """Search for information on any target.
Username, group, or alias is accepted."""
        print(info_search_target)
        target = input("Enter username, group, or alias: ")
        os.system(gam_alias + ' whatis ' + target)

#### 2 Alias

    if chosen_task == "2":
        print("Create an alias for either a user or a group.")
        target = input("Enter target username or group: ")
        alias = input("Enter desired alias: ")
        os.system(gam_alias + ' create alias ' + alias + ' target ' + target)

### Add members to group

    if chosen_task == "3":
        print("Add member to group")
        group = input("Enter group: ")
        user = input("Enter user to add: ")
        os.system(gam_alias + ' update group ' + group + ' add member user ' + user)

### Remove users from group

    if chosen_task == "4":
        print("remove user from group")
        group = input("Enter group: ")
        user = input("Enter user to remove: ")
        os.system(gam_alias + ' update group ' + group + ' remove user ' + user)

### Show Delegates

    if chosen_task == "5":
        print("Show users delegates")
        user = input("Enter User: ")
        os.system(gam_alias + ' user ' + user + ' show delegates')

### Add Delegate

    if chosen_task == "6":
        info_delegates = """
Add a delegate to a user

Gives email and contact access for the given users
(the delegators) to the specified delegate account.
"""
        print(info_delegates)
        print("Delegator Account: Account you wish to grant access to")
        print()
        delegator = input("Enter Delegator: ")
        print("Delegate Account: Account that has access to Delegator's account")
        delegate = input("Enter Delegate: ")
        os.system(gam_alias + ' user ' + delegator + ' delegate to' + delegate)

### Remove Delegate

    if chosen_task == "7":
        print("Remove User's Delegates")
        user = input("Enter Delegator: ")
        print("")
        delegate = input("Enter Delegate: ")
        os.system(gam_alias + ' user ' + user + ' delete delegate' + delegate)

### Quit

    if chosen_task == "8":
        print("Quitting")
        break
