# Godot Patterns And Vocabulary

Use this page when a task uses a Godot word that feels unfamiliar.

## Scene

A scene is a saved object or screen. In this project:

- `Main.tscn` is the whole game.
- `Player.tscn` is the player ship.
- `Spark.tscn` is one collectible.
- `Hunter.tscn` is one enemy.

Scenes can be placed inside other scenes. That placed copy is called an instance.

## Node

A node is one building block inside a scene. Each node has a job.

| Node | Job |
| --- | --- |
| `Node2D` | A general 2D object. |
| `CharacterBody2D` | A moving 2D body with collision. |
| `Area2D` | Detects when something enters an area. |
| `CollisionShape2D` | Gives a body or area an invisible shape. |
| `Label` | Shows text on screen. |
| `Button` | Lets the player click an action. |
| `AudioStreamPlayer` | Plays a sound. |

## Script

A script is code attached to a node. The script gives that node behaviour.

Example:

```gdscript
extends CharacterBody2D
```

This means the script is written for a `CharacterBody2D` node.

## Groups

A group is a label you put on nodes.

In this project:

| Group | Used for |
| --- | --- |
| `player` | Lets sparks and hunters recognise the player. |
| `spark` | Lets `Main` connect to all spark collection signals. |
| `hunter` | Lets `Main` connect to all hunter hit signals. |

## Signals

A signal is a message sent by a node when something happens.

Example:

```gdscript
signal collected(value: int)
```

This creates a signal called `collected`. The spark sends it when the player picks it up.

## Node Paths

Code can find nodes using paths that match the Scene dock.

Example:

```gdscript
$CanvasLayer/ScoreLabel
```

This means:

1. Start from the node that owns the script.
2. Find its child called `CanvasLayer`.
3. Find `ScoreLabel` inside that.

If the name in the Scene dock changes, the path in the code must change too.

## Checkpoints

Run the project after every task. When a new feature breaks something, the last completed checkpoint tells you where to look.
