# Task 8: Draw The Player

## Goal

Make the player visible.

## Do This

1. Open `scenes/Player.tscn`.

2. Right-click `Player`, choose **Add Child Node**, search for `Polygon2D`, and click **Create**.

3. Keep `Polygon2D` selected in the Scene panel and open the **2D** workspace.
   In the toolbar above the canvas, look just to the right of **View** for three
   small polygon icons. Click the first one, marked with a **green +**, to start
   drawing a polygon. This is an icon-only button, not a button labelled “Create Points”.
4. In the 2D view, click once above the centre crosshair, once below and to its right,
   and once below and to its left. Click the first point again to close the triangle.
5. Set the triangle to exactly **32 pixels wide and 40 pixels tall**. Keep `Polygon2D`
   selected, expand **Data** in the Inspector, then expand **Polygon** to show the
   points you just drew. Edit the **x** and **y** values of the three entries using
   the table below. Press **Enter** after typing each value.

   | Entry | Corner | x | y |
   | --- | --- | --- | --- |
   | `0` | Top | `0` | `-20` |
   | `1` | Bottom right | `16` | `20` |
   | `2` | Bottom left | `-16` | `20` |

   There should be **3** entries: closing the triangle does not need an extra point.
   If you accidentally added more, set the array's **Size** to `3` before entering
   these coordinates. **Size** here means the number of points, not the ship's size.
   The width is `16 - (-16) = 32` pixels and the height is `20 - (-20) = 40` pixels.
   Negative **y** is upwards in Godot's 2D view.
6. Under **Node2D → Transform**, keep **Position** at `(0, 0)`, **Rotation** at `0`,
   and **Scale** at `(1, 1)`. Keep the Polygon2D **Offset** at `(0, 0)` too. This
   keeps the triangle centred on the player's origin at the size entered above.
7. In the Inspector, click the white box beside **Color** and choose a bright arcade colour.

!!! tip "Cannot see the polygon tools?"
    Make sure `Polygon2D` is selected in the Scene panel and that the **2D** workspace is
    open. Use the toolbar above the main canvas, not the **Points / Polygons / UV / Bones**
    tabs in the bottom Polygon panel. If that panel takes up too much space, click
    **Polygon** at the bottom of the editor to collapse it. The points drawn in the
    canvas fill the Inspector's **Data → Polygon** property automatically.

![Player checkpoint](../assets/images/task-02-player.png)

## Check

The Scene panel should show this exact hierarchy:

```text
Player
└── Polygon2D
```

The 2D view should show a small triangle centred on the crosshair. Press **Ctrl+S** or **Cmd+S**.
