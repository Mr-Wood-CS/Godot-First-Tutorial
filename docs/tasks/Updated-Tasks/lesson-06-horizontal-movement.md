# :material-arrow-left-right: Lesson 6 - Horizontal Flight

Source video: [Basic 2D Movement! Making a Character Walk](https://www.youtube.com/watch?v=uRoh_H8F2Qs)

## Learning Intention

Make the Player ship fly left and right using keyboard input.

## Success Criteria

- I can check keyboard input.
- I can change velocity.
- I can use `move_and_slide()`.
- I can tune movement speed.

## Keywords

| Keyword | Meaning |
|---|---|
| Input | A key, button, or action controlled by the player. |
| Velocity | Speed and direction of movement. |
| `move_and_slide()` | A Godot method used to move a character body. |
| Speed | How fast an object moves. |

## Worked Example

Replace `player.gd` with this **complete script**:

```gdscript
extends CharacterBody2D

var speed = 200.0

func _physics_process(_delta: float) -> void:
    var direction = Input.get_axis("ui_left", "ui_right")
    velocity.x = direction * speed
    move_and_slide()
```

## Practical Tasks

1. Open `player.gd` and enter the complete script above.
2. Run `main.tscn` and press the Left and Right Arrow keys.
3. Check that the Player stops when neither key is pressed.
4. Try `100.0`, `200.0`, and `400.0` for `speed`.
5. Restore the value that feels easiest to control.

Positive x movement goes right. Negative x movement goes left. `move_and_slide()` applies the velocity to the `CharacterBody2D`.

## Test It

The Player should move left and right and stop when no movement key is held.
