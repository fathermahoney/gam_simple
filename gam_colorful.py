import os
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

print(bcolors.OKBLUE + """
  ___    __    __  __
 / __)  /__\  (  \/  )
( (_-. /(__)\  )    (
 \___/(__)(__)(_/\/\_)
  ___  _____  __    _____  ____  ____  __  __  __
 / __)(  _  )(  )  (  _  )(  _ \( ___)(  )(  )(  )
( (__  )(_)(  )(__  )(_)(  )   / )__)  )(__)(  )(__
 \___)(_____)(____)(_____)(_)\_)(__)  (______)(____)
""" + bcolors.ENDC)
print("A simple GAM tool")
print("Carl Mahoney 2020")

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
print(bcolors.OKGREEN + options + bcolors.ENDC)
print('-' * 35)

create_alias = """Create an alias for either a user or a group."""

chosen_task = ""

while chosen_task not in gam_task:
    print("Enter the number corresponding to the action you'd like to take.")
    chosen_task = input(bcolors.HEADER + "Please select a task: " + bcolors.ENDC)

### 1 Search whatis

    if chosen_task == "1":
        info_search_target = """Search for information on any target.
Username, group, or alias is accepted."""
        print(info_search_target)
        target = input(bcolors.HEADER + "Enter username, group, or alias: " + bcolors.ENDC)
        os.system(gam_alias + ' whatis ' + target)

#### 2 Alias

    if chosen_task == "2":
        print("Create an alias for either a user or a group.")
        target = input(bcolors.HEADER + "Enter target username or group: " + bcolors.ENDC)
        alias = input(bcolors.HEADER + "Enter desired alias: " + bcolors.ENDC)
        os.system(gam_alias + ' create alias ' + alias + ' target ' + target)

### Add members to group

    if chosen_task == "3":
        print("Add member to group")
        group = input(bcolors.HEADER + "Enter group: " + bcolors.ENDC)
        user = input(bcolors.HEADER + "Enter user to add: " + bcolors.ENDC)
        os.system(gam_alias + ' update group ' + group + ' add member user ' + user)

### Remove users from group

    if chosen_task == "4":
        print("remove user from group")
        group = input(bcolors.HEADER + "Enter group: " + bcolors.ENDC)
        user = input(bcolors.HEADER + "Enter user to remove: " + bcolors.ENDC)
        os.system(gam_alias + ' update group ' + group + ' remove user ' + user)

### Show Delegates

    if chosen_task == "5":
        print("Show users delegates")
        user = input(bcolors.HEADER + "Enter User: " + bcolors.ENDC)
        os.system(gam_alias + ' user ' + user + ' show delegates')

### Add Delegate

    if chosen_task == "6":
        info_delegates = """
Add a delegate to a user

Gives email and contact access for the given users
(the delegators) to the specified delegate account.
"""
        print(info_delegates)
        print(bcolors.OKBLUE + "Delegator Account: Account you wish to grant access to")
        print()
        delegator = input(bcolors.HEADER + "Enter Delegator: " + bcolors.ENDC)
        print(bcolors.OKBLUE + "Delegate Account: Account that has access to Delegator's account")
        delegate = input(bcolors.HEADER + "Enter Delegate: " + bcolors.ENDC)
        os.system(gam_alias + ' user ' + delegator + ' delegate to' + delegate)

### Remove Delegate

    if chosen_task == "7":
        print("Remove User's Delegates")
        user = input(bcolors.HEADER + "Enter Delegator: " + bcolors.ENDC)
        print(bcolors.OKBLUE + "")
        delegate = input(bcolors.HEADER + "Enter Delegate: " + bcolors.ENDC)
        os.system(gam_alias + ' user ' + user + ' delete delegate' + delegate)

### Quit

    if chosen_task == "8":
        print("Quitting")
        break
