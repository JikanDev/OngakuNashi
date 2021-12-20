import discord
from discord.ext import commands


class basic(commands.Cog):
    def __init__(self, client):
        self.client = client

    def help_command(self, ctx):
        embed = discord.Embed(
            title='Voici toutes mes commandes :',
            colour=discord.Colour.blue()
        )
        embed.set_footer(text='Ongaku Nashi by Jikan#2712')
        embed.set_thumbnail(
            url='https://cdn.discordapp.com/avatars/778913704292253746/5984efee34968be7ebd8456da7a1dcb7.webp')
        embed.add_field(name='join ou j', value='Te permet de me faire rejoindre ton salon vocal.', inline=False)
        embed.add_field(name='leave ou l', value='Te permet de me faire quitter ton salon vocal.', inline=False)
        embed.add_field(name='play ou p', value='Te permet de me faire jouer une musique de YouTube.', inline=False)
        embed.add_field(name='pause', value='Te permet de mettre en pause la musique actuelle.', inline=False)
        embed.add_field(name='resume ou r', value='Te permet de reprendre la musique actuelle.', inline=False)
        embed.add_field(name='stop ou s', value='Te permet de complètement stopper la musique actuelle.', inline=False)

        return ctx.send(embed=embed)

    @commands.command()
    async def help(self, ctx):
        await self.help_command(ctx)

    @commands.command()
    async def h(self, ctx):
        await self.help_command(ctx)


def setup(client):
    client.add_cog(basic(client))