#!/usr/bin/env python3.7
import sys
print("python version: " + sys.version)

'''
from tkinter import *
from tkinter import ttk
'''
try:
    import tkinter as tk
    from tkinter import ttk
except ImportError:
    import Tkinter as tk
    import ttk

from tkcalendar import Calendar, DateEntry

import time

DEBUG = False

'''
Program Strings
'''

success_msg = "Record saved!" 
success_msg_failure = "Record did not save. Try Again."

if( DEBUG ):
    print("hello")

def remove_sucess_msg():
    print("I'm a cb function")
    success_msg_text.set("")

def record_b(filename):
    print( f'filename: {filename}')
    with open( filename, 'a', encoding='utf-8') as recorder:
        recorder.write("hello ai\n")

def selected_date(*args):
    print(f'date args: {args}')
    print(f'Calendar date: {cal.get_date()}')

def record_bw_cb(*args):

	fitness_data = (bw.get(), date_e.get_date() )
	print("Printing record...")
	print(f'value: {args}')
	print(f'Body weight: {fitness_data[0]}')
    #print(f'Cal dict: {dir(date_e)}' )
    #print(f'Date: {date_e.get_date()}')
	print(f'Date: {fitness_data[1]}')
	if DEBUG:
		for key in date_e.keys():
			print(key)
	record_b('bw_stats.txt')
	success_msg_text.set( success_msg )
	
	if success_msg_text.get() != success_msg_failure:
		print( "Record saved" )
		#time.sleep(5)
		root.after(500, remove_sucess_msg )
		#success_msg_text.set( "" )
    

root = tk.Tk()
#top = tk.Toplevel(root)
root.title("Fitness Tracker")

mainframe = ttk.Frame( root, padding="3 3 12 12")
mainframe.grid( column = 0, row = 0, sticky=('N', 'W', 'E', 'S'))

root.columnconfigure(0, weight = 1 )
root.rowconfigure(0, weight = 1)

ttk.Label( mainframe, text="Body Weight").grid(column=1,row=1, sticky='W')

bw = tk.StringVar()
bw_entry = ttk.Entry( mainframe, width = 7, textvariable = bw)
bw_entry.grid(column=2, row=1, sticky=('W','E'))


ttk.Label( mainframe, text="Choose date").grid( column = 1, row = 2, sticky='W')
date_e = DateEntry(mainframe, width=12, background="darkblue", foreground='white', borderwidth=2, year=2023)
date_e.grid( column=2, row = 2, sticky='E')

if (DEBUG):
	print(f'type DateEntry w/o grid called {type(date_e)}')

ttk.Button( mainframe, text="Record", command = record_bw_cb).grid(column = 3, row = 4, sticky=tk.E)

success_msg_text = tk.StringVar()
success_msg_lbl = ttk.Label( mainframe, textvariable = success_msg_text )
success_msg_lbl.grid( column = 1, row = 5, sticky=tk.E)

if(DEBUG):
    print(f'cal dir is : {dir(DateEntry)}')
    print(f'cal dir is : {dir(date_e.get_date())}')

bw_entry.focus()
root.bind("<Return>", record_bw_cb)
root.bind("<<DateEntrySelected>>", selected_date)

root.mainloop()
