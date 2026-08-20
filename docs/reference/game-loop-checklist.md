# Game Loop Checklist

An arcade game feels good when it has a clear repeatable loop.

## The Neon Drift Loop

1. **Read:** the player sees sparks, hunters, score, and time.
2. **Move:** the player steers the ship.
3. **Choose:** the player decides which spark is worth the risk.
4. **Resolve:** the game responds with score, sound, collision, or game over.
5. **Reset:** the player can start another run quickly.

## Pupil Testing Questions

Ask these questions after each task:

| Question | Why it matters |
| --- | --- |
| What can the player do now? | Checks that the new feature is playable. |
| What does the player need to avoid? | Checks that the challenge is clear. |
| What feedback tells the player what happened? | Checks that the game communicates clearly. |
| What broke since the last checkpoint? | Builds debugging habits. |
| Is the game easier, harder, or clearer? | Encourages design thinking. |

## Change-One-Thing Rule

When pupils customise the game, ask them to change one thing and test it before changing another.

Good one-thing changes:

- Player speed.
- Hunter speed.
- Spark value.
- Number of hunters.
- Run length.
- Sound volume.

Risky many-thing changes:

- Changing player speed, enemy speed, and arena size at the same time.
- Renaming nodes and editing scripts at the same time.
- Adding new art, sound, and code before pressing Play.

## Final Playtest

Before calling the project finished, test a full run:

- [ ] Start from a fresh launch.
- [ ] Move in all four directions.
- [ ] Collect at least three sparks.
- [ ] Let a hunter touch the player.
- [ ] Restart.
- [ ] Let the timer reach zero.
- [ ] Restart again.
- [ ] Export and launch the build outside Godot.
