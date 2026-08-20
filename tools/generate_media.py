from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
IMAGES = ROOT / "docs" / "assets" / "images"
VIDEOS = ROOT / "docs" / "assets" / "videos"


TASKS = [
    (
        "task-01-project-pulse.gif",
        "Task 01 - Project Pulse",
        ["New Project", "Main.tscn", "Title appears", "Press Play"],
    ),
    (
        "task-02-player-movement.gif",
        "Task 02 - Player Movement",
        ["Player.tscn", "CollisionShape2D", "player.gd", "Keyboard control"],
    ),
    (
        "task-03-the-arena.gif",
        "Task 03 - The Arena",
        ["ArenaArt", "Grid drawing", "Wall collision", "Test all sides"],
    ),
    (
        "task-04-collect-the-sparks.gif",
        "Task 04 - Collect The Sparks",
        ["Spark.tscn", "Area2D", "collected signal", "Spark disappears"],
    ),
    (
        "task-05-enemy-pressure.gif",
        "Task 05 - Enemy Pressure",
        ["Hunter.tscn", "Find player group", "Chase target", "Player hit"],
    ),
    (
        "task-06-score-and-survive.gif",
        "Task 06 - Score And Survive",
        ["HUD labels", "60 second timer", "Game over panel", "Restart button"],
    ),
    (
        "task-07-juice-the-loop.gif",
        "Task 07 - Juice The Loop",
        ["Tween pop", "Particle burst", "Sound effects", "Readable feedback"],
    ),
    (
        "task-08-export-the-cabinet.gif",
        "Task 08 - Export The Cabinet",
        ["Main scene set", "Window settings", "Export preset", "Playtest build"],
    ),
]


def font(size: int) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    candidates = [
        "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
        "/System/Library/Fonts/Supplemental/Arial.ttf",
        "/Library/Fonts/Arial.ttf",
    ]
    for candidate in candidates:
        try:
            return ImageFont.truetype(candidate, size)
        except OSError:
            continue
    return ImageFont.load_default()


TITLE_FONT = font(44)
BODY_FONT = font(28)
SMALL_FONT = font(22)


def write_svg(path: Path, body: str) -> None:
    path.write_text(body.strip() + "\n", encoding="utf-8")


def make_missing_svgs() -> None:
    write_svg(
        IMAGES / "task-05-hunter.svg",
        """
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 540" role="img" aria-labelledby="title desc">
  <title id="title">Task 05 hunter chase checkpoint</title>
  <desc id="desc">A red hunter enemy chasing the cyan player ship inside the neon arena.</desc>
  <rect width="960" height="540" fill="#101222"/>
  <g stroke="#252947" stroke-width="2">
    <path d="M0 90h960M0 180h960M0 270h960M0 360h960M0 450h960"/>
    <path d="M120 0v540M240 0v540M360 0v540M480 0v540M600 0v540M720 0v540M840 0v540"/>
  </g>
  <rect x="48" y="48" width="864" height="444" fill="none" stroke="#7df9ff" stroke-width="8"/>
  <polygon points="502,250 532,312 472,312" fill="#7df9ff"/>
  <circle cx="502" cy="292" r="30" fill="none" stroke="#7df9ff" stroke-width="4"/>
  <polygon points="172,138 230,168 174,204" fill="#ff4d8d"/>
  <circle cx="192" cy="170" r="34" fill="none" stroke="#ff4d8d" stroke-width="4"/>
  <path d="M246 188 C320 214 378 240 444 270" fill="none" stroke="#ffb000" stroke-width="6" stroke-dasharray="16 14"/>
  <text x="64" y="88" fill="#ffffff" font-size="34" font-family="Arial, sans-serif" font-weight="700">Hunter chases the player</text>
  <text x="64" y="128" fill="#b7e33b" font-size="24" font-family="Arial, sans-serif">Checkpoint: touching the player prints Player hit</text>
</svg>
        """,
    )
    write_svg(
        IMAGES / "task-08-export.svg",
        """
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 540" role="img" aria-labelledby="title desc">
  <title id="title">Task 08 export checkpoint</title>
  <desc id="desc">A Godot export window leading to a playable desktop build.</desc>
  <rect width="960" height="540" fill="#101222"/>
  <rect x="70" y="70" width="500" height="360" rx="8" fill="#191c32" stroke="#7df9ff" stroke-width="5"/>
  <rect x="95" y="110" width="450" height="44" fill="#242947"/>
  <rect x="95" y="176" width="210" height="38" fill="#2c3155"/>
  <rect x="95" y="234" width="350" height="38" fill="#2c3155"/>
  <rect x="95" y="292" width="285" height="38" fill="#2c3155"/>
  <rect x="360" y="360" width="150" height="48" rx="6" fill="#b7e33b"/>
  <text x="386" y="393" fill="#101222" font-size="26" font-family="Arial, sans-serif" font-weight="700">Export</text>
  <path d="M594 250 C650 250 674 250 728 250" stroke="#ffb000" stroke-width="10" fill="none" marker-end="url(#arrow)"/>
  <defs>
    <marker id="arrow" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto" markerUnits="strokeWidth">
      <path d="M0,0 L0,6 L9,3 z" fill="#ffb000"/>
    </marker>
  </defs>
  <rect x="740" y="175" width="150" height="150" rx="16" fill="#252947" stroke="#ff4d8d" stroke-width="5"/>
  <polygon points="815,214 855,292 775,292" fill="#7df9ff"/>
  <text x="70" y="484" fill="#ffffff" font-size="34" font-family="Arial, sans-serif" font-weight="700">Export a build someone else can play</text>
  <text x="740" y="360" fill="#b7e33b" font-size="24" font-family="Arial, sans-serif">Playable build</text>
</svg>
        """,
    )


def draw_card(title: str, steps: list[str], active: int) -> Image.Image:
    image = Image.new("RGB", (960, 540), "#101222")
    draw = ImageDraw.Draw(image)

    for x in range(0, 961, 80):
        draw.line((x, 0, x, 540), fill="#252947", width=2)
    for y in range(0, 541, 80):
        draw.line((0, y, 960, y), fill="#252947", width=2)

    draw.rectangle((46, 46, 914, 494), outline="#7df9ff", width=6)
    draw.text((78, 74), title, font=TITLE_FONT, fill="#ffffff")
    draw.text((78, 132), "Short teacher video: watch, build, test.", font=SMALL_FONT, fill="#b7e33b")

    for index, step in enumerate(steps):
        y = 196 + index * 62
        active_step = index == active
        fill = "#ffb000" if active_step else "#2c3155"
        text_fill = "#101222" if active_step else "#ffffff"
        draw.rounded_rectangle((88, y, 872, y + 44), radius=8, fill=fill)
        draw.text((112, y + 8), f"{index + 1}. {step}", font=BODY_FONT, fill=text_fill)

    progress_x = 88 + active * 196
    draw.rectangle((88, 460, 872, 472), fill="#2c3155")
    draw.rectangle((88, 460, progress_x + 196, 472), fill="#ff4d8d")
    return image


def make_gifs() -> None:
    VIDEOS.mkdir(parents=True, exist_ok=True)
    for filename, title, steps in TASKS:
        frames = []
        for active in range(len(steps)):
            frame = draw_card(title, steps, active)
            frames.extend([frame] * 4)
        frames[0].save(
            VIDEOS / filename,
            save_all=True,
            append_images=frames[1:],
            duration=350,
            loop=0,
            optimize=True,
        )


def main() -> None:
    IMAGES.mkdir(parents=True, exist_ok=True)
    VIDEOS.mkdir(parents=True, exist_ok=True)
    make_missing_svgs()
    make_gifs()


if __name__ == "__main__":
    main()
