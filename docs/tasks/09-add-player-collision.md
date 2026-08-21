# Task 9: Add Player Collision

## Goal

Give the player an invisible touch shape.

## Do This

1. Open `scenes/Player.tscn`.
2. Right-click `Player`, choose **Add Child Node**, and add a `CollisionShape2D`.
4. Select the `CollisionShape2D`.
5. In the Inspector, click `<empty>` beside **Shape** and choose **New CircleShape2D**.
6. Click the new `CircleShape2D` value to open its settings, then set **Radius** to `18`.

## Check

The yellow warning triangle beside `Player` should disappear. A blue circle should surround the ship in the 2D view.
