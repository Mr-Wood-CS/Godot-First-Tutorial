# Task 11: Add Player To Main

## Goal

Place the player inside the game scene.

## Key Words

| Word | Meaning |
| --- | --- |
| Instance | A copy of a scene placed inside another scene. |
| Group | A label added to a node so other scripts can recognise it. |

## Do This

1. Open `scenes/Main.tscn`.
2. Drag `Player.tscn` from the FileSystem into the scene.
3. Place the player near the centre of the game window.
4. Select the `Player` node.
5. In the Node dock, open **Groups**.
6. Add it to a group called `player`.

![Player in game checkpoint](../assets/images/task-02-player.png){ .media-frame }

## Check

Press Play. The player should appear and move with the arrow keys.
