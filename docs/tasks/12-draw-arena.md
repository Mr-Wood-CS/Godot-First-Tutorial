# Task 12: Draw The Arena

Add a grid and a bright border behind the player.

## 1. Add the arena node

1. Open ==scenes/Main.tscn== from the FileSystem panel.

2. In the Scene panel, ==right-click== Main and choose **Add Child Node**.

3. Search for ==Node2D== and click **Create**.

4. ==Right-click== the new node, choose **Rename**, and enter ==ArenaArt==.

![Scene panel menu with Add Child Node circled](../assets/images/add-child-node.png)

*Use this menu on Main. ArenaArt should sit directly inside Main.*

## 2. Set its position and drawing order

Select ArenaArt. In the Inspector, open **Transform**.

| Setting | Value |
| --- | --- |
| Position | x: 0, y: 0 |
| Rotation | 0 |
| Scale | x: 1, y: 1 |

Under **Ordering**, set **Z Index** to ==-1==. This puts the arena behind the player.

## 3. Add the drawing script

1. With ArenaArt selected, click **Attach Script** above the Scene panel.

2. Set **Path** to ==res://scripts/arena_art.gd== and click **Create**.

3. Replace all the starter code with this, including the first ==@tool== line:

```gdscript
@tool
extends Node2D

func _draw() -> void:
    var grid_colour := Color("24243d")
    var border_colour := Color("7df9ff")

    for x in range(0, 1281, 64):
        draw_line(Vector2(x, 0), Vector2(x, 720), grid_colour, 1.0)

    for y in range(0, 721, 64):
        draw_line(Vector2(0, y), Vector2(1280, y), grid_colour, 1.0)

    draw_rect(Rect2(16, 16, 1248, 688), border_colour, false, 4.0)
```

Save the script. Select the Main scene tab and choose **Scene > Save Scene**.

## 4. Check

Return to the **2D** workspace. The ==@tool== line lets the grid appear in the editor.

![Arena checkpoint](../assets/images/task-03-arena.png)

Press **F5**. You should see the grid and bright border behind the player.

??? tip "The arena is missing"
    - Open Main and press **F6**. If it works with F6, follow [Task 6](06-set-main-scene.md) to set Main as the starting scene.
    - Check ArenaArt sits directly inside Main and has a script icon. Clicking it should open ==res://scripts/arena_art.gd==.
    - If the script is missing, drag it from the FileSystem panel onto ArenaArt's **Script** property in the Inspector.
    - Check Main and ArenaArt have Position (0, 0), Rotation 0, Scale (1, 1), and **Visibility > Visible** switched on.
    - A full-screen Panel or ColorRect inside the HUD can cover the arena. Hide any extra background node you added there.
    - Check the window size is 1280 by 720, as in [Task 4](04-add-background.md).
    - If only the editor view is out of date, save your work and choose **Scene > Reload Saved Scene**.
    - If Godot shows a red error, check the code against the example and show the message to your teacher.

??? tip "Still missing? Check whether the drawing function runs"
    Temporarily add this indented line directly below ==func _draw() -> void:==:

    ```gdscript
        print("ArenaArt drawing at ", global_position)
    ```

    Save and run ==Main.tscn== with **F6**, then check the **Output** panel. A message
    showing ==(0.0, 0.0)== means the drawing function ran at the expected position;
    check for a covering background. A different position means the node or its
    parent is offset. No message means you should recheck the attached script,
    visibility, and any errors. Remove the temporary line afterwards.
