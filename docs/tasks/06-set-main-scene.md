# Task 6: Set The Main Scene

## Goal

Tell Godot which scene should open first.

## Do This

1. Stop any running game with **F8**.
2. In the **FileSystem** panel (bottom-left), expand the `scenes` folder and
   double-click `Main.tscn` to open it. Save it with **Ctrl+S** or **Cmd+S**.
3. In that same **FileSystem** panel, right-click `Main.tscn` and choose
   **Set As Main Scene**. Right-click the scene **file**, not the `Main` node in
   the Scene panel. Do this even if you previously chose a main scene.
4. Press **F5**. Godot should now start `Main.tscn`.

!!! info "F5 and F6 do different jobs"
    **F5 — Run Project:** starts the scene saved as the project's main scene,
    whichever scene tab you currently have open.

    **F6 — Run Current Scene:** starts the scene in the selected scene tab.
    It does not change the project's main scene.

    Naming a scene `Main.tscn` or opening it does **not** automatically make it
    the project's main scene. You must set it using step 3.

!!! tip "Already selected the wrong scene?"
    Repeat step 3 to replace the previous choice. You do not need to wait for
    Godot to ask you to select a main scene: that prompt only appears when no
    main scene is set.

## Check

Pressing **F5** should now open a game window showing the `NEON DRIFT` title without asking you to choose a scene.

Stop the game, keep `Main.tscn` selected, and press **F6**. Both keys should show
the same game. In later tasks, use **F5** to test the whole game, including the
player, arena, sparks, and HUD you add to `Main.tscn`.
