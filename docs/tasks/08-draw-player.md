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
5. To adjust the triangle, click the middle of those three polygon icons (between
   the green **+** and red **×**) and drag its corners. Aim for a ship about 40 pixels
   tall and 32 pixels wide.
6. In the Inspector, click the white box beside **Color** and choose a bright arcade colour.

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
