# Interface for production floor
# gui

import tkinter as tk
import tkinter.messagebox
import tkinter.font
import tkinter.filedialog
import tkinter.ttk
import job as job
import Press as Press
import pickle


class CreateJob_GUI:
    '''This class will make a tkinter window for a program that creates jobs and makes two lists of them'''

    # class level variables
    COURIER_FONT = 'Courier'
    TIMES_FONT = 'Times New Roman'
    BOLD_FONT = 1
    FRAME_SELECT = 1

   

    def __init__(self):

        # Create a list for job orders.
        # and the two Press's.
        self.__job_order_list = []
        self.bl_02 = Press.Press('BL-02')
        self.bl_04 = Press.Press('BL-04')

        # Create the main window
        self.main_window = tk.Tk()
        # Add a window title for main window
        self.main_window.title('Job Orders')
        # Add geometry for main window.
        self.main_window.geometry('450x350+1000+20')

        # Create the two frames that will act as
        # create job window and display job list window
        self.Frame1 = tk.Frame(self.main_window)
        self.Frame2 = tk.Frame(self.main_window)

        # Create frame to hold job widgets
        self.jobFrame = tk.Frame(self.Frame1)
        self.jobFrame.grid(row=0,column=0, rowspan=4, columnspan=4)

        # Create label and entry for job_id
        self.id_label = tk.Label(self.jobFrame, text='Job ID : ')
        self.id_entry = tk.Entry(self.jobFrame, width = 20)
        # Create label and entry for part
        self.part_label = tk.Label(self.jobFrame, text='Part # : ')
        self.part_entry = tk.Entry(self.jobFrame, width=20)
        #create label and entry for production rate
        self.rate_label = tk.Label(self.jobFrame, text='Production Rate : ')
        self.rate_entry = tk.Entry(self.jobFrame, width=20)
        #create label and entry for order_quantity
        self.quantity_label = tk.Label(self.jobFrame, text='Order Quantity')
        self.quantity_entry = tk.Entry(self.jobFrame, width=20)

        # Place widgets in grid
        self.id_label.grid(row=0, column=0, padx=5, pady=3)
        self.id_entry.grid(row=0, column=1, padx=5, pady=3)
        self.part_label.grid(row=1, column=0, padx=5, pady=3)
        self.part_entry.grid(row=1, column=1, padx=5, pady=3)
        self.rate_label.grid(row=2, column=0, padx=5, pady=3)
        self.rate_entry.grid(row=2, column=1, padx=5, pady=3)
        self.quantity_label.grid(row=3, column=0, padx=5, pady=5)
        self.quantity_entry.grid(row=3, column=1, padx=5, pady=3)

        # Create frame to hold buttons
        self.buttonFrame = tk.Frame(self.Frame1)
        # Create buttons
        self.add_button = tk.Button(self.buttonFrame, text= 'Add', command = self.add_item)
        self.show_button = tk.Button(self.buttonFrame, text='Display', command=self.display_items)
        self.clear_button = tk.Button(self.buttonFrame, text='Clear', command=self.clear_entry)
        self.exit_button = tk.Button(self.buttonFrame, text='Exit', command=self.exit_app)

        # This will clear window
        self.text_button = tk.Button(self.buttonFrame, text='Press Page', command=self.to_press)

        # Pack buttons into frame
        self.add_button.pack(side='left', padx=5)
        self.show_button.pack(side='left', padx=5)
        self.exit_button.pack(side='left', padx=5)
        self.clear_button.pack(side='left', padx=5)

        # Pack test button
        self.text_button.pack(side='left', padx=5)

        # Create display frame to hold font selection widgets and listbos/scroller
        self.displayFrame = tk.Frame(self.Frame1)

        # create bold check box
        self.font_weight = tk.IntVar()
        self.font_weight.set(CreateJob_GUI.BOLD_FONT)
        self.bold_check = tk.Checkbutton(self.displayFrame,
                                    text='Bold',
                                    variable=self.font_weight)

        # Create radio buttons
        self.font_fam = tk.StringVar()
        self.font_fam.set(CreateJob_GUI.COURIER_FONT)
        self.courier_button = tk.Radiobutton(self.displayFrame,
                                        text='Courier',
                                        variable=self.font_fam,
                                        value = CreateJob_GUI.COURIER_FONT)
        self.times_button = tk.Radiobutton(self.displayFrame,
                                        text = 'Times',
                                        variable = self.font_fam,
                                        value = CreateJob_GUI.TIMES_FONT)

        # Create scroll bar and listbox
        self.scrollbar = tk.Scrollbar(self.displayFrame, orient = tk.VERTICAL)
        self.listbox = tk.Listbox(self.displayFrame, width=30,
                                        yscrollcommand = self.scrollbar.set)
        self.scrollbar.config(command=self.listbox.yview)

        # add widgets into frame
        self.courier_button.pack(side='left')
        self.times_button.pack(side='left')
        self.bold_check.pack(side='top')
        self.scrollbar.pack(side='right', fill = tk.Y)
        self.listbox.pack(side='left',fill = tk.BOTH, expand = 1)
        
        # Place frames into Frame1
        self.jobFrame.pack(side='top', pady = 5)
        self.buttonFrame.pack(side='top', pady = 5)
        self.displayFrame.pack(side='top', pady = 5)

        # Pack Frame1 in to main_window
        self.Frame1.pack()
        

        # Frames to hold widgets in the press window.
        self.press_label_frame = tk.Frame(self.Frame2)
        self.press_list_frame = tk.Frame(self.Frame2)
        self.press_titles_frame = tk.Frame(self.Frame2)

        # Widgets for Frame2
        self.update_button = tk.Button(self.press_label_frame, text='Print Jobs', command=self.print_jobs)
        self.assign_jobs = tk.Button(self.press_label_frame, text='Assign jobs', command=self.make_job_list)
        self.jobs_page_button = tk.Button(self.press_label_frame, text='Jobs Page', command=self.to_jobs)
        self.press_list_1 = tk.Text(self.press_list_frame, width=30, height=100)
        self.press_list_2 = tk.Text(self.press_list_frame, width=30, height=100)
        self.bl_02_title = tk.Label(self.press_titles_frame, text='BL 02',width=30)
        self.bl_04_title = tk.Label(self.press_titles_frame, text='BL 04',width=30)

        # Pack widgets into Frame2
        self.update_button.pack(side='left')
        self.assign_jobs.pack(side='left')
        self.jobs_page_button.pack(side='left')
        self.press_list_2.pack(side='left')
        self.press_list_1.pack(side='left') 
        self.bl_02_title.pack(side='left')
        self.bl_04_title.pack(side='left')

        # Pack frames
        self.press_label_frame.pack()
        self.press_titles_frame.pack()
        self.press_list_frame.pack()  
            
        # Add menu
        self.menubar = tk.Menu(self.main_window)
        self.main_window.config(menu=self.menubar)

        # Add file menu options
        self.file_menu = tk.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label='File', menu=self.file_menu)
        self.file_menu.add_command(label = 'Save',
                                command=self.save_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label='Exit',
                                    command=self.main_window.destroy)

        # Add help menu
        self.help_menu = tk.Menu(self.menubar, tearoff = 0)
        self.menubar.add_cascade(label='Help', menu = self.help_menu)
        self.help_menu.add_command(label = 'About',
                                    command=self.show_about)

        # Start the window event loop
        self.main_window.mainloop()

    def add_item(self):
        '''get text form entry fields'''
        id = self.id_entry.get()
        part = self.part_entry.get()
        rate = self.rate_entry.get()
        quantity = self.quantity_entry.get()

        # check for positive integer for order number
        try:
            rate = int(rate)
        except ValueError:
            #display error message box
            tk.messagebox.showerror('ERROR', 'ID must be positive integer amount.')
            
            # set focus to id
            self.id_entry.focus()
        else:
            try:
                quantity = int(quantity)
            except ValueError:
                tk.messagebox.showerror('ERROR','Quantity must be positve.')
                #set focus to quantity
                self.quantity_entry.focus()
            else:
                # Create job object
                self.__job_order_list.append(job.Job(id,str(part),int(rate),int(quantity)))

                # Let user know job was created.
                tk.messagebox.showinfo('Information', 'Job Created')
                # reset fields
                self.clear_entry()

    def display_items(self):
        '''Displays jobs created'''
        self.listbox.delete(0, tk.END)

        #check user selections for font type and set listbox font
        if self.font_weight.get() == CreateJob_GUI.BOLD_FONT:
            fontToUse = tk.font.Font(family = self.font_fam.get(),
                                    weight = 'bold')
        else:
            fontToUse = tk.font.Font(family = self.font_fam.get(),
                                    weight = 'normal')

        # config listbox to use font we just chose
        self.listbox.config(font=fontToUse)

        for item in self.__job_order_list:
            item_string1 = 'Job Id      : {:5}'.format(item.job_id)
            item_string2 = 'Part #   : {:3}'.format(item.part)
            item_string3 = 'Rate     : {}'.format(item.production_rate)
            item_string4 = 'Quantity : {} '.format(item.order_quantity)
            self.listbox.insert(tk.END, item_string1)
            self.listbox.insert(tk.END, '   '+item_string2)
            self.listbox.insert(tk.END, '   '+item_string3)
            self.listbox.insert(tk.END, '   '+item_string4)
    
    def clear_entry(self):
        '''Clears data entry fields'''
        self.id_entry.delete(0, tk.END)
        self.part_entry.delete(0, tk.END)
        self.rate_entry.delete(0, tk.END)
        self.quantity_entry.delete(0, tk.END)


    def exit_app(self):
        '''Exits the app'''
        response = tk.messagebox.askyesno('Confirmation', 'Are you sure you want exit')
        
        if response == True:
            self.main_window.destroy()

    # Menu option functions
    def save_file(self):
        '''Save file funtion'''
        # get filename
        file_name = tk.filedialog.asksaveasfilename(initialdir= '/',
                                                    filetypes = [('Bin Files', '*.bin'),
                                                                ('All Files', '*.*')],
                                                    title = 'Selecte file',
                                                    defaultextension = '*.bin')
        # Check for empty string
        if len(file_name) != 0:
            #open file
            self.file_var = open(file_name, 'wb')
            # write to file
            try:
                for item in self.__job_order_list:
                    pickled_item = pickle.dumps(item)
                    self.file_var.write(pickled_item)
            except:
                print('Error! Could not save file.')
            finally:
            # close file    
                self.file_var.close()

    # Message box for help menu
    def show_about(self):
        '''Displays message box for program info'''
        tk.messagebox.showinfo('Help', 'This program was created for CIS 2531\nBy Matt Garcia\n7/12/22.') 

    def to_press(self):
        '''moves to the press list frame'''
        self.Frame2.pack(fill='both', expand=1)
        self.Frame1.pack_forget()

    def to_jobs(self):
        '''moves to the create jobs frame'''
        self.Frame1.pack()
        self.Frame2.pack_forget()

    def print_jobs(self):
        '''Displays jobs in text boxes'''
        self.press_list_1.delete('1.0','end')
        self.press_list_2.delete('1.0','end')
        job_list1 = self.bl_02.job_list()
        job_list2 = self.bl_04.job_list()
        for i in job_list1:
            self.press_list_1.insert('1.0',i)
            self.press_list_1.insert('1.0','\n') 
        for i in job_list2:
            self.press_list_2.insert('1.0',i) 
            self.press_list_2.insert('1.0','\n')         
    
    def make_job_list(self):
        '''takse the jobs in __job_order_list and puts them 
        evenly between the press's bl_02 and bl_04'''
        flop = True
        print(self.__job_order_list)
        for i in self.__job_order_list:
            if i not in self.bl_02.job_list():
                if i not in self.bl_04.job_list():
                    if flop == True:
                        
                        self.bl_02.add_job(i)
                        flop = False
                    else:
                        
                        self.bl_04.add_job(i)
                        flop = True
        
if __name__ == '__main__':
    test = CreateJob_GUI()