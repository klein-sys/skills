# Agent Compatibility & Architecture Report

This report analyzes agentic skill formats, execution models, and compatibility across **Google Antigravity**, **Gemini CLI**, **Claude Code**, and related AI coding harnesses.

---

## Executive Matrix

| Feature / Dimension | Google Antigravity (Your Agent) | Gemini CLI / Extensions | Claude Code | OpenAI Codex / Cursor |
| :--- | :--- | :--- | :--- | :--- |
| **Skill Format** | `skills/<name>/SKILL.md` with YAML frontmatter (`name`, `description`) | `gemini-extension.json` or `.gemini/skills/` | `.claude-plugin/` or `.claude/skills/` | `rules/` or proprietary plugin JSON |
| **Context Model** | **Progressive Disclosure** (only `name` & `description` injected until activated) | Progressive Disclosure or extension manifest | Varies by plugin; often full injection | Full file injection or RAG |
| **Workspace Root** | `.agents/skills/` (or `.agent/`, `_agents/`) | `.gemini/` or `.agents/` | `.claude/` or `.claude-plugin/` | `.cursor/rules/` |
| **Global Root** | `~/.gemini/config/skills/` | `~/.gemini/` | `~/.claude/` | Global config directory |
| **Default Shell** | Platform-native (PowerShell on Windows, Bash on Linux/macOS) | Platform-native | Assumes Unix Bash | System default |
| **Tool Calling API** | `run_command`, `replace_file_content`, `view_file`, `browser_subagent` | Extension commands | `bash`, `str_replace_editor`, `view` | Internal editor tools |

---

## Native Compatibility Standards in This Repository

1. **Progressive Disclosure**:
   Only skill `name` and `description` are exposed initially. The full `SKILL.md`, `references/`, and `examples/` are loaded autonomously only when a matching task is detected.
2. **Cross-Platform Tooling**:
   Commands and scripts avoid unix-only bash assumptions (`sed`, `grep -rn`) and operate seamlessly on Windows PowerShell and Linux/macOS.
3. **Structured Categorization**:
   Skills are organized into domain categories (`software-dev/`, etc.) with a root-level `.agents/skills/` mirror for immediate, zero-friction discovery in any Antigravity workspace.
