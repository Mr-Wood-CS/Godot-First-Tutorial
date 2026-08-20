# Task 24: Track Score

## Goal

Make collecting sparks increase the score.

## Key Words

| Word | Meaning |
| --- | --- |
| Variable | A named value that can change. |
| Score | Points earned by the player. |

## Do This

1. Open `scripts/main.gd`.
2. Replace it with this code:

```gdscript
extends Node2D

var score := 0
var time_left := 60.0
var running := true

@onready var score_label: Label = $CanvasLayer/ScoreLabel
@onready var time_label: Label = $CanvasLayer/TimeLabel
@onready var game_over_panel: Panel = $CanvasLayer/GameOverPanel
@onready var game_over_label: Label = $CanvasLayer/GameOverPanel/GameOverLabel
@onready var restart_button: Button = $CanvasLayer/GameOverPanel/RestartButton

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

Press Play and collect a spark. The score should increase.
