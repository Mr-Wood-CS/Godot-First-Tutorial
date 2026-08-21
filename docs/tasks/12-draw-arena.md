# Task 12: Draw The Arena

## Goal

Draw a clear game area.

## Do This

1. Open `scenes/Main.tscn`.
2. Right-click `Main`, choose **Add Child Node**, and add a `Node2D`.
3. Rename it `ArenaArt`.
4. With `ArenaArt` selected, click **Attach Script**. Set the path to `res://scripts/arena_art.gd` and click **Create**.
5. Replace the starter code with this code:

```gdscript
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

![Arena checkpoint](../assets/images/task-03-arena.png)

## Check

In the Scene panel, drag `ArenaArt` above `Player` but below `ColorRect`. Press **F5**. You should see a grid and bright border behind the player.
