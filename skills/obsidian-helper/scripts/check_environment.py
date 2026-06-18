#!/usr/bin/env python3
"""Read-only, cross-platform discovery for Obsidian Helper."""

from __future__ import annotations

import argparse
import json
import os
import platform
import plistlib
import shutil
import subprocess
from pathlib import Path
from typing import Optional


PLUGIN_IDS = {
    "dataview": "dataview",
    "templater": "templater-obsidian",
    "tasks": "obsidian-tasks-plugin",
    "omnisearch": "omnisearch",
    "calendar": "calendar",
    "periodic_notes": "periodic-notes",
}


def run_quiet(command: list[str]) -> Optional[subprocess.CompletedProcess[str]]:
    try:
        return subprocess.run(
            command,
            capture_output=True,
            text=True,
            check=False,
            timeout=5,
        )
    except (OSError, subprocess.TimeoutExpired):
        return None


def process_running() -> bool:
    system = platform.system()
    if system == "Windows":
        result = run_quiet(["tasklist", "/FI", "IMAGENAME eq Obsidian.exe"])
        return bool(result and "Obsidian.exe" in result.stdout)

    command = ["pgrep", "-x", "Obsidian"] if system == "Darwin" else ["pgrep", "-f", "[Oo]bsidian"]
    result = run_quiet(command)
    return bool(result and result.returncode == 0)


def app_candidates() -> list[Path]:
    system = platform.system()
    home = Path.home()
    if system == "Darwin":
        return [Path("/Applications/Obsidian.app"), home / "Applications" / "Obsidian.app"]
    if system == "Windows":
        candidates: list[Path] = []
        for variable, suffix in (
            ("LOCALAPPDATA", Path("Programs/Obsidian/Obsidian.exe")),
            ("PROGRAMFILES", Path("Obsidian/Obsidian.exe")),
            ("PROGRAMFILES(X86)", Path("Obsidian/Obsidian.exe")),
        ):
            base = os.environ.get(variable)
            if base:
                candidates.append(Path(base) / suffix)
        return candidates
    return [Path("/usr/bin/obsidian"), Path("/usr/local/bin/obsidian"), Path("/opt/Obsidian/obsidian")]


def installed_app() -> Optional[Path]:
    return next((candidate for candidate in app_candidates() if candidate.exists()), None)


def app_version(app_path: Optional[Path]) -> Optional[str]:
    if platform.system() != "Darwin" or app_path is None:
        return None
    plist = app_path / "Contents" / "Info.plist"
    try:
        with plist.open("rb") as handle:
            data = plistlib.load(handle)
        return data.get("CFBundleShortVersionString")
    except (OSError, plistlib.InvalidFileException):
        return None


def obsidian_config() -> Path:
    system = platform.system()
    if system == "Darwin":
        return Path.home() / "Library" / "Application Support" / "obsidian" / "obsidian.json"
    if system == "Windows":
        base = Path(os.environ.get("APPDATA", Path.home() / "AppData" / "Roaming"))
        return base / "obsidian" / "obsidian.json"
    base = Path(os.environ.get("XDG_CONFIG_HOME", Path.home() / ".config"))
    return base / "obsidian" / "obsidian.json"


def registered_vaults() -> list[dict[str, object]]:
    try:
        data = json.loads(obsidian_config().read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return []

    vaults: list[dict[str, object]] = []
    for vault_id, record in data.get("vaults", {}).items():
        path = Path(record.get("path", "")).expanduser()
        vaults.append(
            {
                "id": vault_id,
                "name": path.name,
                "path": str(path),
                "exists": path.is_dir(),
                "open": bool(record.get("open", False)),
            }
        )
    return vaults


def inspect_vault(path: Path, deep: bool) -> dict[str, object]:
    plugin_root = path / ".obsidian" / "plugins"
    plugins = {
        name: (plugin_root / plugin_id).is_dir()
        for name, plugin_id in PLUGIN_IDS.items()
    }
    config_candidates = [
        path / root / namespace / "skill-config.yaml"
        for root in ("90_System", "90.System")
        for namespace in ("ObsidianHelper", "KnowledgeSteward")
    ]
    config_path = next((candidate for candidate in config_candidates if candidate.is_file()), None)
    result: dict[str, object] = {
        "path": str(path),
        "exists": path.is_dir(),
        "writable": os.access(path, os.W_OK),
        "initialized": config_path is not None,
        "config_path": str(config_path) if config_path else None,
        "plugins": plugins,
    }
    if deep:
        try:
            result["markdown_files"] = sum(1 for _ in path.rglob("*.md"))
        except OSError:
            result["markdown_files"] = None
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--vault", type=Path, help="Optional vault path to inspect")
    parser.add_argument("--deep", action="store_true", help="Also count Markdown files")
    args = parser.parse_args()

    app_path = installed_app()
    cli = shutil.which("obsidian")
    payload: dict[str, object] = {
        "platform": platform.system(),
        "obsidian": {
            "installed": app_path is not None or cli is not None,
            "path": str(app_path) if app_path else None,
            "version": app_version(app_path),
            "running": process_running(),
        },
        "official_cli": {"available": cli is not None, "path": cli},
        "registered_vaults": registered_vaults(),
    }
    if args.vault:
        payload["selected_vault"] = inspect_vault(args.vault.expanduser().resolve(), args.deep)

    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
