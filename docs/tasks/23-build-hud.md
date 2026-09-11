# Task 23: Build The HUD

Add score, time, and a game-over box to the screen.

## Watch First

<iframe width="100%" height="360" src="https://www.youtube.com/embed/GwCiGixlqiU" title="YouTube video: Godot 4 first 2D game" allowfullscreen></iframe>

## 1. Find the HUD

Open ==scenes/Main.tscn==. In the **Scene panel at the top left**, expand Main, then CanvasLayer, then HUD.

Use the HUD you made in [Task 5](05-add-title.md). Keep its existing title Label.

## 2. Add score and time

1. ==Right-click== HUD and choose **Add Child Node**.

2. Search for ==Label== and click **Create**.

3. ==Right-click== the new Label, choose **Rename**, and enter ==ScoreLabel==.

![Scene panel menu with Add Child Node circled](../assets/images/add-child-node.png)

*Use this menu on HUD.*

Select ScoreLabel. Set **Text** in the Inspector, then open **Layout > Transform** to enter its position.

Repeat the steps to add a second Label named ==TimeLabel== under HUD.

| Node name | Text | Position x | Position y |
| --- | --- | --- | --- |
| ==ScoreLabel== | ==SCORE 00000== | 32 | 32 |
| ==TimeLabel== | ==TIME 60.0== | 1120 | 32 |

## 3. Add the game-over box

==Right-click== HUD, choose **Add Child Node**, and add a ==Panel==. Rename it ==GameOverPanel==.

In the Inspector, open **Layout > Transform**.

| Setting | x | y |
| --- | --- | --- |
| Position | 440 | 260 |
| Size | 400 | 200 |

## 4. Add its message and button

==Right-click== GameOverPanel and use **Add Child Node** to add each node below. Rename each one, then set its **Text** in the Inspector.

| Node type | Rename to | Text |
| --- | --- | --- |
| Label | ==GameOverLabel== | ==GAME OVER== |
| Button | ==RestartButton== | ==RESTART== |

For each node, open **Layout > Transform** and enter these values:

| Node | Position x | Position y | Size x | Size y |
| --- | --- | --- | --- | --- |
| GameOverLabel | 100 | 35 | 200 | 50 |
| RestartButton | 125 | 115 | 150 | 50 |

Select GameOverLabel and set **Horizontal Alignment** to **Center**. You can find it using **Filter Properties** at the top of the Inspector; clear the filter afterwards.

## 5. Hide the box and check

Select GameOverPanel. In the Inspector, open **Visibility** and switch off **Visible**.

Choose **Scene > Save Scene**.

Check the names and parents match this tree. Task 24 uses these exact names, including capital letters.

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

Press **F5**. Score should appear at the top left and time at the top right. The game-over box should be hidden.

??? tip "A node is in the wrong place"
    Drag it onto the correct parent in the Scene panel. ScoreLabel, TimeLabel and GameOverPanel belong inside HUD.
    GameOverLabel and RestartButton belong inside GameOverPanel.
