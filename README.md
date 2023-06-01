# This is a neural network based WLASL checkpoint provided by "openhands", this project takes the code into the next step by providing a computer vision system that records the videos when hands are in frame, automatically converts them using "mediapipe holistic", translates and inserts the keywords in a NLP machine.

"openhands" provided the checkpoint for the neural network based machine trained on the WLASL dataset

"keytotext" provided the NLP machine to generate sentences from key words

Changes were made to the "openhands" module code, the updated code can be found in "updated_module_openhands_code" and the path names for them can be found in "importantPaths.txt"

Please follow "requirements.txt" and download the versions of the modules that are mentioned there, I do not know if it will work if changes to version are made by user

I am running ubuntu 20.04 with python version "Python 3.8.10" that is the version of python where all modules worked for me properly

Make sure to have a camera connected to your PC and run setup.py to run the project, it will start a recording when hand is in frame, and stop it when its out, those are the words in ASL, then in order to finish the sentence and start the automatic convertion to pkl and translation, point your finger to the top left of the frame, that will automatically close to window and start everything

Please make sure to change all paths accordingly, there are a lot of them, also in the config.yaml file, for more information on that file, please have a look at the openhands github page

Please move the file "pose_landmark_heavy.tflite" to the path mentioned for it in the "importantPaths.txt" file

You may move the directory "finalProject" to home so the paths mentioned in the code will automatically match, the name of my system user is "tester", if you are running this project from a fresh installation you want to call it the same for an easier time

For more info about the paths and what to change, I will do so per request, so please mail me at "talmc100@gmail.com" for more info if needed.

Best Regards,
Tal Shrem
