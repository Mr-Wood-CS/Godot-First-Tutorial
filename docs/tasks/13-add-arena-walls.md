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
   `RectangleShape2D`.

!!! warning "Create a new shape for every wall"
    Do not duplicate `TopWall`. Duplicated nodes can share the same Shape resource,
    so changing one wall may change another.

| Name | Rectangle size | Position |
| --- | --- | --- |
| `BottomWall` | x `1280`, y `16` | x `640`, y `712` |
| `LeftWall` | x `16`, y `720` | x `8`, y `360` |
| `RightWall` | x `16`, y `720` | x `1272`, y `360` |

9. Open `scenes/Player.tscn`, select the `Player` root node, and click its script icon.
10. Replace the whole script with the code below. This is the complete player script
    at this stage. The earlier `clamp()` lines are no longer needed because the
    physical walls now keep the player inside the arena.

!!! warning "No script icon?"
    Complete [Task 10: Add Player Movement](10-add-player-script.md) first.

```gdscript
extends CharacterBody2D

@export var speed := 420.0

func _physics_process(_delta: float) -> void:
    var input_vector := Input.get_vector("ui_left", "ui_right", "ui_up", "ui_down")
    velocity = input_vector * speed
    move_and_slide()
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
