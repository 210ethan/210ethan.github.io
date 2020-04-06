#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 19:12:07 2020

@author: EthanMorse

- open Goodreads book spreadsheet
- go through reviews column. if there is data, add row number to list
- add title, author, rating, and review to html table
    - https://www.csestack.org/python-generate-html/
- write to book_reviews.html file (ensure all the other info has been added
beforehand)

"""

from openpyxl import Workbook
from openpyxl import load_workbook


def get_rows():
    
    # load workbook
    wb = load_workbook(filename = "goodreads_library_export.xlsx")
    ws = wb.active
    
    # initialize row number to be 1, no applicable rows in list yet
    row_num = 1
    row_list = []
    
    # iterate through "read" or "to-read" column (column S)
    for cell in ws["S"]:
        
        #if I've read it, append row numebr to row_list
        if cell.value == ("read"):
            row_list.append(row_num)
        row_num += 1
        
    return row_list
        
            

def create_html_table(row_list):
    
    wb = load_workbook(filename = "goodreads_library_export.xlsx")
    ws = wb.active
    
    start_table = "<table>"
    end_table = "</table>"
    final_table = ""
    header = "<tr><th>Title</th><th>Author</th> \
                     <th>My Rating</th><th>My Review</th></tr>"
    rows = ""
    
    
    for row_num in row_list:
        
        # find specific cell values for title, author, rating, review
        title_cell = "B" + str(row_num)
        author_cell = "C" + str(row_num)
        my_rating_cell = "H" + str(row_num)
        my_review_cell = "T" + str(row_num)
        
        # create HTML table strings containing each cell's info
        start_row = "<tr>"
        title = "<td>" + str(ws[title_cell].value) + "</td>"
        author = "<td>" + str(ws[author_cell].value) + "</td>"
        my_rating = "<td>" + str(ws[my_rating_cell].value) + "</td>"
        my_review = "<td>" + str(ws[my_review_cell].value) + "</td>"
        end_row = "</tr>"
        
        # add all info to create a single HTML table row
        rows = rows + start_row + title + author + my_rating + my_review + end_row
    
    # concatenate all strings to create final table
    final_table = start_table + header + rows + end_table

    return final_table

def html_preamble_end():
    
    preamble = """<!DOCTYPE html><html><head><title>Book Reviews</title><style> \
                table, th, td {border: 1px solid black;}.center { \
                display: block; margin-left: auto; margin-right: auto; \
                width: 50%;}</style> <link rel="stylesheet" type="text/css" \
                href="../../main.css"><link rel="icon" href="../../images/ \ 
                ethan_morse_favicon.png"></head><body>"""
                
    end_html = "</body></html>"
    
    return preamble, end_html



def write_to_file(final_table, preamble, end_html):
    
    file = open("book_reviews.html", "w")
    
    file_contents = preamble + final_table + end_html
   
    file.write(file_contents)

    
def main():
    
    row_list = get_rows()
    
    final_table = create_html_table(row_list)
    
    preamble, end_html = html_preamble_end()
    
    write_to_file(final_table, preamble, end_html)
    
main()
    
    
    
