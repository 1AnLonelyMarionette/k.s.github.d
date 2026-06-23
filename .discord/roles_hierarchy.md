# 🔐 DISCORD ROLE HIERARCHY & PERMISSION MATRIX

## Overview
Hierarchical structure for the **Key Directive Discord Integration** layer. All roles cascade from administrative root down through client chain layers, with specific permission gates for system-critical commands.

---

## 📊 ROLE HIERARCHY (Top → Bottom)

### TIER 0: ROOT OPERATOR
**Role:** `@void_operator`
- **Permissions:** ADMINISTRATOR (unrestricted access)
- **Discord Perms:** Manage Roles, Manage Channels, Manage Messages, Kick Members, Ban Members
- **Bot Commands:** All commands (including `/access_void`)
- **Visibility:** Hidden from standard role lists; operates via side channels only

---

### TIER 1: SESSION ARCHITECT
**Role:** `@session_architect` (Taylor)
- **Permissions:** Server management, channel deployment, telemetry oversight
- **Discord Perms:** Manage Channels, Manage Roles (limited), Manage Messages, Mute Members
- **Bot Commands:** 
  - `/view_archetype` (all slots)
  - `/alchemize` (full)
  - `/stabilize_substrate` (exclusive)
  - `/access_void` (restricted — requires approval)
- **Channel Access:** `#environment-control`, `#telemetry-logs`, `#architecture-planning`
- **Authority Over:** Terrain Analysts, Client Chain members

---

### TIER 2: TERRAIN ANALYST
**Role:** `@terrain_analyst` (Geo)
- **Permissions:** Resource management, substrate verification, architectural consultation
- **Discord Perms:** Manage Messages, View Audit Log
- **Bot Commands:**
  - `/view_archetype` (self + Kamryn only)
  - `/alchemize` (limited — substrate-focused items only)
  - `/stabilize_substrate` (read-only telemetry)
- **Channel Access:** `#terrain-reports`, `#resource-tracking`, `#architecture-planning`
- **Authority Over:** Client Chain members

---

### TIER 3: CLIENT CHAIN (General Members)
**Role:** `@satisfaction_guaranteed` (Kamryn + general users)
- **Permissions:** Basic command access, resource queries
- **Discord Perms:** Send Messages, View Channels, Read Message History
- **Bot Commands:**
  - `/view_archetype` (Kamryn only)
  - `/alchemize` (restricted item list)
- **Channel Access:** `#general`, `#grist-exchange`, `#alchemize-results`
- **Authority Over:** None

---

## 🔒 PERMISSION GATE MATRIX

| Command | Void Operator | Session Architect | Terrain Analyst | Client Chain |
|---------|---------------|-------------------|-----------------|--------------|
| `/view_archetype` | ✅ All | ✅ All | ✅ Self/Kamryn | ✅ Kamryn only |
| `/alchemize` | ✅ Unrestricted | ✅ Full | ✅ Limited | ✅ Limited |
| `/stabilize_substrate` | ✅ Full | ✅ Full (exclusive) | ⚠️ Read-only | ❌ No Access |
| `/access_void` | ✅ Full | ⚠️ Approval Required | ❌ No Access | ❌ No Access |

---

## 📍 CHANNEL STRUCTURE & ACCESS CONTROL

### Public Channels (All Members)
- `#general` — Session announcements, general discussion
- `#grist-exchange` — Grist economy trading and queries
- `#alchemize-results` — Alchemy output logs and item combinations

### Restricted Channels (Tier 1+)
- `#environment-control` — Architecture and substrate commands (Session Architect only)
- `#telemetry-logs` — Real-time system state, entry status updates
- `#architecture-planning` — Long-term structural planning and collaboration

### Highly Restricted Channels (Tier 0)
- `#void-logs` — Encrypted Void Operator logs and anomaly tracking
- `#system-exceptions` — Critical error states and paradox boundary alerts

---

## 🔑 ROLE ASSIGNMENT PROTOCOL

1. **Root Initialization:** Void Operator assigned manually by repository admin.
2. **Tier 1 (Session Architect):** Assigned by Void Operator; requires `M0rb1d_Arch1t3ct_N3t!` authentication.
3. **Tier 2 (Terrain Analyst):** Assigned by Session Architect; requires `F4k3_Must4ch3_D1sgu1s3!` authentication.
4. **Tier 3 (Client Chain):** Auto-assigned on server join; defaults to `@satisfaction_guaranteed` role.

---

## ⚠️ ESCALATION & CONFLICT RESOLUTION

- **Permission Disputes:** Session Architect arbitrates within their authority; escalate to Void Operator if blocked.
- **Void Access Attempts:** All failed `/access_void` attempts logged to `#system-exceptions` with automatic penalty (50 Grist deduction).
- **Role Revocation:** Only Void Operator can strip roles; initiates 24-hour audit window before enforcement.

**[STATUS: HIERARCHY LOCKED AND HIERARCHICALLY ENFORCED]**
