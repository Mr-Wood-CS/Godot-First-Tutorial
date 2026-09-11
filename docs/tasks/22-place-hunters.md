# Task 22: Place Hunters

## Goal

Put hunters into the arena.

## 1. Place the first hunter

1. In the FileSystem panel, double-click ==scenes/Main.tscn==.

2. Select Main in the Scene panel, then drag ==scenes/Hunter.tscn== from the FileSystem panel into the 2D view.

3. Place it inside the border near an edge, away from the player.

## 2. Add it to a group

With the hunter selected, open **Node > Groups** on the right. Create a group called ==hunter== and tick its box.

## 3. Make the copies

In the Scene panel, ==right-click== the hunter and choose **Duplicate**.

Repeat until there are ==3 hunters== altogether. Move each one to a different edge inside the border, away from the player.

Check they all sit directly inside Main, then choose **Scene > Save Scene**.

## Check

All three hunters should appear without yellow warning triangles. Because they are
instances of ==Hunter.tscn==, the collision shape added and saved in the Hunter scene is
shared by all three. Press **F5**; the hunters should move toward the player.
