# python-CI-template
Python CI template for EC500 Software Engineering

Readme:
===
Run main.py to convert video files into 480p and 720p;

Requirements: 
===
showed in requirements.txt

Implementation:
===
Implemented with multi-threading, the program could have this two process simultaneously.
The architecture of it shows below:
![image](https://github.com/ec500-software-engineering/exercise-2-ffmpeg-WayGang/blob/master/architecture.png)


Error/Exceptions Throwing:
===
If you don't have any video files in current path, the program will recognize that and the result:
![image](https://github.com/ec500-software-engineering/exercise-2-ffmpeg-WayGang/blob/master/nofileerror.png)

If you have not installed ffmpeg (or wrong version)yet, the result will be:
![image](https://github.com/ec500-software-engineering/exercise-2-ffmpeg-WayGang/blob/master/noffmpegerror.png)

When you have this problem, please check the requirements of the correct version of ffmpeg, 
this may be the problem that usually shows up.
