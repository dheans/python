from pytube import YouTube  
#where to save  
DOWNLOAD_PATH = "/storage/emulated/0/" #to_do  
#List of links of the video to be downloaded  
video_link=["https://www.youtube.com/watch?v=xWOoBJUqlbI",  
    "https://www.youtube.com/watch?v=xWOoBJUqlbI"  
    ]  
for i in video_link:  
    try:  
        yt = YouTube(i)  
    except:         
        #to handle exception  
        print("Connection Error")  
    mp4files = yt.filter('mp4')  
    d_video = yt.get(mp4files[-1].extension,mp4files[-1].resolution)  
    try:  
        # downloading the video  
        d_video.download(DOWNLOAD_PATH)  
    except:  
        print("There is some Error!")  
print('Videos Download Successfully!')