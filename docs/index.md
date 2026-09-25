# Neon Drift Arcade
![Neon Drift finished game overview](assets/images/neon-drift-overview.png)
Build a small top-down arcade game in Godot 4 while learning how to plan, code, test and improve your own game. Follow one small task at a time, with a clear goal, short steps and a check.

<div class="task-card">
By the end, the game will have a player ship, an arena, sparks to collect, hunters to avoid, score, time, game over, feedback, and an exported build.
</div>

## What You Will Learn

You will learn to use **GDScript**, Godot's text-based programming language, and
explain how the different parts of your game work together.

Use these success criteria to check your understanding as you work. Be ready to
show your game, explain your code and describe how you solved a problem.

| Stage | I am learning to… | I can show this when I… |
| --- | --- | --- |
| [1. Plan and start the game — Tasks 1–6](tasks/01-create-project.md) | break a game into smaller parts and organise a Godot project. | describe what the game needs, sketch a plan, and explain what scenes and nodes do. |
| [2. Build the player and arena — Tasks 7–13](tasks/07-make-player-scene.md) | use keyboard input, variables and calculations to control movement. | move my player in each direction, explain how the movement code works, and test the arena walls. |
| [3. Collect sparks — Tasks 14–18](tasks/14-make-spark-scene.md) | use signals to pass information between game objects. | collect a spark and explain how a collision sends information to the main scene. |
| [4. Create hunters — Tasks 19–22](tasks/19-make-hunter-scene.md) | write an algorithm: a set of steps that controls an enemy. | make a hunter chase the player and explain how the code uses calculations, decisions and repetition. |
| [5. Show score and time — Tasks 23–24](tasks/23-build-hud.md) | store game data in variables and display it clearly. | explain my variables and show how changing a value updates the screen. |
| [6. Finish and restart — Tasks 25–26](tasks/25-add-timer.md) | use decisions and game state to control when the game runs or ends. | test what happens when time reaches zero or a hunter catches the player, then restart the game. |
| [7. Improve the game — Task 27](tasks/27-add-feedback.md) | use feedback to make my game clearer and more enjoyable. | ask someone to test my game, make an improvement and explain why it helps. |
| [8. Test and export — Task 28](tasks/28-export-game.md) | test, debug and evaluate a playable game. | record expected and actual results, fix problems, export a build and describe what I would improve next. |

### Programming Skills You Will Practise

- **Sequence:** put instructions in the right order.
- **Variables and calculations:** store and update values such as speed, score and time.
- **Selection:** use decisions to choose what happens next.
- **Repetition:** repeat actions or work through several game objects.
- **Boolean logic:** use true/false values to control whether the game is running.
- **Signals:** let one part of the game tell another that something has happened.
- **Testing and debugging:** check your game and find and fix errors.

## What You Will Make

- A Godot project called ==NeonDrift==.
- A player ship that moves with the keyboard.
- A neon arena with walls.
- Sparks that disappear when collected.
- Hunters that chase the player.
- A HUD with score and time.
- A game-over panel and restart button.
- A playable exported build.

## What You Need

- Godot 4 installed.
- A keyboard.
- A new empty folder for the project.

## How To Use This Guide

The project is split into nine lessons. Each lesson completes one clear part of the
game and contains two to five short tasks.

1. Open the next lesson in the menu, then choose its first task.
2. Read the **Goal**.
3. Do only the steps on that page.
4. New Godot words are explained on the page before you need them.
5. Run the project when the page asks you to.
6. Move on when the **Check** works.

## Key Godot Words

| Word | Meaning |
| --- | --- |
| Project | The folder that stores one game. |
| Scene | One saved part of a game, such as a level, player, or collectible. |
| Node | One building block in a scene. Each node has one job. |
| Script | Code attached to a node. |
| Scene panel | The list at the top-left that shows the nodes in the open scene. |
| Inspector panel | The area on the right where you change the selected node's settings. |
| FileSystem panel | The area at the bottom-left that shows the files and folders in the project. |


