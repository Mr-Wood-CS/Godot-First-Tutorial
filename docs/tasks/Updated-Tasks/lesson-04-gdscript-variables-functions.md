# :material-code-braces: Lesson 4 - Variables, Functions and Script Structure

Source video: [Your First Code! Hello World in GDScript](https://www.youtube.com/watch?v=pyhBx2JdNmg)

## Learning Intention

Use variables and functions to organise simple GDScript code.

## Success Criteria

- I can create a variable.
- I can update a variable.
- I can write a custom function.
- I can call a function from `_ready()`.

## Keywords

| Keyword | Meaning |
|---|---|
| Variable | A named place to store a value. |
| Value | The data stored in a variable. |
| Function call | Running a function by using its name. |
| Indentation | Spacing that shows which code belongs together. |


## Worked Example

```gdscript
extends Node2D

var score = 0

func _ready():
    add_point()
    print(score)

func add_point():
    score = score + 1
```

## Practical Tasks

1. Create a variable called `score`.
2. Print the starting score.
3. Create a function called `add_point`.
4. Make the function increase the score.
5. Call the function twice and predict the output.

