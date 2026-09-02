# Task 28: Export The Game

## Goal

Make a build that opens without Godot.

## Watch First

<iframe width="100%" height="360" src="https://www.youtube.com/embed/WoXtLBuK11Y" title="YouTube video: Exporting for Windows in Godot" allowfullscreen></iframe>

## Do This

1. Open **Project > Project Settings**.
2. Choose **Application > Run** and check **Main Scene** is `res://scenes/Main.tscn`.
3. Choose **Display > Window > Size**. Check **Viewport Width** is `1280` and **Viewport Height** is `720`, then close Project Settings.
4. Open **Project > Export**.
5. Click **Add...** and choose the preset for the computers that will run the game, such as **Windows Desktop**, **macOS**, or **Linux**.
6. Click **Export Project**, make a folder called `builds`, and save the exported game inside it. Leave **Export With Debug** switched on for this classroom test.
7. Open the exported game and test it.

!!! warning "Missing export templates?"
    Click **Manage Export Templates**, then download and install the version that
    matches Godot.

![Export checkpoint](../assets/images/task-08-export.png)

## Check

The exported build should launch, play, show game over, and restart.
