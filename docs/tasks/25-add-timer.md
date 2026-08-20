# Task 25: Add The Timer

## Goal

Make the time count down.

## Do This

1. Open `scripts/main.gd`.
2. Add this function below `_ready()`:

```gdscript
func _process(delta: float) -> void:
    if not running:
        return

    time_left -= delta
    if time_left <= 0.0:
        time_left = 0.0
        end_run("TIME UP")

    update_hud()
```

3. Add this function above `update_hud()`:

```gdscript
func end_run(message: String) -> void:
    if not running:
        return

    running = false
    game_over_label.text = message
    game_over_panel.visible = true
```

## Check

Press Play. The timer should count down.
