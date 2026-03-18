import unittest


class TestPublicImports(unittest.TestCase):
    def test_gravtice_does_not_reexport_genai_api(self) -> None:
        import gravtice

        self.assertFalse(hasattr(gravtice, "Client"))
        self.assertFalse(hasattr(gravtice, "GenerateRequest"))

    def test_gravtice_genai_is_public_import_path(self) -> None:
        from gravtice.genai import Client, GenerateRequest, Message, OutputSpec, Part

        self.assertIsNotNone(Client)
        self.assertIsNotNone(GenerateRequest)
        self.assertIsNotNone(Message)
        self.assertIsNotNone(OutputSpec)
        self.assertIsNotNone(Part)
