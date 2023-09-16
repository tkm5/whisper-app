# Whisper-app

## Overview

This application outputs meeting minutes using OpenAI's whisper-API.  
It outputs the minutes in the following two formats.

1. csv

    | index | start_time | end_time | speach_text |
    | --- | --- | --- | --- |
    | 1 | 00:00:00 | 00:00:02 | We're all here. |
    | 2 | 00:00:02 | 00:00:08 | Today we discuss Whisper. |
    | 3 | 00:00:08 | 00:00:15 | Let's discuss the model. |
    | 4 | 00:00:15 | 00:00:33 | Large model will be the best system. |
    | 5 | 00:00:33 | 00:00:43 | But the capacity is large. |

2. text
    
    ```
    [00:00:00] --> [00:00:02] | We're all here.
    [00:00:02] --> [00:00:08] | Today we discuss Whisper.
    [00:00:08] --> [00:00:15] | Let's discuss the model.
    [00:00:15] --> [00:00:33] | Large model will be the best system.
    [00:00:33] --> [00:00:43] | But the capacity is large.
    ```
    

## Quick Start

1. Install Dependencies
    1. Linux  
    `$ sudo apt update && sudo apt install ffmpeg`
    2. MacOS  
    `$ brew install ffmpeg`<br>
        Additional Details<br>
        The MacOS installation command requires **[Homebrew](https://brew.sh/?ref=assemblyai.com)**, and the Windows installation command requires **[Chocolatey](https://chocolatey.org/install?ref=assemblyai.com)**, so make sure to install either tool as needed.
    3. Windows  
    `$ chco install ffmpeg`<br>
        Additional Details<br>
        Finally, if using Windows, ensure that Developer Mode is enabled. In your system settings, navigate to **Privacy & security > For developers**
         and turn the top toggle switch on to turn Developer Mode on if it is not already.
2. Install packages  
`$ pip install -r requirements.txt`
3. Set audio file
    1. Please store your files below  
    `whisper-app/audio_files/`
    2. /Please input the file name below
    settings.py
        
        ```python
        AUDIO_FILE = '<input here>'
        ```
        
4. Run the main.py

## To receive notifications of completed transactions in Discord

1. Please refer to the following URL to obtain the webhook url of the discord.  
[Super Easy Python Discord Notifications (API and Webhook)](https://10mohi6.medium.com/super-easy-python-discord-notifications-api-and-webhook-9c2d85ffced9)
2. Create secret.py as follows.
    
    ```python
    web_hook_url = '<input here>'
    ```
    
3. Additional Details
The discordwebhook package has already been downloaded with the requirements.txt.