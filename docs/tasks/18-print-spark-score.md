# Task 18: Print Spark Score

## Goal

Make `Main` listen when a spark is collected.

## Do This

1. Open `scripts/main.gd`.
2. Replace it with this code:

```gdscript
extends Node2D

func _ready() -> void:
    print("Neon Drift online")
    for spark in get_tree().get_nodes_in_group("spark"):
        spark.collected.connect(_on_spark_collected)

func _on_spark_collected(value: int) -> void:
    print("Collected spark worth %s points" % value)
```

## Check

Press Play and collect a spark. The Output panel should print the spark value.
