import os
import random
from tkinter import filedialog


class Model:

    def __init__(self):
        self.name_list = []  # Empty list for names
        self.task_list = []  # Empty list for tasks
        self.result_list = []  # Empty list for result
        self.name_list_result = []  # Empty list for names for result
        self.name_file = ""  # Empty string for name file

    def show_names(self):
        self.name_list = []
        self.name_list_result = []
        name_file = filedialog.askopenfilename()
        with open(name_file, "r", encoding="utf8") as f:
            all_lines = f.readlines()
            for name in all_lines:
                self.name_list.append(name)
        self.name_list_result = list(map(lambda s: s.strip(), self.name_list))
        self.name_list_result = [name + " - " for name in self.name_list_result]

    def show_tasks(self):
        self.task_list = []
        task_file = filedialog.askopenfilename()
        if os.path.isfile(task_file):
            with open(task_file, "r", encoding="utf8") as f:
                all_lines = f.readlines()
                for task in all_lines:
                    self.task_list.append(task)
            self.show_result()

    def shuffle_tasks(self):
        random.shuffle(self.task_list)
        self.show_result()

    def show_result(self):
        self.result_list = [i + k for i, k in zip(self.name_list_result, self.task_list)]
