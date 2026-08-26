# Task 10: Add Player Movement

## Goal

Make the player move with the keyboard.

## Do This

1. Select the `Player` root node.
2. Click the **Attach Script** button above the Scene panel (a scroll with a green plus).
3. In the Attach Node Script window, set **Path** to exactly
   `res://scripts/player.gd`. The `res://scripts/` part matters: it places the file in
   the `scripts` folder instead of beside `project.godot` or inside `scenes`.
4. Click **Create**.
5. Delete the starter code and type or paste this:

```gdscript
extends CharacterBody2D

@export var speed := 420.0

func _physics_process(_delta: float) -> void:
    var input_vector := Input.get_vector("ui_left", "ui_right", "ui_up", "ui_down")
    velocity = input_vector * speed
    move_and_slide()
    global_position.x = clamp(global_position.x, 24.0, 1256.0)
    global_position.y = clamp(global_position.y, 24.0, 696.0)
```

## Check

Press **Ctrl+S** or **Cmd+S**. In the FileSystem panel, expand `scripts` and check that
it contains `player.gd`. The Scene panel should show a script icon beside `Player`, and
there should be no red error marks beside the code.
