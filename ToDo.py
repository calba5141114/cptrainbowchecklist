class ToDo(object):

    def __init__(self):
        self.todos = []

    def create(self, task):
        self.todos.append(task)

    def read(self, index):
        return self.todos[index]

    def update(self, index, task):
        self.todos[index] = task

    def destroy(self, index):
        self.todos.pop(index)

    def list_all_tasks(self):
        count = 0
        for todo in self.todos:
            print("{} {}".format(count, todo))
            count += 1

    def mark_completed(self, index):
        task = self.todos[index]
        self.todos[index] = "√" + task
        task = self.todos[index]
        self.todos[index] = "√" + task

    def select(self, function_code):
        if function_code == "C":
            input_task = self.user_input("Input task: ")
            self.create(input_task)
        elif function_code == "R":
            task_index = self.user_input("Index number? ")
            self.read(task_index)
        elif function_code == "P":
            self.list_all_tasks()
        elif function_code == "Q":
            return False
        else:
            print("Option unknown")
        return True

    def user_input(self, prompt):
        user_input = input(prompt)
        return user_input

    def test(self):
        self.create("task one \n")
        self.create("task two \n ")
        print(self.read(0))
        print(self.read(1))
        self.update(0, "task three \n")
        self.destroy(1)

        self.mark_completed(0)
        print(self.read(0))

        user_value = self.user_input("Please enter a value: \n")
        print(user_value)

        self.select("C")
        self.list_all_tasks()
        self.select("R")
