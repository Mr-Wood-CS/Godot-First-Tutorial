# :material-axis-arrow: Lesson 9 - Four Direction Flight and Vector2

Source idea: movement concepts adapted for Neon Drift

## Learning Intention

Make the Player fly up, down, left, and right.

## Success Criteria

- I can describe `Vector2` as an x and y direction.
- I can read four Input Map actions.
- I can move at the same speed in every direction.
- I can test all eight movement directions.

## Keywords

| Keyword | Meaning |
|---|---|
| Vector2 | A pair of x and y values used for a 2D direction. |
| x axis | Left and right movement. |
| y axis | Up and down movement. |
| Normalised | Kept to the same overall size so diagonal movement is not faster. |


## Worked Example

Replace `player.gd` with this **complete script**:

```gdscript
extends CharacterBody2D

var speed = 240.0

func _physics_process(_delta: float) -> void:
    var direction = Input.get_vector(
        "move_left",
        "move_right",
        "move_up",
        "move_down"
    )
    velocity = direction * speed
    move_and_slide()
```

`Input.get_vector()` combines the four actions into one direction. It also stops diagonal flight from being faster than straight flight.

## Practical Tasks

1. Check that all four actions exist in **Project > Project Settings > Input Map**.
2. Replace `player.gd` with the complete script.
3. Test W, A, S, and D separately.
4. Test the four arrow keys separately.
5. Hold two keys together to test diagonal flight.
6. Release every key and check that the Player stops.

## Test It

The Player should fly smoothly in eight directions and stop when no movement key is held. There should be no gravity and no jump action.

