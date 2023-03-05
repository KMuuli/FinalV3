import tkinter.messagebox
from tkinter import *
from tkinter import filedialog
from Model import Model
from View import View


class Controller:

    def __init__(self):
        self.model = Model()
        self.view = View(self, self.model)

    def main(self):
        self.view.main()

    def click_names(self):
        self.view.box_names.delete(1.0, END)
        self.model.show_names()
        for name in self.model.name_list:
            self.view.box_names.insert(INSERT, name)

    def click_tasks(self):
        self.view.box_tasks.delete(1.0, END)
        self.view.box_result.delete(1.0, END)
        self.model.show_tasks()
        for task in self.model.task_list:
            self.view.box_tasks.insert(INSERT, task)
        if len(self.model.name_list) <= len(self.model.task_list):
            self.view.btn_shuffle["state"] = "normal"
            self.view.btn_save["state"] = "normal"
            for result in self.model.result_list:
                self.view.box_result.insert(INSERT, result)
        else:
            tkinter.messagebox.showwarning("Hoiatus!", "Ülesandeid ei jagu kõigile!")
            self.view.btn_shuffle["state"] = "disabled"
            self.view.btn_save["state"] = "disabled"

    def click_shuffle(self):
        if len(self.model.name_list) <= len(self.model.task_list):
            self.view.box_tasks.delete(1.0, END)
            self.view.box_result.delete(1.0, END)
            self.model.shuffle_tasks()
            for task in self.model.task_list:
                self.view.box_tasks.insert(INSERT, task)
            for result in self.model.result_list:
                self.view.box_result.insert(INSERT, result)
        else:
            tkinter.messagebox.showwarning("Hoiatus!", "Ülesandeid ei jagu kõigile.")

    def click_save(self):
        if 0 < len(self.model.name_list) <= len(self.model.task_list) > 0:
            file = filedialog.asksaveasfilename(filetypes=[("txt file", ".txt")], defaultextension=".txt")
            with open(file, "w") as f:
                for line in self.model.result_list:
                    f.write(f"{line}")
        else:
            tkinter.messagebox.showwarning("Hoiatus!", "Ülesandeid ei saanud välja jagada./nPole midagi salvestada")

