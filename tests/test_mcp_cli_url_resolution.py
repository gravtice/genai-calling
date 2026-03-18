import os
import unittest
from unittest.mock import patch


class TestMcpCliUrlResolution(unittest.TestCase):
    def test_default_host_port_builds_mcp_url(self) -> None:
        from gravtice.genai import mcp_cli

        with patch.dict(
            os.environ,
            {
                "GENAI_CALLING_MCP_URL": "",
                "GENAI_CALLING_MCP_BASE_URL": "",
                "GENAI_CALLING_MCP_PUBLIC_BASE_URL": "",
                "GENAI_CALLING_MCP_HOST": "127.0.0.1",
                "GENAI_CALLING_MCP_PORT": "6123",
            },
            clear=False,
        ):
            self.assertEqual(mcp_cli._mcp_url(), "http://127.0.0.1:6123/mcp")

    def test_explicit_mcp_url_takes_precedence(self) -> None:
        from gravtice.genai import mcp_cli

        with patch.dict(
            os.environ,
            {
                "GENAI_CALLING_MCP_URL": "http://example.com/prefix",
                "GENAI_CALLING_MCP_BASE_URL": "http://bad.example",
                "GENAI_CALLING_MCP_PUBLIC_BASE_URL": "http://bad.example",
                "GENAI_CALLING_MCP_HOST": "127.0.0.1",
                "GENAI_CALLING_MCP_PORT": "6001",
            },
            clear=False,
        ):
            self.assertEqual(mcp_cli._mcp_url(), "http://example.com/prefix/mcp")
