# Task 5: Add The Title

## Goal

Show the game title on screen.

## Do This

1. Right-click `Main` and choose **Add Child Node**.
2. Search for `CanvasLayer`, select it, and click **Create**. A CanvasLayer keeps screen text fixed above the game.
3. Right-click `CanvasLayer`, choose **Add Child Node**, and add a `Label`.
4. Select `Label`. In the Inspector, set **Text** to `NEON DRIFT`.
5. Open **Layout > Transform** in the Inspector. Set **Position** to x `490`, y `24`, and **Size** to x `300`, y `70`.
6. Open **Theme Overrides > Font Sizes** and set **Font Size** to `48`.
7. Set **Horizontal Alignment** to **Center**.

![Title checkpoint](../assets/images/task-01-project.png)

## Check

Press **F6**. You should see `NEON DRIFT` near the top-centre of the dark background.
