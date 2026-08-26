# Task 8: Draw The Player

## Goal

Make the player visible.

## Do This

1. Open `scenes/Player.tscn`.
2. Right-click `Player`, choose **Add Child Node**, search for `Polygon2D`, and click **Create**.
3. Select the new `Polygon2D` node in the Scene panel. In the Inspector, find the
   **Polygon** property near the top of the **Polygon2D** section. Its value may be
   labelled **PackedVector2Array (size 0)**, **0 points**, or simply appear empty,
   depending on your Godot 4 version.
4. Click the value (or its small edit/expand button), then change **Size** to `3`.
   Expand the three entries and enter these x and y values:

```text
(0, -20)
(16, 16)
(-16, 16)
```

5. In the Inspector, click the white box beside **Color** and choose a bright arcade colour.

!!! tip "Cannot find Polygon or Size?"
    Make sure `Polygon2D` (not the root `Player` node) is selected, and clear any text
    from the Inspector's **Filter Properties** box. **Polygon** is a property in the
    **Polygon2D** section; the word **Array** may not be displayed. Click the property's
    value to reveal the **Size** control and point entries.

![Player checkpoint](../assets/images/task-02-player.png)

## Check

The 2D view should show a small triangle centred on the crosshair. Press **Ctrl+S** or **Cmd+S**.
