# Codebase Context

- Repository purpose: shared contracts for the Game Framework ecosystem.
- Packaging: Python package named `game-contracts`, import package `game_contracts`.
- Python requirement: `>=3.12`.
- Runtime dependency: `pydantic>=2.11`.

## Top-Level Structure

- `README.md`: short project overview and cross-repo links.
- `makefile`: helper targets for venv creation, packaging, and tests.
- `pyproject.toml`: build metadata and package discovery.
- `src/game_contracts/`: public Python modules.
- `docs/`: architecture and local setup documentation.
- `dist/`: build output directory.

## Public Modules

- `message.py`
  - `MessageSource`: enum for `client` and `server`.
  - `MessageEnvelope`: shared message schema.
  - `ServerMessage`: server-only message model with timestamp and computed `message_id`.
- `game_ui_abc.py`
  - `GameUI`: async UI base class with queue-based response handling.
- `logic_core_abc.py`
  - `GameState`: abstract Pydantic base model for game state.
  - `CommandResult`: command execution result model.
  - `Command`: abstract command with `execute()` and custom serialization.
- `metadata_handler_abc.py`
  - `GameMetadataHandlerABC`: metadata and player-view contract.
- `runner_client_abc.py`
  - `RunnerClientABC`: client-side runner contract.
- `runner_server_abc.py`
  - `RunnerServerABC`: server-side runner contract.

## Key Patterns

- Use abstract base classes for runtime roles that are implemented in sibling repos.
- Use Pydantic models for data carried across process boundaries.
- Keep the package logic-light; most methods are signatures or small helpers.
- `ServerMessage.message_id` is computed from `client_id`, timestamp, and JSON-sorted payload content.
- `GameUI.start()` launches a background polling task and does not block.

## Entry Points And Behavior

- There is no CLI entry point.
- There are no in-repo tests or application runtime scripts.
- This repository is consumed by other Game Framework repos, not run as a standalone service.

## Build And Packaging

- `make venv` creates `.venv` and installs `pip` and `build` into it.
- `make package` builds sdist and wheel artifacts into `dist/`.
- `make test` runs `pytest -q` inside the venv.
- `make install` currently expects `.[dev]`, but the project metadata does not define a `dev` extra.

## Naming And Conventions

- Module filenames use snake_case with an `_abc` suffix for abstract interfaces.
- Contract classes use `ABC` or abstract methods when implementation is expected downstream.
- Public models are located directly under `src/game_contracts/` rather than split into subpackages.

## Do Not

- Do not add application behavior here; this repo is only the shared contract layer.
- Do not assume a `dev` extra exists unless `pyproject.toml` defines it.
- Do not describe a standalone server, runner, or UI in this repository; those live elsewhere.
- Do not add deployment guidance; this repository is packaged and consumed by other projects.