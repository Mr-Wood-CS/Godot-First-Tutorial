# :material-bug-check: Lesson 19 - Debugging and Refinement

Source videos: Whole playlist review

## Learning Intention

Debug Neon Drift and refine the player experience.

## Success Criteria

- I can test one feature at a time.
- I can use output messages to trace bugs.
- I can identify broken node paths or signal connections.
- I can make one improvement to the game.

## Keywords

| Keyword | Meaning |
|---|---|
| Debugging | Finding and fixing problems. |
| Trace | Follow what the code is doing. |
| Node path | A reference to a node in the scene tree. |
| Refinement | Improving an existing feature. |


## Practical Tasks

1. Test movement.
2. Test up, down, left, right, and diagonal flight.
3. Test each Spark pickup.
4. Test score and win condition.
5. Improve one part of the player experience.

## Symptom and Check

| Symptom | Check these first |
|---|---|
| Player is invisible | Player is instanced in Main and its visible child has a colour or texture. |
| Player cannot move vertically | `move_up` and `move_down` exist and their names match `player.gd`. |
| Player leaves the screen | Check that the clamp lines run after `move_and_slide()`. |
| Spark does not disappear | Both collision shapes exist; Player is in the exact `Player` group; `body_entered` is connected. |
| Score does not change | Spark `collected` is connected to Main and both functions use one `value`. |
| Score changes twice | The signal has been connected twice; keep only one connection. |
| Score label causes a node-path error | The tree contains `UI/ScoreLabel` with the same capital letters. |
| Restart does nothing | `RestartButton.pressed` is connected once to the restart function. |

