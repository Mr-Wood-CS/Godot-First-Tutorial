# Task 4: Add A Background

## Goal

Add a dark background to the game window.

## Do This

The **Scene panel** is the list of nodes at the top-left. The **Inspector** is the settings area on the right.

1. Open **Project > Project Settings**. Choose **Display > Window > Size**.
2. Set **Viewport Width** to `1280` and **Viewport Height** to `720`, then close Project Settings.
3. In the Scene panel, right-click `Main` and choose **Add Child Node**.
4. Search for `ColorRect`, select it, and click **Create**.
5. Select `ColorRect`. Open **Layout > Transform** in the Inspector. Set **Size** to x `1280`, y `720`.
6. In the Inspector, click the white box beside **Color** and choose a very dark blue.
7. In the Scene panel, right-click `ColorRect` and choose **Move Up** until it is the first child under `Main`. This keeps it behind the game objects added later.

![Project background checkpoint](../assets/images/task-01-project.png)

## Check

Press **F6** to run this scene, then click **Run Current Scene** if Godot asks. The game window should be filled with dark blue. Close the game window when finished.
