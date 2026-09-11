# Task 17: Place Sparks

## Goal

Put collectible sparks in the arena.

## 1. Place the first spark

1. In the FileSystem panel, double-click ==scenes/Main.tscn==.

2. Select Main in the Scene panel, then drag ==scenes/Spark.tscn== from the FileSystem panel into the 2D view.

3. Use the Move tool to put the spark inside the bright border.

## 2. Add it to a group

With the spark selected, open **Node > Groups** on the right. Create a group called ==spark== and tick its box.

## 3. Make the copies

In the Scene panel, ==right-click== the spark and choose **Duplicate**.

Repeat until there are ==6 sparks== altogether. Move each one to a different place inside the border.

Check they all sit directly inside Main, then choose **Scene > Save Scene**.

## Check

Press **F5**. You should see six sparks. Touching one with the player should make it disappear.
