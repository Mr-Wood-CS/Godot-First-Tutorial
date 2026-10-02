# :material-loop: Lesson 18 - Complete Game Loop

Source video: [Complete Game Loop! Win Condition, End Screen, & Scene Reset](https://www.youtube.com/watch?v=ymcHxVTLbtI)

## Learning Intention

Connect movement, collecting, scoring, winning and restarting into one complete playable loop.

## Success Criteria

- I can play from start to win screen.
- I can restart after winning.
- I can identify each part of the game loop.
- I can fix missing connections or broken signals.

## Keywords

| Keyword | Meaning |
|---|---|
| Game loop | The repeated cycle of playing, achieving and restarting. |
| Objective | The goal the player tries to complete. |
| Integration | Connecting separate parts into a working whole. |
| Regression | A new change accidentally breaking old behaviour. |


## Practical Tasks

1. Start the game from the main scene.
2. Move the player around the level.
3. Collect all Sparks.
4. Trigger the win screen.
5. Restart and confirm the game resets.

## Connection Checklist

- Each Spark's `body_entered` signal connects once to its own `_on_body_entered` function.
- Each Spark instance's `collected(value)` signal connects once to Main's `_on_spark_collected(value)` function.
- `RestartButton.pressed` connects once to `_on_restart_button_pressed`.
- The score changes once for each Spark.
- The end screen appears only when `target_score` is reached.

