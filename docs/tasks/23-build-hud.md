# Task 23: Build The HUD

## Goal

Add score, time, and game-over text to the screen.

## Watch First

<iframe width="100%" height="360" src="https://www.youtube.com/embed/GwCiGixlqiU" title="YouTube video: Godot 4 first 2D game" allowfullscreen></iframe>

## Do This

1. Open `scenes/Main.tscn`.

    Expand `Main > CanvasLayer > HUD` in the Scene panel. Use the `HUD` Control
    created in [Task 5](05-add-title.md). If it is missing, complete that task first.
    Keep the existing title `Label`.

2. Right-click `HUD`, choose **Add Child Node**, and add a `Label`. Rename it `ScoreLabel`.
3. Set its **Text** to `SCORE 00000`. In the Inspector, expand **Layout > Transform** and set **Position** to x `32`, y `32`. Use **Layout > Transform** for all positions and sizes below.
4. Add another `Label` under `HUD`. Rename it `TimeLabel`, set **Text** to `TIME 60.0`, and set **Position** to x `1120`, y `32`.
5. Add a `Panel` under `HUD`. Rename it `GameOverPanel` and set **Position** to x `440`, y `260` and **Size** to x `400`, y `200`.
6. Add a `Label` as a child of `GameOverPanel`. Rename it `GameOverLabel`, set **Text** to `GAME OVER`, **Position** to x `100`, y `35`, and **Size** to x `200`, y `50`. Set **Horizontal Alignment** to **Center**.
7. Add a `Button` as another child of `GameOverPanel`. Rename it `RestartButton`, set **Text** to `RESTART`, **Position** to x `125`, y `115`, and **Size** to x `150`, y `50`.
8. Select `GameOverPanel`. In the Inspector, open **Visibility** and switch off **Visible**.
9. Save `Main.tscn` with **Ctrl+S** or **Cmd+S**.

Your HUD should now have this structure (the other game nodes are omitted):

```text
Main (Node2D)
└── CanvasLayer (CanvasLayer)
    └── HUD (Control)
        ├── Label (Label — existing title)
        ├── ScoreLabel (Label)
        ├── TimeLabel (Label)
        └── GameOverPanel (Panel — hidden)
            ├── GameOverLabel (Label)
            └── RestartButton (Button)
```

!!! warning "Names and parents must match"
    Task 24 finds these nodes by their exact names, including capital letters.
    `ScoreLabel`, `TimeLabel`, and `GameOverPanel` must be directly under `HUD`.
    Only `GameOverLabel` and `RestartButton` go inside `GameOverPanel`.
    If a node is in the wrong place, drag it onto the correct parent in the Scene panel.

![HUD checkpoint](../assets/images/task-06-score.png)

## Check

Press **F5**. The score should be at the top-left and the time at the top-right. The game-over box should be hidden.
