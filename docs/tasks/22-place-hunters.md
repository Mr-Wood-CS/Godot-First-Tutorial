# Task 22: Place Hunters

## Goal

Put hunters into the arena.

## Do This

1. In the FileSystem panel, double-click `scenes/Main.tscn`.
2. Drag `scenes/Hunter.tscn` from the FileSystem panel into the 2D view.
3. Place it inside the border near an edge, away from the player.
4. Open **Node > Groups** on the right. Create a group called `hunter` and tick its box.
5. Press **Ctrl+D** or **Cmd+D** twice so there are three hunters altogether.
6. Put the three hunters at different edges, all inside the border.
7. Press **Ctrl+S** or **Cmd+S** to save `Main.tscn`.

## Check

All three hunters should appear without yellow warning triangles. Because they are
instances of `Hunter.tscn`, the collision shape added and saved in the Hunter scene is
shared by all three. Press **F5**; the hunters should move toward the player.
