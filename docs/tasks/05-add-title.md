# Task 5: Add The Title

## Goal

Show the game title on screen.

## Do This

1. Right-click `Main` and choose **Add Child Node**.
2. Search for `CanvasLayer`, select it, and click **Create**. A CanvasLayer keeps screen text fixed above the game.
3. Right-click `CanvasLayer`, choose **Add Child Node**, and add a `Control`. Rename it `HUD`. This gives all the labels a proper user-interface parent.
4. Select `HUD`. In the Inspector, expand **Layout**, then click the small arrow beside **Transform**. Set **Position** to x `0`, y `0` and **Size** to x `1280`, y `720`. Leave **Custom Minimum Size** and **Custom Maximum Size** unchanged. The message about not having a Control parent is expected here because `HUD` is directly under a `CanvasLayer`.
5. Right-click `HUD`, choose **Add Child Node**, and add a `Label`.
6. Select `Label`. In the Inspector, set **Text** to `NEON DRIFT`.
7. Open **Layout > Transform** in the Inspector. Set **Position** to x `490`, y `24`, and **Size** to x `300`, y `70`.
8. Open **Theme Overrides > Font Sizes** and set **Font Size** to `48`.
9. Set **Horizontal Alignment** to **Center**.

![Title checkpoint](../assets/images/task-01-project.png)

## Check

The Scene panel should show `Main > CanvasLayer > HUD > Label`. Press **F6**. You should see `NEON DRIFT` near the top-centre of the dark background without a Control-parent warning.
