# Task 11: Add Player To Main

## Goal

Place the player inside the game scene.

## Do This

1. In the FileSystem panel, double-click `scenes/Main.tscn`.
2. Drag `scenes/Player.tscn` from the FileSystem panel into the 2D view.
3. Select the new `Player` node. In **Transform** in the Inspector, set **Position** to x `640`, y `360`.
4. Select the `Player` node.
5. At the top of the right-hand panel, click **Node**, then click **Groups**.
6. Type `player` in the box, click **Add**, and make sure its tick box is selected.

![Player in game checkpoint](../assets/images/task-02-player.png)

## Check

Press **F5**. The player should appear and move with the arrow keys. Close the game window and save the scene.
