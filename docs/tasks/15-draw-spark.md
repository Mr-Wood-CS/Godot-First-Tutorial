# Task 15: Draw The Spark

Make the spark visible and give it a collision shape.

## 1. Add the drawing node

1. Open ==scenes/Spark.tscn== from the FileSystem panel.

2. In the Scene panel, ==right-click== Spark and choose **Add Child Node**.

3. Search for ==Polygon2D== and click **Create**.

## 2. Make a diamond

Select Polygon2D. In the Inspector, open **Data**, then **Polygon**. Set the array's **Size** to ==4==.

| Entry | x | y |
| --- | --- | --- |
| 0 | 0 | -12 |
| 1 | 12 | 0 |
| 2 | 0 | 12 |
| 3 | -12 | 0 |

Click the box beside **Color** and choose yellow.

## 3. Add the collision circle

1. ==Right-click== Spark and choose **Add Child Node**.

2. Search for ==CollisionShape2D== and click **Create**.

3. In the Inspector, open the dropdown beside **Shape** and choose **New CircleShape2D**.

4. Click the new circle resource to open its settings. Set **Radius** to ==14==.

![Example of choosing a circle shape and opening its radius settings](../assets/images/task-09-shape-inspector.svg)

*The example shows radius 18. Use 14 for the spark.*

## 4. Save and check

Choose **Scene > Save Scene**.

![Spark checkpoint](../assets/images/task-04-spark.png)

In the 2D editor, select CollisionShape2D. You should see a circle centred over the yellow diamond.

Both Polygon2D and CollisionShape2D should sit directly inside Spark. The collision warning should disappear once you have assigned the circle shape.
