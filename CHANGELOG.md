# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.7] - 2026-03-18

### Changed

- Remove remaining legacy `nous` naming from code and docs
- Require Python imports via `gravtice.genai`
- Update env examples to prefer provider-native API key names

## [0.1.6] - 2026-03-18

### Changed

- Publish package metadata under `genai-calling`

## [0.1.5] - 2026-03-18

### Changed

- Publish package metadata under `gravtice-genai-calling`
- Switch Python import package to `gravtice`
- Use only `GENAI_CALLING_*` env vars and `~/.genai-calling/.env`

## [0.1.4] - 2026-03-11

### Changed

- Switch project license from Apache-2.0 to MIT

## [0.1.3] - 2026-03-10

### Changed

- Lower minimum Python version from 3.12 to 3.10
- Make `TypedDict` usage compatible with Python 3.10 (`typing_extensions.TypedDict`)
- Update CI matrix to test both Python 3.10 and 3.12

## [0.1.2] - 2026-02-04

### Changed

- Format code with ruff (no functional changes)

## [0.1.1] - 2026-02-04

### Fixed

- Tuzi-web chirp music: poll by `task_id` (fetch) and accept `complete` statuses

### Changed

- Remove `suno-*` / `suno_*` model ids; use `chirp-*` directly

## [0.1.0] - 2026-01-27

### Added

- Initial release of genai-calling
- Unified `Client.generate()` API for multi-provider, multi-modal generation
- Support for multiple providers:
  - OpenAI (GPT-4, DALL-E, Whisper, TTS)
  - Google (Gemini, Imagen, Veo)
  - Anthropic (Claude)
  - Aliyun (DashScope / Bailian)
  - Volcengine (Doubao)
  - Tuzi (web/openai/google/anthropic protocols)
- Multi-modal support:
  - Text input/output
  - Image input/output (understanding & generation)
  - Audio input/output (transcription & TTS)
  - Video input/output (understanding & generation)
  - Embedding generation
- Streaming support via `generate_stream()`
- Async job support for long-running tasks (video generation)
- Tool calling support (function calling)
- JSON schema output support
- MCP Server with Streamable HTTP and SSE transports
- CLI tool (`genai`) for quick testing
- Security features:
  - SSRF protection (private/loopback URL blocking)
  - DNS pinning to prevent rebinding attacks
  - URL download size limits
  - Bearer token authentication for MCP
  - Token rules for fine-grained access control
- Zero-config design with `.env` file auto-loading
- Comprehensive test suite (103 tests)

### Security

- Default rejection of private/loopback URLs (configurable via `GENAI_CALLING_ALLOW_PRIVATE_URLS`)
- URL download hard limit (default 128MiB, configurable via `GENAI_CALLING_URL_DOWNLOAD_MAX_BYTES`)
- MCP artifact memory limits with LRU eviction
- Signed artifact URLs for authenticated access

[Unreleased]: https://github.com/gravtice/genai-calling/compare/v0.1.7...HEAD
[0.1.7]: https://github.com/gravtice/genai-calling/compare/v0.1.6...v0.1.7
[0.1.6]: https://github.com/gravtice/genai-calling/compare/v0.1.5...v0.1.6
[0.1.5]: https://github.com/gravtice/genai-calling/compare/v0.1.4...v0.1.5
[0.1.4]: https://github.com/gravtice/genai-calling/compare/v0.1.3...v0.1.4
[0.1.3]: https://github.com/gravtice/genai-calling/compare/v0.1.2...v0.1.3
[0.1.2]: https://github.com/gravtice/genai-calling/compare/v0.1.1...v0.1.2
[0.1.1]: https://github.com/gravtice/genai-calling/compare/v0.1.0...v0.1.1
[0.1.0]: https://github.com/gravtice/genai-calling/releases/tag/v0.1.0
