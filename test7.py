import tkinter as Tk
from tkinter import filedialog
import table

########################################################################
class UploadFile(Tk.Toplevel):
    #----------------------------------------------------------------------
    def __init__(self, original):
        self.original = original
        Tk.Toplevel.__init__(self)
        self.resizable(False, False)
        self.geometry('400x200')
        main = Tk.Frame(self)
        main.pack(fill="both", expand=True)

        head_frame = Tk.Frame(main)
        head_frame.pack(fill="both")

        body_frame = Tk.Frame(main)
        body_frame.pack(fill="both", pady=(0,50))

        footer_frame = Tk.Frame(main)
        footer_frame.pack(fill="both",expand=True)

        lbl = Tk.Label(head_frame, text='Eula Scanner', font=('Verdana', 12))
        lbl.grid(row=0,column=0, sticky="w")

        lbl_description = Tk.Label(head_frame, text='License Agreement To Analyze')
        lbl_description.grid(row=1,column=0,padx=5, pady=(0,10))

        self.file_count = Tk.StringVar()
        file_button = Tk.Button(body_frame, text='Select file(s)...', command=self.file_picker, anchor='w')
        file_button.grid(row=0,column=0, padx=(15,5), pady=(15,0))
        file_label = Tk.Label(body_frame, textvariable=self.file_count, anchor='e')
        file_label.grid(row=0,column=1, pady=(15,0))

        btn_next = Tk.Button(footer_frame, text="Analyze", command=self.onNext)
        btn_next.grid(row=1,column=1)
        btn_back = Tk.Button(footer_frame, text="Back", command=self.onBack)
        btn_back.grid(row=1,column=0, pady=20, padx=(280,10))


    #----------------------------------------------------------------------
    def onNext(self):
        self.withdraw()
        subFrame = AnalyzeFile(self)
    def onBack(self):
        self.destroy()
        self.original.show()
    def file_picker(self):
        self.selected_files = filedialog.askopenfilenames(parent=self)
        self.file_count.set('{} file(s)'.format(len(self.selected_files)))

########################################################################
class PasteFile(Tk.Toplevel):
    #----------------------------------------------------------------------
    def __init__(self, original):
        self.original = original

        Tk.Toplevel.__init__(self)
        self.resizable(False, False)
        self.geometry('400x200')
        main = Tk.Frame(self)
        main.pack(fill="both", expand=True)

        head_frame = Tk.Frame(main)
        head_frame.pack(fill="both")

        body_frame = Tk.Frame(main)
        body_frame.pack()

        footer_frame = Tk.Frame(main)
        footer_frame.pack(fill="both",expand=True)

        lbl = Tk.Label(head_frame, text='Eula Scanner', font=('Verdana', 12))
        lbl.grid(row=0,column=0, sticky="w")

        lbl_description = Tk.Label(head_frame, text='License Agreement To Analyze')
        lbl_description.grid(row=1,column=0,padx=5, pady=(0,10))

        self.text_field = Tk.Text(body_frame, height=6)
        self.text_field.config(font=("consolas", 10),width=50, undo=True, wrap='word')
        self.text_field.focus_set()
        self.text_field.grid(row=0, column=0, sticky="nsew")

        scrollb = Tk.Scrollbar(body_frame, command=self.text_field.yview)
        scrollb.grid(row=0, column=1, sticky='nsew')
        self.text_field['yscrollcommand'] = scrollb.set

        btn_next = Tk.Button(footer_frame, text="Analyze", command=self.onNext)
        btn_next.grid(row=1,column=1)
        btn_back = Tk.Button(footer_frame, text="Back", command=self.onBack)
        btn_back.grid(row=1,column=0,pady=10, padx=(280,10))

    #----------------------------------------------------------------------
    def onNext(self):
        self.withdraw()
        subFrame = AnalyzeFile(self)
    def onBack(self):
        self.destroy()
        self.original.show()

########################################################################
class AnalyzeFile(Tk.Toplevel):
    #----------------------------------------------------------------------
    def __init__(self, original):

        self.class_file = original
        Tk.Toplevel.__init__(self)
        self.resizable(False, False)
        self.geometry('400x200')
        main = Tk.Frame(self)
        main.pack(fill="both", expand=True)

        head_frame = Tk.Frame(main)
        head_frame.pack(fill="both")

        body_frame = Tk.Frame(main)
        body_frame.pack(fill="both",expand=True)

        footer_frame = Tk.Frame(main)
        footer_frame.pack(fill="both",expand=True)

        lbl = Tk.Label(head_frame, text='Eula Scanner', font=('Verdana', 12))
        lbl.grid(row=0,column=0, sticky="w")

        lbl_description = Tk.Label(head_frame, text='License Agreement Analysis')
        lbl_description.grid(row=1,column=0,padx=5, pady=(0,10))

        t = table.SimpleTable(body_frame)
        t.pack(side="top", fill="x", padx=5)
        t.set(0,0,"Category")
        t.set(0,1,"Interpretation")
        t.set(0,2,"Text")
        t.set(1,0,"Sample Category")
        t.set(1,1,"Sample Interpretation")
        t.set(1,2,"Sample Text")
        t.set(2,0,"Sample Category2")
        t.set(2,1,"Sample Interpretation2")
        t.set(2,2,"Sample Text2")

        btn = Tk.Button(footer_frame, text="Home", command=self.onClose)
        btn.grid(row=0,columnspan=2,padx=(340,10), pady=(15,0))

    #----------------------------------------------------------------------
    def onClose(self):
        self.class_file.onBack()
        self.class_file.destroy()
        self.destroy()

########################################################################
class MainGui(object):
    #----------------------------------------------------------------------
    def __init__(self, parent):
        """Constructor"""
        self.root = parent
        self.root.title("Eula")
        self.root.resizable(False, False)
        self.root.pack_propagate(0)
        main = Tk.Frame(self.root,  width=100, height=90)
        main.pack(fill="both", expand=True)

        head_frame = Tk.Frame(main)
        head_frame.pack(fill="both")

        body_frame = Tk.Frame(main)
        body_frame.pack()

        lbl = Tk.Label(head_frame, text='Eula Scanner', font=('Verdana', 12))
        lbl.grid(row=0,column=0, sticky="w")

        lbl_description = Tk.Label(head_frame, text='Scan new license agreement.')
        lbl_description.grid(row=1,column=0,padx=5, pady=(0,10))

        btn_upload = Tk.Button(body_frame, text="Upload File", command=self.openUpload)
        btn_upload.grid(row=1,column=0, pady=10)
        btn_paste = Tk.Button(body_frame, text="Paste File", command=self.openPaste)
        btn_paste.grid(row=2,column=0, pady=10)

    #----------------------------------------------------------------------
    def hide(self):
        self.root.withdraw()

    #----------------------------------------------------------------------
    def openUpload(self):
        self.hide()
        subFrame = UploadFile(self)
    #----------------------------------------------------------------------
    def openPaste(self):
        self.hide()
        subFrame = PasteFile(self)
    #----------------------------------------------------------------------
    def show(self):
        self.root.update()
        self.root.deiconify()

#----------------------------------------------------------------------
if __name__ == "__main__":
    root = Tk.Tk()
    #root.geometry("800x600")
    app = MainGui(root)
    root.mainloop()