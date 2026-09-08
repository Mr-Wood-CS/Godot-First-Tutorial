# Task 12: Draw The Arena

## Goal

Draw a clear game area.

!!! warning "Arena appears with F6 but disappears with F5?"
    Your arena works, but F5 is starting a different scene. Fix the project's
    starting scene:

    1. Stop the game with **F8**.
    2. In the **FileSystem** panel (bottom-left), open the `scenes` folder.
    3. Right-click the **file** `Main.tscn` and choose **Set As Main Scene**.
       Use the FileSystem panel, not the Scene tree.
    4. Press **F5** again. The arena should now appear with the player.

    **F5 runs the project's chosen main scene. F6 runs the currently open scene.**
    Opening `Main.tscn` does not change what F5 runs. You do not need to rebuild
    the arena or change its drawing code to fix this.

## Do This

1. Open `scenes/Main.tscn`.
2. In the Scene panel, right-click the root `Main` node—not `CanvasLayer`, `HUD`, or
   `Player`—choose **Add Child Node**, and add a `Node2D`.
3. Rename it `ArenaArt`. In the Inspector, expand **Transform** and set **Position**
   to x `0`, y `0`, **Rotation** to `0`, and **Scale** to x `1`, y `1`.
   Under **Ordering**, set **Z Index** to `-1` so the arena draws behind the player.
4. With `ArenaArt` selected, click **Attach Script**. In the Attach Node Script window,
   set **Path** to exactly `res://scripts/arena_art.gd`, then click **Create**.
5. Replace **all** the starter code with this code, including the first `@tool` line:

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

6. Save the script with **Ctrl+S** or **Cmd+S**, then select the `Main` scene tab and
   save the scene too. Return to the **2D** workspace.
7. The `@tool` line lets the grid appear in the editor as well as in the game.
   If the editor has not updated, save everything, then choose
   **Scene > Reload Saved Scene**.
8. With `Main.tscn` open, press **F6** to run this specific scene. You should see the
   grid and cyan border. Stop the game, then press **F5** to check the project's main
   scene gives the same result.

![Arena checkpoint](../assets/images/task-03-arena.png)

## Check

There is no need to drag nodes to change their drawing order: `ArenaArt` has
**Z Index** `-1`, while the player's default is `0`.

!!! warning "Keep ArenaArt under Main"
    `ArenaArt` must remain a direct child of `Main`. Do not drop it onto `CanvasLayer`
    or `HUD`.

Check that `ArenaArt` has a script icon beside it. Click that icon: it must open
`res://scripts/arena_art.gd` with the code above. A script file in the FileSystem
panel does nothing unless it is attached to the node. The relevant scene hierarchy
should be (the order of the direct children of `Main` can differ):

```text
Main
├── CanvasLayer
│   └── HUD
├── ArenaArt
└── Player
```

Press **F5**. You should see a grid and bright border behind the player.

## If The Arena Is Missing When You Run

1. **Check which scene is running.** Open `Main.tscn` and press **F6**. If the arena
   appears with F6 but not F5, use the **Set As Main Scene** fix at the top of this
   page. [Task 6](06-set-main-scene.md) explains the two run buttons in more detail.
2. **Check the script is attached.** Select `ArenaArt` and look at its **Script**
   property at the bottom of the Inspector. If it is empty, drag
   `res://scripts/arena_art.gd` from the FileSystem panel onto that property.
   Save `Main.tscn` and run again.
3. **Check position and visibility.** `ArenaArt` must be directly under `Main`.
   Both nodes should have Position `(0, 0)`, Rotation `0`, Scale `(1, 1)`, and
   **Visibility > Visible** switched on. The drawing starts at the top-left of the
   game; do not move `ArenaArt` to the player's position `(640, 360)`.
4. **Check for something covering it.** Task 4 uses the project's background colour.
   If you added a full-screen `ColorRect`, `Panel`, or background image under
   `CanvasLayer` or `HUD`, temporarily hide that extra node and run again. That
   layer draws over the arena, even when the arena's Z Index is changed.
5. **Check the window size.** In **Project Settings > Display > Window**, confirm
   **Viewport Width** is `1280` and **Viewport Height** is `720`, as in Task 4.
6. **Check for script errors.** If Godot stops on a red error, copy its complete
   message for your teacher. Make sure the function is named `_draw()` (with the
   underscore) and the indented lines match the example.

!!! note "Still missing? Check whether the drawing function runs"
    Temporarily add this indented line directly below `func _draw() -> void:`:

    ```gdscript
        print("ArenaArt drawing at ", global_position)
    ```

    Save and run `Main.tscn` with **F6**, then check the **Output** panel. A message
    showing `(0.0, 0.0)` means the drawing function ran at the expected position;
    check for a covering background. A different position means the node or its
    parent is offset. No message means you should recheck the attached script,
    visibility, and any errors. Remove the temporary line afterwards.
