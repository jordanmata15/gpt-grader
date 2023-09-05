import tkinter as tk
import tkinter.filedialog

import GPTGrader

class GPTGraderGUI():
    
    def __init__(self):
        """Initialize the GUI and start the main loop.
        """
        self.src_dir = None
        self.dest_dir = None
        self.root = tkinter.Tk()
        self.root.geometry("1000x500")
        self.src_button = tkinter.Button(self.root, 
                                    text="Select Submissions Location", 
                                    command=lambda: self.get_source_folder())
        self.dest_button = tkinter.Button(self.root, 
                                    text="Select Feedback Location", 
                                    command=lambda: self.get_destination_folder())
        self.start_grading_button = tkinter.Button(self.root, 
                                                    text="Start Grading", 
                                                    command=lambda: self.run_grader())
        self.src_label = tk.Text(self.root, width=100, height=2, bg='light grey')
        self.dest_label = tk.Text(self.root, width=100, height=2, bg='light grey')

        self.src_button.pack()
        self.src_label.pack()
        self.src_label.pack(padx=(0, 0), pady=(0, 30))
        
        self.dest_button.pack()
        self.dest_label.pack()
        self.dest_label.pack(padx=(0, 0), pady=(0, 30))

        tk.mainloop()
    
    def get_source_folder(self):
        """Callback to set the source folder for the student submissions.
        """
        self.src_dir = tkinter.filedialog.askdirectory()
        self.src_label.delete(1.0, "end")
        self.src_label.insert("end", self.src_dir)
        self.is_ready()

    def get_destination_folder(self):
        """Callback to set the destination folder for the feedback files.
        """
        self.dest_dir = tkinter.filedialog.askdirectory()
        self.dest_label.delete(1.0, "end")
        self.dest_label.insert("end", self.dest_dir)
        self.is_ready()

    def run_grader(self):
        """Callback to start the grading process.
        """
        grader = GPTGrader.GPTGrader(self.src_dir, self.dest_dir)
        grader.start()

    def is_ready(self):
        """Check if the source and destination folders have been selected. 
        If so, enable the start grading button.
        """
        if (self.src_dir and self.dest_dir):
            self.start_grading_button.pack()

if __name__=="__main__":
    grader_gui = GPTGraderGUI()