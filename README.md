# game-framework-contracts

Contract types and abstract interfaces for the Game Framework ecosystem.

![Project Architecture Diagram with Contracts highlighted](docs/game-framework-contracts.png)

This repository provides the shared Python package used to coordinate game state, client/server messaging, and game-specific implementations across the Game Framework projects. It does not contain an app or runner implementation; it defines the interfaces and data models that the other repositories build against.

## Repository Structure

- `src/game_contracts/`: public contract modules
- `src/game_contracts/message.py`: message envelope models used for client/server exchange
- `src/game_contracts/game_ui_abc.py`: base UI contract
- `src/game_contracts/logic_core_abc.py`: game state and command contracts
- `src/game_contracts/metadata_handler_abc.py`: metadata/storage contract
- `src/game_contracts/runner_client_abc.py`: client-side runner contract
- `src/game_contracts/runner_server_abc.py`: server-side runner contract
- `docs/`: supporting documentation and the architecture diagram image

## Prerequisites

- Python 3.12 or newer
- `pip`
- Optional: `make` for the convenience targets in the bundled Makefile

## Local Setup

1. Create and activate a virtual environment.
2. Install the package in editable mode with its direct runtime dependency.
3. Install test/build tooling if you plan to run the Makefile targets.

Example:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e .
python -m pip install build pytest
```

The Makefile includes `make venv`, `make package`, and `make test` targets. The `make install` target currently assumes a `.[dev]` extra, but `pyproject.toml` does not declare one, so the direct editable install above is the reliable path.

## Usage

This package is intended to be imported by sibling Game Framework repositories. Typical imports look like this:

```python
from game_contracts.message import ServerMessage
from game_contracts.runner_client_abc import RunnerClientABC
from game_contracts.logic_core_abc import GameState, Command
```

The main data model is `ServerMessage`, which wraps server-originated payloads and computes a deterministic `message_id`. The abstract base classes define the contracts that runner, UI, metadata, and game logic implementations must satisfy.

## Related Repositories

- [Game Framework - Runners](https://github.com/threnjen/game-framework-runners)
- [Game Framework - App Server](https://github.com/threnjen/game-framework-app-server)
- [Sample Game UI](https://github.com/threnjen/sample-game-ui)
- [Sample Game Logic](https://github.com/threnjen/sample-game-logic)

## Documentation

- [Architecture](docs/ARCHITECTURE.md)
- [Codebase Context](docs/CODEBASE_CONTEXT.md)
- [Local Development](docs/LOCAL_DEVELOPMENT.md)