from ToDo import ToDo

td = ToDo()

if __name__ == "__main__":

        td.test()
        running = True
        while running:
            selection = td.user_input("Press C to add to list of tasks, R to read from list and P to display list...")
            running = td.select(selection)


