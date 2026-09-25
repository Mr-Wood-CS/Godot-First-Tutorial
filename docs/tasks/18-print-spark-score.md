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

Save the script and `Main.tscn` with **Ctrl+S** or **Cmd+S**.

The loop connects the `collected` signal on every node in the `spark` group.
Each of those nodes must have `spark.gd` attached to provide that signal.

## Check

The Scene panel should now show a script icon beside the `Main` root node. You can
click that icon whenever a later task asks you to edit the Main script.

Press **F5** and collect a spark. Close the game window, then look at the **Output** panel along the bottom of Godot. It should show `Collected spark worth 10 points`.

## If You Get An Invalid Access Error

An error such as `Invalid access to property or key 'collected' on a base object`
at `spark.collected.connect(...)` means a node in the `spark` group does not
provide that signal. The node's name alone does not give it a signal.

1. Stop the game. Check the spelling in both scripts: use
   `signal collected(value: int)` in `spark.gd` and
   `spark.collected.connect(_on_spark_collected)` in `main.gd`.
   Names are case-sensitive: `Collected` and `collected` are different.
2. Open `scenes/Spark.tscn` and select the `Spark` root. Its **Script** property
   must be `res://scripts/spark.gd`. If it is empty, drag that script from the
   FileSystem panel onto the root. Check the code against
   [Task 16](16-add-spark-script.md), fix any red errors, and save the scene.
3. Open `scenes/Main.tscn`. Check **Node > Groups** for the nodes in the Scene
   panel. Untick `spark` on anything that is not a Spark instance root,
   especially `Main` or either of a spark's children. Keep it ticked on each
   of the six Spark roots.
4. Select each Spark instance and check its **Script** property too. If you
   added a plain `Area2D` instead of instancing the saved scene, replace that
   node by dragging in `scenes/Spark.tscn`, set its position, and tick `spark`
   on its root as in [Task 17](17-place-sparks.md).
5. Save the script and `Main.tscn`, then press **F5** again.

To identify the offending node if it is still unclear, temporarily insert this
line inside the `for` loop, immediately before `spark.collected.connect(...)`,
at the same indentation:

```gdscript
        print(spark.get_path(), " | script: ", spark.get_script(), " | collected signal: ", spark.has_signal("collected"))
```

Run again and look at **Output**. The last printed node before the error is the
one to check; `collected signal: false` confirms that it lacks the signal.
Fix its script or group membership, then remove the temporary print line.

If sparks disappear but no points message appears, check that all six Spark
instance roots have `spark` ticked and that `main.gd` is attached to `Main`.
