# Task 13: Add Arena Walls

## Goal

Add invisible wall collision around the arena.

## Key Words

| Word | Meaning |
| --- | --- |
| StaticBody2D | A 2D body that does not move. Good for walls. |
| RectangleShape2D | A rectangular collision shape. |

## Do This

1. Open `scenes/Main.tscn`.
2. Add a `StaticBody2D`.
3. Rename it `ArenaBounds`.
4. Add four `CollisionShape2D` children.
5. Give each one a `RectangleShape2D`.
6. Name them `TopWall`, `BottomWall`, `LeftWall`, and `RightWall`.
7. Place them around the edges of the window.

## Check

Press Play and try to move through every wall. The player should stay inside the arena.
