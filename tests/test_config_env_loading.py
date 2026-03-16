import os
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest.mock import patch


class TestConfigEnvLoading(unittest.TestCase):
    def test_load_env_files_loads_global_home_env_as_lowest_priority(self) -> None:
        from nous.genai._internal.config import load_env_files

        with TemporaryDirectory() as tmpdir:
            root = Path(tmpdir) / "project"
            home = Path(tmpdir) / "home"
            root.mkdir()
            (home / ".nous").mkdir(parents=True)
            global_env = home / ".nous" / ".env"
            global_env.write_text("NOUS_GENAI_OPENAI_API_KEY=global-key\n", encoding="utf-8")

            with patch("nous.genai._internal.config.Path.home", return_value=home):
                with patch.dict(os.environ, {}, clear=True):
                    loaded = load_env_files(root=root)
                    value = os.environ.get("NOUS_GENAI_OPENAI_API_KEY")

            self.assertEqual(value, "global-key")
            self.assertEqual(loaded, [global_env])

    def test_project_env_overrides_global_home_env(self) -> None:
        from nous.genai._internal.config import load_env_files

        with TemporaryDirectory() as tmpdir:
            root = Path(tmpdir) / "project"
            home = Path(tmpdir) / "home"
            root.mkdir()
            (home / ".nous").mkdir(parents=True)
            (root / ".env.local").write_text(
                "NOUS_GENAI_OPENAI_API_KEY=local-key\n", encoding="utf-8"
            )
            global_env = home / ".nous" / ".env"
            global_env.write_text("NOUS_GENAI_OPENAI_API_KEY=global-key\n", encoding="utf-8")

            with patch("nous.genai._internal.config.Path.home", return_value=home):
                with patch.dict(os.environ, {}, clear=True):
                    loaded = load_env_files(root=root)
                    value = os.environ.get("NOUS_GENAI_OPENAI_API_KEY")

            self.assertEqual(value, "local-key")
            self.assertEqual(loaded, [root / ".env.local", global_env])

    def test_process_env_overrides_project_and_global_env(self) -> None:
        from nous.genai._internal.config import load_env_files

        with TemporaryDirectory() as tmpdir:
            root = Path(tmpdir) / "project"
            home = Path(tmpdir) / "home"
            root.mkdir()
            (home / ".nous").mkdir(parents=True)
            (root / ".env.local").write_text(
                "NOUS_GENAI_OPENAI_API_KEY=local-key\n", encoding="utf-8"
            )
            (home / ".nous" / ".env").write_text(
                "NOUS_GENAI_OPENAI_API_KEY=global-key\n", encoding="utf-8"
            )

            with patch("nous.genai._internal.config.Path.home", return_value=home):
                with patch.dict(
                    os.environ, {"NOUS_GENAI_OPENAI_API_KEY": "process-key"}, clear=True
                ):
                    load_env_files(root=root)
                    value = os.environ.get("NOUS_GENAI_OPENAI_API_KEY")

            self.assertEqual(value, "process-key")
