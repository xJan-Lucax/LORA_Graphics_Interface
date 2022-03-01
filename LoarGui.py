import matplotlib

import data_converter
import timex
import ttndata

from datetime import datetime

matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg #NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib import style
import matplotlib.dates

import tkinter as tk
from tkinter import ttk


import threading

#Threads zur Datenerfassung
def co2Data():
    data_converter.loopDataCo2()
def tmpData():
    data_converter.loopDataTMP()
def parData():
    data_converter.loopDataPAR()

def checkDatattnLoop():
    #data_converter.resetTTNdata()
    ttndata.ttndatacheck()

LARGE_FONT = ("Verdana", 12)
style.use("ggplot")

co2graph = Figure(figsize=(5, 5), dpi=100)
co2graphsub = co2graph.add_subplot(111)
temperaturegraph = Figure(figsize=(5, 5), dpi=100)
temperaturegraphsub = temperaturegraph.add_subplot(111)
particlegraph = Figure(figsize=(5, 5), dpi=100)
particlegraphsub = particlegraph.add_subplot(111)

def animateCo2(i):
    pullData = open('dataco2','r').read()
    dataArray = pullData.split('\n')
    xar=[]
    yar=[]
    for eachLine in dataArray:
        if len(eachLine)>1:
            y,x = eachLine.split(',')
            x = datetime.strptime(x, "%Y%m%d%H%M%S")
            xar.append(x)
            dates = matplotlib.dates.date2num(xar)
            yar.append(int(y))
    co2graphsub.clear()
    co2graphsub.plot_date(dates, yar, linestyle ='dotted')

def animateTemperature(i):
    pullData = open('datatemperatur','r').read()
    dataArray = pullData.split('\n')
    xar=[]
    yar=[]
    for eachLine in dataArray:
        if len(eachLine)>1:
            y,x = eachLine.split(',')
            x = datetime.strptime(x, "%Y%m%d%H%M%S")
            xar.append(x)
            dates = matplotlib.dates.date2num(xar)
            yar.append(int(y))
    temperaturegraphsub.clear()
    temperaturegraphsub.plot_date(dates, yar, linestyle ='dotted')

def animateParticle(i):
    pullData = open('datattn','r').read()
    dataArray = pullData.split('\n')
    xar=[]
    yar=[]
    for eachLine in dataArray:
        if len(eachLine)>1:
            y,x = eachLine.split(',')
            x = datetime.strptime(x, "%Y%m%d%H%M%S")
            xar.append(x)
            dates = matplotlib.dates.date2num(xar)
            yar.append(int(y))
    particlegraphsub.clear()
    particlegraphsub.plot_date(dates, yar, linestyle ='dotted')

class LORA_Graphics_Interface(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        tk.Tk.wm_title(self, "LORA_Graphics_Interface")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, temperture_graph_page, particle_graph_page, co2_graph_page):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Hauptmenü:", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button = ttk.Button(self, text="Temperatur Sensor Graphische Auswertung",
                            command=lambda: controller.show_frame(temperture_graph_page))
        button.pack()

        button2 = ttk.Button(self, text="Partikel Sensor Graphische Auswertung",
                             command=lambda: controller.show_frame(particle_graph_page))
        button2.pack()

        button3 = ttk.Button(self, text="CO2 Sensor Graphische Auswertung",
                             command=lambda: controller.show_frame(co2_graph_page))
        button3.pack()


class temperture_graph_page(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Temperatur Sensor Graphische Auswertung", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                             command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = ttk.Button(self, text="Reset",
                             command=lambda: data_converter.resetTMPdata())
        button2.pack()

        canvas = FigureCanvasTkAgg(temperaturegraph, self)
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


class particle_graph_page(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Partikel Sensor Graphische Auswertung", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                             command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = ttk.Button(self, text="Reset",
                             command=lambda: data_converter.resetTTNdata())
        button2.pack()

        canvas = FigureCanvasTkAgg(particlegraph, self)
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

class co2_graph_page(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="CO2 Sensor Graphische Auswertung", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                             command=lambda: controller.show_frame(StartPage))
        button2 = ttk.Button(self, text="RESET",
                             command=lambda: data_converter.resetCO2data())
        button1.pack()
        button2.pack()

        canvas = FigureCanvasTkAgg(co2graph, self)
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


co2Thread = threading.Thread(target=co2Data, daemon=True)
co2Thread.start()
tmpThread = threading.Thread(target=tmpData, daemon=True)
tmpThread.start()
parThread = threading.Thread(target=parData, daemon=True)
parThread.start()
ttnThread = threading.Thread(target=checkDatattnLoop, daemon=True)
ttnThread.start()

app = LORA_Graphics_Interface()
anico2 = animation.FuncAnimation(co2graph, animateCo2, interval=1000)
anitmp = animation.FuncAnimation(temperaturegraph, animateTemperature, interval=1000)
anipar = animation.FuncAnimation(particlegraph, animateParticle, interval=1000)
app.mainloop()
