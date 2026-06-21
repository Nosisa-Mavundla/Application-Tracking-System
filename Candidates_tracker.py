"""""
==========================================================
APPLICATION TRACKING SYSTEM
A production-grade Python CLI application
Author: Nosisa Mavundla
Description: Track, manage, and report on job candidates
            using csv storage and OOP design principles.

===========================================================
"""""
import csv
import json
import os
import uuid
import datetime
import re

#The name of our storage file
CSV_FILE = "candidates.csv"

#Statuses a candidate can have in the order of the hiring pipeline.
VALID_STATUSES =["Applied,", "Screening", "Interview", "Offer","Hired", "Rejected"]

#CSV Headers
CSV_HEADERS = ["Id","FullName", "Email", "Phone", "Location", "Position","SalaryExpectation", "Status", "DateApplied", "Source", "Notes"]

#Clear the terminal
def clear_screen():
    os.system("cls" if os.name=="nt" else "clear")

#Get today's date
def get_today():
    return datetime.date.today.isoformat()

#Checking if the email i valid
def is_email_valid(Email):
    pattern =r"^[\w\.-]+@[\w\.-]+\.\w{2,}$"
    return re.match(pattern, Email) is not None

#Prints a decorative line to make the terminal output look clean
def print_separator(char="-", length= 60):
    print(char*length)

def print_header(tittle):
    print()
    print_separator("=")
    print(f" {tittle}")
    print_separator("=")
    print()
    


