# Task 20: Draw The Hunter

## Goal

Make the hunter visible and touchable.

## Do This

1. Open `scenes/Hunter.tscn`.
2. Add a `Polygon2D` child. Set its **Polygon** array size to `4` and use the points `(0, -20)`, `(20, 0)`, `(0, 20)`, and `(-20, 0)`.
3. Set its **Color** to pink.
4. Select the `Hunter` root node, then add a `CollisionShape2D`. It must be a direct
   child of `Hunter`, alongside `Polygon2D`.
5. Select `CollisionShape2D`. In the Inspector, beside **Shape**, choose
   **New CircleShape2D**. Adding the node without choosing a shape leaves the hunter
   unable to collide and displays a yellow warning triangle.
6. Click the new `CircleShape2D` resource and set **Radius** to `18`.
7. Press **Ctrl+S** or **Cmd+S** to save `Hunter.tscn`.

![Hunter checkpoint](../assets/images/task-05-hunter.png)

## Check

The hunter should look like a pink diamond with a blue collision circle around it.
There should be no yellow warning triangle beside the `Hunter` node. If the warning
says that the node has no shape, check that `CollisionShape2D` has a `CircleShape2D`
assigned in its **Shape** property, then save the scene.
