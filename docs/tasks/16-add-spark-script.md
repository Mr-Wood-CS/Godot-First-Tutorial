# Task 16: Add Spark Collection

## Goal

Make the spark disappear when the player touches it.

## Do This

1. Open ==scenes/Spark.tscn== and select the ==Spark== root node (the Area2D).

2. Click **Attach Script**, set the path to ==res://scripts/spark.gd==, and click **Create**.

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

Save the script and choose **Scene > Save Scene** so the script attachment is saved too.

The script should have no red error text.

The script connects ==body_entered== itself. You do not need to connect it again
through the Signals panel. Test collection in Main after placing sparks in [Task 17](17-place-sparks.md).

??? tip "The player touches a spark but it does not disappear"
    1. Open ==Main.tscn== and select the **Player** node. In **Node > Groups**, check that ==player== is ticked, exactly lowercase. The group must be on Player, not its Polygon2D or CollisionShape2D child. See [Task 11](11-add-player-to-main.md).
    2. Open ==Spark.tscn==. The **Spark root** must have ==res://scripts/spark.gd== attached. Click its script icon and compare the whole script with the example above, including ==_ready()== and ==queue_free()==.
    3. Check Player and Spark each have a **CollisionShape2D** directly beneath their root. Each needs a Shape resource, **Disabled** off, and Position (0, 0). Use radius 18 for Player and 14 for Spark.
    4. Select the Spark root and check **Monitoring** is on. Under **Collision**, its **Mask** must include layer **1**. In Player's scene, select the Player root and check its collision **Layer** includes **1**.
    5. Save both scenes. Open Main and press **F6**. Check the **Debugger** for errors if collection still fails.

    The ==player== group allows collection. The separate ==spark== group in Task 17
    lets Main connect the score signal; it does not control whether the spark disappears.

??? tip "Check whether the spark detects the player"
    Temporarily add this line directly below ==func _on_body_entered(body: Node2D) -> void:==,
    before the ==if==, indented by one level:

    ```gdscript
        print("Spark touched by ", body.name, " | player group: ", body.is_in_group("player"))
    ```

    Run Main, move into a spark, and check **Output**:

    - A Player message with ==false== means the Player node needs the ==player== group ticked.
    - No message means you should check the script attachment, signal connection, Monitoring, and collision settings above. Enable **Debug > Visible Collision Shapes** before running to check that the actual circles overlap.
    - A Player message with ==true== means detection and the group check work. Check that ==queue_free()== is indented inside the ==if== and look for a runtime error in the Debugger.

    Remove the temporary print line afterwards.
