def get_event_date(event):
    return event.date
def current_users(events):
    events.sort(key=get_event_date)
    #dictionnary to store names and users
    machines = {}
    #go to list of events
    for event in events:
        #look if the machine is affected by this event in the dictionnary
        if event.machine not in machines:
            machines[event.machine] = set()
        if event.type = "login":
            machines[event.machine].add(event.user)
        elif event.type = "logout":
            machines[event.machine].remove(event.user)
    return machines
def generate_report(machines):
    for machines, users in machines.items():
        if len(users) > 0:
            users_list = ", ".join(users)
            print("{}: {}".format(machine, user_list))

"""users = current_users(events)
print(users)
generate_report(users)"""
for char in file_contents:
    if char in punctuations:
        file_contents = file_contents.remove(char)
for char in file_contents:
    if char in uninteresting_words:
        file_contents = file_contents.remove(char)