# 🚀 Installation Steps


1. Clone or Download the Repository
You can either clone the repository using Git or download it as a ZIP file.

Option 1: Clone the repository using Git
Open a terminal or command prompt and run:

git clone https://github.com/vilmero11e/plex-mood-player.git

## Option 2: Download as a ZIP file
If you don't have Git installed, you can manually download the ZIP file from the repository's GitHub page. Extract it to a folder on your computer.

## 2. Install Required Python Libraries
Navigate to the folder where Plex Mood Player is located. You will need to install the required dependencies listed in the requirements.txt file. To install them, run the following:


pip install -r requirements.txt
This will automatically install all necessary libraries for the script to function properly.

Required Libraries:
urllib
random
webbrowser
urllib.parse
Note: These libraries are standard Python libraries, so if you are using Python 3.x, they should already be installed.

## 3. Run the Script
Once the dependencies are installed, you can run the Plex Mood Player script.

Open a terminal or command prompt.
Navigate to the folder where the script is located.
Run the following command:
bash
Copy code
python plex_mood_player.py
The program will prompt you to input your mood (e.g., "happy," "sad," "action," "romantic," "comedy," or "horror") and will recommend a movie accordingly.

## 4. Enjoy the Movie!
Once the program recommends a movie based on your mood, it will automatically open the movie search page in your default web browser on the Plex platform.

## 💡 Troubleshooting
Python Not Installed: If you don’t have Python installed, download it from https://www.python.org/.
Missing Libraries: If you encounter errors about missing libraries, make sure you run pip install -r requirements.txt in the correct folder and that your Python environment is set up properly.
Permission Issues: If you encounter permission errors when installing packages, try running the command with sudo (for macOS/Linux) or run the Command Prompt as Administrator (for Windows).

## 📝 License
This project is licensed under the MIT License. For more information, see the LICENSE file.
