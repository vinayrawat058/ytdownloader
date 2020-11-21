from pytube import YouTube
from tkinter.filedialog import *
from tkinter.messagebox import *
from tkinter import *
from threading import *
from PIL import ImageTk,Image

# for checking all streams of the video 

#st = yt.streams.first()
#st.download()

font = ('verdana', 20)
file_size = 0

#oncomplete callback function 
def completeDownload(stream=None,file_path = None):
    print("Download completed")
    showinfo("Message", "File has been downloaded...")
    downloadBtn['text'] = "Download Video "
    downloadBtn['state'] = 'active'
    urlField.delete(0, END)

#onprogress callback function 

def progressDownload(stream=None,chunk = None,bytes_remaining = None):
    percent = (100*(file_size - bytes_remaining)/file_size)
    downloadBtn['text'] = "{:00.0f}%  downloaded ".format(percent)


# download function 
def startDownload(url):
    global file_size
    path_to_save = askdirectory()
    if path_to_save is None:
        return 
    
    try:
        yt = YouTube(url)
        st = yt.streams.first()

        yt.register_on_complete_callback(completeDownload)
        yt.register_on_progress_callback(progressDownload)

        # filesize in bytes
        file_size = st.filesize
        st.download(output_path = path_to_save)
    except Exception as e:
        print(e)
        print("Oops... Something went Wrong!!!")

def btnClicked():
    try:
        downloadBtn['text'] = "Please wait"
        downloadBtn['state'] = 'disabled'
        url = urlField.get()
        if url == '':
            return
        print(url)
        thread =Thread(target = startDownload, args = (url,))
        thread.start()

    except Exception as e:
        print(e)


# gui coding
root = Tk()
root.title("Video Downloader")
#root.iconbitmap("img/icon.ico")
root.geometry("600x600")


#main icon section 

#file = PhotoImage()
#headingIcon = Label(root,image = file)
#headingIcon.pack(side = TOP, pady = 3)

urlField = Entry(root,font=font,justify=CENTER)
urlField.config(bg='cyan')
urlField.pack(side = TOP, fill=X, padx = 20,pady = 100)
#for cursor to automatically go on Entry 
urlField.focus()


# download button
downloadBtn = Button(root,text = "Download Video", font = font,relief = 'ridge', command = btnClicked)
downloadBtn.pack(side = TOP, pady = 10)
downloadBtn.config(bg='navy',fg='white')

root.mainloop()


