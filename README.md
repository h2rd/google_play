simple-googleplay
=================

simple google play spider

Setup
-----

```
pip install git+https://github.com/h2rd/google_play
```

Example
-------

This is example which return info about app

```python
python
>>> from google_play import app
>>> app('com.twitter.android')
{'category': 'Social',
 'rating': 4.0,
 'rewievs': 2045719,
 'description': u"Twitter is the best way to connect, express yourself and discover...",
 'package_name': 'com.twitter.android',
 'title': 'Twitter',
 'url': 'https://play.google.com/store/apps/details?id=com.twitter.android&hl=en',
 'price': '0',
 'installs': '100,000,000 - 500,000,000',
 'developer_email': 'android-support@twitter.com',
 'developer_name': 'Twitter, Inc.',
 'version': 'Varies with device',
 'developer_website': 'https://support.twitter.com/articles/20169915',
 'images': [
 'https://lh6.ggpht.com/uUslqIsgo-3u38k_R-8rQYBNZvseBNAuwdcuuRfwgWiMpWfe5NFBkMUf758e4p7USNE=h310', 
 'https://lh4.ggpht.com/PplZu3Dfy_8Lqgr8lNWCMxd43jHqgTwaBdWwqPnVjmY7J93xrOgTKaB3jITsUafRuX0=h310', 
 'https://lh6.ggpht.com/udwukvUDYgnNOXwFqOXJ2lxZ3jghInCGD8RhSMuz2vtZ-GCI05nZpgxAnNG8IdOPyuXU=h310', 
 'https://lh5.ggpht.com/umqC1YkziBLMkVUOK1AIyeKQ21XenVPHKcuyQ-0cF_d-iWu0_qzUTmNYSr0-mQD1QBG8=h310', 
 'https://lh3.ggpht.com/KvS39jtOqDgg6dvhwnPOG6ut_CryiErqNhbAI3lMcmyrgaqvkVF7KkY8iul1KFRp2Rgg=h310', 
 'https://lh6.ggpht.com/LNrJyrT6qIZWnT3U_owhgsIALL5MKwbRg5-RLA-Vq7t2ClYDCp-VsaLw60oVDvn4pgk=h310', 
 'https://lh5.ggpht.com/eQlbgeBhehtnexZVlFXZynfmtJ88UeBoy28yUskYJohqNVc_-mtMHcJUikQrBLn8lIaP=h310', 
 'https://lh6.ggpht.com/GI2phoWIHPh3rsB3htlaozGpWSCniOXKvRlZHgcT_937fBPHhrXEhbNbsn3rcgpaHUk=h310'], 
 'logo': 'https://lh3.ggpht.com/lSLM0xhCA1RZOwaQcjhlwmsvaIQYaP3c5qbDKCgLALhydrgExnaSKZdGa8S3YtRuVA=w300',
 'android': 'Varies with device',,
 'similar': ['com.handmark.tweetcaster', 'com.instagram.android', 'com.levelup.touiteur', 'com.facebook.katana',
 'com.handlerexploit.tweedle', 'com.echofon', 'com.twidroid', 'com.sgiggle.production',
 'net.janesoft.janetter.android.free', 'com.instachat.android', 'jp.jig.jigtwi.android', 'jp.ne.biglobe.twipple',
 'com.seesmic', 'com.innovatty.followersplus', 'com.dotsandlines.carbon', 'com.hootsuite.droid.full'],
 'size': 'Varies with device'}

# return first 24 developer apps
>>> from google_play import developer
>>> developer('Zynga')
['com.zynga.words', 'com.zynga.livepoker', 'com.zynga.scramble', 'com.zynga.gswf',
 'com.zynga.hanging', 'com.zynga.castlevillelegends', 'com.zynga.draw2.googleplay.free', 'com.zynga.matching', 'com.zynga.zjayakashi',
 'com.zynga.bubblesafari.ent', 'com.zynga.scramble.paid', 'com.zynga.fatpebble.clayjam', 'com.zynga.zombiesmash', 'com.zynga.rwf.googleplay',
 'com.c4mprod.ezcodescanner', 'com.zynga.gems.googleplay', 'com.zynga.warofthefallen', 'com.areacode.drop7.rev1', 'com.zynga.gswfpaid',
 'com.zynga.draw2.googleplay.paid', 'com.zynga.inis.edentogreen', 'com.zynga.words_intl' ]

# returns search apps
>>> from google_play import search
>>> search('Zynga')
['com.zynga.livepoker', 'com.zynga.gswf', 'com.zynga.castlevillelegends', 'com.zynga.digitallegends.respawnables',
 'com.areacode.drop7.rev1', 'com.zynga.draw2.googleplay.free', 'com.appmakr.app388899', 'com.zynga.zyngapoker1',
 'com.zynga.rwf.googleplay', 'com.zynga.scramble', 'com.zynga.bubblesafari.ent', 'com.zynga.fatpebble.clayjam',
 'com.zynga.hanging', 'com.zynga.gems.googleplay', 'com.c4mprod.ezcodescanner', 'com.zynga.words', 'com.zynga.matching',
 'com.zynga.zjayakashi', 'com.dreamstep.wTheFacebookandZyngaPodcast', 'com.appsupdatestore.topgames', 'com.igg.pokerdeluxe',
 'com.zynga.warofthefallen', 'com.omgpop.dstfree', 'com.dragonplay.slotcity' ]

# get leaderboard free and paid apps by category
>>> from google_play import leaderboard, FREE, PAID
>>> leaderboard(FREE, 'game')
['com.seriouscorp.clumsybird', 'com.turbochilli.unrollme', 'com.kiloo.subwaysurf', 'com.lego.city.my_city',
 'com.outfit7.mytalkingtomfree', 'com.fingersoft.hillclimb', 'air.ru.pragmatix.wormix.mobile', 'air.com.socialquantum.atlantis',
 'com.gameloft.android.ANMP.GloftIAHM', 'com.gameloft.android.ANMP.GloftDMHM', 'me.pou.app',
 'com.smilerlee.jewels', 'com.halfbrick.fruitninjafree', 'com.warnerbros.game300ROE', 'com.KuninNikolay.FrozenBridges.Free',
 'com.rovio.angrybirds', 'com.byril.seabattle', 'com.outfit7.jigtyfree', 'com.supercell.hayday', 'com.vg.MonsterDashHillRacer',
 'com.rovio.angrybirdsgo', 'com.fgol.HungrySharkEvolution', 'com.zeptolab.ctr.ads', 'com.ea.games.r3_row']
>>> leaderboard(PAID, 'game')
['com.mojang.minecraftpe', 'se.feomedia.quizkampen.de.premium', 'com.FireproofStudios.TheRoom2', 'com.FireproofStudios.TheRoom',
 'com.gameloft.android.ANMP.GloftM4HM', 'com.worms2armageddon.app', 'com.popcap.pvz_row', 'com.ninjakiwi.bloonstd5',
 'com.candyrufusgames.survivalcraft', 'com.disney.WMW', 'com.bubblezapgames.supergnes', 'com.halfbrick.fruitninja',
 'com.astragon.cs2014', 'com.tangram3D.WinterSportsFull', 'com.flukedude.impossiblegame', 'com.ea.games.nfs13_row',
 'com.rockstargames.gtasa', 'com.gameloft.android.ANMP.GloftA7HM', 'com.zeptolab.ctr.paid', 'com.fastemulator.gba',
 'com.hemispheregames.osmos', 'com.ironhidegames.android.kingdomrushfrontiers', 'com.DefiantDev.SkiSafari', 'com.rockstargames.gtavc']
```
