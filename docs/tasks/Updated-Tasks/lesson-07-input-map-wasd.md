# :material-keyboard: Lesson 7 - Four Direction Controls

Source video: [Custom Controls! Add WASD & Input Actions Setup](https://www.youtube.com/watch?v=V7nb2uASbx8)

## Learning Intention

Use Godot's Input Map to create controls for flying in four directions.

## Success Criteria

- I can open the Input Map.
- I can create four custom movement actions.
- I can bind keys to actions.
- I can update code to use custom actions.

## Keywords

| Keyword | Meaning |
|---|---|
| Input Map | Godot settings where input actions are created. |
| Action | A named control such as `move_left`. |
| Bind | Connect a key or button to an action. |
| WASD | Common keyboard controls for movement. |


## Practical Tasks

1. Click **Project > Project Settings**, then open the **Input Map** tab.
2. Create `move_left` and add both **A** and **Left Arrow**.
3. Create `move_right` and add both **D** and **Right Arrow**.
4. Create `move_up` and add both **W** and **Up Arrow**.
5. Create `move_down` and add both **S** and **Down Arrow**.
6. Close Project Settings and open `player.gd`.
7. Keep horizontal movement working by replacing only the `Input.get_axis` line with:

```gdscript
var direction = Input.get_axis("move_left", "move_right")
```

8. Run the game. Test A, D, Left Arrow, and Right Arrow separately. Up and down movement will be added in Lesson 9.

Action names must match the code exactly, including underscores and capital letters.

