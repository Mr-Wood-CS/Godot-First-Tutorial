# Neon Drift Arcade

A heavily scaffolded MkDocs Material tutorial for building a first Godot arcade game, broken into one small task per page.

The guide is broken into 28 small build tasks, with one task per page. Each page includes:

- a clear goal and checkpoint
- beginner terminology explanations
- YouTube videos
- image checkpoints
- numbered Godot editor steps
- short checks

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

The tutorial uses PNG checkpoint images in `docs/assets/images` and YouTube videos on the task pages.
