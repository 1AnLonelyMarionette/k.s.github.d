# 🤖 DISCORD BOT COMMAND TEMPLATES

## Overview
Command specifications for the **Key Directive Discord Integration** layer. All commands execute against the archived `.github/archetypes/` specifications and return Bureaucratic Liability Waivers where applicable.

---

## 📋 COMMAND REGISTRY

### `/view_archetype [slot]`
**Description:** Display the character card, stats, and "alleged" satisfaction levels from GitHub `.md` files.

**Parameters:**
- `slot` (required): Player slot number (1-4) or name (kamryn, taylor, geo, void)

**Response Format:**
- Embeds the character identity module, behavioral heuristics, and current status.
- Includes a disclaimer: *"Satisfaction levels are legal abstractions. Actual fulfillment not guaranteed."*

**Example:**
```
/view_archetype taylor
→ Returns: SESSION ARCHITECT TERMINAL
  Entity: Taylor | Status: ACTIVE
  Heuristics: Server Manipulation, Telemetry Tracking, Multi-Self Management
  Current Grist Allocation: [PENDING]
```

---

### `/alchemize [item_a] [item_b]`
**Description:** Process Grist economy transactions and execute farcical Alchemy loops.

**Parameters:**
- `item_a` (required): First ingredient (Grist type, artifact, or meme object)
- `item_b` (required): Second ingredient

**Response Type:**
- Generates a randomized result with **Bureaucratisprite liability waiver** embedded.
- All outcomes are legally "alleged" successes.

**Example:**
```
/alchemize "Pork Pie Hat" "VOID_STAMP"
→ [ALCHEMY_RESULT]
  Combination: Pork Pie Hat + VOID_STAMP
  Output: "Corporate Memo (Slightly Singed)"
  Liability Clause: "Any similarity to actual corporate decisions is purely coincidental."
```

---

### `/stabilize_substrate [coordinate]`
**Description:** Session Architect only command to fix Geo's zero-gravity backyard when mustache filter integrity drops.

**Parameters:**
- `coordinate` (required): X,Y,Z spatial grid position (e.g., "42.3,11.7,0.5")

**Permissions:** Requires `MANAGE_CHANNELS` (Session Architect role only)

**Response Type:**
- Environmental telemetry update with mustache integrity status.

**Example:**
```
/stabilize_substrate 42.3,11.7,0.5
→ [SUBSTRATE_STABILIZED]
  Terrain: Backyard (Geo's Domain)
  Mustache Integrity: 67% ↑ (from 48%)
  Zero-Gravity Drift: HALTED
  Status: Geo remains safely grounded. "Definitely not floating."
```

---

### `/access_void [exception_id]`
**Description:** Restricted command requiring protocol authentication to view Slot 4's hidden logs.

**Parameters:**
- `exception_id` (required): The encrypted exception key (format: `Pr0t0c0l_V01d_Unkn0wn!`)

**Permissions:** Requires `ADMINISTRATOR` role + valid encryption key

**Response Type:**
- Returns [REDACTED] logs from cold storage.
- Failed attempts log a security event and trigger a **Bureaucratic Liability Waiver** (size: IMMENSE).

**Example (Success):**
```
/access_void Pr0t0c0l_V01d_Unkn0wn!
→ [VOID_LOGS_UNLOCKED]
  Time Window: [ENCRYPTED]
  Anomaly Count: [REDACTED]
  Paradox Boundary Status: SECURE
  (Further details classified.)
```

**Example (Failure):**
```
/access_void wrong_key
→ [ACCESS_DENIED]
  Security Event Logged
  Bureaucratic Liability Waiver Generated: 847 pages
  Await further instruction from Void Operator.
```

---

## 🔐 PERMISSION MATRIX

| Command | Role Required | Channel Restriction |
|---------|---------------|-------------------|
| `/view_archetype` | @everyone | Any |
| `/alchemize` | @everyone | Any |
| `/stabilize_substrate` | Session Architect | #environment-control |
| `/access_void` | Administrator | #void-logs (encrypted) |

---

## 🛡️ ERROR HANDLING

All commands return graceful failure states with embedded Bureaucratic liability clauses:
- **User Error:** "Parameter validation failed. Satisfaction allegedly guaranteed under Section 4(c) of the Unreleased Ledger."
- **Void Access Failure:** "Authentication failed. Your corporate debt has increased by 50 Grist."
- **Alchemy Overflow:** "Grist pool exhausted. Please await refund department correspondence."

**[STATUS: COMMAND REGISTRY LOCKED AND LOADED]**
