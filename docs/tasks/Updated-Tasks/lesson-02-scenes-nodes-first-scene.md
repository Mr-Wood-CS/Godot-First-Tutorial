# :material-family-tree: Lesson 2 - Scenes, Nodes and First Scene

Source video: [Godot 4.5 Basics: Setup, Nodes, Scenes, & The Editor Explained!](https://www.youtube.com/watch?v=amGXbHVMPX0)

## Learning Intention

Understand how Godot games are built from scenes and nodes.

## Success Criteria

- I can create a new scene.
- I can add nodes to a scene.
- I can rename nodes clearly.
- I can save and run a basic scene.

## Keywords

| Keyword | Meaning |
|---|---|
| Scene | A reusable part of a game, such as a level, player or menu. |
| Node | A building block with a specific job. |
| Root node | The top node in a scene. |
| Child node | A node placed underneath another node. |


## Practical Tasks

1. In the Project Manager, open `NeonDrift`.
2. Click **2D Scene**. Godot creates a `Node2D` root.
3. In the Scene panel, right-click the root, choose **Rename**, and type `Main`.
4. Press **Command+S** and save the scene as `res://scenes/main.tscn`.
5. Click **Run Current Scene** in the top-right corner. This runs the scene that is open.
6. Stop the game, then click **Run Project**. If Godot asks for a main scene, choose **Select Current**.

An empty scene shows a blank game window. That is correct for now. A visible Player will be added in Lesson 5.

## Check Your Work

Your scene tree should contain one node:

```text
Main  Node2D
```

The FileSystem panel should contain `scenes/main.tscn`.

