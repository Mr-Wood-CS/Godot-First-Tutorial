# Task 7: Make The Player Scene

## Goal

Create the player ship scene.

## Watch First

<iframe width="100%" height="360" src="https://www.youtube.com/embed/CQ36QANa44M" title="YouTube video: Godot 4 top-down movement" allowfullscreen></iframe>

## Do This

1. In the top menu, choose **Scene > New Scene**. Click **Save** first if Godot asks about unsaved work.
2. Click **Other Node** in the middle of the editor.
3. Search for `CharacterBody2D`.
4. Select `CharacterBody2D` and click **Create**.
5. Rename the new root node to `Player`.
6. Press **Ctrl+S** or **Cmd+S**, open the `scenes` folder, and save the file as `Player.tscn`.

The scene should contain only one node for now:

```text
Player
```

## Check

In the FileSystem panel, check that the file is at `res://scenes/Player.tscn`.
It must not be inside the `scripts` folder.
