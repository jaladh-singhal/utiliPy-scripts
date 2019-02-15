# Movie Subtitle Filename Changer
Are you annoyed to add subtitle file everytime you watch a movie on your computer?

#### Simple solution:
1. Put your movie file & subtitle file in a common dedicated directory (which you usually do while downloading the subtitles)
2. Change the name of Subtitle file to same as that of Movie filename so that subtitles are automatically added everytime when you play the movie. 

###### But aren't you lazy to change the names of all those subtitles files?
#### Here comes the Automation Aid: 
Run this script, it will do this job.

## Usage
1. Run script from terminal: 
```
$python3 mov-sub-changer.py
```
2. You will be prompted to input the path of directory which contains all of your movie subdirectories, e.g.: 
```
Input path of directory: ~/Movies/Holly
```
3. Voila! the script will walk down to all subdirectories in the specified path to identify the movie files & change the names of corresponding subtitle files. 
##### Optional parameter:
You can also specify minimum movie size (in MBs) while running the script, e.g.:
```
$python3 mov-sub-changer.py 250
```
This will tell the script that in the input directory path, all video files with less than specified size are not to be considered as movies. Hence the samples or trailers (of smaller size) present along with movies will not misguide the script in movie name selection. 
Default value of this minimum size is: 100MB
