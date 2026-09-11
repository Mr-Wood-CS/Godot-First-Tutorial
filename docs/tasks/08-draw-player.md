# Task 8: Draw The Player

Draw a small triangle for the player ship.

## 1. Add the drawing node

1. In the **FileSystem panel at the bottom left**, open ==scenes/Player.tscn==.

2. In the **Scene panel at the top left**, ==right-click== Player and choose **Add Child Node**.

    ![Scene panel menu with Add Child Node circled](../assets/images/add-child-node.png)

    *Use this menu on Player.*

3. Search for ==Polygon2D== and click **Create**.

4. Keep Polygon2D selected and click **2D** at the top of the editor.

## 2. Draw a triangle

In the toolbar above the 2D view, find the three polygon icons just to the right of **View**. Click the first icon, marked with a **green +**.

1. Click once above the centre crosshair.

2. Click below and to its right, then below and to its left.

3. Click your first point again to close the triangle.

## 3. Set its size

With Polygon2D selected, open **Data**, then **Polygon** in the **Inspector on the right**.

There should be three entries. If you have more, set the array's **Size** to ==3==.

Enter these values and press Enter after each one:

| Entry | Corner | x | y |
| --- | --- | --- | --- |
| 0 | Top | 0 | -20 |
| 1 | Bottom right | 16 | 20 |
| 2 | Bottom left | -16 | 20 |

This makes the ship 32 pixels wide and 40 pixels tall. Negative y values move a point upwards.

Under **Node2D > Transform**, check these settings:

| Setting | Value |
| --- | --- |
| Position | x: 0, y: 0 |
| Rotation | 0 |
| Scale | x: 1, y: 1 |

Keep the Polygon2D **Offset** at x: 0, y: 0 too.

## 4. Choose a colour and check

In the Inspector, click the box beside **Color** and choose a bright colour.

![Player checkpoint](../assets/images/task-02-player.png)

The Scene panel should look like this:

```text
Player
└── Polygon2D
```

Your triangle should be centred on the crosshair. Choose **Scene > Save Scene**.

??? tip "Cannot find the polygon tools?"
    Select Polygon2D and open the **2D** workspace. Use the toolbar above the main view.
    If the Polygon panel at the bottom is in the way, click its **Polygon** tab to collapse it.
