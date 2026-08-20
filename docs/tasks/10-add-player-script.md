# Task 10: Add Player Movement

## Goal

Make the player move with the keyboard.

## Do This

1. Select the `Player` root node.
2. Attach a new script.
3. Save it as `scripts/player.gd`.
4. Replace the code with this:

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

There should be no red error text in the script editor.
