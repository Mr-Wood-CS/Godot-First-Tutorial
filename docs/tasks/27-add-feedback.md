# Task 27: Add Feedback

## Goal

Make collecting a spark feel clearer.

## Watch First

<iframe class="video-frame" src="https://www.youtube.com/embed/04TB9gxz-uM" title="YouTube video: How to Tween in Godot 4" allowfullscreen></iframe>

## Key Words

| Word | Meaning |
| --- | --- |
| Feedback | A sound or visual effect that tells the player what happened. |
| Tween | A small animation made by code. |

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

![Feedback checkpoint](../assets/images/task-07-juice.png){ .media-frame }

## Check

Collect a spark. It should pop before disappearing.
