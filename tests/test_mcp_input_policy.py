import os
import unittest
from unittest.mock import patch


class TestMcpInputPolicy(unittest.TestCase):
    def test_mcp_transport_rejects_path_source(self) -> None:
        from gravtice.genai import GenAIError
        from gravtice.genai.client import Client
        from gravtice.genai.types import (
            GenerateRequest,
            Message,
            OutputSpec,
            Part,
            PartSourcePath,
        )

        with patch.dict(os.environ, {"GENAI_CALLING_TRANSPORT": "sse"}, clear=False):
            client = Client()
            req = GenerateRequest(
                model="unknown:demo",
                input=[
                    Message(
                        role="user",
                        content=[
                            Part(
                                type="image",
                                mime_type="image/png",
                                source=PartSourcePath(path="/tmp/x.png"),
                            )
                        ],
                    )
                ],
                output=OutputSpec(modalities=["text"]),
            )
            with self.assertRaises(GenAIError) as cm:
                client.generate(req)
            self.assertEqual(cm.exception.info.type, "InvalidRequestError")
            self.assertIn("MCP transport does not support", cm.exception.info.message)

    def test_mcp_transport_rejects_bytes_source(self) -> None:
        from gravtice.genai import GenAIError
        from gravtice.genai.client import Client
        from gravtice.genai.types import (
            GenerateRequest,
            Message,
            OutputSpec,
            Part,
            PartSourceBytes,
        )

        with patch.dict(os.environ, {"GENAI_CALLING_TRANSPORT": "sse"}, clear=False):
            client = Client()
            req = GenerateRequest(
                model="unknown:demo",
                input=[
                    Message(
                        role="user",
                        content=[
                            Part(
                                type="audio",
                                mime_type="audio/wav",
                                source=PartSourceBytes(data=b"123"),
                            )
                        ],
                    )
                ],
                output=OutputSpec(modalities=["text"]),
            )
            with self.assertRaises(GenAIError) as cm:
                client.generate(req)
            self.assertEqual(cm.exception.info.type, "InvalidRequestError")
            self.assertIn("MCP transport does not support", cm.exception.info.message)

    def test_mcp_transport_allows_base64_source(self) -> None:
        from gravtice.genai import GenAIError
        from gravtice.genai.client import Client
        from gravtice.genai.types import (
            GenerateRequest,
            Message,
            OutputSpec,
            Part,
            PartSourceBytes,
        )

        with patch.dict(os.environ, {"GENAI_CALLING_TRANSPORT": "sse"}, clear=False):
            client = Client()
            req = GenerateRequest(
                model="unknown:demo",
                input=[
                    Message(
                        role="user",
                        content=[
                            Part(
                                type="image",
                                mime_type="image/png",
                                source=PartSourceBytes(data="AA==", encoding="base64"),
                            )
                        ],
                    )
                ],
                output=OutputSpec(modalities=["text"]),
            )
            with self.assertRaises(GenAIError) as cm:
                client.generate(req)
            self.assertEqual(cm.exception.info.type, "InvalidRequestError")
            self.assertIn("unknown provider", cm.exception.info.message)
