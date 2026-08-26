# Task 13: Add Arena Walls

## Goal

Add invisible wall collision to the arena.

## Do This

1. Open `scenes/Main.tscn`.
2. In the Scene panel, right-click the root `Main` node—not `CanvasLayer`, `HUD`,
   `ArenaArt`, or `Player`—choose **Add Child Node**, and add a `StaticBody2D`.
3. Rename it `ArenaBounds`.
4. Add a `CollisionShape2D` as a child of `ArenaBounds` and rename it `TopWall`.
5. Set its **Shape** to **New RectangleShape2D**. Open the new shape and set **Size** to x `1280`, y `16`.
6. In **Transform**, set **Position** to x `640`, y `8`.
7. Right-click `ArenaBounds` and add a new `CollisionShape2D`. Rename it `BottomWall`,
   give it a **New RectangleShape2D**, and use the size and position below.
8. Repeat that step to create `LeftWall` and `RightWall`. Give every wall its own new
   `RectangleShape2D`; do not duplicate `TopWall`, because duplicated nodes can share
   the same Shape resource.

| Name | Rectangle size | Position |
| --- | --- | --- |
| `BottomWall` | x `1280`, y `16` | x `640`, y `712` |
| `LeftWall` | x `16`, y `720` | x `8`, y `360` |
| `RightWall` | x `16`, y `720` | x `1272`, y `360` |

9. Open `res://scripts/player.gd`. Delete these two lines, because the physical walls
   now keep the player inside the arena:

```gdscript
    global_position.x = clamp(global_position.x, 24.0, 1256.0)
    global_position.y = clamp(global_position.y, 24.0, 696.0)
```

## Check

`ArenaBounds` must be a direct child of `Main`, with all four wall shapes beneath it:

```text
Main
├── ArenaArt
├── Player
└── ArenaBounds
    ├── TopWall
    ├── BottomWall
    ├── LeftWall
    └── RightWall
```

Press **F5**. Move into all four edges. The player should stop at the bright border and remain on screen.
