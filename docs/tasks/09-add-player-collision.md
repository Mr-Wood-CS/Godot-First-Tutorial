# Task 9: Add Player Collision

## Goal

Give the player an invisible shape Godot can use for touching walls, sparks, and enemies.

## Key Words

| Word | Meaning |
| --- | --- |
| Collision | The invisible shape Godot uses to know when things touch. |
| CollisionShape2D | A node that stores a collision shape. |
| CircleShape2D | A round collision shape. |

## Do This

1. Open `scenes/Player.tscn`.
2. Right-click `Player`.
3. Add a `CollisionShape2D`.
4. Select the `CollisionShape2D`.
5. Set **Shape** to **New CircleShape2D**.
6. Set the radius to about `18`.

## Check

The warning icon on the player should disappear once the collision shape has a shape.
