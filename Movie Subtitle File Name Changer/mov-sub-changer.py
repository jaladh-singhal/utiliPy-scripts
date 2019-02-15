import sys, os, re, shutil

#Input: Min size of video files to be considered as movies 
if len(sys.argv)>1:
	minMovMB=int(sys.argv[1])
else:
	minMovMB=100
minMovSize=minMovMB*(10**6) #1MB=10^6B

#Input: Directory Path - 
path=input('Input path of directory: ')
if not os.path.isdir(path):
	print('Invalid directory path!')
	sys.exit()

cnt=0
for folder,subfolders,files in os.walk(path):
    movName=''
    subtFile=''
    for f in files:
        movMO=re.search(r'^(.+)(\.(mkv|mp4|avi))$',f)
        if movMO:
            movSize=os.path.getsize(os.path.join(folder,f))
            if movSize>=minMovSize: #To exclude Sample/Trailer present in the folder
                movName=movMO.group(1)  #Capture Movie Filename (without extension)

        if f.endswith('.srt'):
            subtFile=f #Capture Subtitle Filename (with extension)

    if movName and subtFile and (movName+'.srt'!=subtFile):
        subtPath=os.path.join(folder,subtFile)
        newSubtPath=os.path.join(folder,movName+'.srt')
        print('Renaming the subtitle file present in %s...\n%s ---> %s\n'%(folder,subtFile,movName+'.srt'))
        shutil.move(subtPath,newSubtPath)   #Renaming Subtitle Name in same location
        cnt+=1

print('\n%s files successfully renamed'%cnt)
