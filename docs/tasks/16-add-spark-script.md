# Task 16: Add Spark Collection

## Goal

Make the spark disappear when the player touches it.

## Do This

1. Open `scenes/Spark.tscn` and select its `Spark` root node (`Area2D`).
2. Click **Attach Script**, set the path to `res://scripts/spark.gd`, and click **Create**.
3. Replace the starter code with this:

```gdscript
extends Area2D

signal collected(value: int)

@export var value := 10

func _ready() -> void:
    body_entered.connect(_on_body_entered)

func _on_body_entered(body: Node2D) -> void:
    if body.is_in_group("player"):
        collected.emit(value)
        queue_free()
```

## Check

The script should have no red error text.

Press **Ctrl+S** or **Cmd+S** to save the script and `Spark.tscn`.
Select the `Spark` root and check that its **Script** property in the Inspector
is `res://scripts/spark.gd`. Clicking the script icon beside the root should
open the code above, including `signal collected(value: int)`.

!!! note "The script belongs on the Spark root"
    Open `scenes/Spark.tscn` before attaching the script. Attach it to the
    `Spark` root (`Area2D`), not `Polygon2D`, `CollisionShape2D`, or `Main`.
    Creating a file called `spark.gd` is not enough: the root must use it.
    A plain `Area2D` has no `collected` signal; this script adds that signal.
    Use a lowercase `c`: `Collected` and `collected` are different names.
