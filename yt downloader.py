from pytube import YouTube

n = input("Enter Url = ")

YouTube(n).streams.first().download()

yt = YouTube(n)

yt.streams

first()

download()
