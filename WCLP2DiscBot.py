from discord.ext.commands import Bot
from bs4 import BeautifulSoup as BeautifulSoup
import requests
BCommand = '!'
BTok = 'NTAxNTM4ODg4OTIyNDMxNDg4.Dqa3nw.WqmL-hw_QCqwmSCANhJuJWFyFUQ'

client = Bot(command_prefix=BCommand)

@client.command(name='wclp')
async def wclparser():
	res = ("Welcome To WarcraftLogs Parser! For A List Of Commands Type: [wclp_help]")
	await client.say(res)
@client.command(name='wclp_help')
async def wclhelp():
	res2 = ("For Commands You Can Type [wclp_CHARCTERNAME_REALM_CLASS_SPECILIZATION_DIFFICULTY")
	await client.say(res2)
@client.command()
async def wclp_allstar(name1, server, class2, specin, dif1):
	class1 = str(class2)
	special = str(specin)
	difficulty = str(dif1)
	name2 = str(name1)
	realm = str(server)
	if class1.lower() in ['dk', 'death knight']:
		class1 = "DeathKnight/"
		if special.lower() in ['blood', 'bld', '1']:
			special = "Blood"
		if special.lower() in ['unholy', 'unhly', '2']:
			special = "Unholy"
		if special.lower() in ['frost', 'frst', '3']:
			special = "Frost"
	if class1.lower() in ['dh', 'demon hunter']:
		class1 = "DemonHunter/"
		if special.lower() in ['vengeance', 'vengence', 'vengance', 'veng', '1']:
			special = "Vengeance"
		if special.lower() in ['havoc', 'hav' '2']:
			special = "Havoc"
	if class1.lower() in ['druid', 'drud']:
		class1 = "Druid/"
		if special.lower() in ['balance', 'boomkin', 'boomy', '4']:
			special = "Balance"
		if special.lower() in ['feral', 'shitrogue', '3']:
			special = "Feral"
		if special.lower() in ['restoration', 'resto', 'rest' '2']:
			special = "Restoration"
		if special.lower() in ['guardian', 'bear' '1']:
			special = "Guardian"
	if class1.lower() in ['hunter', 'hunt']:
		class1 = "Hunter/"
		if special.lower() in ['beast master', 'bm', 'beastmaster', 'beast mastery', '1']:
			special = "Beast Mastery"
		if special.lower() in ['mm', 'marksmanship', 'marks', 'marksman', '2']:
			special = "Marksmanship"
		if special.lower() in ['survival', 'surv', '3']:
			special = "Survival"
	if class1.lower() in ['mage', 'mag']:
		class1 = "Mage/"
		if special.lower() in ['arcane', 'arc', 'cane', '1']:
			special = "Arcane"
		if special.lower() in ['fire', '3']:
			special = "Fire"
		if special.lower() in ['frost', 'frosty', 'frst' '2']:
			special = "Frost"
	if class1.lower() in ['monk', 'mnk']:
		class1 = "Monk/"
		if special.lower() in ['bm', 'brew', 'brewmaster', '1']:
			special = "Brewmaster"
		if special.lower() in ['mist', 'weaver', 'mistweaver', 'resto', '2']:
			special = "Mistweaver"
		if special.lower() in ['ww']:
			special = "Windwalker"
	if class1.lower() in ['paladin', 'pally']:
		class1 = "Paladin/"
		if special.lower() in ['holy', '1']:
			special = "Holy"
		if special.lower() in ['protection', 'prot' '2']:
			special = "Protection"
		if special.lower() in ['retribution', 'ret', '3']:
			special = "Retribution"
	if class1.lower() in ['priest', 'prst']:
		class1 = "Priest/"
		if special.lower() in ['holy', '2']:
			special = "Holy"
		if special.lower() in ['discipline', 'disc', '1']:
			special = "Discipline"
		if special.lower() in ['shadow', '3']:
			special = "Shadow"
	if class1.lower() in ['rogue', 'rouge', 'rog']:
		class1 = "Rogue/"
		if special.lower() in ['ass', 'assas', 'assass', 'assassination', '1']:
			special = "Assassination"
		if special.lower() in ['outlaw' 'combat' '2']:
			special = "Outlaw"
		if special.lower() in ['subtlety', 'sub', '3']:
			special = "Subtlety"
	if class1.lower() in ['shaman', 'shammy', 'sham']:
		class1 = "Shaman/"
		if special.lower() in ['ele', 'elemental', '1']:
			special = "Elemental"
		if special.lower() in ['resto', 'restoration', '2']:
			special = "Restoration"
		if special.lower() in ['enhance', 'enhancement', 'ehanc', '3']:
			special = "Enhancement"
	if class1.lower() in ['warlock', 'wl']:
		class1 = "Warlock/"
		if special.lower() in ['affy', 'affliction', 'aff' '1']:
			special = "Affliction"
		if special.lower() in ['destro', 'dest', 'destruction', '2']:
			special = "Destruction"
		if special.lower() in ['demon', 'demonology', '3']:
			special = "Demonology"
	if class1.lower() in ['warrior', 'war']:
		class1 = "Warrior/"
		if special.lower() in ['arms', '1']:
			special = "Arms"
		if special.lower() in ['fury', 'cudfed', '2']:
			special = "Fury"
		if special.lower() in ['prot', 'protection', '3']:
			special = "Protection"
	if difficulty.lower() in ['m', 'mythic']:
		difficulty = "/5/20/1/"
	if difficulty.lower() in ['h', 'heroic']:
		difficulty = "/4/10/1/"
	if difficulty.lower() in ['n', 'normal']:
		difficulty = "/3/10/1/"
	pag = 1
	page = ("page=" + str(pag))
	jp = "https://www.warcraftlogs.com/zone/rankings/table/19/dps/-1"
	ul = jp + difficulty + class1 + special + "/0/0/1/0/?search=&" + page
	a = requests.get(ul)
	soup = BeautifulSoup(a.text, "html.parser")
	b = soup.find_all('td', {'class': 'rank'})
	c = []
	r = []
	g = []
	for search in b:
		d = (search.text.split())
		c.append(d)
	for search2 in range(len(c)):
		r.extend(c[search2])
		if realm in c[search2]:
			g.append(c[search2])
		if name2 in c[search2]:
			e = search2
	if name2 in r:
		for tidal in c[e + 2: 99]:
			if realm in tidal:
				g.remove(tidal)
		for search3 in c[0: e + 1]:
			if name2 in search3:
				await client.say("Looks Like I Found You! >>>" + str(search3) + "<<<")
		await client.say("It Looks As If You Are Rank " + (str(len(g))) + " On Your Realm " + realm + "!")
	if name2 not in r:
		while name2 not in r:
			pag += 1
			page = ("page=" + str(pag))
			jp = "https://www.warcraftlogs.com/zone/rankings/table/19/dps/-1"
			ul = jp + difficulty + class1 + special + "/0/0/1/0/?search=&" + page
			a = requests.get(ul)
			soup = BeautifulSoup(a.text, "html.parser")
			b = soup.find_all('td', {'class': 'rank'})
			c = []
			r = []
			for search in b:
				d = (search.text.split())
				c.append(d)
			for search2 in range(len(c)):
				r.extend(c[search2])
				if realm in c[search2]:
					g.append(c[search2])
				if name2 in c[search2]:
					e = search2
			if name2 in r:
				for tidal in c[e + 2: 99]:
					if realm in tidal:
						g.remove(tidal)
				for search3 in c[0: e + 1]:
					if name2 in search3:
						await client.say("Looks Like I Found You! >>>" + str(search3) + "<<<")
				await client.say("It Looks As If You Are Rank " + (str(len(g))) + " On Your Realm " + realm + "!")
			if pag > 20:
				break
			if pag in [20]:
				await client.say("Sorry It Looks Like We Cloudn't Find You Through 20 Pages :(")

client.run(BTok)