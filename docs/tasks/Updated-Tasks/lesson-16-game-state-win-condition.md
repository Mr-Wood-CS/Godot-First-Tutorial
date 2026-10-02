# :material-trophy: Lesson 16 - Game State and Win Condition

Source video: [Complete Game Loop! Win Condition, End Screen, & Scene Reset](https://www.youtube.com/watch?v=ymcHxVTLbtI)

## Learning Intention

Create a win condition that checks whether the Player has collected enough Spark points.

## Success Criteria

- I can track the total Spark score.
- I can compare the score with a target.
- I can trigger a win state.
- I can prevent the win logic from running too early.

## Keywords

| Keyword | Meaning |
|---|---|
| Win condition | The rule that decides when the player wins. |
| Target | The amount needed to complete the objective. |
| Boolean | A true or false value. |
| State | The current condition of the game. |


## Worked Example

```gdscript
var score = 0
var target_score = 5
var has_won = false

func _on_spark_collected(value) -> void:
    score += value
    $UI/ScoreLabel.text = "Score: " + str(score)
    if score >= target_score and not has_won:
        has_won = true
        print("You win!")
```

## Practical Tasks

1. Keep the existing `_on_spark_collected(value)` function from Lesson 14.
2. Add `target_score` and `has_won` near the top of `main.gd`.
3. Add the `if` block after the score label update.
4. Test with `target_score = 1`, then change it to match the total value of the Sparks.
5. Confirm that the win message appears once, only after the target is reached.

