# Task 24: Track Score

## Goal

Make collecting sparks increase the score.

## Do This

1. Open `scenes/Main.tscn`, select `Main`, and click its script icon.
2. Replace the code with this:

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
    game_over_panel.visible = false
    restart_button.pressed.connect(_on_restart_pressed)

    for spark in get_tree().get_nodes_in_group("spark"):
        spark.collected.connect(_on_spark_collected)

    update_hud()

func _on_spark_collected(value: int) -> void:
    if not running:
        return

    score += value
    update_hud()

func update_hud() -> void:
    score_label.text = "SCORE %05d" % score
    time_label.text = "TIME %04.1f" % time_left

func _on_restart_pressed() -> void:
    get_tree().reload_current_scene()
```

## Check

Save the script and check that `scripts/main.gd` appears in the FileSystem panel.
Press **F5** and collect a spark. The score should change from `SCORE 00000` to `SCORE 00010`.
