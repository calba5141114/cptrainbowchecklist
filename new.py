import uuid
import sys
import datetime
import time


class TodoList(object):

    def __init__(self):
        self.notes = []

    def show(self):
        ''' show all existing notes '''
        if len(self.notes) > 0:
            for note in self.notes:
                print("\n"+str(note))
        else:
            print("You currently have zero notes L")

    def changeState(self, id, state):
        ''' mark tasks as complete or uncomplete '''
        note = self.getByID(id)
        note['state'] = state

    def create(self, content, title):
        ''' append note to the notes list '''
        id = uuid.uuid1()
        self.notes.append({"content": content,
                           "title": title,
                           "state": False,
                           "createdAt": datetime.datetime.now(),
                           "id": id})
        print("{} created".format(title))
        return id

    def delete(self, id):
        ''' deletes note by id '''
        for note in self.notes:
            if note["id"] == id:
                print("\n Deleting {}".format(id))
                try:
                    self.notes.remove(note)
                except Exception as e:
                    print(
                        "\n Error: {e} You will be redirected to the main program".format(e))
                    self.show()

    def updateByID(self, id, content):
        ''' updates note contents with id '''
        for note in self.notes:
            if note["id"] == id:
                print("\n Updating {}".format(id))
                try:
                    note['content'] = content
                except Exception as e:
                    print(
                        "\n Error: {e} You will be redirected to the main program".format(e))
                    self.show()

    def getByID(self, id):
        ''' get note by id '''
        for note in self.notes:
            if note["id"] == id:
                return note

    def exitProgram(self):
        ''' closes program '''
        print(
            " \n We will be closing the program in 10 seconds but we'll show your notes first \n")
        self.show()
        time.sleep(10)
        sys.exit(0)

    def takeUserInput(self, prompt):
        ''' gets user input '''
        uinput = input("\n"+str(prompt))
        return uinput

    def test(self):
        self.show()
        noteref = self.create("Hello World", "Test")
        self.changeState(noteref, True)
        self.show()
        self.updateByID(noteref, "BNye World")
        self.getByID(noteref)
        time.sleep(20)
        self.delete(noteref)
        self.exitProgram()


if __name__ == "__main__":
    x = TodoList()
    x.test()
