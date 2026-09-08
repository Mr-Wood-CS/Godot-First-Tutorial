# Task 24: Track Score

## Goal

Make collecting sparks increase the score.

## Do This

1. Check your Scene panel matches the HUD tree in [Task 23](23-build-hud.md), then save `Main.tscn`.
2. Select the `Main` root node and click the script icon beside it. This opens `res://scripts/main.gd`, which you attached in [Task 18](18-print-spark-score.md).
3. Replace **all** the code in `main.gd` with the complete version below. Do not paste it underneath the old code or attach it to `HUD`.

!!! warning "No script icon beside Main?"
    Complete the script attachment steps in [Task 18](18-print-spark-score.md) first,
    then return here. This code belongs on the `Main` **Node2D** root node.

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

The time stays at `TIME 60.0` until Task 25.

## If It Does Not Work

- **`Node not found` or an error mentioning a `null instance`:** stop the game and compare your Scene panel with the tree in [Task 23](23-build-hud.md). For example, `$CanvasLayer/HUD/ScoreLabel` means `Main > CanvasLayer > HUD > ScoreLabel`. Check every name and parent, including the hidden panel and its children: this script needs all five HUD nodes.
- **An error about a script inheriting from `Node2D`:** check that `main.gd` is attached to `Main`, not `HUD` or `CanvasLayer`.
- **Sparks disappear but the score stays at zero:** select each spark instance in `Main.tscn` and check that the group `spark` (lowercase, singular) is ticked, as in [Task 17](17-place-sparks.md). Save the scene and run again.
- **An error about a function already being declared:** replace the whole script with the code above. There should be only one `_ready()` and one `_on_spark_collected()`.
