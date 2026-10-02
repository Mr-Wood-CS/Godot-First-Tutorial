# :material-run: Lesson 5 - Build the Player Ship

Source video: [Basic 2D Movement! Making a Character Walk](https://www.youtube.com/watch?v=uRoh_H8F2Qs)

## Learning Intention

Create a 2D Player ship that Godot can move and detect.

## Success Criteria

- I can create a player scene.
- I can add a collision shape.
- I can explain why physics bodies need collision.
- I can use `_physics_process()`.

## Keywords

| Keyword | Meaning |
|---|---|
| CharacterBody2D | A node used for controllable 2D characters. |
| CollisionShape2D | A shape that defines physical boundaries. |
| Collision | The shape Godot uses to detect when objects touch. |
| `_physics_process()` | A function that runs regularly for physics updates. |


## Practical Tasks

1. Click **Scene > New Scene**, then **Other Node**. Choose `CharacterBody2D`.
2. Rename the root node `Player` and save the scene as `res://scenes/player.tscn`.
3. Add a `Polygon2D` child and make a simple ship shape, or use the Player image supplied by your teacher.
4. Select `Player` and add a `CollisionShape2D` child.
5. Select `CollisionShape2D`. Beside **Shape**, choose **New RectangleShape2D**, then resize it to cover the visible player.
6. Select `Player`, attach a script, and save it as `res://scripts/player.gd`.
7. Add this starting script:

```gdscript
extends CharacterBody2D

func _physics_process(delta: float) -> void:
    pass
```

8. Open `main.tscn`. Click **Instantiate Child Scene** above the Scene panel, choose `player.tscn`, and click **Open**.
9. Move the Player near the middle of the viewport and run `main.tscn`.

## Check Your Work

The Player scene should look similar to this:

```text
Player  CharacterBody2D
├── Polygon2D
└── CollisionShape2D
```

If a yellow warning icon appears beside `CollisionShape2D`, select it and check that **Shape** is not empty.

