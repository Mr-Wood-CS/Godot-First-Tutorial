# Task 13: Add Arena Walls

## Goal

Add invisible wall collision to the arena.

## Do This

1. Open `scenes/Main.tscn`.
2. Right-click `Main`, choose **Add Child Node**, and add a `StaticBody2D`.
3. Rename it `ArenaBounds`.
4. Add a `CollisionShape2D` as a child of `ArenaBounds` and rename it `TopWall`.
5. Set its **Shape** to **New RectangleShape2D**. Open the new shape and set **Size** to x `1280`, y `16`.
6. In **Transform**, set **Position** to x `640`, y `8`.
7. Duplicate `TopWall` three times with **Ctrl+D** or **Cmd+D**.
8. Rename and set the copies like this:

| Name | Rectangle size | Position |
| --- | --- | --- |
| `BottomWall` | x `1280`, y `16` | x `640`, y `712` |
| `LeftWall` | x `16`, y `720` | x `8`, y `360` |
| `RightWall` | x `16`, y `720` | x `1272`, y `360` |

## Check

Press **F5**. Move into all four edges. The player should stop at the bright border and remain on screen.
