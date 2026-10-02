# :material-button-pointer: Lesson 14 - UI Buttons and Interaction

Source video: [Node Communication! Using Signals for UI Interaction](https://www.youtube.com/watch?v=MYYM1J5UIk0)

## Learning Intention

Display the score clearly, then create a simple test button.

## Success Criteria

- I can add a UI button.
- I can connect the button's pressed signal.
- I can run code when a button is clicked.
- I can place UI elements clearly.

## Keywords

| Keyword | Meaning |
|---|---|
| UI | User interface: buttons, labels and menus. |
| Button | A UI node the player can click. |
| Pressed signal | A signal emitted when a button is clicked. |
| Control node | A Godot node used for interface layouts. |


## Practical Tasks

1. Open `main.tscn` and add a `CanvasLayer` named `UI`.
2. Add a `Label` below UI and name it `ScoreLabel`.
3. Change its text to `Score: 0` and place it near the top-left corner.
4. In `main.gd`, update the existing Spark function:

```gdscript
func _on_spark_collected(value) -> void:
    score += value
    $UI/ScoreLabel.text = "Score: " + str(score)
```

5. Test one Spark. The label should change from `Score: 0` to `Score: 1` once.
6. Add a `Button` below UI and change its text to `Test Button`.
7. Select the Button, open **Node > Signals**, and connect `pressed` to Main.
8. In the new function, add `print("Button pressed")` and test it.

The node path `$UI/ScoreLabel` only works if the nodes have those exact names and positions in the scene tree.

