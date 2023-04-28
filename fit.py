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

def show_mainframe( *args ):
	mainframe.tkraise()

def show_workout( *args ):
	"""Raise the given frame to the top of the stacking order"""
	workout_frame.tkraise()

def show_program():
	program_frame.tkraise()

def show_exercises():
	exercises_frame.tkraise()

def show_history():
	history_frame.tkraise()



def remove_sucess_msg():
    print("I'm a cb function")
    success_msg_text.set("")

def record_b(filename, msg):
	print(f'{msg[0]},{msg[1]},{msg[2]}')
	print( f'filename: {filename}')
	with open( filename, 'a', encoding='utf-8') as recorder:
		recorder.write("hello ai\n")
		recorder.write(f'{msg[2]},{msg[0]},{msg[1]}\n')

def selected_date(*args):
    print(f'date args: {args}')
    print(f'Calendar date: {cal.get_date()}')

def record_bw_cb(*args):

	fitness_data = (bw.get(), body_fat.get(), date_e.get_date() )
	print("Printing record...")
	print(f'value: {args}')
	print(f'Body weight: {fitness_data[0]}, type: {type(fitness_data[0])}')
	print(f'Body fat: {fitness_data[1]}, type: {type(fitness_data[1])}')
	print(f'Date: {fitness_data[2]}, type: {type(fitness_data[2])}')
	if DEBUG:
		for key in date_e.keys():
			print(key)
	record_b('bw_stats.txt', fitness_data)
	success_msg_text.set( success_msg )
	
	if success_msg_text.get() != success_msg_failure:
		print( "Record saved" )
		#time.sleep(5)
		root.after(500, remove_sucess_msg )
		#success_msg_text.set( "" )
    

root = tk.Tk()
#top = tk.Toplevel(root)
root.title("Fitness Tracker")

# Navigation Frame
navigation_frame = ttk.Frame( root, padding="3 3 12 12", width = 400, height=200 )
navigation_frame.grid( column = 0, row = 5, columnspan = 4)

ttk.Button( navigation_frame, text="Workout", command = show_workout).grid(column = 0, row = 4, sticky=tk.E)
ttk.Button( navigation_frame, text="Program", command = show_program).grid(column = 1, row = 4, sticky=tk.E)
ttk.Button( navigation_frame, text="Exercise", command = show_exercises).grid(column = 2, row = 4, sticky=tk.E)
ttk.Button( navigation_frame, text="History", command = show_history).grid(column = 3, row = 4, sticky=tk.E)


mainframe = ttk.Frame( root, padding="3 3 12 12", width = 400, height = 400)
mainframe.grid( column = 0, row = 0, sticky=('N', 'W', 'E', 'S'))

root.columnconfigure(0, weight = 1 )
root.rowconfigure(0, weight = 1)

ttk.Label( mainframe, text="Body Weight").grid(column=1,row=1, sticky='W')

bw = tk.StringVar()
bw_entry = ttk.Entry( mainframe, width = 7, textvariable = bw)
bw_entry.grid(column=2, row=1, sticky=('W','E'))

ttk.Label( mainframe, text="Body Fat").grid(column=1, row=2, sticky='W')

body_fat = tk.StringVar()
body_fat_entry = ttk.Entry( mainframe, width = 7, textvariable = body_fat)
body_fat_entry.grid(column=2, row=2, sticky=('W', 'E'))

ttk.Label( mainframe, text="Choose date").grid( column = 1, row = 3, sticky='W')
date_e = DateEntry(mainframe, width=12, background="darkblue", foreground='white', borderwidth=2, year=2023)
date_e.grid( column=2, row = 3, sticky='E')

if (DEBUG):
	print(f'type DateEntry w/o grid called {type(date_e)}')

ttk.Button( mainframe, text="Record", command = record_bw_cb).grid(column = 3, row = 4, sticky=tk.E)

success_msg_text = tk.StringVar()
success_msg_lbl = ttk.Label( mainframe, textvariable = success_msg_text )
success_msg_lbl.grid( column = 1, row = 5, sticky=tk.E)

ttk.Button(mainframe, text="Workout", command=show_workout).grid(column=2, row=4, stick=tk.E)


# Workout Frame
workout_frame = ttk.Frame( root, padding="3 3 12 12", width=400, height=400)
workout_frame.grid( column = 0, row = 0, sticky=('N', 'W', 'E', 'S'))

ttk.Label(workout_frame, text="Squat").grid( column = 2, row = 1, sticky='W')

# Show Program Frame
program_frame = ttk.Frame(root, padding="3 3 12 12", width=400, height= 400)
program_frame.grid(column = 0, row = 0, sticky=('N', 'W', 'E', 'S'))

ttk.Label( program_frame, text="Program Frame").grid(column = 2, row = 2, sticky=tk.E)

# Show Exercises
exercises_frame = ttk.Frame(root, padding="3 3 12 12", width=400, height=400)
exercises_frame.grid(column= 0, row = 0, sticky=('N', 'W', 'E', 'S'))

ttk.Label( exercises_frame, text="Exercise Frame").grid(column = 2, row = 2, sticky=tk.E)

# Show History
history_frame = ttk.Frame(root, padding="3 3 12 12", width=400, height=400)
history_frame.grid( column = 0, row = 0, sticky=('N', 'W', 'E', 'S'))

ttk.Label( history_frame, text="History Frame").grid( column = 2, row = 2, sticky=tk.E)

mainframe.tkraise()


if(DEBUG):
    print(f'cal dir is : {dir(DateEntry)}')
    print(f'cal dir is : {dir(date_e.get_date())}')

bw_entry.focus()
root.bind("<Return>", record_bw_cb)
root.bind("<<DateEntrySelected>>", selected_date)

root.mainloop()
