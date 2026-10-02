# :material-speedometer: Lesson 10 - Flight Feel and Screen Boundaries

Source idea: movement tuning adapted for Neon Drift

## Learning Intention

Tune the Player's flight speed and stop the ship leaving the screen.

## Success Criteria

- I can test speed values systematically.
- I can choose a speed that feels controllable.
- I can use `clamp()` to keep a position inside limits.
- I can test every edge of the screen.

## Keywords

| Keyword | Meaning |
|---|---|
| Game feel | How satisfying and responsive a game feels to play. |
| Tuning | Adjusting a value to improve behaviour. |
| Boundary | A limit the Player should not pass. |
| `clamp()` | Keeps a number between a minimum and maximum. |


## Add Screen Boundaries

In `player.gd`, add these two lines after `move_and_slide()`:

```gdscript
var screen_size = get_viewport_rect().size
global_position = global_position.clamp(Vector2.ZERO, screen_size)
```

This keeps the centre of the Player inside the game window. If the Player image still goes slightly beyond an edge, that is because the code is limiting its centre. Your teacher can help add a margin based on the size of the Player image.

## Practical Tasks

1. Test `speed` values of `120.0`, `240.0`, and `400.0`.
2. Change only the speed value between tests.
3. Record which value is easiest to control while collecting Sparks.
4. Add the two screen-boundary lines.
5. Fly into the left, right, top, and bottom edges.
6. Check that the Player remains visible.

| Speed | Too slow, suitable, or too fast? | Reason |
|---|---|---|
| 120.0 |  |  |
| 240.0 |  |  |
| 400.0 |  |  |

