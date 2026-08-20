# Task 21: Add Hunter Chase

## Goal

Make the hunter chase the player.

## Key Words

| Word | Meaning |
| --- | --- |
| Target | The object an enemy follows. |
| `direction_to()` | Finds the direction from one position to another. |

## Do This

1. Select the `Hunter` root node.
2. Attach a script called `scripts/hunter.gd`.
3. Add this code:

```gdscript
extends CharacterBody2D

signal player_hit

@export var speed := 130.0

var target: Node2D

func _ready() -> void:
    target = get_tree().get_first_node_in_group("player") as Node2D

func _physics_process(_delta: float) -> void:
    if target == null:
        return

    velocity = global_position.direction_to(target.global_position) * speed
    move_and_slide()

    for index in get_slide_collision_count():
        var collision := get_slide_collision(index)
        var body := collision.get_collider()
        if body is Node and body.is_in_group("player"):
            player_hit.emit()
```

## Check

The script should have no red error text.
