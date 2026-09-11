# Task 26: Add Game Over

## Goal

End the run when a hunter touches the player.

## Do This

1. Open ==scenes/Main.tscn==, select ==Main==, and click its script icon.

2. Replace the whole of ==main.gd== with this complete version:

!!! warning "No script icon?"
    Complete [Task 24: Track Score](24-track-score.md) first.

```gdscript
extends Node2D

var score := 0
var time_left := 60.0
var running := true

@onready var score_label: Label = $CanvasLayer/HUD/ScoreLabel
@onready var time_label: Label = $CanvasLayer/HUD/TimeLabel
@onready var game_over_panel: Panel = $CanvasLayer/HUD/GameOverPanel
@onready var game_over_label: Label = $CanvasLayer/HUD/GameOverPanel/GameOverLabel
@onready var restart_button: Button = $CanvasLayer/HUD/GameOverPanel/RestartButton

func _ready() -> void:
    game_over_panel.process_mode = Node.PROCESS_MODE_ALWAYS
    game_over_panel.visible = false
    restart_button.pressed.connect(_on_restart_pressed)

    for spark in get_tree().get_nodes_in_group("spark"):
        spark.collected.connect(_on_spark_collected)

    for hunter in get_tree().get_nodes_in_group("hunter"):
        hunter.player_hit.connect(_on_player_hit)

    update_hud()

func _process(delta: float) -> void:
    if not running:
        return

    time_left -= delta
    if time_left <= 0.0:
        time_left = 0.0
        end_run("TIME UP")

    update_hud()

func end_run(message: String) -> void:
    if not running:
        return

    running = false
    game_over_label.text = message
    game_over_panel.visible = true
    get_tree().paused = true

func _on_spark_collected(value: int) -> void:
    if not running:
        return

    score += value
    update_hud()

func _on_player_hit() -> void:
    end_run("GAME OVER")

func update_hud() -> void:
    score_label.text = "SCORE %05d" % score
    time_label.text = "TIME %04.1f" % time_left

func _on_restart_pressed() -> void:
    get_tree().paused = false
    get_tree().reload_current_scene()
```

## Check

Save the script.

Press **F5** and let a hunter touch the player.

- The ==GAME OVER== panel should appear.
- The player and hunters should stop moving.
- Clicking **RESTART** should reset the scene, score and timer, and let you move again.

Test once more by letting the timer reach zero. The same thing should happen with the message ==TIME UP==.

??? tip "The timer stops but the ship still moves"
    Replace the whole Main script with the version above. Setting ==running== to ==false== stops the timer and scoring; ==get_tree().paused = true== also stops the player and hunters.

??? tip "The game-over panel is missing"
    Stop the game and follow the panel visibility check in [Task 23](23-build-hud.md#check-the-game-over-box). If the Debugger shows a red error, check the node names and parents against Task 23.
