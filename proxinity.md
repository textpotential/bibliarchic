CONCLUSIONS: A PROLIFERATION OF INTERFACES

**Proxinity - Contact Without Grasp**

Through the generous support of the Baker-Nord Center for the Humanities
at Case Western Reserve University, I have had the privilege of working
with an inspiring and inquisitive team to collaboratively explore ways
in which digital media technologies might unsettle our notions of sacred
text translation. Over the past year, Timothy Beal, Sarah Gridley, Eric
Pellish, William Deal, and I have been working remotely and
residentially to imagine a web application that would shape a
disposition of attention to ambiguity in the translation processes of
Genesis 1.1. This ongoing project through Baker-Nord deeply shapes one
of the material bible experiments in my dissertation which I have called
"facing the deep." Below I outline some early discussions of interface
possibilities for this web application, including my incredibly rough
sketches.

Even though our current project app is called *Tohu*, I am toying with
an app name of proxinity as a mashup of proximity and infinity to signal
my value on shaping dispositions toward reading as contact without
grasp. Sarah Gridley helpfully raised the concern that "contact without
grasp" could connote a kind of consumptive tourism or voyerism. This is
decidedly NOT what I am hoping from proxinity. So, along the way, I hope
to reflect on the difference between cantact as consumptive tourism that
tokenizes and contact as encounter that engages deeply without a demand
for full comprehension.

**Hints and Openings**

Several technologies have shaped my imagination of what might be
possible in an app that facilitates dispositions of close reading,
encounter and opening.

-   \[diigo\]([*https://www.diigo.com/user/mphemenway*](https://www.diigo.com/user/mphemenway))\
    a deeply collaborative tool where communities can annotate and
    discuss web artifacts in the space of the 'page' itself. A wonderful
    enactment of participatory reading as making. Diigo also has some
    social media aggregation possibilities than can lead to further
    conversation around fragments.

-   \[rebelmouse\]([*https://www.rebelmouse.com/aproximatebible/*](https://www.rebelmouse.com/aproximatebible/))\
    My preferred social media aggregator and an integral part of this
    dissertation project. Rebelmouse is a hashtag structured community
    aggregation tool that can pull together endless channels into
    a stream. What I love about rebelmouse is the spatial proximity of
    fragments that come from all kinds of different sources, both people
    and platforms.

-   \[genius - The Waste
    Land\]([*http://genius.com/Ts-eliot-the-waste-land-annotated/*](http://genius.com/Ts-eliot-the-waste-land-annotated/))\
    Genius is a fantastic tool for crowd/community annotation of text
    that allows media annotations as well as text. Another tool that
    embodies reading as making, but I wish the base text didn't remain
    so dominant in the space of the tool. Genius is a new media
    translation of marginalia of sorts, but with a different spatiality
    determined by a digital notion of page.

-   \[on
    broadway\]([*http://www.on-broadway.nyc*](http://www.on-broadway.nyc/))\
    A recent project by one of my favorite new media scholars, Lev
    Manovich, and others. Both a physical installation and a web
    application that perform a material media translation of a 1966
    print piece. A radically new spatial rendering of life in the city
    using large and dynamic social media data sets. The infinite
    entanglement of data and interface in this project is a great model
    for making new media objects.

-   \[ArtLENS\]([*http://www.clevelandart.org/gallery-one/artlens*](http://www.clevelandart.org/gallery-one/artlens))\
    A new media translation of access to a fixed museum collection.
    ARTLens has many interesting features in both the large touchscreen
    installation and the mobile app, especially realted to user
    generated pathways as a part of the growing dataset.

**Two Lobes of Infinity**

I think of our application design as the constant interplay of the two
lobes of the infinity sign. *Lobe 1* is an ongoing and iterative machine
learning process taking data from sources and from user interaction and
creating correlative **metadata** via semantic connection to conceptual
domains.

-   OCR and image recognition tools 'read' media for potential terms or
    attributes that can be passed into the conceptual algorithm map for
    metadata processing.

-   Using an object oriented database problematizes the strict
    database/interface dichotomy often operative in app design.

-   Natural language processing provides the algorithms to take streams
    of data and find correlations between artifacts and create the
    corresponding metadata by moving back and forth between semantic and
    conceptual realms. My colleague Justin Barber suggests we look at a
    tool called
    \[WordNet\]([*https://wordnet.princeton.edu*](https://wordnet.princeton.edu/))
    to help our application correlate semantic data with higher order
    conceptual frameworks to enable metadata correlations beyond direct
    semantic or linguistic equivalence. Here, at the programmatic level,
    we would be embodying a value on problematizing simple notions of
    equivalence in translation.

*Lobe 2* involves rendering an interface that allows user interaction
with and participation in constellations of artifacts that make up the
lives of a text/tradition.

-   Interface will model contact without grasp and hopefully develop new
    reading dis-positions toward attention to ambiguity.

-   We could moderate user input regarding additional artifacts and
    possible correlations between and feed into machine
    learning process.

-   Like ARTLens, we could also use user pathway data as a source for
    NLP metadata learning.

**Initial Design Principles**

*Begin with NRSV*

The proxinity interface could offer one translation as the initial point
of contact. I suggest NRSV here simply out of pragmatics of possible
translation projects in the near future. One alternative here would be
to randomly select one translation/version from the existing dataset as
the initial contact text, limited by browser language setting and/or
user profile preference.

*Define Units*

Ideally, emulating the Genius platform, we would have an algorithm and
an interface that would allow users to select a portion of text (e.g.
highlight 3 words or entire sentence) and have the application generate
the corresponding constellation on the fly based on selection. Yet,
perhaps for an initial phase, we define units of text from the chosen
contact translation (NRSV) and make these independently touchable to
move into the corresponding constellation. Artifacts in the collection
could appear in many constellations depending on the NLP constructed
metadata and its connection to multiple portions of the contact text.

*Initial Interface *

Users arrive at app and are presented with the contact translation as
NRSV. A touch on a portion of text zooms to that portion of text as
shimmering objects making up letters, almost as if letters are buzzing
and then these objects release from formation in letters into a slowly
swirling constellation of objects. Should we keep the contact text
phrase on the screen above the swirling constellation to remind user of
their path?

![](media/image18.tiff){width="6.5in" height="4.875in"}

To the left of the constellation will be a clickable cloud of object
type toggles to allow filtering of artifacts in constellation by
particular object types. All types will be on by default. Clicking on a
type marker one time will remove that object type from the constellation
and clicking again will bring these objects back into the swirl. To the
right of the constellation will be a clickable cloud of concept toggles
for filtering in a similar fashion. We could have countless clouds or
cascading clouds that allowed filtering by different attributes
(language, time period, genre, etc.).

![](media/image19.tiff){width="6.5in" height="4.875in"}

Our team discussed having ways to organize the swirling artifacts (e.g.
versions) by time or other attribute for pedagogical aims (e.g. show
historical trajectory of translations for comparison and showing
geneology).

*Item View*

A click on any object will bring it into focus and show annotations,
share options, and maybe even a way to suggest correlation with another
object in constellation (search by concept). The annotation feature will
allow general comments and spatially located point specific annotations.
All annotations can be text, image, html embeds, audio, or video. I'm
guessing we will want annotation moderation of some sort and definitely
require account registration to participate like this. I would like to
call this participation "translation," to emphasize the point that
participating in the engagement of a text and tradition is translation.

![](media/image20.tiff){width="6.5in" height="4.875in"}

Item view will also offer clickable clouds of related concepts and
object types as in constellation view. Yet, in item view, a click on a
cloud item will take user to a new constellation based on their
selection to move to other constellations. Maybe the object type cloud
would keep user in the same contact translation space but give
constellation of similar object types as item. BUT, concept cloud would
take user to new constellation not based on contact translation segment,
but rather on conceptual attribute. In this case, we would need a way
for users to move from conceptual constellation to related contact
translation segments? Maybe one of the material limits we put on the
interface is that access to constellations is always tied to contact
translation segment?

*Sources *

We would recruit our friends to help find suitable sources for artifacts
that our algorithm could use for ongoing training and collecting. Many
sources are already available and we will be building both an
aggregation of these existing sources and asking for people to
contribute artifacts (e.g. drawings or pictures of catacomb art related
to a contact translation segment). All artifacts included would come
with source link so that user can always push out to other spaces for
further exploration. I have no desire to keep user traffic inside app or
to absorb artifacts into our own dataset! We will simply use pointers to
sources but we will handle annotations, etc. within the app. Some
possible sources or source types might be:

-   [*bible.com*](http://bible.com/) for translations

-   versions in ancient languages as well (not THE Hebrew, but a set
    of Hebrew/Greek/etc. versions that shape contact with this passage,
    let's not even assume MT as original)

-   literature (ancient near east creation epics)

-   art

-   manuscripts (e.g. api for sinaiticus or for U of Michigan
    collection, etc.)

-   video (initially cull textual metadata from vimeo and youtube
    description, title and even captions. beyond this, there are tools
    that can watch the video and extract metadata)

-   music

-   architecture

-   social media engagement with related hashtags
