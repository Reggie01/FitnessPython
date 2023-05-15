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
from PIL import ImageTk, Image

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

def prepend_zero(_time):
	if(_time == '00'):
		return _time
	elif(int(_time) < 10):
		return f'0{_time}'
	else:
		return _time
	
class Workout_Window(ttk.Frame):
	def __init__(self,parent):
		ttk.Frame.__init__(self, parent, padding='3 3 12 12', width = 400, height = 800)
		DEBUG = True
		if( DEBUG ):
			print(f'workout window parent: {type(parent)}')
			print(f'self type: {type(self)}')
		self.grid(column = 0, row = 0, sticky=('N', 'W', 'E', 'S') )
		self.heading = ttk.Label(self, padding = '3 3 3 3', anchor = 'center', text="Workout Frame")
		self.heading['borderwidth']=1
		self.heading['relief'] = 'sunken'
		self.heading.grid( column=0, row = 0, columnspan = 4, sticky=('N','S','E','W'))	
		self.columnconfigure([0,1,2,3], weight = 1)

		self.squat_photo = ImageTk.PhotoImage(Image.open("insert_your_photo.gif"))
		exercise_heading = ttk.Label(self, padding='3 3 6 6', anchor = 'center', text='Photo Image')
		exercise_heading.grid( column = 0, row = 1, columnspan = 4, sticky=('N', 'S', 'E', 'W'))
		if DEBUG:
			print(f'type(squat_photo): {type(self.squat_photo)}')
		exercise_heading['image'] = self.squat_photo
		exercise_heading['borderwidth'] = 3
		exercise_heading['relief'] = 'sunken'

		self.set_one_results = tk.StringVar()
		first_set_squat = ttk.Checkbutton(self, text='', variable=self.set_one_results, onvalue='True', offvalue='False', padding="3 3 12 12", command=self.completed_set)
		first_set_squat.grid( column = 0, row = 2, sticky=('W'))
		
		self.results = tk.StringVar()
		squat = ttk.Label(self, text="", padding="3 3 6 6")
		squat.grid( column=1, row = 2, sticky=('W'))
		squat['textvariable'] = self.results
		self.results.set("results")

		squat = (12, 60, 'lb')
		self.rest_timer = 60

		first_squat = ttk.Label(self, padding="3 3 6 6")
		first_squat.grid(column = 2, row = 2, sticky='W')
		self.first_squat_contents = tk.StringVar()
		first_squat['textvariable'] = self.first_squat_contents
		self.first_squat_contents.set(f'{squat[0]} x {squat[1]}{squat[2]}') 
		
		ttk.Label(self, text="Rest", padding='3 3 6 6').grid(column = 0, row = 3, sticky=('W'))
		rest_time_label = ttk.Label( self, padding="3 3 6 6")
		rest_time_label.grid(column = 1, row = 3, sticky=('W'))
		self.rest_time_label_text = tk.StringVar()
		rest_time_label['textvariable'] = self.rest_time_label_text

		mins, secs = divmod(self.rest_timer, 60) 
		self.mins = prepend_zero( str(mins) )
		self.secs = prepend_zero( str(secs) )
		
		self.rest_time_label_text.set(f'{self.mins}:{self.secs}')

		self.progressbar_one = ttk.Progressbar(self, orient = tk.HORIZONTAL, length = 200, mode = 'determinate')
		self.progressbar_one.grid( column = 0, row = 4, columnspan = 2, sticky=('W'))
		self.progressbar_one['maximum'] = mins * 60 * 1.0 + secs * 1.0
		self.progressbar_one['value'] = 0
		
		if DEBUG:
			print(f'self grid size: {self.grid_size()}')
		ttk.Button(self, text="Start", padding="3 3 3 3", command=self.start_workout).grid(column=3, row = 6, sticky=('N', 'W', 'E', 'S'))

	def lift(self):
		print('raising')
		self.tkraise()

	def start_workout(self):
		if DEBUG:		
			print( 'starting workout' ) 
		if( self.rest_timer == 0):
			if DEBUG:			
				print(f'rest timer is: {self.rest_timer}')
			return
		else:
			if DEBUG:
				print(f'rest timer: {self.rest_timer}')
			self.progressbar_one['value'] = self.progressbar_one['value'] + 1
			self.rest_timer = self.rest_timer - 1
			mins, secs = divmod(self.rest_timer, 60)
			self.secs = prepend_zero( str(secs) )
			self.mins = prepend_zero( str(mins) )
			self.rest_time_label_text.set(f'{self.mins}:{self.secs}')
			root.after(1000, self.start_workout)
		

	def completed_set(*args):
		print(args)
		print('completed set')
		print( args[0].set_one_results.get() )
		if( args[0].set_one_results.get() == 'True'):
			print("hey, completed set")
		

root = tk.Tk()
root.title("Fitness Tracker")
root.geometry("400x600")
root.columnconfigure(0, weight = 1 )
root.rowconfigure(0, weight = 1)

# Navigation Frame
navigation_frame = ttk.Frame( root, padding="3 3 12 12", width = 400, height=200 )
navigation_frame.grid( column = 0, row = 10, columnspan = 4)

ttk.Button( navigation_frame, text="Workout", command = show_workout).grid(column = 0, row = 4, sticky=tk.E)
ttk.Button( navigation_frame, text="Program", command = show_program).grid(column = 1, row = 4, sticky=tk.E)
ttk.Button( navigation_frame, text="Exercise", command = show_exercises).grid(column = 2, row = 4, sticky=tk.E)
ttk.Button( navigation_frame, text="History", command = show_history).grid(column = 3, row = 4, sticky=tk.E)


mainframe = ttk.Frame( root, padding="3 3 12 12", width = 400, height = 800)
mainframe.grid( column = 0, row = 0, sticky=('N', 'W', 'E', 'S'))



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


# Workout Frame

workout_frame = Workout_Window(root)
workout_frame['borderwidth'] = 3
workout_frame['relief'] = 'sunken'
#print( type(workout_frame))
#print( Workout_Window.__mro__ )

# Show Program Frame
program_frame = ttk.Frame(root, padding="3 3 12 12", width=400, height= 800)
program_frame.grid(column = 0, row = 0, sticky=('N', 'W', 'E', 'S'))

ttk.Label( program_frame, text="Program Frame").grid(column = 2, row = 2, sticky=tk.E)

# Show Exercises
exercises_frame = ttk.Frame(root, padding="3 3 12 12", width=400, height=800)
exercises_frame.grid(column= 0, row = 0, sticky=('N', 'W', 'E', 'S'))

ttk.Label( exercises_frame, text="Exercise Frame").grid(column = 2, row = 2, sticky=tk.E)

# Show History
history_frame = ttk.Frame(root, padding="3 3 12 12", width=400, height=800)
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
