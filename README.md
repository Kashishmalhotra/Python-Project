# Python-Project
 



CAC -1
PYTHON PROJECT
(REPORT)

Prof. 
Kandula Balagangadhar



MUSIC PLAYER



By:- 
Kashish
22112015
3BSC DS-A

Introduction:
This Python Music Player application is a simple yet powerful programme that allows users to browse, play, pause, and stop MP3 music files using an easy-to-use graphical user interface (GUI). This programme, created with the ‘tkinter’ and ‘pygame’ libraries, allows users to enjoy their favourite music tracks on their computer in an accessible and interactive manner.
Functionality:
Users can use the music player application to do the following:
1)Browse: Users can browse the directories on their computer and select an MP3 file to play.
2)Play: After selecting a music file, users can start playing it by clicking the "Play" button.
3)Pause: While music is playing, users can pause it by clicking the "Pause" button.
4)Stop: Users can pause music playback by clicking the "Stop" button.
Code Description:
 

•	The ‘os’ module is imported to provide access to various operating system functionalities.
•	The ‘Tk’, ‘Label’, ‘Button’, and ‘filedialog’ classes are imported from the tkinter module. ‘Tk’ is the main class for creating a GUI window, and the others are used to create GUI elements such as labels, buttons, and file dialogs.
•	The pygame module is imported to handle music playback functionality.

 
•	The code defines a class called ‘MusicPlayer’ that represents the music player. It has an ‘__init__’ method, which is the constructor method that initializes the class instance.
•	The constructor takes a window parameter, representing the main window of the GUI, and assigns it to ‘self.window’.
•	The title of the window is set to "Music Player" using ‘self.window.title()’.
 
Three instance variables are initialized:
•	‘self.current_dir’ is set to the current working directory obtained using ‘os.getcwd()’. It will store the directory path of the music player script.
•	‘self.music_file’ is an empty string that will hold the path of the selected music file.
•	‘self.playing’ is a boolean flag that indicates whether music is currently being played. It is set to False initially.
 
The ‘create_widgets()’ method is called to create the various buttons and labels in the GUI.
 
•	The ‘create_widgets’ method creates a Label widget with the text "Music Player".
•	The Label widget is associated with ‘self.window’, the main GUI window.
•	The pack method is called on the Label widget to add it to the window and display it. The ‘pady=10’ argument adds vertical padding of 10 pixels.
 
•	The code creates a Button widget labeled "Browse".
•	The Button widget is associated with ‘self.window’, the main GUI window.
•	The command parameter is set to ‘self.browse_file’, which means that when the button is clicked, the ‘self.browse_file’ method will be called.
•	The pack method is called on the Button widget to add it to the window and display it. The ‘pady=5’ argument adds vertical padding of 5 pixels.
 
A similar process is repeated for the "Play" button.
The command parameter is set to ‘self.play_music’, so when the button is clicked, the ‘self.play_music’ method will be called.
 
A similar process is repeated for the "Pause" button.
The command parameter is set to ‘self.pause_music’, so when the button is clicked, the ‘self.pause_music’ method will be called.
 
A similar process is repeated for the "Stop" button.
The command parameter is set to ‘self.stop_music’, so when the button is clicked, the ‘self.stop_music’ method will be called.
 
•	The ‘browse_file’ method is called when the "Browse" button is clicked.
•	It opens a file dialog using filedialog.askopenfilename, which allows the user to select an MP3 file.
•	The initialdir parameter is set to ‘self.current_dir’, so the file dialog opens in the current directory.
•	The title parameter sets the title of the file dialog window.
•	The filetypes parameter defines the types of files that can be selected. In this case, it allows the selection of MP3 files (".mp3") and all files (".*").
•	If the user selects a file and clicks "Open" in the file dialog, the selected file's path is stored in ‘self.music_file’.
•	If a file is selected, the ‘self.current_dir’ is updated to the directory containing the selected file using ‘os.path.dirname()’.
 
•	The ‘play_music’ method is called when the "Play" button is clicked.
•	It first checks if ‘self.music_file’ contains a valid file path and if music is not already playing.
•	If the conditions are met, it initializes the ‘pygame’ mixer using ‘pygame.mixer.init()’.
•	Then, it loads the selected music file using ‘pygame.mixer.music.load(self.music_file)’.
•	Finally, it starts playing the music using ‘pygame.mixer.music.play()’.
•	The ‘self.playing’ flag is set to True to indicate that music is currently playing.
 
•	The ‘pause_music’ method is called when the "Pause" button is clicked.
•	It checks if music is currently playing by verifying the ‘self.playing’ flag.
•	If music is playing, it pauses the playback using ‘pygame.mixer.music.pause()’.
•	The ‘self.playing’ flag is set to False to indicate that music is paused.
 
•	The ‘stop_music’ method is called when the "Stop" button is clicked.
•	It checks if music is currently playing by verifying the ‘self.playing’ flag.
•	If music is playing, it stops the playback using ‘pygame.mixer.music.stop()’.
•	The ‘self.playing’ flag is set to False to indicate that music has stopped.
 
•	The code block is executed only if the script is run directly and not imported as a module (indicated by __name__ == "__main__").
•	‘pygame.init()’ is called to initialize the ‘pygame’ module for music playback.
•	An instance of the Tk class is created, representing the main window of the GUI, and assigned to the variable root.
•	An instance of the MusicPlayer class is created, passing the root window as a parameter, and assigned to the variable ‘music_player’.
•	Finally, the ‘root.mainloop()’ method is called to start the GUI event loop and display the window until it is closed by the user.
