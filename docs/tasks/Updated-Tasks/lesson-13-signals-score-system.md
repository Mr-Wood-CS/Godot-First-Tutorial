# :material-bell-ring: Lesson 13 - Signals and Score System

Source video: [Reusable Scene! Creating a Coin Pickup](https://www.youtube.com/watch?v=jWh_IC6e43U)

## Learning Intention

Use a signal to notify Main when a Spark is collected and update the score.

## Success Criteria

- I can describe what a signal does.
- I can emit a custom signal.
- I can update a score variable.
- I can test whether each Spark increases the score once.

## Keywords

| Keyword | Meaning |
|---|---|
| Emit | Send out a signal. |
| Listener | Code that responds to a signal. |
| Score | A value that tracks progress or points. |
| Custom signal | A signal created by the programmer. |


## Worked Example

Replace `spark.gd` with this **complete script**:

```gdscript
extends Area2D

signal collected(value)

@export var value = 1

func _on_body_entered(body: Node2D) -> void:
    if body.is_in_group("Player"):
        collected.emit(value)
        queue_free()
```

The Spark sends its value before it removes itself.

### Connect Spark to Main

1. Open `main.tscn` and select the Spark instance.
2. Click **Node**, then **Signals**.
3. Double-click the custom `collected` signal.
4. Choose the `Main` node as the receiver and click **Connect**.
5. Godot opens `main.gd` and creates a receiving function.
6. Add the score variable near the top of `main.gd`, then make the receiving function match this example:

```gdscript
var score = 0

func _on_spark_collected(value) -> void:
    score += value
    print("Score: ", score)
```

`collected.emit(value)` sends one value, so the receiving function must also have one `value` parameter.

**Do not connect the same signal in both the editor and code.** If the score increases twice or Godot reports that a signal is already connected, inspect **Node > Signals** and keep only one connection.

## Practical Tasks

1. Add the custom `collected(value)` signal to Spark.
2. Emit it only when a body in the `Player` group enters.
3. Connect the custom signal from the Spark instance to Main once.
4. Add `score` to `main.gd` and increase it by `value`.
5. Test one Spark. It should disappear and print `Score: 1` once.
6. Only after that works, add more Spark instances and connect each instance's `collected` signal to the same Main function.

