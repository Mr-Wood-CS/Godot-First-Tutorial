# Task 15: Draw The Spark

## Goal

Make the spark visible and touchable.

## Do This

1. Open `scenes/Spark.tscn`.
2. Add a `Polygon2D` child to `Spark`.
3. Select it, set the **Polygon** array size to `4`, and enter these x and y values:

```text
(0, -12)
(12, 0)
(0, 12)
(-12, 0)
```

4. Set **Color** to yellow.
5. Add a `CollisionShape2D` as another child of `Spark`.
6. Beside **Shape**, choose **New CircleShape2D**.
7. Click the new shape and set **Radius** to `14`.

![Spark checkpoint](../assets/images/task-04-spark.png)

## Check

The spark should be visible and should have a collision shape.
