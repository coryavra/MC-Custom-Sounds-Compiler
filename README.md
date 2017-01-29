# Minecraft Custom Sound Compiler!

## Why do I need this program?
The purpose of this program is to spare you the physical/emotional/spiritual toll that comes along with designing your own custom sounds for Minecraft. In the past, any Resource Pack Creator who wanted to add custom sounds had to manually edit and update a file called sounds.json. In order to make this (potentially gigantic) file a little more managable, I wrote this python script. 

## What does this program do?
This program is meant to revolutionize the way Resource Pack Creators add custom sounds to the game. It is well-commented, so if you want to understand it, I recommend reading the script itself. Basically, it creates a file system that converts each sound event name to its own directory. If the directory already exists at runtime, it will scan the directory for sounds. If any exist, it will write them to sounds.json. This allows users to easily manage their custom sounds. 

## How do I run the program?
The first step is to locate the default Minecraft sounds.json file. This can be done by going into Minecraft/assets/indexes and opening the current version file. Then search for "sounds.json" and make note of the first 2 characters in its hash. Use these characters in Minecraft/assets/objects to find a folder. In that folder you should find the default sounds.json file, disguised as a hash. Copy this into this folder and rename it as "default_sounds.json". Make sure to place this folder in your resource pack like so: "resourcepacks/*packname*/assets/minecraft/program". After this is done, you are ready to execute the program.

To execute the tree building program, just run 

    $ ./compile_sounds.py

On the first time you run the program, you should see a directory called "sounds" appear with a whole bunch of subdirectories. Simply fill these subdirectories with any .ogg sound file and run the program again to have it compile an updated sounds.json file. Anytime you want to add or remove sounds, just run the program again with your changes made to the directory tree, and it will automatically fix the sounds.json file for you. 

The program will tell you if you have any empty directories (empty directories = no custom sounds for this event)

TL;DR

- Run the program once to get the file directory set up.
- Add any sounds you want to their respective event directory.
- Run the program again to have an updated sounds.json.
- Enjoy!
