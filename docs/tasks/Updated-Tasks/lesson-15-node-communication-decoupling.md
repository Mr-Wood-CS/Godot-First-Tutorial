# :material-call-split: Lesson 15 - Node Communication and Decoupling

Source video: [Node Communication! Using Signals for UI Interaction](https://www.youtube.com/watch?v=MYYM1J5UIk0)

## Learning Intention

Explain how the Spark, Main, and ScoreLabel share jobs without each node doing everything.

## Success Criteria

- I can explain node communication.
- I can connect a signal between nodes.
- I can update UI from game state.
- I can explain decoupling in simple terms.

## Keywords

| Keyword | Meaning |
|---|---|
| Communication | One node sending information to another. |
| Decoupling | Giving nodes separate jobs so they do not need to control one another directly. |
| Game state | Important values such as score, lives or win status. |
| Callback | A function that runs in response to an event. |


## Practical Tasks

1. Draw three boxes labelled Spark, Main, and ScoreLabel.
2. Draw an arrow from Spark to Main labelled `collected(value)`.
3. Draw an arrow from Main to ScoreLabel labelled `update text`.
4. Explain the jobs: Spark detects collection, Main stores the score, and ScoreLabel displays it.
5. Add a message Label if there is time, but do not change the working signal connection.
6. Test that one Spark changes the score once and updates the Label once.

The technical word for keeping these jobs separate is **decoupling**. The important idea is that the Spark does not need to know where the score label is.

