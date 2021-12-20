import discord
from discord.ext import commands
import youtube_dl


class music(commands.Cog):
    def __init__(self, client):
        self.client = client

    async def join_command(self, ctx):
        if ctx.author.voice is None:
            await ctx.send("Vous n'êtes pas dans un salon vocal !")
        else:
            voice_channel = ctx.author.voice.channel
            if ctx.voice_client is None:
                await voice_channel.connect()
                await ctx.send("Je me suis connecté avec succès !")
            else:
                await ctx.voice_client.move_to(voice_channel)
                await ctx.send("Je me suis connecté avec succès !")

    async def leave_command(self, ctx):
        await ctx.voice_client.disconnect()
        await ctx.send("Je me suis déconnecté avec succès !")

    async def play_command(self, ctx, url):
        if ctx.author.voice is None:
            await ctx.send("Vous n'êtes pas dans un salon vocal !")
        else:
            voice_channel = ctx.author.voice.channel
            if ctx.voice_client is None:
                await voice_channel.connect()
            else:
                await ctx.voice_client.move_to(voice_channel)
            ctx.voice_client.stop()
            FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
                              'options': '-vn'}
            YDL_OPTIONS = {'format': "bestaudio"}
            vc = ctx.voice_client

            with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
                info = ydl.extract_info(url, download=False)
                url2 = info['formats'][0]['url']
                source = await discord.FFmpegOpusAudio.from_probe(url2, **FFMPEG_OPTIONS)
                vc.play(source)
                await ctx.send("Musique en cours de lecture...")

    async def pause_command(self, ctx):
        ctx.voice_client.pause()
        await ctx.channel.send("Pause ⏸")

    async def resume_command(self, ctx):
        ctx.voice_client.resume()
        await ctx.channel.send("Lecture ⏯")

    async def stop_command(self, ctx):
        ctx.voice_client.stop()
        await ctx.channel.send("Musique stoppée !")

    @commands.command()
    async def join(self, ctx):
        await self.join_command(ctx)

    @commands.command()
    async def j(self, ctx):
        await self.join_command(ctx)

    @commands.command()
    async def leave(self, ctx):
        await self.leave_command(ctx)

    @commands.command()
    async def l(self, ctx):
        await self.leave_command(ctx)

    @commands.command()
    async def play(self, ctx, url):
        await self.play_command(ctx, url)

    @commands.command()
    async def p(self, ctx, url):
        await self.play_command(ctx, url)

    @commands.command()
    async def pause(self, ctx):
        await self.pause_command(ctx)

    @commands.command()
    async def resume(self, ctx):
        await self.resume_command(ctx)

    @commands.command()
    async def r(self, ctx):
        await self.resume_command(ctx)

    @commands.command()
    async def stop(self, ctx):
        await self.stop_command(ctx)

    @commands.command()
    async def s(self, ctx):
        await self.stop_command(ctx)


def setup(client):
    client.add_cog(music(client))