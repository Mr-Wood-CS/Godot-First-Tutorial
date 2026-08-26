# Task 8: Draw The Player

## Goal

Make the player visible.

## Do This

1. Open `scenes/Player.tscn`.
2. Right-click `Player`, choose **Add Child Node**, search for `Polygon2D`, and click **Create**.
3. Keep `Polygon2D` selected. Above the 2D view, click the **Create Points** tool. Its
   icon looks like a pencil drawing a polygon.
4. In the 2D view, click once above the centre crosshair, once below and to its right,
   and once below and to its left. Click the first point again to close the triangle.
5. If the shape is too large, select the **Edit Points** tool and drag its corners. Aim
   for a ship about 40 pixels tall and 32 pixels wide.
6. In the Inspector, click the white box beside **Color** and choose a bright arcade colour.

!!! tip "Cannot see the polygon tools?"
    Make sure `Polygon2D` is selected in the Scene panel and that the **2D** workspace is
    open. Do not add an Array in the Inspector; the points drawn in the 2D view fill the
    `Polygon` property automatically.

![Player checkpoint](../assets/images/task-02-player.png)

## Check

The Scene panel should show this exact hierarchy:

```text
Player
└── Polygon2D
```

The 2D view should show a small triangle centred on the crosshair. Press **Ctrl+S** or **Cmd+S**.
