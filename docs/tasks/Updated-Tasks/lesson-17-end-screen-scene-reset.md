# :material-refresh: Lesson 17 - End Screen and Scene Reset

Source video: [Complete Game Loop! Win Condition, End Screen, & Scene Reset](https://www.youtube.com/watch?v=ymcHxVTLbtI)

## Learning Intention

Show an end screen when the player wins and allow the scene to restart.

## Success Criteria

- I can show or hide a UI panel.
- I can connect a restart button.
- I can reload the current scene.
- I can test the game from start to finish.

## Keywords

| Keyword | Meaning |
|---|---|
| End screen | A screen shown after the objective is complete. |
| Reset | Start the scene again. |
| Visible | Whether a node can be seen. |
| Reload | Load the current scene again from the beginning. |


## Worked Example

Build this scene tree below the existing `UI` node:

```text
UI  CanvasLayer
├── ScoreLabel
└── EndScreen  Panel
    ├── WinLabel
    └── RestartButton
```

Select `EndScreen` and untick **Visible** in the Inspector. Change `WinLabel` to `You win!` and `RestartButton` to `Restart`.

```gdscript
func show_end_screen():
    $UI/EndScreen.visible = true

func _on_restart_button_pressed() -> void:
    get_tree().reload_current_scene()
```

Call `show_end_screen()` directly after setting `has_won = true` in the existing win-condition function. Then select `RestartButton` and connect its `pressed` signal to Main once.

## Practical Tasks

1. Create the exact UI scene tree shown above.
2. Hide `EndScreen` using its **Visible** property.
3. Call `show_end_screen()` when the Player wins.
4. Connect `RestartButton.pressed` to Main once.
5. Run the complete game, win, click Restart, and check that the score and Sparks reset.

