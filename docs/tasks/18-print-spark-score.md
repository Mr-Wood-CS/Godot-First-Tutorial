# Task 18: Print Spark Score

## Goal

Make `Main` listen when a spark is collected.

## Do This

The `Main` scene does not have a script yet, so make one now.

!!! note "Scene and script are different files"
    `scenes/Main.tscn` stores the nodes in the scene. In this task you attach a new
    script called `main.gd` to its `Main` node. The script is not already inside the
    scene file.

1. Open `scenes/Main.tscn` and select the `Main` root node.
2. Click **Attach Script** above the Scene panel.
3. Set the path to `res://scripts/main.gd` and click **Create**.
4. Replace the starter code with this:

```gdscript
extends Node2D

func _ready() -> void:
    print("Neon Drift online")
    for spark in get_tree().get_nodes_in_group("spark"):
        spark.collected.connect(_on_spark_collected)

func _on_spark_collected(value: int) -> void:
    print("Collected spark worth %s points" % value)
```

## Check

The Scene panel should now show a script icon beside the `Main` root node. You can
click that icon whenever a later task asks you to edit the Main script.

Press **F5** and collect a spark. Close the game window, then look at the **Output** panel along the bottom of Godot. It should show `Collected spark worth 10 points`.
