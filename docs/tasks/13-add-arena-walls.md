# Task 13: Add Arena Walls

## Goal

Add invisible wall collision to the arena.

## Do This

1. Open `scenes/Main.tscn`.
2. Add a `StaticBody2D`.
3. Rename it `ArenaBounds`.
4. Add four `CollisionShape2D` children.
5. Give each one a `RectangleShape2D`.
6. Name them `TopWall`, `BottomWall`, `LeftWall`, and `RightWall`.
7. Place them on the four edges of the window.

## Check

Press Play. Move into every wall. The player should stay inside the arena.
