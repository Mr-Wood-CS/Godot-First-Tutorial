# :material-script-text: Lesson 3 - First GDScript and Hello World

Source video: [Your First Code! Hello World in GDScript](https://www.youtube.com/watch?v=pyhBx2JdNmg)

## Learning Intention

Write and run the first GDScript program in Godot.

## Success Criteria

- I can attach a script to a node.
- I can use `_ready()`.
- I can use `print()` to test code.
- I can read the Output panel.

## Keywords

| Keyword | Meaning |
|---|---|
| GDScript | Godot's built-in scripting language. |
| Script | A file containing code attached to a node. |
| Function | A named block of code. |
| Output | The panel where printed messages appear. |


## Worked Example

```gdscript
extends Node2D

func _ready() -> void:
    print("Hello Godot")
```

## Practical Tasks

1. Open `main.tscn` and select the `Main` node.
2. Click **Attach Script** above the Scene panel.
3. Save it as `res://scripts/main.gd`, then click **Create**.
4. Replace the script with the worked example and run the scene.
5. Open the **Output** panel at the bottom. It should show `Hello Godot` once.
6. Add `print("My name is ...")` on the next indented line and test again.
7. As a controlled error test, remove the final quotation mark from one message and run the scene. Read the error, press **Command+Z**, and test again.

Do not continue until the Output panel shows both messages without a red error.

