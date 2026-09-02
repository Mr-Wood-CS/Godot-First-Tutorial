# Task 11: Add Player To Main

## Goal

Place the player inside the game scene.

## Do This

1. In the FileSystem panel, double-click `res://scenes/Main.tscn`.
2. In the Scene panel, click the root `Main` node.
3. Click **Instantiate Child Scene** above the Scene panel. Choose
   `res://scenes/Player.tscn` and click **Open**.
4. Select the new `Player` node. In **Transform** in the Inspector, set **Position** to
   x `640`, y `360`.
5. Keep `Player` selected. At the top of the right-hand dock, click **Node**, then open
   the **Groups** tab.
6. Click the **+** button to create a group. In the **Create New Group** window, type
   `player`, leave **Global** off, and click **OK**.
7. Under **Scene Groups**, check that `player` exists and that the box beside it is
   ticked. A tick means the selected `Player` node belongs to that group.

!!! warning "Keep game objects out of the HUD"
    `Player` must be a direct child of `Main`. If it appears under `CanvasLayer` or
    `HUD`, undo the last step, select `Main`, and instantiate it again.

## Check

Before running, the relevant part of the Scene panel must look like this:

```text
Main
├── CanvasLayer
│   └── HUD
└── Player
```

Press **F5**. The player should appear and move with the arrow keys. Close the game
window and save the scene.
