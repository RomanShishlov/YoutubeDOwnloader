# pip install youtube-dl pafy
import sys
import os
import pafy
from RS_logo import logo

url = ""

v = pafy.new(url)
print(v)
print(v.title)
print(v.duration)
print(v.viewcount)

streams = v.streams
for item in streams:
     print(item)

audio_streams = v.audiostreams
for item in audio_streams:
    print(item)

all_streams = v.allstreams
for item in all_streams:
     print(item.quality)
print(logo)
print("If you want to download video or audio paste the url below...")
url = input("Enter URL: ")

print("For video, press: 1 | For audio press: 2 ")
choice = input("Enter your preffered option: ")

def download(choice):
    try:
        v = pafy.new(url)

        if choice == "1":
            streams = v.streams
        elif choice == "2":
            streams = v.audiostreams
        else:
            sys.exit()

        print("Enter desired quality of. Example: 1: ") if choice == "1" else print("Enter desired audio quality. Example: 2: ")

        available_streams = {}
        count = 1
        for stream in streams:
            available_streams[count] = stream
            print(f"{count}: {stream}")
            count += 1
        print(available_streams)

        stream_count = int(input("Enter the number: "))
        d = streams[stream_count - 1].download()

        if choice == "2":
            audio_extension = str(available_streams[stream_count])
            audio_extension = audio_extension.split("@")[0].split(":")[1]

            file_name = v.title
            music_file = f"{file_name}.{audio_extension}"
            base = os.path.splitext(music_file)[0]
            os.rename(music_file, base + ".mp3")

        print("Download complete!")
    except:
        print("Something went wrong! Please check your data")


download(choice)


# if choice == "1":
#     try:
#         v = pafy.new(url)
#         # print(v.title)
#
#         print("Choose the quality of the video. Example: 1: ")
#
#         available_streams = {}
#         count = 1
#         video_streams = v.streams
#         for stream in video_streams:
#             available_streams[count] = stream
#             print(f"{count}: {stream}")
#             count += 1
#         # print(available_streams)
#
#         stream_count = int(input("Enter the number: "))
#         d = video_streams[stream_count - 1].download()
#         print("Download complete!")
#     except:
#         print("Check data")
# elif choice == "2":
#     try:
#         v = pafy.new(url)
#         # print(v.title)
#
#         print("Choose audio quality. Example : 1: ")
#
#         available_streams = {}
#         count = 1
#         video_streams = v.audiostreams
#         for stream in video_streams:
#             available_streams[count] = stream
#             print(f"{count}: {stream}")
#             count += 1
#         # print(available_streams)
#
#         stream_count = int(input("Enter number: "))
#         d = video_streams[stream_count - 1].download()
#         print("Download complete!")
#     except:
#         print("Check data")
# else:
#     print("Whaaat???")