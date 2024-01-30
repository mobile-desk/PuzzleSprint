notes = {}

def add_note(title, content):
    notes[title] = content
    print("Note added successfully!")
    return notes

def view_notes():
    if len(notes) == 0:
        print("No notes available.")
    else:
        print("Notes:")
        for i in notes.keys():
            print(f"{i}: {notes[i]}")
      
            
def delete_note(title):
    if title in notes.keys():
      del notes[title]
      print(f"{title} has been deleted.")
    else:
      print(f"{title} does not exist.")
    return notes

while True:
    user = input("What do you want to do: \n A: add notes \n B: Delete notes \n C: View notes \n D: Exit App \n Chose either A, B, C or D: ")
    if user.lower() == 'a':
        title = input("Enter a title: ").strip().capitalize()
        content = input("Enter your note: ")
        add_note(title, content)
    elif user.lower() == 'b':
        title = input("Enter a title: ").strip().capitalize()
        delete_note(title)
    elif user.lower() == 'c':
        view_notes()
    elif user.lower() == 'd':
        exit()
    else:
        print("Input Error")