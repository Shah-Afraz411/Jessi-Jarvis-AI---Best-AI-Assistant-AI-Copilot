# Jessi-Jarvis-AI---Best-AI-Assistant-AI-Copilot

<br><br>
Jessi is AI virtual assitant chatbot like Jarvis of Ironman.
<br>
Morelikely the female version of Jarvis.
<br>
# Hope U like my project
<br>

*Description:*
<br>
Jessi is your AI Assistant enabled on your voice. It uses Gemini chatbot API to make answers of your questions. It performs task that you say to her.
<br>
Step 1: Jessi is initialized
<br>
Step 2: Say Jessi To wake it up. Once, waked up U are good to go.
<br>
Step3: Jessi can do some tasks for you which are.
<br>
  1- Say  "OPen GOOGLE/Facebook/Youtube/LinkedIN" to open GOOGLE/Facebook/Youtube/LinkedIN
  <br>
  2- Say "News Tesla/Apple" to Open their news i have added only these two. You can add more by your self.
  <br>
  3- Say "Play afsany/softly" to play any of this song you want on youtube. you can add more songs on MusicLibrary.py file.
  <br>
  4- Say anything, Jessi will answer it. As, it integrated with Gemini chatbot. And it uses Gemini to answer your every question.

 * Key Features:*
Speech Recognition:

Listens to user input via a microphone using the speech_recognition library.
Uses Google's Speech-to-Text API to convert speech into text.
Task Processing:

Web Browsing: Opens Google, Facebook, Instagram, LinkedIn, YouTube based on commands.
Music Playback: Plays specific songs from a predefined music library.
News Updates: Fetches and reads out Tesla or Apple-related news using the NewsAPI.
Chatbot Interaction: For general queries, Jessy interacts with Google's Gemini ChatBot API to provide intelligent responses.
Text-to-Speech:

Converts text responses into audio using the pyttsx3 library.
Error Handling:

Handles ambient noise by adjusting the microphone sensitivity.
Includes exceptions for unrecognized speech or issues with APIs.
Continuous Listening:

The assistant remains active in a loop, waiting for the wake word ("Jessy") to activate.


  +-------------------------+       +----------------------------+
|     Microphone Input    |       |   Google Speech-to-Text    |
|                         |       |    (speech_recognition)    |
+-------------------------+       +----------------------------+
             |                                |
             v                                v
   +----------------+            +----------------------------+
   | Speech Command | ---------->| Command Processing Module  |
   | Detection      |            | (process_audio function)   |
   +----------------+            +----------------------------+
                                           |
       +-----------------------------------+----------------------------------+
       |                                   |                                  |
+--------------+                   +--------------------+           +-------------------------+
| Open Website |                   |  Fetch News (API) |           |  Interact with ChatBot   |
| (Webbrowser) |                   |  (requests module)|           | (Google Gemini API)      |
+--------------+                   +--------------------+           +-------------------------+
       |                                  |                                |
       v                                  v                                v
+-------------------+          +-------------------+           +---------------------+
| Launch Browser    |          | Display News &    |           | Generate ChatBot    |
|                   |          | Speak Titles      |           | Response & Speak    |
+-------------------+          +-------------------+           +---------------------+
                                      
                             +------------------------------+
                             | Text-to-Speech Conversion    |
                             | (pyttsx3)                    |
                             +------------------------------+
