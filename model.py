import json
from datetime import datetime

GUESTBOOK_ENTRIES_FILE = "entries.json"
entries = []
next_id = 0

def init():
    global entries, next_id
    try:
        f = open(GUESTBOOK_ENTRIES_FILE)
        entries = json.loads(f.read())
        next_id = len(entries) + 1
        f.close()
    except:
        entries = []

def get_entries():
    global entries
    return entries

def add_entry(name, text):
    global entries, GUESTBOOK_ENTRIES_FILE, next_id
    now = datetime.now()
    time_string = now.strftime("%b %d, %Y %-I:%M %p")
    # if you have an error using this format, just use
    # time_string = str(now)
    entry = {"author": name, "text": text, "timestamp": time_string, "id": next_id}
    entries.insert(0, entry) ## add to front of list
    next_id += 1
    try:
        f = open(GUESTBOOK_ENTRIES_FILE, "w")
        dump_string = json.dumps(entries)
        f.write(dump_string)
        f.close()
    except:
        print("ERROR! Could not write entries to file.")

def delete_entry(id):
    global entries, GUESTBOOK_ENTRIES_FILE
    for i,e in enumerate(entries):
        if str(e['id']) == str(id):
            index = i
    id = int(index)
    del entries[id]
    try:
        f = open(GUESTBOOK_ENTRIES_FILE, "w")
        dump_string = json.dumps(entries)
        f.write(dump_string)
        f.close()
    except:
        print("ERROR! Could not write entries to file.")