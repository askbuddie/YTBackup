# !/usr/bin/python3

import os
import json
import sys
import time

import subprocess
import urllib.request
from bs4 import BeautifulSoup
from pytube import YouTube
import tkinter as tk
import tkinter.filedialog as fd
from tkinter import ttk
from tkinter import messagebox

COMMAND_TYPE = sys.argv
dest_folder_path = ""
dest_file_path = ""
ERROR = ''

# Backup function
def Backup():
    def get_media_metadata(filename):
        result = subprocess.Popen(
            ["hachoir-metadata", filename, "--raw"],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
        )
        results = result.stdout.read().decode("utf-8").split("\r\n")

        # just a little bit of error checking
        if isinstance(results, list):
            try:
                if results[0].startswith("[err!]"):
                  ERROR = 'FILE_ERROR'
                  return ERROR
                
                if results[3].startswith("- height: "):
                    return int(results[3].lstrip("- height: "))
                else:
                    return None
            except IndexError:
                messagebox.showerror("Error","Unable to find any dimensions")
                return None
        else:
            return None

    data = []
    PATH_NAME = dest_folder_path

    
    # creates the array
    def create_file_lists(path):
        # spinner
        

        if os.path.isfile(path):
          video_info = get_media_metadata(os.path.relpath(path))
          # checks if there is any error (ie: if its not a video)
          if video_info != 'FILE_ERROR':
            data.append([os.path.relpath(path), video_info])

        if os.path.isdir(path):
            for x in os.listdir(path):
                # recursively get the files
                create_file_lists(os.path.join(path, x))
        return data

    # create json file
    def createJSON():
       
        with open(dest_file_path, "w") as outfile:
            json.dump(create_file_lists(dest_folder_path), outfile)
            messagebox.showinfo("Backup Succesfully", "Succesfully Created Backup :)")

    createJSON()


# Restore function
def Restore():
    # BACKUP_FILE = 'videos.json'
    BACKUP_FILE = input("Enter Backup file path: ")
    OUTPUT_FOLDER = input("Enter Output Folder Name: ")

    # mix it up, soup it up
    def get_video_link(title):
        print('\nFetching "' + title + '"')
        query = urllib.parse.quote(title)
        url = "https://www.youtube.com/results?search_query=" + query
        response = urllib.request.urlopen(url)
        html = response.read()
        soup = BeautifulSoup(html, "html.parser")
        return soup.find(attrs={"class": "yt-uix-tile-link"})["href"]

    # progress bar
    def get_progress(stream, chunk, file_handle, bytes_remaining):
        percent = float(round((1 - bytes_remaining / filesize), 2))
        progress = "\rProgress: [{0:50s}] {1:.1f}%".format("#" * int(percent * 50), percent * 100)
        print(progress, end="")

    global filesize
    global filesizeMB

    # read json
    with open(BACKUP_FILE) as f:
        data = json.load(f)
        for i in data:

            # get the title - "my-video.mp"
            title = os.path.basename(i[0])
            title, ext = os.path.splitext(title)

            # get the dirname - "/video/html"
            dirname = os.path.join(OUTPUT_FOLDER, os.path.dirname(i[0]))
            if not os.path.exists(dirname):
                os.makedirs(dirname)

            yt = YouTube(get_video_link(title), on_progress_callback=get_progress)

            # get the video by resolution/quality
            video = yt.streams.filter(res=str(i[1]) + "p").first()
            # if the specific quality is not available fallback to max quality
            if video is None:
                video = yt.streams.first()

            filesize = video.filesize
            filesizeMB = str(round(filesize / float(1 << 20), 2)) + "MB"

            print('\nDownloading "' + str(title) + '" size: ' + filesizeMB)
            video.download(dirname)




def backup():
    BackupButton.config(text="Loading...")
    Backup()
    BackupButton.config(text="Backup")


def openfolder():
    global dest_folder_path
    directory = fd.askdirectory(parent=window)
    folderNameLabel.config(text=directory)
    dest_folder_path = directory
    #implementation needed upon folder
    
    
def openfile():
    global dest_file_path
    file = fd.asksaveasfilename(parent=window)
    dest_file_path = file
    outputFolderNameLabel.config(text=file)
    #implementation needed upon file    


window = tk.Tk()

window.title("YT Backup")
window.geometry('800x400')
window.resizable(width=False, height=False)

tabbedView = ttk.Notebook(window)
backupTab = ttk.Frame(tabbedView)
restoreTab = ttk.Frame(tabbedView)

tabbedView.add(backupTab, text='Backup')
tabbedView.add(restoreTab, text='Restore')
tabbedView.pack(expand=1, fill='both')

staticOpenFolderLabel = tk.Label(backupTab, text="Destination Folder")
staticOpenFolderLabel.place(x=150,y=100)

openFolderButton= tk.Button(backupTab,text='Browse', command=openfolder, width=10)
openFolderButton.place(x=150,y=130)


folderNameLabel = tk.Label(backupTab,text="")
folderNameLabel.place(x=150,y=170)


staticOutputFileLabel = tk.Label(backupTab,text="Destination File")
staticOutputFileLabel.place(x=505,y=100)

openFileButton= tk.Button(backupTab,text='Browse', command=openfile, width=10)
openFileButton.place(x=500,y=130)


outputFolderNameLabel = tk.Label(backupTab,text="")
outputFolderNameLabel.place(x=500,y=170)

BackupButton = tk.Button(backupTab,text='Backup',command=backup)
BackupButton.place(x=250,y=300,width=300,height=50) #400 2006


RestoreButton = tk.Button(restoreTab,text='Restore')
RestoreButton.place(x=250,y=300,width=300,height=50)


window.mainloop()







# # check for args
# if len(COMMAND_TYPE) > 1:
#   if COMMAND_TYPE[1] == "--backup":
#       Backup()
#   elif COMMAND_TYPE[1] == "--restore":
#       Restore()
# else:
#     print("Please specify what do you want to do --backup or --restore")

