# Neon Drift Arcade

A heavily scaffolded, task-by-task MkDocs Material tutorial for building a first Godot arcade game.

The pupil-facing guide is broken into eight build tasks, with one task per page. Each page includes:

- a clear goal and checkpoint
- beginner terminology explanations
- embedded YouTube videos
- image checkpoints
- numbered Godot editor steps
- code translations
- troubleshooting tables

## Run locally

```sh
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
mkdocs serve
```

Open the local address printed by MkDocs.

## Build the static site

```sh
mkdocs build --strict
```

The tutorial uses SVG checkpoint images in `docs/assets/images` and embedded YouTube videos on the task pages.
