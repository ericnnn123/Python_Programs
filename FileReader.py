import tkinter as tk
from tkinter import filedialog
import os

class FileReader(tk.Frame):
    #window setup
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        current_directory = os.getcwd()

        #adjust layouts and function calls here
        self.title_label = tk.Label(self, text="Welcome to the file reader! Browse for a text file that you would like to read!")
        self.file_path_label = tk.Label(self, text="File Path: ", width=10)
        self.file_path_input = tk.Entry(self, width=30)
        self.file_browser_button = tk.Button(self, text="Browse", command=self.browse_files)
        self.read_file_button = tk.Button(self, text= "Read File", width=10, command=self.read_and_write_file)
        self.text_box = tk.Text(self)

        self.file_path_input.insert(0, str(current_directory))
        #adjust locations here
        self.title_label.pack()
        self.file_path_label.pack()
        self.file_path_input.pack()
        self.file_browser_button.pack()
        self.read_file_button.pack()
        self.text_box.pack()

    #functionality beyond this point
    def browse_files(self):
        search_directory = filedialog.askopenfilename()
        if search_directory:
            self.file_path_input.delete(0, tk.END)
            self.file_path_input.insert(0, str(search_directory))
        return search_directory

    def read_and_write_file(self):
        file_path = self.file_path_input.get()
        with open(file_path) as file:
            self.text_box.delete(tk.END)

            self.text_box.insert(tk.INSERT, "Some information about the file: \n")
            self.text_box.insert(tk.INSERT, "Filename: " + str(file.name) + "\n")
            self.text_box.insert(tk.INSERT, "File mode: " + str(file.mode) + "\n")
            self.text_box.insert(tk.INSERT, "File Contents: \n")
            self.text_box.insert(tk.INSERT, str(file.read()))


def main():
    FileReader(root).pack()
    root.wm_title("File Reader")
    root.geometry("500x500")
    root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    main()
