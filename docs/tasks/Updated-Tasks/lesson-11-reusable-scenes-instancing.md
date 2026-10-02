# :material-content-copy: Lesson 11 - Reusable Scenes and Instancing

Source video: [Reusable Scene! Creating a Coin Pickup](https://www.youtube.com/watch?v=jWh_IC6e43U)

## Learning Intention

Create a reusable Spark scene that can be placed multiple times in a level.

## Success Criteria

- I can create a separate Spark scene.
- I can instance a scene into another scene.
- I can explain why reusable scenes save time.
- I can organise scene files clearly.

## Keywords

| Keyword | Meaning |
|---|---|
| Instance | A copy of a scene placed inside another scene. |
| Reusable | Designed so it can be used more than once. |
| Packed scene | A saved scene that can be instanced. |
| Level | The game area where the player moves. |


## Practical Tasks

1. Create a new scene with an `Area2D` root node and rename it `Spark`.
2. Add a visible `Polygon2D` or `Sprite2D` child.
3. Add a `CollisionShape2D` child. Give it a shape and resize it to cover the visible Spark.
4. Save the scene as `res://scenes/spark.tscn`.
5. Attach a script named `res://scripts/spark.gd` containing `extends Area2D`.
6. Open `main.tscn` and use **Instantiate Child Scene** to add one Spark.
7. Run the game and check that the Spark is visible. Use only one Spark until collection and scoring work.

The Spark scene should look similar to this:

```text
Spark  Area2D
├── Polygon2D or Sprite2D
└── CollisionShape2D
```

