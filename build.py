#!/usr/bin/env python3
# Generator voor ea-autocleaning.nl - onafhankelijke kennisgids over autoreiniging en detailing.
import os, json, html, hashlib
def _ver(p):
    try: return hashlib.md5(open(os.path.join(os.path.dirname(__file__),p),'rb').read()).hexdigest()[:8]
    except Exception: return "1"
BASE="https://ea-autocleaning.nl"; SITE="EA Autocleaning"; EMAIL="info@ea-autocleaning.nl"
AUTEUR="Erik Aalders"; AUTEUR_ROL="Redacteur autoverzorging"
SRC=os.path.dirname(__file__); OUT=os.path.join(SRC,"site"); CSS_VER=_ver("assets/css/style.css")
def esc(s): return html.escape(str(s), quote=True)
DISC="Werkwijzen verschillen per lak, leeftijd en staat van een auto. Bij twijfel over een aanpak is een proefstuk op een onopvallende plek of het inschakelen van een vakman de veiligste route."

IC={
 "check":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"/></svg>',
 "arrow":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg>',
 "mail":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 7-10 6L2 7"/></svg>',
 "doc":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M7 21a4 4 0 0 0 4-4c0-3-4-9-4-9s-4 6-4 9a4 4 0 0 0 4 4z"/><path d="M14 4h7v7"/><path d="M21 4l-8 8"/></svg>',
 "scale":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 13l2-5a3 3 0 0 1 3-2h8a3 3 0 0 1 3 2l2 5"/><path d="M3 13h18v4H3z"/><circle cx="7" cy="18" r="1.6"/><circle cx="17" cy="18" r="1.6"/></svg>',
 "clock":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"/><polyline points="12 7 12 12 15 14"/></svg>',
 "book":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 4h7a3 3 0 0 1 3 3v13a2.5 2.5 0 0 0-2.5-2.5H4z"/><path d="M20 4h-3a3 3 0 0 0-3 3v13a2.5 2.5 0 0 1 2.5-2.5H20z"/></svg>',
 "menu":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><line x1="4" y1="7" x2="20" y2="7"/><line x1="4" y1="12" x2="20" y2="12"/><line x1="4" y1="17" x2="20" y2="17"/></svg>',
}
NAV=[("Home","/"),("Onderwerpen","/onderwerpen/"),("Gidsen","/gidsen/"),("Nieuws","/nieuws/"),("Over","/over/"),("Contact","/contact/")]

def head(t,d,path,ld=None):
    can=BASE+path
    j="".join('<script type="application/ld+json">'+json.dumps(b,ensure_ascii=False)+'</script>' for b in (ld or []))
    nav="".join(f'<a class="navlink" href="{h}">{esc(l)}</a>' for l,h in NAV)
    return f"""<!DOCTYPE html>
<html lang="nl"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(t)}</title><meta name="description" content="{esc(d)}">
<link rel="canonical" href="{can}">
<meta property="og:type" content="website"><meta property="og:locale" content="nl_NL">
<meta property="og:site_name" content="{esc(SITE)}"><meta property="og:title" content="{esc(t)}">
<meta property="og:description" content="{esc(d)}"><meta property="og:url" content="{can}">
<meta name="theme-color" content="#0E5E77">
<link rel="icon" href="/assets/icons/logo-mark.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/css/style.css?v={CSS_VER}">
{j}</head><body>
<header class="site-head"><nav class="nav" id="nav">
  <a class="brand" href="/"><img class="mark" src="/assets/icons/logo-mark.svg" alt=""><span><b>EA Autocleaning</b><span>Kennisgids</span></span></a>
  {nav}
  <button class="menu-toggle" aria-label="Menu" onclick="document.getElementById('nav').classList.toggle('open')">{IC['menu']}</button>
</nav></header>
"""

def footer():
    return f"""<footer class="foot"><div class="wrap"><div class="cols">
  <div><a class="brand" href="/"><img class="mark" src="/assets/icons/logo-mark.svg" alt=""><span><b>EA Autocleaning</b><span style="color:#7BA0AB">Kennisgids</span></span></a>
    <p class="note">EA Autocleaning is een onafhankelijke kennisgids over het reinigen en verzorgen van auto's. Het platform verkoopt geen producten en voert geen werkzaamheden uit.</p></div>
  <div><h4>Kennis</h4><a href="/onderwerpen/">Onderwerpen</a><a href="/gidsen/">Gidsen</a><a href="/nieuws/">Nieuws</a><a href="/redactie/">Over de redactie</a></div>
  <div><h4>Informatie</h4><a href="/over/">Over dit platform</a><a href="/contact/">Contact</a><a href="/privacybeleid/">Privacybeleid</a><a href="/cookiebeleid/">Cookiebeleid</a></div>
</div><div class="foot-bottom"><span>&copy; 2026 {esc(SITE)}</span>
<span><a href="/contact/">Contact</a> &middot; <a href="/privacybeleid/">Privacy</a> &middot; <a href="/cookiebeleid/">Cookies</a></span></div></div></footer>
</body></html>"""

def crumb(i): return {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":k+1,"name":n,"item":BASE+u} for k,(n,u) in enumerate(i)]}
def crumbs_html(i):
    o=[f'<a href="{u}">{esc(n)}</a>' for n,u in i[:-1]]; o.append(f'<span>{esc(i[-1][0])}</span>')
    return '<div class="wrap"><nav class="crumbs">'+' / '.join(o)+'</nav></div>'
def write(path,c):
    f=os.path.join(OUT,"index.html") if path=="/" else os.path.join(OUT,path.strip("/"),"index.html")
    os.makedirs(os.path.dirname(f),exist_ok=True); open(f,"w",encoding="utf-8").write(c)
def blocks(bs):
    o=[]
    for b in bs:
        if b[0]=="p": o.append(f"<p>{esc(b[1])}</p>")
        elif b[0]=="h2": o.append(f"<h2>{esc(b[1])}</h2>")
        elif b[0]=="ul": o.append("<ul>"+"".join(f"<li>{esc(x)}</li>" for x in b[1])+"</ul>")
        elif b[0]=="callout": o.append(f'<div class="callout"><p>{esc(b[1])}</p></div>')
    return "".join(o)
def byline(): return f'<div class="byline"><img src="/assets/img/auteur.svg" alt="{esc(AUTEUR)}"><div class="who">{esc(AUTEUR)}<small>{esc(AUTEUR_ROL)}</small></div></div>'

ONDERWERPEN=[
 {"slug":"wassen-zonder-krassen","naam":"Wassen zonder krassen",
  "resume":"Het grootste deel van de fijne krassen in lak ontstaat tijdens het wassen zelf, niet door gebruik onderweg.",
  "specs":[("Methode","Twee emmers"),("Risico","Vuil in de spons"),("Volgorde","Boven naar onder")],
  "secties":[("Waarom er krassen ontstaan","Zand en straatvuil dat in de washandschoen achterblijft, wordt bij de volgende haal over de lak getrokken. Dat geeft het patroon van fijne cirkelvormige krassen dat vooral bij donkere lak in de zon zichtbaar wordt. De schade komt dus niet van het wassen, maar van het vuil dat meegenomen wordt."),
   ("De tweeëmmermethode","Een emmer met sop en een emmer met schoon spoelwater, beide met een zeefinzet op de bodem. De handschoen gaat na elke paneel eerst in het spoelwater, waar het vuil naar de bodem zakt onder de zeef, en pas daarna terug in het sop. Voorspoelen met een hogedrukreiniger haalt bovendien het grofste vuil eraf voordat er iets de lak raakt.")],
  "punten":["Eerst grondig voorspoelen","Twee emmers met zeefinzet","Van boven naar onder werken","Aparte handschoen voor de onderste panelen"]},
 {"slug":"decontamineren","naam":"Decontamineren en kleien",
  "resume":"Lak die na het wassen ruw aanvoelt, bevat vastzittende deeltjes die met wassen alleen niet weggaan.",
  "specs":[("Test","Zakje over de hand"),("Middel","Klei of ijzeroplosser"),("Frequentie","Een of twee keer per jaar")],
  "secties":[("De test met een plastic zakje","Een hand in een dun plastic zakje over schone, droge lak halen maakt oneffenheden voelbaar die met de blote hand nauwelijks opvallen. Voelt het als schuurpapier, dan zitten er remstofdeeltjes, teer of industriële neerslag in de laklaag."),
   ("Chemisch en mechanisch","Een ijzeroplosser reageert met metaaldeeltjes en spoelt die weg, herkenbaar aan de paarse verkleuring. Wat daarna nog achterblijft, gaat eraf met een kleistaaf of kleipad, altijd met ruim glijmiddel. Werken zonder glijmiddel veroorzaakt precies de krassen die vermeden moeten worden.")],
  "punten":["Zakjestest wijst vervuiling aan","Eerst chemisch, dan mechanisch","Altijd ruim glijmiddel gebruiken","Daarna opnieuw beschermen"]},
 {"slug":"polijsten","naam":"Polijsten",
  "resume":"De enige stap die krassen echt verwijdert, door een dunne laag lak af te nemen, en daarmee de stap met het meeste risico.",
  "specs":[("Werking","Laklaag afnemen"),("Meten","Laagdiktemeter"),("Herhaalbaar","Beperkt")],
  "secties":[("Wat polijsten doet","Polijsten haalt geen kras weg maar neemt de laklaag eromheen af tot het niveau van de bodem van de kras. Een blanke laklaag is doorgaans veertig tot vijftig micron dik, en per polijstbeurt verdwijnt daarvan enkele microns. Dat kan niet onbeperkt worden herhaald."),
   ("Machine en pad","Een excentrische machine is voor de meeste situaties de veiligste keuze, omdat de beweging warmteopbouw beperkt. De combinatie van pad en polijstmiddel bepaalt de agressiviteit; beginnen met de mildste combinatie die het gewenste resultaat geeft, is de gangbare werkwijze.")],
  "punten":["Verwijdert laklaag, niet alleen de kras","Laagdikte meten voorkomt doorpolijsten","Excentrische machine is vergevingsgezind","Beginnen met de mildste combinatie"]},
 {"slug":"wax-sealant-coating","naam":"Wax, sealant en coating",
  "resume":"Drie manieren om lak te beschermen, met een groot verschil in standtijd, prijs en benodigde voorbereiding.",
  "specs":[("Wax","1 tot 3 maanden"),("Sealant","4 tot 8 maanden"),("Coating","1 tot 5 jaar")],
  "secties":[("Waar het verschil zit","Carnaubawax geeft diepe glans en een warme uitstraling, maar smelt bij warmte en spoelt er relatief snel af. Een synthetische sealant hecht chemisch en houdt het langer vol. Een keramische coating vormt een harde laag die jaren meegaat, maar vraagt vlekkeloos voorbereide lak, omdat elk defect eronder wordt vastgelegd."),
   ("Voorbereiding bepaalt het resultaat","Bij alle drie geldt dat de bescherming alleen zo goed is als wat eronder zit. Aanbrengen over vervuilde of beschadigde lak levert een gladde laag over een slecht oppervlak, wat het resultaat niet beter maakt en bij een coating jarenlang zichtbaar blijft.")],
  "punten":["Wax voor glans, coating voor standtijd","Coating vraagt vlekkeloze voorbereiding","Bescherming maakt vuil losser, niet onzichtbaar","Onderhoud blijft nodig, ook met coating"]},
 {"slug":"interieurreiniging","naam":"Interieurreiniging",
  "resume":"Kunststof, stof en leer vragen elk een andere aanpak, en agressieve middelen richten hier sneller schade aan dan buiten.",
  "specs":[("Kunststof","Neutrale reiniger"),("Stof","Extractie"),("Leer","Ph-neutraal")],
  "secties":[("Volgorde en stof","Eerst grondig stofzuigen, inclusief de naden, daarna pas nat werken. Vuil dat nog los ligt, wordt bij natte reiniging juist verder in het textiel gewreven. Voor stoffen bekleding geeft een extractiereiniger, die het vocht direct weer opzuigt, het beste resultaat zonder dat schuim achterblijft."),
   ("Kunststof en leer","Dashboardonderdelen verdragen doorgaans een neutrale allesreiniger in lage concentratie, met een zachte borstel voor structuur. Glansmiddelen die een vettige laag achterlaten geven reflectie in de voorruit en trekken stof aan. Leer vraagt een ph-neutrale reiniger en daarna een middel dat de toplaag soepel houdt.")],
  "punten":["Eerst droog, dan nat","Extractie voorkomt achterblijvend schuim","Geen glansmiddel op het dashboard","Leer altijd ph-neutraal reinigen"]},
 {"slug":"velgen-en-banden","naam":"Velgen en banden",
  "resume":"Remstof is chemisch agressief en vreet zich in de laklaag van een velg wanneer het te lang blijft zitten.",
  "specs":[("Vervuiling","Remstof"),("Reiniger","Zuurvrij"),("Bandenzwart","Watergedragen")],
  "secties":[("Waarom velgen apart worden gedaan","Remstof bestaat uit hete metaaldeeltjes die zich in de coating van een velg inbranden. Hoe langer dat blijft zitten, hoe dieper het inwerkt. Velgen worden daarom als eerste gereinigd, met eigen borstels en een eigen emmer, om te voorkomen dat die deeltjes op de lak belanden."),
   ("Zuurvrij als uitgangspunt","Zure velgenreinigers werken snel maar tasten gepolijste en gelakte velgen aan bij herhaald gebruik. Een zuurvrije reiniger op ph-neutrale basis vraagt meer inwerktijd en borstelwerk, maar is voor de meeste velgen de veiligere keuze. Bij twijfel over het type velg geldt de mildste optie.")],
  "punten":["Velgen eerst, met eigen materiaal","Remstof niet laten inbranden","Zuurvrij is veiliger voor de coating","Watergedragen bandenzwart spat minder"]},
]
def onderwerp(s): return next(x for x in ONDERWERPEN if x["slug"]==s)

GIDSEN=[
 {"slug":"wasstraat-of-handwas","titel":"Wasstraat of handwas: wat het met de lak doet","ic":"doc",
  "resume":"Niet elke wasstraat is schadelijk en niet elke handwas is veilig. De techniek en het onderhoud bepalen het verschil.",
  "body":[("p","De discussie over wasstraten wordt vaak in absolute termen gevoerd. In de praktijk hangt het resultaat af van het type installatie, het onderhoud ervan en van hoe de auto ervoor stond."),
   ("h2","Borstels, doeken en tekstiel"),("p","Oudere installaties met harde borstels veroorzaken zichtbare krassen. Moderne installaties met zachte tekstiellappen zijn aanzienlijk milder, mits die lappen regelmatig worden gereinigd. Vuil dat in de lappen achterblijft van de vorige auto is het werkelijke risico, niet het materiaal zelf."),
   ("h2","Borstelloos wassen"),("p","Een borstelloze installatie raakt de lak niet aan en werkt met chemie en hoge druk. Dat is de veiligste geautomatiseerde optie, maar verwijdert hardnekkig vuil minder goed. Voor een auto met een goede beschermlaag volstaat dat vaak."),
   ("h2","Handwas is niet automatisch beter"),("ul",["Een spons met vuil erin krast dieper dan een goed onderhouden wasstraat.","Wassen in de volle zon geeft droogvlekken door indrogende zeep.","Een oude handdoek als droogdoek veroorzaakt fijne krassen.","Afwasmiddel tast bestaande beschermlagen aan."]),
   ("callout","Wie zelf wast, haalt het meeste rendement uit twee dingen: grondig voorspoelen en een schone microvezeldroogdoek. Die twee doen meer voor het eindresultaat dan de keuze van de shampoo."),
   ("p",DISC)]},
 {"slug":"seizoensonderhoud","titel":"Seizoensonderhoud: wat wanneer aandacht vraagt","ic":"clock",
  "resume":"Strooizout in de winter en insecten in de zomer vragen een andere aanpak dan de standaardwasbeurt.",
  "body":[("p","De belasting op lak, rubber en onderstel verschilt sterk per seizoen. Een vast ritme dat daarop aansluit voorkomt schade die achteraf lastig te herstellen is."),
   ("h2","Winter"),("p","Strooizout versnelt corrosie, vooral op plekken waar vocht blijft staan. Regelmatig spoelen van de onderzijde en de wielkasten is in deze periode belangrijker dan een glanzend paneel. Een beschermlaag die voor de winter wordt aangebracht, maakt het losspoelen aanzienlijk makkelijker."),
   ("h2","Voorjaar"),("ul",["Grondige decontaminatie na de winter.","Rubbers van deuren en ramen behandelen tegen uitdrogen.","Onderzijde en wielkasten controleren op zoutresten.","Beschermlaag opnieuw aanbrengen."]),
   ("h2","Zomer"),("p","Insectenresten en vogelpoep bevatten zuren die zich bij warmte snel in de laklaag etsen. Hoe eerder die eraf gaan, hoe minder er van achterblijft. Wassen in de volle zon geeft droogvlekken; vroeg in de ochtend of in de schaduw werkt beter."),
   ("h2","Najaar"),("p","Bladeren en boomhars laten vlekken achter en houden vocht vast op horizontale vlakken. Hars laat zich verwijderen met een daarvoor bedoeld middel; krabben beschadigt de laklaag vrijwel zeker."),
   ("p",DISC)]},
]

ARTIKELEN=[
 {"slug":"waarom-donkere-lak-meer-toont","titel":"Waarom donkere lak elke kras laat zien","cat":"Achtergrond","datum":"2026-07-17","datum_nl":"17 juli 2026","lees":4,
  "resume":"Het verschil zit niet in de hardheid van de lak, maar in hoe licht wordt weerkaatst.",
  "body":[("p","Zwarte en donkerblauwe auto's staan bekend als kwetsbaar. De laklaag is echter niet zachter dan die van een witte auto; het verschil zit in wat zichtbaar wordt."),
   ("h2","Contrast bepaalt de zichtbaarheid"),("p","Een kras verstrooit licht en oogt daardoor lichter dan het oppervlak eromheen. Op een donker vlak levert dat een groot contrast op, op een licht vlak vrijwel geen. Dezelfde beschadiging is op wit nauwelijks te zien en op zwart onmiskenbaar."),
   ("h2","Metallic en solid"),("p","Metallic lak bevat deeltjes die licht in meerdere richtingen weerkaatsen, wat kleine oneffenheden optisch verzacht. Effen lak zonder die deeltjes weerkaatst gelijkmatiger, waardoor elke onderbreking opvalt. Zwart zonder metallic is daarmee de meest onvergevingsgezinde combinatie."),
   ("h2","Wat dat betekent voor onderhoud"),("p","Bij donkere lak loont zorgvuldig wassen dus meer dan bij lichte lak, niet omdat er sneller schade ontstaat, maar omdat elke fout blijvend zichtbaar is."),
   ("p",DISC)]},
 {"slug":"microvezel-doeken","titel":"Microvezeldoeken: waarom sorteren en wassen uitmaakt","cat":"Praktijk","datum":"2026-07-02","datum_nl":"2 juli 2026","lees":3,
  "resume":"Een doek die op de grond is gevallen of met wasverzachter is gewassen, richt meer schade aan dan hij voorkomt.",
  "body":[("p","Microvezeldoeken zijn het meest gebruikte hulpmiddel bij autoverzorging en tegelijk de meest onderschatte bron van krassen."),
   ("h2","Waarom een gevallen doek weg moet"),("p","Vezels nemen kleine steentjes en zandkorrels op en houden die vast. Een doek die de grond heeft geraakt, bevat daarmee precies het materiaal dat krassen veroorzaakt. Uitkloppen haalt dat er niet uit."),
   ("h2","Wasverzachter is het probleem"),("ul",["Wasverzachter legt een laag om de vezels en vermindert de opnamecapaciteit.","Hoge temperaturen beschadigen de vezelstructuur onomkeerbaar.","Wassen met katoen zorgt voor pluisresten tussen de vezels.","Een aparte was op lage temperatuur zonder verzachter houdt de doeken bruikbaar."]),
   ("h2","Sorteren op gebruik"),("p","Doeken voor velgen, interieur, glas en lak horen gescheiden te blijven, ook in de was. Een doek die remstof of dressing heeft opgenomen, brengt dat over op het volgende oppervlak."),
   ("p",DISC)]},
]

def tile(s):
    return f"""<a class="tile" href="/onderwerpen/{s['slug']}/"><h3>{esc(s['naam'])}</h3><p>{esc(s['resume'][:96].rsplit(' ',1)[0])}...</p></a>"""
def newscard(a):
    return f"""<article class="news"><span class="cat">{esc(a['cat'])}</span>
  <h3><a href="/nieuws/{a['slug']}/" style="color:inherit;text-decoration:none">{esc(a['titel'])}</a></h3>
  <p>{esc(a['resume'])}</p><div class="meta">{esc(a['datum_nl'])} &middot; {a['lees']} min lezen</div></article>"""

def p_home():
    ld=[{"@context":"https://schema.org","@type":"WebSite","@id":BASE+"/#w","url":BASE+"/","name":SITE,"inLanguage":"nl-NL",
         "description":"Onafhankelijke kennisgids over autoreiniging en detailing, van wassen en polijsten tot beschermen en interieur."},
        {"@context":"https://schema.org","@type":"Organization","@id":BASE+"/#o","name":SITE,"url":BASE+"/","email":EMAIL},crumb([("Home","/")])]
    gids="".join(f'<div class="card"><div class="ic">{IC[g["ic"]]}</div><h3><a href="/gidsen/{g["slug"]}/" style="color:inherit;text-decoration:none">{esc(g["titel"])}</a></h3><p>{esc(g["resume"])}</p></div>' for g in GIDSEN)
    h=head("EA Autocleaning | kennisgids over autoreiniging",
      "Onafhankelijke kennisgids over het reinigen en verzorgen van auto's. Wassen zonder krassen, decontamineren, polijsten, beschermen en interieur.","/",ld)
    h+=f"""<section class="hero"><div class="wrap hero-inner">
  <div><span class="eyebrow">{IC['scale']}Kennisgids</span>
  <h1>Auto's reinigen <em>zonder schade</em></h1>
  <p class="lead">Wassen, decontamineren, polijsten en beschermen: wat elke stap doet, in welke volgorde het loont en waar lak beschadigd raakt. Onafhankelijk en zonder productverkoop.</p>
  <div class="hero-actions"><a class="btn btn-plum" href="/onderwerpen/">Bekijk de onderwerpen {IC['arrow']}</a><a class="btn btn-ghost" href="/gidsen/">Naar de gidsen</a></div>
  <div class="hero-meta"><span>{IC['check']}6 onderwerpen</span><span>{IC['check']}Volgorde uitgelegd</span><span>{IC['check']}Geen productverkoop</span></div></div>
  <div class="hero-art"><img src="/assets/img/hero.svg" alt="Illustratie van een auto die wordt gereinigd" width="480" height="340"></div>
</div></section>

<section class="section"><div class="wrap">
  <div class="section-head"><span class="eyebrow">{IC['doc']}Onderwerpen</span><h2>De stappen op een rij</h2>
  <p class="lead">Per stap wat er gebeurt, waarom de volgorde uitmaakt en waar het in de praktijk misgaat.</p></div>
  <div class="grid cols-3">{"".join(tile(s) for s in ONDERWERPEN)}</div></div></section>

<section class="section panel"><div class="wrap">
  <div class="section-head"><span class="eyebrow">{IC['book']}Gidsen</span><h2>Twee praktische gidsen</h2></div>
  <div class="grid cols-2">{gids}</div></div></section>

<section class="section"><div class="wrap">
  <div class="section-head"><span class="eyebrow">{IC['clock']}Nieuws</span><h2>Laatste artikelen</h2></div>
  <div class="grid cols-2">{"".join(newscard(a) for a in ARTIKELEN)}</div>
  <p style="margin-top:22px"><a class="more" href="/nieuws/">Alle artikelen {IC['arrow']}</a></p></div></section>

<section class="section tight"><div class="wrap"><div class="cta">
  <h2>Een onderwerp gemist?</h2><p>Deze gids groeit op basis van vragen die binnenkomen. Suggesties en correcties zijn welkom bij de redactie.</p>
  <a class="btn btn-gold" href="/contact/">Mail de redactie {IC['arrow']}</a></div></div></section>"""
    write("/",h+footer())

def p_ond_index():
    path="/onderwerpen/"; c=[("Home","/"),("Onderwerpen",path)]
    ld=[{"@context":"https://schema.org","@type":"CollectionPage","@id":BASE+path,"url":BASE+path,"name":"Onderwerpen","inLanguage":"nl-NL"},
        {"@context":"https://schema.org","@type":"ItemList","itemListElement":[{"@type":"ListItem","position":i+1,"name":s["naam"],"url":BASE+f"/onderwerpen/{s['slug']}/"} for i,s in enumerate(ONDERWERPEN)]},crumb(c)]
    h=head("Onderwerpen autoverzorging | "+SITE,"Overzicht van onderwerpen rond autoreiniging: wassen, decontamineren, polijsten, beschermen, interieur en velgen.",path,ld)+crumbs_html(c)
    h+=f"""<section class="section"><div class="wrap"><div class="section-head"><span class="eyebrow">{IC['doc']}Overzicht</span>
  <h1>Onderwerpen</h1><p class="lead">Zes stappen die samen het volledige proces vormen, van de eerste emmer water tot de beschermlaag.</p></div>
  <div class="grid cols-3">{"".join(tile(s) for s in ONDERWERPEN)}</div></div></section>"""
    write(path,h+footer())

def p_ond(s):
    path=f"/onderwerpen/{s['slug']}/"; c=[("Home","/"),("Onderwerpen","/onderwerpen/"),(s["naam"],path)]
    ld=[{"@context":"https://schema.org","@type":"Article","@id":BASE+path,"headline":s["naam"],"description":s["resume"],
         "inLanguage":"nl-NL","author":{"@type":"Person","name":AUTEUR},"publisher":{"@type":"Organization","name":SITE}},crumb(c)]
    sp="".join(f"<div><dt>{esc(l)}</dt><dd>{esc(v)}</dd></div>" for l,v in s["specs"])
    sec="".join(f"<h2>{esc(t)}</h2><p>{esc(p)}</p>" for t,p in s["secties"])
    pt="".join(f'<li>{IC["check"]}<span>{esc(x)}</span></li>' for x in s["punten"])
    anders=[x for x in ONDERWERPEN if x["slug"]!=s["slug"]][:3]
    h=head(f"{s['naam']} | uitgelegd | {SITE}", s["resume"], path, ld)+crumbs_html(c)
    h+=f"""<section class="section tight"><div class="wrap prose"><span class="eyebrow">{IC['scale']}Onderwerp</span>
  <h1>{esc(s['naam'])}</h1><p class="lead">{esc(s['resume'])}</p></div>
  <div class="wrap"><dl class="specs">{sp}</dl></div>
  <div class="wrap prose">{sec}<h2>Kort samengevat</h2><ul class="ticks" style="margin-bottom:16px">{pt}</ul>
  <p class="disc">{esc(DISC)}</p>{byline()}</div></section>
<section class="section panel"><div class="wrap"><div class="section-head"><h2>Andere onderwerpen</h2></div>
  <div class="grid cols-3">{"".join(tile(x) for x in anders)}</div></div></section>"""
    write(path,h+footer())

def p_gidsen():
    path="/gidsen/"; c=[("Home","/"),("Gidsen",path)]
    ld=[{"@context":"https://schema.org","@type":"CollectionPage","@id":BASE+path,"url":BASE+path,"name":"Gidsen","inLanguage":"nl-NL"},crumb(c)]
    cards="".join(f'<div class="card"><div class="ic">{IC[g["ic"]]}</div><h3><a href="/gidsen/{g["slug"]}/" style="color:inherit;text-decoration:none">{esc(g["titel"])}</a></h3><p>{esc(g["resume"])}</p><p style="margin-top:10px"><a class="more" href="/gidsen/{g["slug"]}/">Lees de gids {IC["arrow"]}</a></p></div>' for g in GIDSEN)
    h=head("Gidsen | wassen en seizoensonderhoud | "+SITE,"Praktische gidsen over de keuze tussen wasstraat en handwas en over onderhoud per seizoen.",path,ld)+crumbs_html(c)
    h+=f"""<section class="section"><div class="wrap"><div class="section-head"><span class="eyebrow">{IC['book']}Gidsen</span>
  <h1>Gidsen</h1><p class="lead">Twee onderwerpen die losstaan van een enkele stap en het hele jaar spelen.</p></div>
  <div class="grid cols-2">{cards}</div></div></section>"""
    write(path,h+footer())

def p_gids(g):
    path=f"/gidsen/{g['slug']}/"; c=[("Home","/"),("Gidsen","/gidsen/"),(g["titel"],path)]
    ld=[{"@context":"https://schema.org","@type":"Article","@id":BASE+path,"headline":g["titel"],"description":g["resume"],
         "inLanguage":"nl-NL","author":{"@type":"Person","name":AUTEUR},"publisher":{"@type":"Organization","name":SITE}},crumb(c)]
    h=head(f"{g['titel']} | {SITE}", g["resume"], path, ld)+crumbs_html(c)
    h+=f"""<section class="section"><div class="wrap prose"><span class="eyebrow">{IC[g['ic']]}Gids</span>
  <h1>{esc(g['titel'])}</h1><p class="lead">{esc(g['resume'])}</p>{blocks(g['body'])}{byline()}</div></section>"""
    write(path,h+footer())

def p_nieuws():
    path="/nieuws/"; c=[("Home","/"),("Nieuws",path)]
    ld=[{"@context":"https://schema.org","@type":"CollectionPage","@id":BASE+path,"url":BASE+path,"name":"Nieuws","inLanguage":"nl-NL"},crumb(c)]
    h=head("Nieuws | artikelen over lak en materiaal | "+SITE,"Achtergrondartikelen over lak, materiaal en gereedschap bij het verzorgen van auto's.",path,ld)+crumbs_html(c)
    h+=f"""<section class="section"><div class="wrap"><div class="section-head"><span class="eyebrow">{IC['clock']}Nieuws</span>
  <h1>Artikelen</h1><p class="lead">Achtergrond bij wat er met lak en materialen gebeurt tijdens het reinigen.</p></div>
  <div class="grid cols-2">{"".join(newscard(a) for a in ARTIKELEN)}</div></div></section>"""
    write(path,h+footer())

def p_art(a):
    path=f"/nieuws/{a['slug']}/"; c=[("Home","/"),("Nieuws","/nieuws/"),(a["titel"],path)]
    ld=[{"@context":"https://schema.org","@type":"Article","@id":BASE+path,"headline":a["titel"],"description":a["resume"],
         "datePublished":a["datum"],"inLanguage":"nl-NL","author":{"@type":"Person","name":AUTEUR},"publisher":{"@type":"Organization","name":SITE}},crumb(c)]
    h=head(f"{a['titel']} | {SITE}", a["resume"], path, ld)+crumbs_html(c)
    h+=f"""<section class="section"><div class="wrap prose"><span class="eyebrow">{IC['clock']}{esc(a['cat'])}</span>
  <h1>{esc(a['titel'])}</h1><p class="meta" style="margin-bottom:22px">Door {esc(AUTEUR)} &middot; {esc(a['datum_nl'])} &middot; {a['lees']} min lezen</p>
  {blocks(a['body'])}{byline()}</div></section>
<section class="section panel"><div class="wrap"><div class="section-head"><h2>Meer lezen</h2></div>
  <div class="grid cols-2">{"".join(newscard(x) for x in ARTIKELEN if x['slug']!=a['slug'])}</div></div></section>"""
    write(path,h+footer())

def p_over():
    path="/over/"; c=[("Home","/"),("Over",path)]
    ld=[{"@context":"https://schema.org","@type":"AboutPage","@id":BASE+path,"url":BASE+path,"name":"Over","inLanguage":"nl-NL"},crumb(c)]
    h=head("Over EA Autocleaning | wat dit platform is | "+SITE,
      "EA Autocleaning is een onafhankelijke kennisgids over autoreiniging. Geen webshop, geen dienstverlening en geen merkvoorkeuren.",path,ld)+crumbs_html(c)
    h+=f"""<section class="section"><div class="wrap prose"><span class="eyebrow">{IC['book']}Over het platform</span>
  <h1>Een kennisgids, geen poetsbedrijf</h1>
  <p class="lead">EA Autocleaning legt uit wat er tijdens het reinigen en verzorgen van een auto werkelijk gebeurt, zodat een keuze berust op techniek in plaats van op marketing.</p>
  <h2>Waarom deze gids bestaat</h2>
  <p>Rond autoverzorging bestaat een grote markt aan producten die elk beloven het probleem op te lossen. Wat vaak ontbreekt is uitleg over wat een stap doet en waarom de volgorde uitmaakt. Zonder die uitleg wordt geld uitgegeven aan een middel dat het onderliggende probleem niet raakt.</p>
  <div class="callout"><p><strong>Geen bedrijf, geen webshop.</strong> Dit platform verkoopt geen producten, voert geen werkzaamheden uit en heeft geen afspraken met fabrikanten. Overeenkomsten met namen van bestaande poetsbedrijven berusten niet op enige samenwerking of betrokkenheid.</p></div>
  <h2>Wat hier wel staat</h2>
  <p>Per onderwerp wat de stap doet, welk materiaal daarbij hoort en waar het misgaat. Merknamen blijven achterwege, omdat het assortiment sneller verandert dan de techniek erachter.</p>
  <h2>Verschillen per auto</h2>
  <p>Laksoort, leeftijd en eerdere behandelingen bepalen wat verstandig is. Een aanpak die op de ene auto goed uitpakt, kan op de andere schade geven. Bij twijfel blijft een proefstuk op een onopvallende plek de veiligste route.</p>
  <p style="margin-top:16px"><a class="btn btn-plum" href="/redactie/">Over de redactie {IC['arrow']}</a> <a class="btn btn-ghost" href="/onderwerpen/">Naar de onderwerpen</a></p></div></section>"""
    write(path,h+footer())

def p_redactie():
    path="/redactie/"; c=[("Home","/"),("Over de redactie",path)]
    ld=[{"@context":"https://schema.org","@type":"Person","@id":BASE+"/#erik","name":AUTEUR,"jobTitle":AUTEUR_ROL,"worksFor":{"@type":"Organization","name":SITE}},
        {"@context":"https://schema.org","@type":"ProfilePage","@id":BASE+path,"url":BASE+path,"name":"Over de redactie","inLanguage":"nl-NL"},crumb(c)]
    h=head(f"Over de redactie: {AUTEUR} | {SITE}", f"{AUTEUR} schrijft de onderwerpen en gidsen van EA Autocleaning.",path,ld)+crumbs_html(c)
    h+=f"""<section class="section"><div class="wrap"><div class="persona">
  <div class="persona-photo"><img src="/assets/img/auteur.svg" alt="Illustratie van {esc(AUTEUR)}"></div>
  <div><span class="eyebrow">{IC['scale']}De redactie</span><h1>{esc(AUTEUR)}</h1>
  <p class="lead">{esc(AUTEUR_ROL)}. Erik schrijft de onderwerpen, de gidsen en de artikelen op deze site.</p></div></div></div></section>
<section class="section panel"><div class="wrap prose">
  <h2>Van de wasplaats naar de redactie</h2>
  <p>Erik werkte jaren bij een autopoetsbedrijf, waar wekelijks auto's binnenkwamen met krassen die tijdens het wassen thuis waren ontstaan. Wat daar zichtbaar werd over volgorde en materiaal, vormt de kern van deze gids.</p>
  <h2>Techniek boven producten</h2>
  <p>Rond autoverzorging worden veel middelen aangeprezen die elkaar grotendeels overlappen. Op deze site staat wat een bewerking doet en welk type middel daarbij hoort, zonder merknamen en zonder aanbevelingen die niet te onderbouwen zijn.</p>
  <h2>Een getekend portret</h2>
  <p>De illustratie op deze pagina is een tekening, geen foto.</p>
  <h2>Contact</h2>
  <p>Correcties en suggesties komen binnen via <a href="mailto:{EMAIL}">{EMAIL}</a>.</p></div></section>"""
    write(path,h+footer())

def p_contact():
    path="/contact/"; c=[("Home","/"),("Contact",path)]
    ld=[crumb(c),{"@context":"https://schema.org","@type":"ContactPage","@id":BASE+path,"url":BASE+path,"name":"Contact","inLanguage":"nl-NL"}]
    h=head("Contact | "+SITE,"Vraag, correctie of suggestie voor EA Autocleaning? Een e-mail komt rechtstreeks bij de redactie binnen.",path,ld)+crumbs_html(c)
    h+=f"""<section class="section"><div class="wrap prose"><span class="eyebrow">{IC['mail']}Contact</span>
  <h1>Contact met de redactie</h1>
  <p class="lead">Deze site heeft geen contactformulier. Een e-mail komt rechtstreeks bij de redactie binnen.</p>
  <div class="callout"><p><strong>E-mailadres</strong></p><p style="margin:.3em 0"><a href="mailto:{EMAIL}" style="font-size:1.1rem;font-weight:600">{EMAIL}</a></p></div>
  <h2>Waar de redactie iets mee kan</h2>
  <ul><li>Een correctie op een beschrijving, met onderbouwing.</li><li>Een onderwerp dat nog ontbreekt in de gids.</li><li>Praktijkervaring die iets aanvult of tegenspreekt.</li></ul>
  <h2>Waar niet</h2>
  <p>Dit platform verkoopt niets, voert geen werkzaamheden uit en beoordeelt geen schadegevallen. Voor herstel van lakschade is een schadeherstelbedrijf of een gespecialiseerd detailer de aangewezen partij.</p></div></section>"""
    write(path,h+footer())

def legal(path,titel,bs):
    c=[("Home","/"),(titel,path)]
    ld=[crumb(c),{"@context":"https://schema.org","@type":"WebPage","@id":BASE+path,"url":BASE+path,"name":titel,"inLanguage":"nl-NL"}]
    h=head(f"{titel} | {SITE}", f"{titel} van {SITE}.",path,ld)+crumbs_html(c)
    h+=f'<section class="section"><div class="wrap prose"><h1>{esc(titel)}</h1>{"".join(bs)}</div></section>'
    write(path,h+footer())

def p_legal():
    legal("/privacybeleid/","Privacybeleid",[
      "<p>EA Autocleaning is een redactioneel platform en verwerkt zo min mogelijk persoonsgegevens.</p>",
      "<h2>Welke gegevens</h2><p>De site bevat geen contactformulier. Wie per e-mail contact opneemt, deelt uitsluitend wat in dat bericht staat, en dat wordt alleen gebruikt om te antwoorden.</p>",
      "<h2>Statistieken</h2><p>Als bezoekcijfers worden bijgehouden, gebeurt dat zo privacyvriendelijk mogelijk en zonder verkoop aan derden.</p>",
      "<h2>Bewaartermijn</h2><p>E-mails worden niet langer bewaard dan nodig is voor de afhandeling.</p>",
      f"<h2>Vragen</h2><p>Vragen over privacy kunnen naar {EMAIL}.</p>"])
    legal("/cookiebeleid/","Cookiebeleid",[
      "<p>Deze site gebruikt zo min mogelijk cookies en plaatst geen advertentiecookies.</p>",
      "<h2>Functioneel</h2><p>Alleen cookies die nodig zijn voor het functioneren van de pagina's kunnen worden geplaatst.</p>",
      "<h2>Lettertypen</h2><p>De lettertypen worden geladen via een externe dienst, wat bij het tonen van een pagina een verzoek naar die dienst met zich meebrengt.</p>",
      f"<h2>Vragen</h2><p>Vragen over cookies kunnen naar {EMAIL}.</p>"])

def p_404():
    h=head("Pagina niet gevonden | "+SITE,"De opgevraagde pagina bestaat niet.","/404.html",None)
    h+=f"""<section class="section"><div class="wrap prose" style="text-align:center">
  <span class="eyebrow" style="justify-content:center">404</span><h1>Deze pagina bestaat niet</h1>
  <p class="lead">De link is mogelijk verouderd. Het overzicht van onderwerpen is een goed vertrekpunt.</p>
  <p><a class="btn btn-plum" href="/">Naar de homepage {IC['arrow']}</a> <a class="btn btn-ghost" href="/onderwerpen/">Alle onderwerpen</a></p></div></section>"""
    open(os.path.join(OUT,"404.html"),"w",encoding="utf-8").write(h+footer())

def extras():
    u=["/","/over/","/redactie/","/onderwerpen/","/gidsen/","/nieuws/","/contact/","/privacybeleid/","/cookiebeleid/"]
    u+=[f"/onderwerpen/{s['slug']}/" for s in ONDERWERPEN]+[f"/gidsen/{g['slug']}/" for g in GIDSEN]+[f"/nieuws/{a['slug']}/" for a in ARTIKELEN]
    open(os.path.join(OUT,"sitemap.xml"),"w").write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+"".join(f"  <url><loc>{BASE}{x}</loc></url>\n" for x in u)+"</urlset>\n")
    open(os.path.join(OUT,"robots.txt"),"w").write(f"User-agent: *\nAllow: /\nSitemap: {BASE}/sitemap.xml\n")
    open(os.path.join(OUT,"_headers"),"w").write("/assets/*\n  Cache-Control: public, max-age=31536000, immutable\n/*\n  X-Content-Type-Options: nosniff\n  Referrer-Policy: strict-origin-when-cross-origin\n")
    open(os.path.join(OUT,"_redirects"),"w").write(f"https://www.ea-autocleaning.nl/* {BASE}/:splat 301!\n")

def main():
    import shutil
    if os.path.exists(OUT): shutil.rmtree(OUT)
    os.makedirs(OUT,exist_ok=True)
    shutil.copytree(os.path.join(SRC,"assets"), os.path.join(OUT,"assets"))
    p_home(); p_over(); p_redactie(); p_ond_index()
    for s in ONDERWERPEN: p_ond(s)
    p_gidsen()
    for g in GIDSEN: p_gids(g)
    p_nieuws()
    for a in ARTIKELEN: p_art(a)
    p_contact(); p_legal(); p_404(); extras()
    print("Build klaar in", OUT)

if __name__=="__main__": main()
