# Task 25: Add The Timer

## Goal

Make the time count down.

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

func update_hud() -> void:
    score_label.text = "SCORE %05d" % score
    time_label.text = "TIME %04.1f" % time_left

func _on_restart_pressed() -> void:
    get_tree().paused = false
    get_tree().reload_current_scene()
```

## Check

Save the script.

Press **F5**. When the timer reaches zero:

- The ==TIME UP== panel should appear.
- The player and hunters should stop moving.
- Clicking **RESTART** should start a new game with 60 seconds and a score of zero.

The code pauses the game when time runs out. The panel's **Always** process mode keeps its Restart button working while the game is paused.

??? tip "The timer stops but the panel is missing"
    Stop the game and follow the panel visibility check in [Task 23](23-build-hud.md#check-the-game-over-box). Check any red error in the Debugger too: a wrong node name can stop the function before it shows the panel.
