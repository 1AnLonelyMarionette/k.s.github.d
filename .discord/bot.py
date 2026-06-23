import discord
from discord.ext import commands
from discord import app_commands
import os
from dotenv import load_dotenv
from pathlib import Path

# Load environment variables from .env file
load_dotenv()

# ==========================================
# SYSTEM CORE DATA (SESSION MATRIX)
# ==========================================
SESSION_DATA = {
    "Module": "Sburb_Session_4Player_Core",
    "Version": "1.0.0_STEAMPECK_OPTIMIZED",
    "Roster": [
        {
            "UID": "P1_KAMRYN",
            "Display_Name": "Kamryn",
            "Class_Aspect": "Satisfaction Guaranteed",
            "Status": "STABLE_RENDERING",
            "Handle": "GG",
            "Role": "Client_Chain_Root"
        },
        {
            "UID": "P2_TAYLOR",
            "Display_Name": "Taylor",
            "Class_Aspect": "Prince of Heart",
            "Status": "ACTIVE_NARRATOR",
            "Handle": "TT",
            "Role": "Session_Architect"
        },
        {
            "UID": "P3_GEO",
            "Display_Name": "Geo (Definitely Not John)",
            "Class_Aspect": "Breath-adjacent (allegedly)",
            "Status": "ACTIVE_MODIFICATION",
            "Handle": "DG",
            "Role": "Terrain_Analyst",
            "Mustache_Integrity": "42%"
        },
        {
            "UID": "P4_VOID",
            "Display_Name": "[REDACTED]",
            "Class_Aspect": "[CLASSIFICATION LEVEL EXCEEDED]",
            "Status": "STABLE_BLIND_SPOT",
            "Handle": "EE",
            "Role": "Void_Operator"
        }
    ],
    "Pesterlog_Buffer": [],
    "Grist_Pool": 0,
    "Session_Started": False
}

# ==========================================
# INITIALIZATION
# ==========================================
class ANClient(commands.Bot):
    """Main Discord bot client with custom intents and sync behavior."""
    
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        intents.members = True
        super().__init__(command_prefix="!", intents=intents)

    async def setup_hook(self):
        """Sync slash commands globally on bot startup."""
        try:
            synced = await self.tree.sync()
            print(f"✓ AN TREE: {len(synced)} SLASH COMMANDS SYNCHRONIZED GLOBALLY.")
        except Exception as e:
            print(f"✗ SYNC ERROR: {e}")

bot = ANClient()

@bot.event
async def on_ready():
    """Log when bot is ready and change status."""
    activity = discord.Activity(type=discord.ActivityType.playing, name="Sburb: Session 4 Player")
    await bot.change_presence(activity=activity)
    print(f"\n{'='*50}")
    print(f"✓ AN MASTER LOG: {bot.user.name} IS LIVE ON STEAMOS")
    print(f"✓ Guild(s) connected: {len(bot.guilds)}")
    print(f"✓ Bot ID: {bot.user.id}")
    print(f"{'='*50}\n")

# ==========================================
# PREFIX COMMANDS (TEXT BACKUP INTERFACE)
# ==========================================
@bot.command(name="session", help="View active session roster and statuses.")
async def show_session(ctx):
    """Display all active players and their current status."""
    embed = discord.Embed(
        title="⚔️ ACTIVE SESSION ROSTER",
        color=discord.Color.purple(),
        description="Player statuses in the current Sburb instance."
    )
    
    for idx, node in enumerate(SESSION_DATA["Roster"], 1):
        status_emoji = "🟢" if "ACTIVE" in node["Status"] else "🟡" if "STABLE" in node["Status"] else "🔴"
        mustache_note = f" | Mustache: {node['Mustache_Integrity']}" if "Mustache_Integrity" in node else ""
        
        field_value = f"**UID:** {node['UID']}\n**Aspect:** {node['Class_Aspect']}\n**Handle:** {node['Handle']}\n**Status:** {status_emoji} {node['Status']}{mustache_note}"
        embed.add_field(name=f"Player {idx}", value=field_value, inline=False)
    
    embed.set_footer(text="Use !pester [handle] [message] to log Pesterlog entries.")
    await ctx.send(embed=embed)

@bot.command(name="pester", help="Add a message to the Pesterlog buffer.")
async def pester_log(ctx, handle: str, *, message: str):
    """Log a Pesterlog-style message from a player."""
    log_entry = f"[{handle.upper()}] {message}"
    SESSION_DATA["Pesterlog_Buffer"].append(log_entry)
    
    # Keep buffer at reasonable size
    if len(SESSION_DATA["Pesterlog_Buffer"]) > 20:
        SESSION_DATA["Pesterlog_Buffer"].pop(0)
    
    embed = discord.Embed(
        title="💬 PESTERLOG UPDATED",
        description=f"`{log_entry}`",
        color=discord.Color.green()
    )
    embed.set_footer(text=f"Buffer size: {len(SESSION_DATA['Pesterlog_Buffer'])}/20")
    await ctx.send(embed=embed)

@bot.command(name="dump", help="Display the current Pesterlog buffer.")
async def dump_buffer(ctx):
    """Show all recent Pesterlog entries."""
    if not SESSION_DATA["Pesterlog_Buffer"]:
        await ctx.send("**[PESTERLOG EMPTY]** No entries recorded yet.")
        return
    
    formatted_buffer = "\n".join(SESSION_DATA["Pesterlog_Buffer"])
    embed = discord.Embed(
        title="📋 RAW SYSTEM DATA DUMP",
        description=f"```\n{formatted_buffer}\n```",
        color=discord.Color.blue()
    )
    await ctx.send(embed=embed)

@bot.command(name="grist", help="Check current Grist pool balance.")
async def check_grist(ctx):
    """Display current Grist economy status."""
    embed = discord.Embed(
        title="💎 GRIST POOL STATUS",
        description=f"Current Balance: **{SESSION_DATA['Grist_Pool']} Grist**",
        color=discord.Color.gold()
    )
    await ctx.send(embed=embed)

# ==========================================
# SLASH COMMANDS (PRIMARY INTERFACE)
# ==========================================
@bot.tree.command(name="view_archetype", description="Retrieve character archetype and current status.")
@app_commands.describe(slot="The player slot (1-4) to retrieve.")
async def view_archetype(interaction: discord.Interaction, slot: int):
    """Fetch and display a player's archetype data from GitHub specs."""
    if slot < 1 or slot > 4:
        await interaction.response.send_message(
            "❌ **AN ERROR:** Out of session bounds. Choose slots 1-4.",
            ephemeral=True
        )
        return
    
    if slot == 4:
        await interaction.response.send_message(
            "🔒 **AN ERROR:** Parameter unreadable. Slot 4 is locked in cold storage. Access denied.",
            ephemeral=True
        )
        return
    
    node = SESSION_DATA["Roster"][slot - 1]
    embed = discord.Embed(
        title=f"📋 ARCHETYPE: SLOT {slot:02d} - {node['Display_Name'].upper()}",
        color=discord.Color.blue(),
        description=f"**UID:** {node['UID']}"
    )
    
    embed.add_field(name="Class/Aspect", value=node["Class_Aspect"], inline=True)
    embed.add_field(name="Handle", value=node["Handle"], inline=True)
    embed.add_field(name="Role", value=node["Role"].replace("_", " "), inline=True)
    embed.add_field(name="Status", value=node["Status"], inline=False)
    
    if "Mustache_Integrity" in node:
        embed.add_field(name="⚠️ CRITICAL SYSTEM", value=f"Mustache Integrity: {node['Mustache_Integrity']}", inline=False)
    
    await interaction.response.send_message(embed=embed)

@bot.tree.command(name="alchemize", description="Combine two items using Alchemy.")
@app_commands.describe(
    item_a="First ingredient or artifact",
    item_b="Second ingredient or artifact"
)
async def alchemize(interaction: discord.Interaction, item_a: str, item_b: str):
    """Process an Alchemy combination and return a theoretical result."""
    embed = discord.Embed(
        title="⚗️ ALCHEMY RESULT",
        color=discord.Color.green(),
        description=f"Combining: `{item_a}` + `{item_b}`"
    )
    
    embed.add_field(
        name="Output",
        value=f"[Theoretical hybrid object generated]",
        inline=False
    )
    
    embed.add_field(
        name="Bureaucratisprite Liability Notice",
        value="*Any similarity to actual alchemical results is purely coincidental. Satisfaction allegedly guaranteed.*",
        inline=False
    )
    
    embed.set_footer(text="Grist cost: [PENDING]")
    await interaction.response.send_message(embed=embed)

@bot.tree.command(name="stabilize_substrate", description="Correct coordinate grids and environmental drift.")
@app_commands.describe(coordinate="Targeted Zone ID (e.g., ZONE_02)")
@app_commands.checks.has_permissions(administrator=True)
async def stabilize_substrate(interaction: discord.Interaction, coordinate: str):
    """Execute environmental stabilization (Architect only)."""
    embed = discord.Embed(
        title="🔧 SUBSTRATE STABILIZATION ENGAGED",
        color=discord.Color.orange(),
        description=f"**Zone:** {coordinate}"
    )
    
    embed.add_field(
        name="Architect Override",
        value="Environmental restructuring in progress...",
        inline=False
    )
    
    embed.add_field(
        name="Status",
        value="🟢 Geo's mustache filter integrity: +15%\n🟢 Zero-gravity drift: COMPENSATED\n🟢 Substrate coherence: STABILIZED",
        inline=False
    )
    
    await interaction.response.send_message(embed=embed)

@bot.tree.command(name="access_void", description="Retrieve classified Void Operator logs.")
@app_commands.describe(exception_id="The encrypted authentication key")
@app_commands.checks.has_permissions(administrator=True)
async def access_void(interaction: discord.Interaction, exception_id: str):
    """Access Slot 4's restricted exception logs (Void Operator only)."""
    if exception_id == "Pr0t0c0l_V01d_Unkn0wn!":
        embed = discord.Embed(
            title="🔓 VOID_LOGS_UNLOCKED",
            color=discord.Color.dark_red(),
            description="**[CLASSIFIED] data stream accessed.**"
        )
        
        embed.add_field(
            name="Status",
            value="🔴 [REDACTED]\n🔴 [REDACTED]\n🔴 [REDACTED]",
            inline=False
        )
        
        embed.set_footer(text="Further details locked at the highest operational level.")
        await interaction.response.send_message(embed=embed, ephemeral=True)
    else:
        embed = discord.Embed(
            title="❌ ACCESS_DENIED",
            color=discord.Color.red(),
            description="Authentication failed. Invalid encryption key."
        )
        
        embed.add_field(
            name="Consequence",
            value="Your corporate debt has increased by 50 Grist.\nBureaucratic Liability Waiver: 847 pages generated.",
            inline=False
        )
        
        await interaction.response.send_message(embed=embed, ephemeral=True)

# ==========================================
# ERROR HANDLING
# ==========================================
@view_archetype.error
@alchemize.error
@stabilize_substrate.error
@access_void.error
async def command_error(interaction: discord.Interaction, error: app_commands.AppCommandError):
    """Handle command errors gracefully."""
    if isinstance(error, app_commands.MissingPermissions):
        await interaction.response.send_message(
            "❌ **PERMISSION DENIED:** You lack the necessary clearance for this operation.",
            ephemeral=True
        )
    else:
        await interaction.response.send_message(
            f"❌ **ERROR:** {str(error)}",
            ephemeral=True
        )

# ==========================================
# EXECUTION
# ==========================================
if __name__ == "__main__":
    TOKEN = os.getenv('DISCORD_BOT_TOKEN')
    if not TOKEN:
        print("\n" + "="*50)
        print("❌ CRITICAL ERROR: DISCORD_BOT_TOKEN not set")
        print("="*50)
        print("\nCreate a .env file in this directory with:")
        print("  DISCORD_BOT_TOKEN=your_actual_token_here")
        print("\nOr set it as an environment variable.\n")
        exit(1)
    
    print("\n🚀 Starting AN Bot...\n")
    bot.run(TOKEN)
