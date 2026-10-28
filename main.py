from dotenv import load_dotenv
from os import getenv
import discord
from discord.ext import commands

from Mot_Mystere import main, MotDuJour
from Date import est_mercredi

load_dotenv("TOKEN.env")
TOKEN = getenv("TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

#Lancement
@bot.event
async def on_ready():
    print(f"awdwadawdawd caillou {bot.user}")
    await bot.tree.sync()

#Bouton roue du gambling
class RoueDuGamblingView(discord.ui.View):
    @discord.ui.button(label="Cliquez-moi", style=discord.ButtonStyle.green)
    async def trouner_la_roue(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("You are VERY gay")

#Commande !rouedugambling
@bot.tree.command(name="rouedugambling", description="Tourne la roue du Gambling")
async def roue_du_gambling(interaction: discord.Interaction):
    await interaction.response.send_message("Choisis :", view=RoueDuGamblingView())

#Formulaire MotMystere
class MotMystereModal(discord.ui.Modal, title="Mot Mystère"):
    mot = discord.ui.Label(
        text=f"Il faut trouver un mot de : {len(MotDuJour)} lettres",
        #description="",
        component=discord.ui.TextInput(
            placeholder="Écris ton mot ici...",
            min_length=len(MotDuJour),
            max_length=len(MotDuJour),
        ),
    )
    #Rep Formulaire MotMystere
    async def on_submit(self, interaction: discord.Interaction):
        proposition = self.mot.component.value.upper()
        ans=main(proposition)
        if ans == ("✅"*len(MotDuJour)):
            await interaction.response.send_message(f"Tu as proposé : {proposition}\n {ans}\n GG tu as trouvé le mot du jour",
                                                    ephemeral = True)
            await interaction.followup.send(f"{interaction.user.mention} a trouvé la bonne réponse !!")
        else:
            await interaction.response.send_message(f"Tu as proposé : {proposition}\n {ans}",
                                                    view=RejouerView(),
                                                    ephemeral = True,
                                                    )
            #await interaction.followup.send("Choisis :", view=RejouerView())

#Bouton rejouer
class RejouerView(discord.ui.View):
    @discord.ui.button(label="Rejouer", style=discord.ButtonStyle.green)
    async def rejouer(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_modal(MotMystereModal())

#Commande !motmystere
@bot.tree.command(name="motmystere", description="Essaye de deviner le Mot Mystère")
async def motmystere(interaction: discord.Interaction):
    await interaction.response.send_modal(MotMystereModal())

# Commande !mercredi
@bot.tree.command(name="mercredi", description="Demande a Doji si il est l'heure de sortir les poubelles")
async def mercredi(interaction: discord.Interaction):
    if est_mercredi():
        await interaction.response.send_message(f"Nous sommes mercredi, ça tombe bien c'est l'heure de sortir les poubelles",
                                                file= discord.File("Mercredi.gif"))
    else:
        await interaction.response.send_message("Nous ne sommes pas mercredi,ce n'est pas le moment de sortir les poubelles")


bot.run(TOKEN)