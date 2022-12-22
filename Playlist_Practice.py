# Solution by Pros. Dung Lai
class Video:
	def __init__(self, title, link):
		self.title = title
		self.link = link

# ------------------------------------------------------ #

def read_video(): # Read one video from user
	title = input("Please enter video title: ")
	link = input("Please enter video link: ")
	video = Video(title, link)
	return video

def read_videos():
	videos_arr = []
	total_video = int(input("Enter how many videos in your playlist? "))
	for i in range(total_video):
		print("Enter video", i+1)
		vid = read_video()
		videos_arr.append(vid) # Create an array of all the videos
	return videos_arr

# ------------------------------------------------------ #

def print_video(video): # Output the info of a video
	print("Video title: " + video.title, end="") 
	print("Video link: " + video.link, end="")

def print_videos(videos):
	print("---")
	for i in range(len(videos)):
		print_video(videos[i])

# ------------------------------------------------------ #

def write_video_txt(videos, file):
	file.write(videos.title + "\n")
	file.write(videos.link + "\n")

def write_videos_txt(videos):
	total_vid = len(videos)
	with open("data.txt", "w") as file:
		file.write(str(total_vid) + "\n")
		for i in range(total_vid):
			write_video_txt(videos[i], file)

# ------------------------------------------------------ #

def read_video_txt(file): # Read 1 video
	title = file.readline() #Read the next line -> Title
	link = file.readline() #Read the next line -> Link
	video = Video(title, link) # Create a new type of video
	return video
	
def read_videos_txt():
	read_videos_arr = []
	with open("data.txt", "r") as file:
		total = file.readline() # Find the total videos
		for i in range(int(total)):
			video = read_video_txt(file)
			read_videos_arr.append(video) # Add the video -> array		
	return read_videos_arr

# ------------------------------------------------------ #

def main():
	videos = read_videos() # Read from user input
	write_videos_txt(videos) # Store -> text file
	videos = read_videos_txt() # Read the text file -> Store into a list var
	print_videos(videos) # Print out all the video from the list

main()

# HW Assignment:
# Copy the main section and Delete everything else
# Practice program each func from scratch 
	






# Note:
# 1st: Always start a project w/ define main and main()
# 

# What does readline do?
#	It read each individual line everytime it got call
# Subscriptable: Truy Cap
