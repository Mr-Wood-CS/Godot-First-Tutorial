# Task 17: Place Sparks

## Goal

Put collectible sparks in the arena.

## Do This

1. In the FileSystem panel, double-click `scenes/Main.tscn`.
2. Drag `scenes/Spark.tscn` from the FileSystem panel into the 2D view.
3. Use the Move tool to put the spark inside the bright border.
4. With the spark selected, open **Node > Groups** on the right. Create a group called `spark` and tick its box.
5. Press **Ctrl+D** or **Cmd+D** five times so there are six sparks altogether.
6. Move each spark to a different place inside the border.

## Check

Press **F5**. You should see six sparks. Touching one with the player should make it disappear.

!!! note "Check the instance and the group"
    Save `Spark.tscn` before placing it in `Main.tscn`. Drag in the scene file,
    not `spark.gd`, and do not create a fresh `Area2D` and just rename it
    `Spark`. Each instance needs the script and children from Tasks 14–16.

    For step 4, select the Spark instance root (`Area2D`) in the Scene panel.
    Only the six Spark roots should have `spark` ticked in **Node > Groups**.
    Leave `Main`, `Player`, `Polygon2D`, and `CollisionShape2D` out of that group.
    Duplicating the first instance copies its group membership too.

Save `Main.tscn` with **Ctrl+S** or **Cmd+S** before running.

If sparks do not disappear, check that the `Player` instance root belongs to
`player`, as in [Task 11](11-add-player-to-main.md), and check the script
attachment from [Task 16](16-add-spark-script.md). The Spark's **Monitoring**
should be on and its collision shape should not be disabled. With the default
collision settings, the Player's **Collision Layer** and the Spark's
**Collision Mask** should both include layer `1`.
