# Task 27: Add Feedback

## Goal

Make the spark pop when collected.

## Watch First

<iframe width="100%" height="360" src="https://www.youtube.com/embed/04TB9gxz-uM" title="YouTube video: How to Tween in Godot 4" allowfullscreen></iframe>

## Do This

1. Open `scripts/spark.gd`.
2. Replace `queue_free()` with `pop()`.
3. Add this function:

```gdscript
func pop() -> void:
    var tween := create_tween()
    tween.tween_property(self, "scale", Vector2.ONE * 1.6, 0.08)
    tween.tween_property(self, "modulate:a", 0.0, 0.12)
    tween.tween_callback(queue_free)
```

![Feedback checkpoint](../assets/images/task-07-juice.png)

## Check

Collect a spark. It should pop before disappearing.
