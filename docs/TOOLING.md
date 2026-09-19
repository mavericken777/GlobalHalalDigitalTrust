# AHTE / IQ300 Approved Tooling Registry

- Artifact: `docs/TOOLING.md`
- Revision: `v1.0.0`
- Control date: `2026-09-19`
- Suggested commit: `docs(tooling): add runtime-verified tool registry [DOCTRINE-CRITICAL]`

This registry is human-facing. Agent instructions govern behaviour; this file
records what has actually been verified about each external tool.

No tool in this registry is project authority. Presence here means "known and
characterised," not "approved for unrestricted use."

## Verification status legend

- VERIFIED — current official documentation retrieved and cited.
- PARTIAL — existence and one or more properties verified; others unverified.
- UNVERIFIED — not yet checked.
- UNSUITABLE — verified as incompatible with a specific target context.

---

## A. Built-in GitHub MCP servers

### GitHub MCP Server

- **Status:** VERIFIED
- **Type:** built-in MCP server for Copilot cloud agent and code review
- **Endpoint (remote form):** `https://api.githubcopilot.com/mcp/`
- **Authentication:** automatic; built-in server receives a repo-scoped,
  read-only token by default.
- **Reference syntax:** `github/*` for all tools, or `github/<tool-name>`.
- **Governance note:** Do not re-declare this server in a custom agent profile.
  It is auto-configured for the cloud agent.

### Playwright MCP Server

- **Status:** VERIFIED
- **Type:** built-in MCP server for Copilot cloud agent
- **Tools available:** Playwright tools, configured to access localhost only.
- **Reference syntax:** `playwright/*` or `playwright/<tool-name>`.

---

## B. Repository MCP configuration

- **Where:** GitHub.com → repository Settings → Copilot → MCP servers.
- **Format:** JSON with `mcpServers` object.
- **Shared by:** Copilot cloud agent and Copilot code review.
- **Limitations:**
  - Only MCP **tools** are supported; resources and prompts are not.
  - Remote MCP servers that use **OAuth** are not currently supported for
    cloud agent and code review.
- **Secrets:** Must be prefixed `COPILOT_MCP_`.

---

## C. Characterised external tools (not project doctrine)

### Website / full-stack

| Tool | Status | Notes |
|------|--------|-------|
| Totalum | VERIFIED (capability) | Prompt → Next.js; API key required; free tier limits |
| Lovable MCP | VERIFIED / UNSUITABLE for cloud-agent repo MCP | OAuth path not supported on Copilot cloud agent MCP settings |
| GitHub Spark | VERIFIED | Copilot Pro+ / Enterprise; natural language → full-stack app |

### Brand / identity

| Tool | Status | Notes |
|------|--------|-------|
| LogoLoom (`@mcpware/logoloom`) | VERIFIED | Local MCP; SVG + brand kit (tool default file count is not AHTE doctrine) |
| Forge-Space/branding-mcp | PARTIAL | Design tokens / identity tooling |

### Infographics / charts

| Tool | Status | Notes |
|------|--------|-------|
| aizzaku/aiz-infographic | VERIFIED | Agent skill; HTML + PNG |
| Charta MCP / AntV MCP Server Chart | PARTIAL | Chart generation packages |

### Video

| Tool | Status | Notes |
|------|--------|-------|
| OpenMontage | VERIFIED | Agentic video studio; heavy setup; AGPL |
| Unofficial Google Flow MCPs | PARTIAL | Use existing Flow credits; UI-fragile; no official Google API |

### Business cards

| Tool | Status | Notes |
|------|--------|-------|
| SamurAIGPT/ai-business-card | VERIFIED | Open-source Next.js SaaS boilerplate |

---

## D. Runtime verification rule

If a tool is not listed here, or is listed as UNVERIFIED, an agent must emit
`[TOOL-SPEC UNVERIFIED: <tool> — assumed: <capability>]` before relying on it.

Before any paid generation, public deployment, or controlled-data upload:

1. verify the current official tool specification;
2. verify runtime availability;
3. verify authentication and secret-handling;
4. verify cost and approval;
5. verify data-retention and upload implications;
6. verify output licensing and provenance;
7. apply least privilege;
8. obtain explicit authorization.

External tool output counts, brand-kit file numbers, and third-party marketing
claims are **not** AHTE normative doctrine.
