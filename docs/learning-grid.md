# BGE Fourth Level Learning Grid

## Neon Drift Arcade: Computing Science

This learning grid maps the **Neon Drift Arcade** Godot project to the Scottish
Curriculum for Excellence (CfE) **Fourth Level Technologies – Computing Science**
benchmarks. It is intended to support planning and professional judgement, not to
turn the benchmarks into a checklist.

The project provides substantial evidence for textual programming and the design,
construction, testing and evaluation of a digital solution. Some Fourth Level
benchmarks require additional learning beyond this project; these are identified in
the coverage audit below.

**Suggested duration:** 8–12 hours  
**Context:** Individual or paired development of a top-down arcade game in Godot 4  
**Core resource:** Tasks 1–28 in this tutorial

## Learning grid

| Learning focus | Learning intention | Success criteria: I can… | Tutorial tasks | Fourth Level alignment | Possible evidence and assessment |
| --- | --- | --- | --- | --- | --- |
| 1. Analyse and plan the solution | Understand a game as a system of connected scenes, nodes, inputs, processes and outputs. | identify the project requirements; break the solution into player, arena, collectible, enemy and interface components; explain the information passed between components; create a storyboard, structure diagram or pseudocode plan. | [Tasks 1–6](tasks/01-create-project.md) and teacher planning activity | **TCH 4-13a**, **TCH 4-14b**, **TCH 4-15a** | Annotated requirements, scene tree diagram, storyboard or pseudocode; learner explanation of input → processing → output; teacher questioning. |
| 2. Build the player and arena | Use an appropriate textual language and development environment to build part of a solution. | create and organise reusable scenes; use variables, calculations and sequence in GDScript; explain how keyboard input changes velocity and position; test the player against stated requirements. | [Tasks 7–13](tasks/07-make-player-scene.md) | **TCH 4-14a**, **TCH 4-14b**, **TCH 4-15a** | Working `Player` scene and arena; annotated movement code; test table covering four directions, diagonal movement and boundaries. |
| 3. Model collection and communication | Understand how independently running game objects communicate information. | use a signal to send a value from a collectible to the main scene; use selection to decide which bodies can collect it; use iteration to connect multiple instances; trace the value from collision to output. | [Tasks 14–18](tasks/14-make-spark-scene.md) | **TCH 4-13a**, **TCH 4-14a**, **TCH 4-14b**, **TCH 4-15a** | Working spark collection; trace table or data-flow diagram; explanation of the signal, parameter and event handler; collision test evidence. |
| 4. Create an enemy algorithm | Apply selection, repetition, variables and calculations to a real-time behaviour. | explain the chase algorithm; use a typed variable to store the target; calculate direction and velocity; detect collisions using repetition and selection; identify syntax and logic errors. | [Tasks 19–22](tasks/19-make-hunter-scene.md) | **TCH 4-14a**, **TCH 4-14b**, **TCH 4-15a** | Working hunter scene; annotated code; debugging log that classifies errors; learner walkthrough of the chase process. |
| 5. Process and present game data | Select suitable data and interface components to present changing information. | store score, time and game state using appropriate types; update interface labels from variables; use selection to protect game state; justify the chosen display format. | [Tasks 23–24](tasks/23-build-hud.md) | **TCH 4-14a**, **TCH 4-14b**, **TCH 4-15a** | Working HUD; variable table showing name, type, purpose and initial value; annotated screenshot; peer feedback on clarity and accessibility. |
| 6. Control game states | Combine sequence, selection, repetition, variables, calculations and Boolean logic in a complete textual program. | implement countdown, win/lose state and restart; explain event-driven and frame-based processing; use `not` correctly; predict program behaviour for boundary cases. | [Tasks 25–26](tasks/25-add-timer.md) | **TCH 4-14a**, **TCH 4-14b**, **TCH 4-15a** | Working time-up and collision endings; trace table for `running` and `time_left`; boundary tests at 0 seconds and repeated collisions. |
| 7. Refine and compare | Evaluate the solution against requirements and compare alternative algorithms using relevant criteria. | gather user feedback; fix identified issues; compare two valid approaches to one feature; judge correctness, speed, memory, readability or maintainability; justify an improvement. | [Task 27](tasks/27-add-feedback.md) plus extension activity | **TCH 4-13b**, **TCH 4-15a** | Before/after evidence; peer test report; reasoned comparison, such as node groups versus stored references or per-frame pursuit versus timer-based updates; evaluation linked to requirements. |
| 8. Test, evaluate and publish | Select an appropriate platform, produce a testable build and evaluate the finished solution. | design normal, boundary and erroneous tests; record expected and actual results; distinguish syntax, runtime and logic errors; select an export platform from the requirements; evaluate strengths, limitations and next steps. | [Task 28](tasks/28-export-game.md) plus teacher assessment activity | **TCH 4-15a**; supports **TCH 4-01a** when learners share or publish through an approved service | Exported build; completed test plan; error/debugging log; evaluation report; short demonstration or code review. |

## Benchmark coverage audit

The wording below is a concise classroom summary. Use the official benchmark
document when making assessment decisions.

| E&amp;O | Relevant benchmark expectation | Coverage in this project | What is needed for secure evidence |
| --- | --- | --- | --- |
| **TCH 4-13a** | Describe real-world information processes, including transfers between computing and physical elements and human decision-making. | **Partial.** Learners can describe keyboard input, collision events, signals, processing and screen output. | Compare the game system with a genuinely complex real-world system containing people, computers and physical artefacts. |
| **TCH 4-13b** | Compare alternative algorithms for correctness and efficiency, recognising that “better” depends on context. | **Partial.** The core tutorial supplies one main implementation of each feature. | Require learners to implement or analyse two approaches and justify a choice using explicit criteria such as time, space, readability or responsiveness. |
| **TCH 4-14a** | Understand textual-language constructs and data structures. | **Strong for constructs; partial for data structures.** GDScript uses sequence, selection, repetition, typed variables, Boolean logic and calculations. | Add a learner-designed `Array` or `Dictionary`, explain its representation and use it meaningfully in the game. |
| **TCH 4-14b** | Explain the overall operation and architecture of a digital solution. | **Strong.** Scenes, nodes, scripts, groups, signals and UI elements form a connected solution. | Ask each learner to produce and explain an architecture or data-flow diagram without relying on the tutorial wording. |
| **TCH 4-14c** | Understand relationships between a high-level language and computer operation, representations, formats and levels of abstraction. | **Limited.** Godot and GDScript expose useful abstraction, but the tutorial does not teach translation or low-level execution. | Add focused learning on source, bytecode/intermediate representation, machine instructions, memory and binary representation. |
| **TCH 4-15a** | Analyse requirements; design, build, debug, test, evaluate and justify a textual solution using suitable constructs, structures and platform. | **Strong for building; partial across the full benchmark.** The project uses textual code, variables, sequence, selection, repetition, `not`, debugging checks and platform export. | Collect independent design notation, a classified debugging log, structured test/evaluation reports, a learner-designed data structure and reasoned platform choice. A separate relational-database task and interactive-web task are still required. |
| **TCH 4-01a** | Use a range of digital tools and services to create, collaborate and publish, and connect digital literacy with future pathways. | **Optional/partial.** Creation and export are present. | Add collaborative version control or an approved sharing platform, online publication and a short careers reflection. |

## Suggested holistic assessment

Give learners a change request after they complete the guided build, for example:

> Add three kinds of spark with different values and effects. Show the remaining
> sparks on the HUD, make the game finish when all are collected, and ensure the
> solution remains easy to extend.

Ask learners to submit:

1. a short requirements analysis and an accepted design representation;
2. their working Godot project and exported build;
3. annotated extracts showing variables, sequence, selection, repetition, logical
   operators and a learner-designed data structure;
4. a test report containing normal, boundary and erroneous cases;
5. a debugging log distinguishing syntax, runtime and logic errors;
6. an evaluation that compares an alternative algorithm and justifies improvements.

This unfamiliar extension gives stronger evidence of independent application than a
completed guided tutorial alone.

## Planning notes

- Use observation, discussion, code review, practical outcomes and written evidence
  together. One artifact does not need to evidence every benchmark.
- The official guidance advises against assessing or ticking off individual benchmarks
  in isolation. Make a holistic judgement from the learner's breadth, consistency and
  ability to apply learning in unfamiliar situations.
- The relational-database and interactive-web expectations within TCH 4-15a are not
  addressed by a Godot game and should be planned elsewhere.
- Digital Literacy and Cyber Resilience benchmarks are not automatically evidenced by
  using a computer. Add separate, purposeful learning if those organisers are part of
  the intended course coverage.

## Official source

- [Education Scotland: Technologies Benchmarks (Fourth Level begins on page 20; Computing Science on pages 23–24)](https://education.gov.scot/media/irimoozl/technologiesbenchmarkspdf.pdf)

