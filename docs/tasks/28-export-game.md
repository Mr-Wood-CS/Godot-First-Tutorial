# Task 28: Export The Game

## Goal

Make a build someone else can play without opening Godot.

## Watch First

<iframe class="video-frame" src="https://www.youtube.com/embed/WoXtLBuK11Y" title="YouTube video: Exporting for Windows in Godot" allowfullscreen></iframe>

## Key Words

| Word | Meaning |
| --- | --- |
| Export | Build the game into files that run outside the editor. |
| Preset | A saved group of export settings for one platform. |
| Build | The playable exported game. |

## Do This

1. Open **Project > Project Settings**.
2. Check the main scene is `res://scenes/Main.tscn`.
3. Set the window size to `1280 x 720`.
4. Open **Project > Export**.
5. Add a preset for your platform.
6. Export into a `builds` folder.
7. Open the exported game and test it.

![Export checkpoint](../assets/images/task-08-export.png){ .media-frame }

## Check

The exported build should launch, play, show game over, and restart.
