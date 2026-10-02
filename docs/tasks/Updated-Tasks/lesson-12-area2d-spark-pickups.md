# :material-circle-slice-8: Lesson 12 - Area2D Spark Pickups

Source video: [Reusable Scene! Creating a Coin Pickup](https://www.youtube.com/watch?v=jWh_IC6e43U)

## Learning Intention

Use `Area2D` to detect when the Player collects a Spark.

## Success Criteria

- I can use an `Area2D` pickup.
- I can add a collision shape for detection.
- I can connect a body entered signal.
- I can remove a collected Spark.

## Keywords

| Keyword | Meaning |
|---|---|
| Area2D | A node used to detect when objects enter an area. |
| Detection | Noticing when one object enters another object's area. |
| Signal | A message emitted when something happens. |
| `queue_free()` | Removes a node safely from the scene. |


## Worked Example

### Add the Player group

1. Open `player.tscn` and select the top `Player` node.
2. Click **Node** on the right, then **Groups**.
3. Type `Player` with a capital **P** and click **Add**.
4. Make sure the box beside `Player` is ticked.

Group names are case-sensitive. `Player` and `player` are different names.

### Connect the built-in signal

1. Open `spark.tscn` and select the top `Spark` node.
2. Click **Node**, then **Signals**.
3. Double-click `body_entered` and click **Connect**.
4. Godot opens `spark.gd` and creates `_on_body_entered`.
5. Make the new function look like this:

```gdscript
extends Area2D

func _on_body_entered(body: Node2D) -> void:
    if body.is_in_group("Player"):
        queue_free()
```

`body` is the object that entered the Spark. The `if` line makes sure the object belongs to the exact `Player` group before removing the Spark.

**Connect this signal once.** If `body_entered` already shows a connection icon in the Signals list, do not connect it again and do not also connect it in `_ready()`.

## Practical Tasks

1. Check that Spark is an `Area2D` with a `CollisionShape2D`.
2. Add the Player to the exact group `Player`.
3. Connect `body_entered` once.
4. Use `queue_free()` only after the Player group check.
5. Run `main.tscn` and touch the single Spark with the Player.

## If It Does Not Work

Check these in order:

1. Both Player and Spark have a `CollisionShape2D` with a Shape resource.
2. The Player is in the group `Player`, with a capital **P**.
3. `body_entered` is connected to `_on_body_entered` in `spark.gd`.
4. The Spark's collision layer and mask allow it to detect the Player.

