from django.shortcuts import render
import csv
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

# Create your views here.
def Index(request):
    return render(request, 'Index.html')

def Mumbai(request):
    return render(request, 'Mumbai.html')

def CourseAnalysis(request):
    labels = 'Airforce', 'Navy', 'Armed forces', 'RPF'    
    sizes = [15, 30, 45, 10]
    explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    # list = []
    # plt.savefig('books_read.png')
    # list.append('books_read.png')
    return render(request, 'CourseAnalysis.html', plt.show())

def Ques(request):
    with open('Rough.csv', encoding="utf8") as f:
        csv_reader = csv.reader(f)
        list = []
        for line in csv_reader:
            if line != ['Roll No.', 'Name', 'Phone no.']:
                list.append(line)           
    return render(request, 'Ques.html', {'data': list})
    



# Create your views here.
