# Task 26: Add Game Over

## Goal

End the run when a hunter touches the player.

## Key Words

| Word | Meaning |
| --- | --- |
| Game over | The state when the run has ended. |
| `running` | A variable that says whether the run is still active. |

## Do This

1. Open `scripts/main.gd`.
2. In `_ready()`, add this loop:

```gdscript
for hunter in get_tree().get_nodes_in_group("hunter"):
    hunter.player_hit.connect(_on_player_hit)
```

3. Add this function:

```gdscript
func _on_player_hit() -> void:
    end_run("GAME OVER")
```

## Check

Press Play and let a hunter touch the player. The game-over panel should appear.
