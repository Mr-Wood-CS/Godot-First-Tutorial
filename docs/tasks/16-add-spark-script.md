# Task 16: Add Spark Collection

## Goal

Make the spark disappear when the player touches it.

## Do This

1. Select the `Spark` root node.
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
