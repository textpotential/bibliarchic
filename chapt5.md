# Chapter 5: Proliferation of Interfaces #

To differing degrees and through different materialities, we have seen the affordances of high surface area, collaboration, and anarchy at work in bible as interface in books and in an early attempt to extend beyond the book in the web Sinaiticus interface.
In this chapter, I will look toward bible interfaces that move decidedly beyond book, meaning these interfaces are no longer governed by the binding together of pages in a singular volume.
As we have seen in other technological shifts in interface, such as the move from roll to codex, these emerging bible interfaces will not entirely erase or leave behind the structures of the page.
Rather, as bible moves beyond book, the affordances of high surface area, collaboration, and anarchy will arise from user relationships with platform materialities that exceed the pages of a book.

Extending the analysis of bible interface into the realm of emerging digital technologies[^reminder] involves two important shifts that will demand some new imagination on our part.
First, as bible distances itself from the materiality of the page, it is important to understand the continued materialities of emerging digital technologies.
Approaching these digital technologies as interface and attending to their affordances reinforces the materiality of the digital, since affordances describe the possible relationships between a user and the material characteristics an environment or platform.
In no way are we leaving the material realm of books and entering some immaterial virtual world of computers and the internet.

[^reminder]: By digital, I simply mean technologies pertaining to computing, including things like software, hardware, mobile devices and the internet.
I use the language of emerging instead of new to remind us of the ongoing palimpsestuous process of material media translation to gives rise to so called "new" technologies without starting from scratch and never fully leaving previous technologies behind.

As I mentioned in the introduction, digital technologies have multiple layers of materiality.
Computers and mobile devices are made of material components like capacitors, wires, precious metals, etc.
and the internet is dependent on vast amounts of electricity both to power the devices connected but also to power the cooling systems that keep the equipment in good shape.
This is not the materiality I am interested in here.
I am interested in the layers of structure that produce digital technologies and which inevitably impact both the possible and the more probable relationships with a user.
This is a digital materiality.
In the previous chapter, the digital materiality of the web Sinaiticus interface was visible to the user through the four structured sections of the web page and the limited navigation options.
On a different level, typically not visible to most users, the HTML of the page and the XML of the transcription also play a role in the materiality of the interface, structuring the possible uses available in interface.[^forensic] Awareness of and facility with these often hidden materialities of digital interfaces and their relationship to the other layers of materiality involved in the production and use of digital interfaces is quickly becoming a necessary set of skills demanded of biblical scholars who wish to study bible in the emerging technological landscape.
To explore the kinds of capacities that might be needed to work closely with the materialities of bible interfaces at the programming and database level, I will analyze one digital bible interface, Digital Bible Library that functions as the database for two additional bible interfaces, Bible App and BibleSearch API, and pay attention to how their materialities interact.

[^forensic]: For a thorough outline of the scholarship on digital materiality in the last decade, see Sydney J.
Shep, "Digital Materiality," in Susan Schreibman, Raymond George Siemens, and John Unsworth, eds., *A New Companion to Digital Humanities* (Malden, MA, USA: John Wiley & Sons, Ltd, 2016), 386-396.
There are four main categories of digital materiality that emerge from the current scholarship.
Matthew Kirschenbaum offers the terms forensic and formal materiality, the former addressing the "evidence" of physical traces left by a digital artifact in processes such as storage and the latter describing the material aspects of a digital artifact that allow for its symbolic transmission, such as the HTML code underlying a web page.
In his best attempt to summarize the relationship between these two materialities, Kirshenbaum, *Mechanisms*, 15, writes, "Forensic and formal materiality are perhaps better brought to rest on the twin textual and technological bases of inscription
(storage) and transmission (or multiplication)." Building on Kirschenbaum's two pronged materiality and Jean-François Blanchette's notion of distributed materiality, Johanna Drucker, “Performative Materiality and Theoretical Approaches to Interface,” Digital Humanities Quarterly 7, no.
1 (2013), section 8, suggests a performative materiality for digital artifacts.
Much like her work with interface, here Drucker is shifting the focus of materiality from physical properties of a particular artifact to the process of producing materialities in the event that is interface.
Drucker's performative materiality is also close to Hayles's redefinition of an emergent materiality as "the interplay between a text’s physical characteristics and its signifying strategies" in “Print Is Flat, Code Is Deep: The Importance of Media-Specific Analysis,” *Poetics Today* 25, no.
1 (March 20, 2004): 72.
Both Drucker and Hayles articulate a concept of materiality that seems rather close to the notion of affordance at work in our analysis here, which further reinforces the usefulness of affordance as a reminder of the materiality of digital interfaces.
I have elected not to use any of the technical categories of digital materiality, because I am worried they will distract from the simpler point that digital interfaces have structures that shape possibilities and limits for use, just as pre-digital interfaces did.
Attention to these material structures and the affordances they bring in interface remains a critical part of our work as bible scholars.

The second shift involved in a move toward exploring digital bible interfaces is a growing attention to the proliferation of interfaces.
By proliferation, I simply mean the continual building of interface upon interface, which in turn could give rise to another interface, and so on.
Emerging digital technologies highlight the proliferation of interfaces that bible can become.
In one sense, proliferation of interfaces is not a new phenomenon for bible.
Wachtel's suggestion that Codex Sinaiticus may have become an exemplar for scribes to use to produce additional copies of the manuscript illustrates one kind of proliferation of interface.
Given the broad definition of interface as relationality irreducible to consumption articulated in chapter one, we could also imagine a proliferation of interfaces from the study of a codex bible by a preacher (interface 1) that gives rise to a sermon that preacher gives on a bible passage that is pondered by a parishioner (interface 2), who takes that bible verse and writes it on a protest sign in a march against immigration (interface 3).
The sign with the verse gets photographed, tweeted, and discussed on the internet for days (interface 4).
One of the characteristics of the interfaces dealt with in this chapter is that they all participate in an ecosystem that is designed to facilitate the ongoing proliferation of bible interfaces as much as to facilitate particular user encounters with bible.
This value on enabling the ongoing construction of interfaces also points out that emerging digital bible interfaces may have both human users and machine users at different layers of the interface.
For example, the XML of the web Sinaiticus interface was designed for both human users (programmers had to be able to produce, read, and understand the XML) and machine users (their site generator software had to read the XML to produce HTML for the web page).
In this chapter we will see two examples of a bible interface (BibleSearch API, Bible App) built upon another bible interface (Digital Bible Library), one of which is built explicitly to afford the design of additional bible interfaces by users around the world.

## The Bible of Bibles ##

One bible interface that decidedly moves into a digital materiality is a recently emerging project called the Digital Bible Library (DBL).
At its simplest, The Digital Bible Library (DBL) operates as a giant storage container that can hold any item related to bible.[^iconicity]
At the time of their public April 2017 Content Update, DBL contained 1508 text entries in 1145 unique languages and 444 audio entries in 374 unique languages.[^2]
The governing impulse behind this bible repository is to make the content of the bible, "Scripture translation content," available in "every language spoken on earth." The mention of every tribe in every nation here signals the deep involvement in DBL of the alliance of bible translation agencies known as "Every Tribe Every Nation" (ETEN).
DBL is the primary project funded and managed by ETEN and a quick glance at the homepage of their website shows how ETEN locates DBL in the trajectory of technological innovation begun by Gutenberg.[^4] The fact that DBL is funded and managed primarily by an aggregation of bible translation agencies helps explain why the content of this library is primarily focused on bible translations, which seems to come with a bias toward bible as reducible to linguistic content.
For all of the language of validation, safeguarding, and authorizing in the DBL mission and vision statement, there is little awareness of the impact of interface on the relationship between users and content.[^3]
While DBL provides a mechanism for validation and authorization of the linguistic content of a bible, it shows very little interest in controlling the interfaces built around this content except through policing which institutions can hold a DBL Library Card.

[^iconicity]: In its aim to become the definitive, comprehensive, and authoritative source for all things bible, DBL performs the cultural iconicity of bible as defined by Timothy Beal, *Rise and Fall of the Bible*, Kindle location 66-74.
Beal, *Rise and Fall of the Bible*, Kindle location 2006, also helpfully reminds us that bible has always been a kind of library, gathering a cacophony of voices and writings together from different times and places, such that DBL could even be viewed as a bible of bibles.

There are two reasons why I am considering DBL a bible interface even though it may seem more like simply a repository of bible interfaces.
First, DBL provides the data backend for one of the most widely used bible interfaces in the world, YouVersion's Bible App.
As a database that provides structured bible translations for the Bible App, DBL is a part of the materiality of the Bible App that goes largely unnoticed or even considered by users or scholars of bible.
Second, DBL provides a platform for proliferation, allowing others to create any number of bible interfaces using the artifacts and data available in the library.
In fact, DBL itself is a proliferation of interfaces with a web interface for participants to manage their licenses,[^web] an interface with the primary bible translation management software used by translators around the world, ParaText,[^paratext] and their application programming interface that allows users to download translations for use in building other interfaces.[^api] 
While the licensing and distribution aspects of DBL still operate in a paradigm primarily governed by the ideologies of book production, the interfaces enabled by DBL are pushing bible beyond its long history of governed by the page.
After an introduction to the technological and cultural situatedness of DBL, I will look closely at two interfaces that interface with DBL, the incredibly successful and popular mobile bible app from YouVersion and the American Bible Society's BibleSearch API.
In different ways, these two bible interfaces provide a definitive move beyond the book for bible, while continuing to afford high surface area, collaboration, and anarchy through their exploration of emerging technologies.

[^web]: DBL user login, https://app.thedigitalbiblelibrary.org/user/login?_next=/, accessed on September 9, 2017.
[^paratext]: DBL Complete Workflow, https://app.thedigitalbiblelibrary.org/static/docs/about.html#complete-workflow, accessed on September 9, 2017.
[^api]: DBL API, https://app.thedigitalbiblelibrary.org/static/docs/api/index.html, accessed on September 9, 2017.

## Bible in XML ##

On a closer look at the workflow and data structure of DBL, it is clear that the foundational unit for the datastore is the textual content of a particular translation, which is no surprise given the translation context from which this whole project arose.[^8] The data stored in DBL comes in two forms, an archive bundle and a release bundle.
The archive bundle is simply a highly redundant backup of the project files used to produce a given bible text so that the project can be reconstituted if lost.
The release bundle is what becomes part of the interfaces we will discuss below and is the primary bible interface of DBL.
An example of this DBL bible interface looks like this,

~~~
    <para style="p"> ...
Large crowds followed him from Galilee and the Ten Towns, from Jerusalem, Judea,
    and the land on the other side of the Jordan.</para>
    <chapter number="5" style="c" />
    <para style="s">The Sermon on the Mount</para>
    <para style="p">
    <verse number="1" style="v" />Jesus saw the crowds and went up a hill, where he sat down.
    His disciples gathered around him, <verse number="2" style="v" />and he began to teach them:</para>
~~~

Like we saw with the transcription data of the Codex Sinaiticus web bible interface, this release bundle data in DBL is encoded in XML (Extensible Markup Language).
The materiality of this XML code becomes a part of the material limits and possibilities of the bible interfaces built from the DBL.
The users of this XML are both human programmers, who need to be able to read this code in order to build interfaces from it, and other machine interfaces that will process this XML code to construct the bible interface used by more typical bible users looking to read the contents.
In syntax, XML is similar to HyperText Markup Language (HTML), the more familiar markup standard that web browsers read to present web pages to a user.
Two important differences between HTML and XML are 1) HTML is used to display data, while XML is used to describe data and 2) HTML tags are fixed and standard, while XML tags are flexible and defined as they are used.
Although any XML document can define its own structure and tags, there are often advantages to using a standard encoding practice to allow for predictable processing across multiple documents.
The XML used by DBL is a specialized encoding standard designed specifically for digitizing biblical texts called Unified Scripture XML (USX).[^9] This particular USX standard holds together the versification needs of bible data and continues to contain encoding for structural and style definitions that might be useful for producing print versions of the digitized text.
Given ICAP's history of making software to assist in print production of bibles and the continued high demand for print bibles in the world, this print based encoding makes sense.
This is another example of how new interfaces reproduce features of their predecessors.[^10] The smallest textual unit of this USX encoding is the biblical verse, not the word like we saw in the Codex Sinaiticus Project transcription XML.[^11] 

The way the XML of a DBL bible works is through a hierarchical structure of tagged entities with attributes and content.
In the example above, the tags are designated by the brackets "<>," which define "paragraph," "chapter," and "verse" tags in this particular selection.
As I mentioned above, XML allows for developers to create any tag they need, so the naming and structuring of tags can tell us something about the assumptions and values of an interface.
All tags in XML have some form of opening and closing.
The simplest form of this open/close syntax is demonstrated by the \<para\> tags in this sample.
You will notice that each \<para\> tag in the code is followed somewhere later in the code by a \</para\> tag, these mark the opening and the closing of a paragraph, respectively, with the forward slash indicating a closure.[^12] Everything contained between these tags is a part of that paragraph element, which can include text as well as other tags, specifically tags to indicate verses.
Given the typical difference between XML and HTML I mentioned above, where HTML deals with displaying data and XML with describing data, the presence of \<para\> tags in this DBL XML is surprising.
Chapter and verse tags make sense, since these would be describing and labeling the kind of data in the interface.
A paragraph tag has more to do with display than with type of data.
In fact, one of the core tags used in most HTML standards is a paragraph tag, \<p\> instead of \</para\>.
Yet, in the DBL bible interface, paragraph operates as a data descriptor at the same level in the hierarchy as book and chapter elements.
The prominence of the paragraph element in the XML of the DBL bible interface suggests that though this interface has made a move away from the dominance of the page as the primary unit of encounter for a user, the structural and stylistic demands of organizing text on a page remain a part of the dataset that constitutes bible.


If we look at the style attribute values of the paragraph element in this USX standard used by DBL, we can see the demands of print production of bibles at work.[^13] In XML, attributes are additional data that indicate specific details about a given element defined by a tag to offer additional data to describe this element.
In the example above, each \<para\> element has a style attribute indicated by the keyword "style" inside the brackets that define the tag followed by an equals sign and a value, such as \<para style="p"\>.
A given tag can have multiple attributes that offer different kinds of additional information about the element.
For example, the verse and chapter tags in our sample have both a number attribute and a style attribute.
The style attribute in the paragraph elements of DBL XML functions much like the style definitions in a word processor like Microsoft Word.
In Word, a user can select a style of "Heading 1" or "Quote" or "Footnote" for a particular selection of text in the document and Word will apply a predefined set of formatting rules to that unit of text, such as font size, emphasis, and distance from the margins, to name a few.
The predefined set of possible values for the style attribute of the paragraph element in the XML of DBL provide a mechanism of uniform formating for like elements within a bible, much like the heading and quote styles found in Microsoft Word.
A \<para\> style attribute value of "p" indicates a normal paragraph, which signals that no additional formatting is needed for the content of that paragraph element.
In our sample XML, we have one paragraph element with style="s", indicating a section heading, which can then be treated differently than a normal paragraph when displayed.[^14] 

The ubiquity of this style attribute in the DBL bible interface indicates a continued investment in the control and standardization of the display of text on a page.
The release bundle that comprises the XML that is the interface with bible in DBL contains a styles.xml file that contains explicit definitions for each of the possible values of the style attribute.
Users of this DBL bible interface can elect to adjust these style definitions, choosing a particular font to render normal paragraphs or a different color to emphasize section headings.
Yet, the structure of these elements, the definition of headings and the beginning and ending of paragraphs is already cooked into the bible interface through these \<para\> elements and their style attributes.
Due to the involvement of DBL in the production of other bible interfaces in both print and digital forms, the XML encoding of DBL does the work of what is typically divided between XML and HTML, both describing the data of these bibles (XML) and establishing the appropriate parameters for displaying this data (HTML).
Including such explicit encoding for display and presentation in the XML of DBL bibles seems to continue to pay homage, perhaps anachronistically or unnecessarily, to the role of the book in defining bible as interface.[^also]

[^also]: This detailed attention to stylistic and structural elements in the XML of DBL also reinforces that bible as interface continues to exceed simply the content a bible contains.

## The Demands of the Page Remain ##

In terms of data description elements, the smallest unit in USX, the DBL XML standard, is the verse.
There are a few smaller elements in the USX hierarchy, such as the character element (\<char\>), the table cell element (\<cell\>), and the optional break element (\<optbreak\>), but as I noted with the paragraph (\<para\>) tag, these elements are focused on the display of data, not on its description.[^15] Since a verse element is always contained within a paragraph element in the USX hierarchy, the words of verses are functionally content of a paragraph, with the verse element simply indicating where a verse number should be inserted in the paragraph element.[^empty]
Though a subtle point, again we see the structure of text on a page emerge as the governing architecture in USX, with paragraphs containing verses.[^18] With verse as the smallest unit of data description in the XML of DBL and with the content of verses essentially functioning as content of paragraphs due to the hierarchical structure of the elements in USX, the DBL bible interface is lower surface area than it could be by encoding at smaller intervals, such as the word or the character.
We saw a similar tendency toward lower surface area in the XML of the transcription of the Codex Sinaiticus web interface, where the high surface area character by character processing demanded by *scripta continua* on the parchment page was lowered by the word by word encoding of the transcription.
The move from character to word to verse as the smallest unit of discrete data encoded in an interface is a consistent move toward lower surface area.
The lower surface area of the XML provides for more efficient processing on the user end.
If DBL XML encoded in a higher surface area manner, at the word or character level, then users of the interface (other interfaces such as a mobile bible study application in this case) would have to build in mechanisms for handling these additional surfaces, which could slow down or impede the ability of a user to work through this XML to render the text in an interface.
These design decisions toward lower surface area may increase the efficiency of use, but they can also over determine the contours of an interface such that the user has less demand to participate in the production of the interface.


[^empty]: Unlike the paragraph element, which includes explicit open and close tags, the verse element marks only the opening of a verse, not its end.
Technically, a verse element can be a child of the \<para\>, \<row\>, or \<cell\> elements, but row and cell elements are only used for tabular display of verses.
Instead of including a \</verse\> tag at the end of each verse, the verse element opens and closes in the same tag, such that technically, the words of the verse are not the content of the verse element, the verse element is empty.
The way a verse element indicates open and close in a single tag is to include the forward slash character at the end of the open tag, just before the close bracket.
So, instead of \<verse\>...\</verse\>, we have \<verse ...
/\>.
In the strictest terms, the verse element has no content, since there is no data in between an open and close tag.
A verse element simply has attributes such as number, style, and alternative verse numberings.
Each verse tag includes at least a style and a number attribute, with "v" for verse as the only acceptable value for the style attribute and number having a value that indicates the sequential number of the verse within the chapter of which it is a part.
Since there is only one acceptable value for the style attribute of the verse element, this attribute is entirely redundant and unnecessary, since the tag name already identifies the element uniquely as a verse.
The style attribute is also redundant in the chapter element, which has exactly the same structure as the verse element, but indicates the beginning of a chapter, not a verse, and the chapter element is not a child of the paragraph element.

## Interfacing Interfaces ##

DBL is designed with interface proliferation in mind, meaning DBL is an interface for other interfaces.
The release bundle XML interface I have just described is intended produce another bible interface such as a print edition, a kindle bible, or a web interface that affords access to several translations at once.
Even though the print paradigm encoding governed by the paragraph is present in the DBL interface, a particular user designing a different interface could choose to manipulate the material structures of the XML to resist or alter the conventions embedded in this DBL bible interface.
There are explicit suggestions and demands for how a DBL bible is to be used in the construction of a new interface, through the structure of the XML, the style definitions, and the licensing requirements contained in the release bundle.
Yet, the attempted persuasive language of "should" used by the documentation for the elements of the DBL XML standard highlights the collaborative and anarchic affordances of this DBL bible interface.[^19] Because the XML of DBL does not contain explicit HTML code or complete print layout definitions, the DBL bible interface demands a user to participate in the construction of the bible.
This complicated relationship between users and an interface that seeds the development of new interfaces also points to the inability of the DBL XML to govern entirely how users will participate in constructing the next layer of interface, an anarchic affordance.

As we have seen with a close look at the XML of DBL bibles, DBL can not be reduced to simply a data or content source for bible interfaces, it is an interface of its own.
Yet, the vast collaborative capacities afforded by the myriad ways to translate DBL XML into different media interfaces, working with the structural elements of the DBL interface, resists the ability of DBL to dictate or determine use of this bible interface.
One of the ways in which DBL attempts to mitigate these anarchic tendencies of its bible interface is to closely control who can be a library card holder, hence to have a high level of control over users of the interface.
The DBL bible interface is decidedly not public.
A user, which in this case is an institution such as American Bible Society or YouVersion, has to be a library card holder (LCH) in the DBL, which they also refer to as publishers, and abide by the licensing requirements of a given bible in order to have the ability to download and use a release bundle from DBL.
The criteria for becoming a LCH include 

> **Reputable Standing** – Only reputable organizations will be considered for participation in the DBL.
A reputable organization is one that follows the historic tenets of Christianity
**Cooperation** – While we don’t expect all partners to hold to similar confessional practices or standards, we do expect them all to be able to operate cordially and constructively with all ETEN members, including the inter-confessional ones.
Applying organizations should not have any outstanding conflicts with any current ETEN partners or other Library Card Holders.[^20]

Unlike the Codex Sinaiticus web bible interface, which was released to any user that has access to the internet, the DBL interface is only available to those approved by the Partnership Credentials Committee.
The need for such a process of approval likely has to do with the sensitive copyright information being negotiated in the DBL, but at the same time, it functions as a means of limiting the anarchic tendencies built into the interface itself.
The four terms listed under the tag line for the DBL on the main page of their website are, in order, "Security," "Uniformity," "Availability," and "Accountability."[^21] The positioning of these terms is important.
Availability, the value that connects most closely to the anarchic tendencies of the DBL interface, is bracketed by security and accountability.
Only in the context of these kinds of controls does the DBL interface champion availability and the close attention to criteria for attaining a library card in DBL supports this kind of minimization of anarchy.
Technologically, DBL affords proximity in a reasonably high surface area interface, though lower than some others we have seen, that has expansive collaborative capacities and anarchic tendencies in the possibilities of developing new interfaces from the DBL interface.
In practice, there are logistical processes in place that could limit the range of collaborative capacities and anarchic tendencies available in the DBL interface.
To see how this negotiation plays out in practice, we will look at two of the early and significant users of the DBL bible interface, YouVersion bible app (bible.com) and American Bible Society's Bible Search site (bibles.org).

## Bible Goes Mobile ##

One of the main users of the DBL bible interface is the incredibly popular bible interface produced by Life.Church called YouVersion.[^22] It's utter dominance in the mobile bible market has allowed the app to take on the more generic name of simply "The Bible App."[^23] In the app store on Apple's iOS, the name of the app is simply "Bible" and their own language in the description of the app simply refers to it as The Bible App.[^24] Although this bible interface most definitely pushes far beyond the book in many ways, the icon for The Bible App is a cartoon representation of a leather bound print codex with a red silk bookmark and the title "Holy Bible" in gold letters on the cover.[^25] The iconicity of bible as book still has a role to play even in these emerging interfaces that seem to crack its binding.[^26] Though the Bible App works in a web browser and on any internet capable mobile device on the market today, I will focus on the operation of the Bible App on an iPhone 7 running iOS 10.3.
As I have mentioned before, each different device interface offers different affordances in concert with the Bible App interface, yet the basic insights about the possibility for proximity in interface would apply to all of the possible devices.


Perhaps the place to begin with a bible interface like the Bible App, which is used predominantly on mobile devices, is a consideration of the high surface area promoted by the sheer number of users of this interface.
The number of users of a roll or codex bible interface are quite limited given geographical, social, and literacy limitations.
A Kindle bible interface is limited by the finances of purchasing the Kindle book and having a device that can read Kindle books.
The Codex Sinaiticus Project speaks often of its one million visitors, which is a massive expansion of accessibility in terms of a single bible interface.
DBL as an interface only has a handful of library card holders, so the number of users is kept to a minimum.
The Bible App has a counter on their site's home page that tracks the number of unique devices that have installed the "completely free, with no advertising and no in-app purchases" mobile app.
Of course, this number is always expanding, but at the time of writing this sentence, the number of devices having downloaded the Bible App was 270,763,095.
Nearly three hundred million devices using this one bible interface is a grand scale of high surface area.

## Our Daily Bread ##

Once a user opens the app, the expansive surface area continues.
At the time of this writing, the Bible App offers a user just over 1500 bible versions in over 1000 different languages and some of these versions include both audio and text.
Much like the codex bible was as much a library as a book, collecting together different writings from different contexts together in one interface, the Bible App too functions as a library of bible content in a consolidated interface.[^27] The home page of the app presents a user with an array of messages signaling things that can be done with the app or ways to get involved in the communities who use the app, such as downloading bible versions for offline use or participating in reading plans.
One of the predominant structures found in the Bible App interface is the Verse of the Day functionality, which also appears on the home page when users access the app.
Every day, a verse is selected and presented in text and in text over image form and offered to users across the platform.[^28] The text of the bible is broken into verse size bits and offered as a different surface each day of the year.
These daily bits are also gathered together in an aggregated Verse of the Day view in the interface to provide a calendrical navigation through the bible in image and text.
By breaking the text into verse sized bits, delivering them to a user out of context, and creating an ongoing emerging aggregation of these bits that need not reflect the organization of any original, the Verse of the Day function in the Bible App demonstrates both high surface area and anarchic tendencies.
The collaborative capacities of the Bible App interface are also on display in the Verse of the Day functionality, by allowing a user to attach their own image to the verse of the day and easily share this out through social media channels.
In the settings associated with the Verse of the Day, a user can elect to have the text and/or image verse of the day sent to their email or sent to the screen notifications of their mobile device (push notifications).
Though these settings offer efficient ways for users to contact the content provided by the Bible App interface, they could have an effect of disincentivizing user participation in the interface and thus lowering the surface are and collaborative capacities of the Bible App.
Surface area as a part of the affordance of proximity increases user involvement, it does not simply enable more efficient consumption of content.

## Reading as Participation ##

Moving from left to right along the global navigation of the Bible App interface, the next user option after Home is "Read."[^29] The primary reading interface does not require an account and offers a simple and accessible set of features for a user.
The textual area shows one chapter of scrollable text at a time including in-line verse numbers and copyright information at the bottom of each chapter.
A user can enable or disable options to show red letters, cross references, and footnotes when available in the text.[^30] Much like we saw in the Kindle bible interface, additional collaborative capacities in the interface affording user construction of the space include choice of font size, font type, and a light or dark background.
Unlike the Kindle bible interface, user selection of a larger font in the Bible App does not change the amount of text displayed on a single page, if we consider a page the scrollable text available at one time without having to navigate using the next page or previous page icons.
A Kindle user, by choosing a font size, actually determines the size of a page, requiring more page turns for larger fonts and vice versa.
In the Bible App, font size does impact how much text is on the viewable screen at a time and can increase or decrease the amount a user needs to scroll to get through the text.
Yet, structurally, in the Bible App, chapter defines the "page," not amount of text, and page numbers are not present anywhere within the interface.
In this way, the Bible App has made a decisive move beyond the book as an interface.


The basic navigation of the Bible App interface reinforces this chapter based structure.
There are simple forward and backward arrow icons at the bottom of the screen that allow the user to easily move linearly through the bible chapter by chapter.
At the top of the reader view, there are two selection menus that display the current book, chapter and version being displayed.
Clicking on the chapter selector menu allows a user to browse through the content of this bible version and choose a book and chapter to display.
The books in this selection list can by ordered by "traditional" canonical order, as they typically appear in print bibles, or alphabetically.
Changing bible versions is made simple by the version selector, which allows for filtering the list by language and offers a search function to locate a particular version by name or abbreviation.
Finally, the basic reading interface of the Bible App also offers search as a navigational option.
This exponential expansion of non-linear access to text affords a user an incredible amount of agency in participating in the interface.
A search for keywords, names, references, etc.
will return an aggregated list of verses from throughout the text that have some mention of or relationship to the search terms.
Clicking on any one of the verses returned will show that single verse alone in the interface, with an option to see the full chapter from which the verse comes.[^31] By default, these search results are returned in order of relevance, but a user can elect to have them listed in the order in which they appear in a print edition of the text, which they label as "traditional." Either sort order of a search result has the potential to bring pieces of the bible text near to one another that usually exist at a great distance.
For example, I just ran a search on the word "death" and the first two verses returned by relevance were 2 Kings 1:1 and 1 Corinthians 15:55.
These verses have no explicit connection within the typical structuring of the text, but the interests of the user articulated in the search function of the interface have constructed an emergent relationship.
This collaborative capacity of the Bible App that allows the user to construct new relationships between text in the interface leverages the nearness of the many points of contact with the bible and reinforces the distance of an inability to master the interface, since new combinations can be crafted all the time.


The collaborative capacities of the Bible App interface are most prevalent in the ways in which a user can interact with the text of bible versions in the interface.
By simply tapping on a verse in the text, the verse is underlined to identify that it is the focus and a user is present with anew set of menu options at the bottom of the screen.
A user can select a single verse or many verses at the same time, with a second tap on a verse deselecting it.
A user can not select a smaller unit of text than an entire verse, which is much lower surface area than a Kindle bible or the Codex Sinaiticus web bible interface, which both allow selection at the word level.
Given that the source of the bible versions in the Bible App is the DBL bible interface, which encoded verse as the smallest unit of text in the XML of the release bundle, it is not a surprise to see verse as the smallest unit in the Bible App.
The menu that appears when selecting a verse or group of verses allows a user to highlight the selection, share the selection with any channel available in the iOS sharing system, associate an image with the selection, compare the selection with other bible versions, bookmark the selection, add a note to the selection, copy the text of the selection, and see a list of related items attached to this selection by users from the Bible App community.
The highlighting, sharing, bookmarking, and note features we saw in the Kindle bible interface.


The two most interesting collaborative capacities in this verse selection menu are the "compare" and the "related" features.
The compare feature allows the user to look at the selected verse or verses in different versions together on the screen.
Using the version selector, I can pick any of the 1500 versions to include in the comparison.
There are 50 English language versions alone that could be read side by side to see the variability of translation and the semantic potential of a given verse just in a single language, let alone through comparison with other language systems.
This compare feature gives the user another way in the Bible App to construct the interface by choosing texts that are displayed together in an organization scheme decided upon by the user.
More importantly, the ability to see a verse in several different versions, some of which a user may not even be able to read fully, challenges the notion of a single text that governs all versions and can awaken the user to difference and ambiguity in the interface.
The anarchic tendencies of this compare feature can resist attempts by a user to master the interface by not allowing reduction of bible to a singular governing version.
Instead, the compare feature and the ever growing versions available can interrupt any tendency toward mastery and open users up to the emerging polyvocality of the text.


In concert with the note facility, the "related" feature of the Bible App opens a text beyond simply the words contained in the version file loaded from DBL.
A user can add a note to a verse and mark this note private, for friends only, or public.
If a note is marked public, then any other user can select the same verse and choose the related menu item and see this note.
On an iPhone 7, this list of related notes loads in a new screen so the text of the selected verse isn't visible anymore.
Instead, the user is presented with a reverse chronological, most recent first, list of notes added to this particular verse by users all over the world.
This list of notes on a given verse gives a user a window into the larger community of users engaging in the interface, much like we saw in the popular highlights feature of the Kindle bible.
There is not a reply or conversation mechanism in this part of the Bible App interface to facilitate in-line or ongoing dialog, but a user can request to "friend" another user and then contact them through the app.
This functionality of the Bible App enacts two layers of collaborative capacities.
First, it allows users to participate in shaping the interface with their own highlights and notes.
Second, this annotative and sharing feature provides the scaffolding for users to locate themselves within a reading community and has the potential to make connections between users.


There are many additional features offered by the Bible App that continue to push bible beyond book including that these features continue to evolve as the app matures.
The Verse of the Day and search features heighten the surface area of the interface by creating many points of encounter with the interface and resisting total mastery of all the interface contains.
The compare functionality provides a possibility for anarchic tendencies as different versions challenge a consolidation of the text of bible to any single expression.
The annotative capacities, particularly the "related" list of community notes on a verse expand the collaborative capacities of the Bible App interface by involving the user in constructing the space and encouraging connection with other users through sharing and friending.
Together, these characteristics suggest that the Bible App has all it needs to afford proximity, even if not always realized.
Perhaps these capacities for proximity can problematize the tendency to focus on bible interfaces beyond the book as doomed to distraction.[^32] 

## Bible API ##

The last interface I will consider is another user of the DBL, but with a very different interface than the highly developed mobile interface of the Bible App.
American Bible Society (ABS) is a Library Card Holder in the DBL and one of the founding partners.
As a Library Card Holder, ABS has built a bible interface called BibleSearch at bibles.org using data from DBL to provide a public web search engine for bible and an application programming interface (API) for bible content.[^33] The web search engine of BibleSearch is clean and simple and offers a great deal of the same functionality as the Bible App in a browser, without the multimedia capacities of the mobile app.
The more interesting interface offered by BibleSearch is their BibleSearch API, which allows developers to build new bible interfaces using the data BibleSearch has remediated from the DBL interface.
As we found with DBL, one characteristic of the emerging digital media landscape is the potential for a proliferation of interfaces.
With the BibleSearch API, we see a user (American Bible Society) building a bible interface from the bible interface of DBL in order to facilitate the construction of other bible interfaces.
Though the layers of interface in the mobile internet world are myriad, this proliferation is not a new phenomenon for bible.
With its significant borrowing from, interpretation of and building on the Hebrew Bible, the Christian Testament can be considered a bible interface constructed from an earlier bible interface.
Bishop Karen Oliveto offering a sermon in a chapel service is a bible interface built upon the interface of the biblical text and the liturgical sung response in said service offers another layer of interface.
This ongoing interface of interfaces has been a part of the life of bible since long before the advent of XML or APIs and this continuity is important as we consider bible as interface in our current emerging media landscape.


An Application Programming Interface (API) is just that, an interface, a space of encounter between two or more entities that is irreducible to the properties or content of any one participant.
Much like a graphical user interface makes it easier for a user to navigate a software application through interaction with graphical representations of objects and functions, rather than resorting to the obtuse syntax of a command line prompt, an API makes it easier for one software application to interface with another.
APIs are zones of contact where two software systems interact and negotiate a relationship based on rules and processes defined by the API.
In a growing landscape of application interoperability, APIs are becoming ubiquitous.
Google has several APIs, Twitter and Facebook have APIs, Amazon has APIs, and the list goes on.[^34] DBL has an API that we did not discuss earlier, which allows Intellectual Property Contributors and Library Card Holders easy read only access to metadata (attributes describing the data in a translation) and file downloads for DBL content for which they have a license.[^35] The BibleSearch API offers programmatic access to a select set of DBL bible content for any registered BibleSearch user, which anyone can become.
The BibleSearch API is taking secured and authorized DBL bibles and making them available to a much larger public than has access to DBL.
Given the copyright and licensing constraints on public access to bibles in DBL, it is no surprise that the number of bible versions available in the BibleSearch API is much smaller than those existing in DBL.
The BibleSearch team at ABS is working hard to offer more access in the API, but currently there are 302 versions available in 276 langauges, a fifth of the versions made available to the public through the Bible App.[^36]

## BibleSearch Interface ##

So, what does this bible API look like? The best way to see the operations of this interface is by using it, but through the documentation provided by BibleSearch, much can be learned about the API.[^37] The introduction to the documentation makes it clear that the API is designed for developers and is not intended for commercial use.
The language of the documentation suggests that the API is a means of including "Scripture content and text" in as site or application.
Though the data available in the BibleSearch API is oriented around biblical text, the interface can not be reduced to the content available within, it is a framework upon which new bible interfaces can be built.
To use this bible API, a user need not meet the complicated criteria for becoming a Library Card Holder in the DBL.
All a user needs to do is register an account to identify themselves within BibleSearch and provide a brief description of the interface/application being built to use the BibleSearch API.
These barriers to use are far lower than for DBL, allowing exponentially more users to participate in the interface.
Like DBL, the BibleSearch API administrators do provide some stated guidelines for use to help mitigate the potential anarchy of the openness of the interface.
The second in their list of frequently asked questions, titled "How can I use the data?," says, 

> You cannot use the Scripture content retrieved from the API for any commercial purposes, nor in any application that is illegal, offensive, obscene, violent, immoral, or derogatory towards others or the Scriptures itself.
Basically, play nice.
Don't alter or change the meaning of the Scripture, or how it could be interpreted.[^38]

The focus on bible as content here is pronounced, but there is also a distinct awareness of the vast possibilities for use of this bible interface.
Again, a caution about use of bible is not a new phenomenon in our emerging technological landscape.
It doesn't take much effort to recall violent and derogatory uses of earlier bible interfaces throughout history, such as war, slavery, and oppression of difference.
Yet, that a developer could use this API to build a new bible interface that enacts or propagates these harmful adjectives to an uncontrollably large internet audience does perhaps introduce a heightened scale into the caution here.
The final clause of these brief guidelines for use betrays an utter lack of any concept of the importance of interface in the construction and use of bible.
Even if bible were reducible to content alone, this articulation of the already established and static meaning and possibilities for interpretation of bible devalues the role of readers as users.
More poignantly, as I have been arguing since the beginning of this project, this anxiety over the dynamic potential of bible ignores the proximity afforded by bible as interface, holding together the nearness of use and the distance of exceeding mastery.
It is not lost on me that this naivte about the power of the proximity of interface probably contributes to the willingness of ABS to offer this API at all.


The BibleSearch API is a read-only API that provides either XML (eXtensible Markup Language) or JSON (JavaScript Object Notation) results through HTTPS (Secure HyperText Transfer Protocol) GET requests.
Let us look more closely at each of these technical aspects of the API, in reverse order.
HTTPS GET requests are basically what we run when we enter a web address into a browser address bar or click on a link, asking (GET) for a server somewhere to return to us a page and its data in a web browser.[^39] Like we saw in the DBL bible interface, the BibleSearch API provides users access to bible via XML or an alternative data encoding language called JSON.
Like XML, JSON is self-describing hierarchical data description notation, meaning the elements in a JSON data set and their hierarchy are defined by the data itself, not by some external standard.
Instead of the open and close tag notation syntax of XML, JSON is structured by a hierarchy of objects that contain key/value pairs.[^40] We will see more specific examples of JSON below when we look more closely at the API in use.
Finally, the BibleSearch API is read-only, which indicates that this API only allows users to view data and does not allow users to modify, add, or delete data in the interface.[^41] The fact that the BibleSearch API uses familiar HTTP methods and common data encoding standards for the results of these methods makes this bible interface more accessible to a larger population of users.
Limiting the interface to read-only decreases the collaborative capacities of the interface, since users can not make any marks on the interface itself to participate in constructing the space of the interface.
On the other hand, the myriad uses that this interface can afford beyond a simple "reading" of the JSON results does allow users to construct interfaces with greater collaborative capacities.

## Requesting Bible ##

To begin participating in this bible interface, I had to register an account with BibleSearch and then register an application that will be using the API.
This registration process provides an authentication token that must be used every time I as a user participate in the interface through the API.
Though this registration and authentication provides an efficient and comprehensive means for BibleSearch to monitor a user's behavior in the interface, the barriers to attaining this access in the first place are incredibly low, particularly compared to the criteria required to become a Library Card Holder in DBL.
So, in one sense, the BibleSearch API is providing a public interface for a limited subset of the DBL interface, which is more tightly controlled.[^42] The simplest way to describe the structure of this API interface is that it consists of endpoints that take requests and return responses.
An endpoint in this case, such as the verses endpoint, is a URL that provides instructions for a user to request a particular response from the API.
For example, to request a specific verse from a particular version with a JSON response I would use syntax modeled by 

    GET /verses/#{version_id}:#{book_id}.#{chapter_number}.
    #{verse_number}.js?include_marginalia=true

In this schematic, we see the explicit GET method I referenced earlier and then we have "/verses/," which stipulates the verse endpoint of the API.
The rest of the items in this URL are parameters or instructions a user passes to the endpoint to ask for a specific verse.
The version_id is a unique code identifying the specific version from which the verse will be requested.[^43] Book_id is an abbreviation for the biblical book in which the verse is located and these abbreviations are based on the Open Scripture Information Standard (OSIS) definitions for biblical books.[^44] Chapter_number and verse_number are numerical values that identify the specific verse requested.
The ".js" in the URL tells the API that a user wants the results in JSON rather than XML.
Finally, "include_marginalia=true" is an optional flag that can be passed in the API request to include footnotes and cross references in the response along with the indicators for these notes within the text itself.
So, if a user wanted to request a JSON response for the sixth verse of the third chapter of 2 Corinthians in the English Standard Version, including footnotes and cross references, the API request would look like:[^45]

    GET https://bibles.org/v2/verses/eng-ESV:2Cor.3.6.js?include_marginalia=true

This API based verse request interface is essentially the same as a verse picker browse function in a web browser, where a user would select a version, book, chapter and verse from a list and select the option to display footnotes.
The passage selection mechanism of the Bible App we explored earlier could use the graphical user interface of the mobile app to construct this very kind of API request to send to a server and return the results, formatted for reading on a screen, to a user.
The BibleSearch web interface does just this, taking the user input from the version and chapter selections at the top of the page and constructing an API request much like we have seen above.[^46] Here we see BibleSearch itself building layers of interface upon the interface of DBL.
The BibleSearch web bible interface is a user of the BiblSearch API, which is a user of DBL bible interface.
Bible interfaces in this emerging media landscape continue to challenge any stark boundaries between user and interface as interfaces become users and users construct new interfaces on the fly.


## Bible as Data Objects ##

The response from the sample API request we constructed above contains several pieces of data related to the request, including copyright information, next and previous verse identifiers to provide context for this verse and easy machine navigation, the parent object of this verse (2 Corinthians book object), and the verse information including verse number, verse text, and footnotes and cross references.
One advantage of an API type interface is that the textual content of the verse is explicitly only one piece of the bible object that makes up this interface.
The verse content itself is only one contact point with this interface, reinforcing the irreducibility of bible to the content it contains.
In the small selection below, I show both the list of keys that make up the JSON response from this verse request and the value of the text key.

~~~
verse object keys = ['footnotes', 'reference', 'label', 'auditid', 'prev_osis_id', 'copyright', 'verse', 'id', 'previous', 'lastverse', 'parent', 'crossreferences', 'text', 'next', 'next_osis_id', 'osis_end']

'text':  '<p class="p"><sup id="2Cor.3.6" class="v">6</sup>who has made us '
         'sufficient to be <a href="#2Cor.3.6!x.1" id="link_2Cor.3.6!x.1" '
         'class="notelink x-link"><span>+</span></a> ministers of <a '
         'href="#2Cor.3.6!x.2" id="link_2Cor.3.6!x.2" class="notelink '
         'x-link"><span>+</span></a> a new covenant, not of <a '
         'href="#2Cor.3.6!x.3" id="link_2Cor.3.6!x.3" class="notelink '
         'x-link"><span>+</span></a> the letter but of the Spirit.
For the '
         'letter kills, but <a href="#2Cor.3.6!x.4" id="link_2Cor.3.6!x.4" '
         'class="notelink x-link"><span>+</span></a> the Spirit gives '
         'life.</p>'
~~~

The "text" of the verse object is indicated by the 'text' key followed by a colon and then the long string following the colon is the text value of the verse object.
The ESV text of this verse, 2 Corinthians 3:6 is very short, "who has made us sufficient to be ministers of a new covenant, not of the letter but of the Spirit.
For the letter kills, but the Spirit gives life." All of the other encoding in the text of the verse in the API interface is an HTML translation of the XML provided by the DBL interface for this verse.
You will recall the \<para\> and \<verse\> elements from the DBL XML that had style values of "p" and "v" respectively.
In the HTML of the text of this verse object from the API, we see \<p class="p"\> as a translation of the DBL \<para style="p"\> and \<sup id="2Cor.3.6" class="v"\>6\</sup\> as a translation of the DBL \<verse number="6" style="v"/\>.
All of \<a\> and \<span\> elements in the HTML of the verse text are constructing the mentions of cross references in the text.
The href attribute of the \<a\> element maps to the "id" attribute of one item in an ordered list of cross reference objects returned by the API in this verse request.


Including cross references like this in the API contributes to the surface area of the interface by providing more points of contact within the verse that interrupt a user's ability to contain the verse by pointing toward other places in the biblical text.
Interestingly, these cross reference objects are not formatted in such a way to make it easy for an application or a user to link from the verse in view to the verses mentioned in the references.
Providing easy linkability by formatting the references using syntax that could easily be passed back to the API would increase the surface area and collaborative capacities of this interface even further by providing avenues for the user to construct different pathways through the text.
Cross reference objects are just one example of the many points of contact provided by this API bible interface.
As we saw with DBL and the Bible App, the verse is the smallest unit in the API bible interface, yet the JSON results contain many distinct access points for the verse beyond just the content of the text of the verse, as demonstrated by the keys list in the sample above.
The JSON structure of a verse object makes it clear that a verse has many more properties than simply the words it contains.
Although each verse object contains data contextualizing it within the larger textual framework, such as next, previous and parent attributes, the sheer fact of constructing verses as objects that a user can engage and use individually foregrounds the typical role of bible as an aggregation of distinct objects rather than a homogeneous whole.


The read-only nature of the BibleSearch API definitely limits the collaborative capacities available in this interface.
If a user could write back to the API notes or amendments or other assets that might relate to a verse, such as images, videos, links, etc., this bible interface would provide more opportunities for users to participate in the construction of the space.[^47] Yet, the fact that a user has to learn how to construct an API request using some form of application language, such as perl, python, php, etc.
demands a level of participation that we may not find in some of the other interfaces considered here.
Of course, any bible interface carries with it some kind of linguistic or semiotic demands to engage the text for more than its aesthetic material value.
In these emerging media interfaces of bible that are built primarily as platforms upon which users will build new interfaces, the demands for participation are quite high because a user has to have the literacies and capacities to both interpret the responses from the interface and to construct something meaningful from them.
It is part of our task as bible interface explorers to evaluate the possibility for the affordance of proximity in each layer of these proliferating and integrated interfaces.
Much like the roll interface shaped some of the possibilities and limits of the codex, so each of these interface layers, such as DBL and BibleSearch API will impact the affordances of the interfaces built upon them.
We as scholars will need to continue to develop literacies at each layer of these interfaces in order to critically examine the assumptions at work.
It is my hope that this project is an initial experiment in that direction.

## Expanding the Anarchic ##

As I mentioned earlier, a bible interface that is expressly designed to encourage users to build other interfaces can present expansive anarchic tendencies.
Using the BibleSearch API, I could build an interface that constructs an entirely new bible version from a randomized selection of passages from different versions in multiple languages and present this to users in a web browser that allows them to move verses around to construct an entirely different narrative than was presented to them.
This kind of use most certainly challenges the reign of an original intention or singular principle governing the interface.
So, much like the community reading use of the roll bible we encountered with 1QIsa^a^, this API interface, in use, offers great potential for anarchic tendencies, even if American Bible Society has offered suggested guidelines for use that are less anarchic and has the ability to terminate a user's access at any time.
Within the structure of the API, there are also some anarchic tendencies at work.
Several endpoints in the API offer a query parameter or search function that can open up new combinations of verses and interrupt the dominance of the typical order of the text.
The API also provides a basic search endpoint that allows for passage or keyword requests.
A query based request to the API simply means a user is constructing a question to ask the API, rather than just providing explicit values for parameters to return a specific response.
The most interesting of the query based requests is offered in the verses endpoint, where a user can ask any keyword(s) question of the API and get a response that aggregates all verses that meet the criteria provided in the query.[^48] For example, if I want to find all mentions of "book" in the bible, I can make a request that looks like[^python_request]
    
    GET https://bibles.org/v2/verses.js?keyword=book

[^python_request]: The python code I use to run this API request is included here: 

	~~~
	import requests
	from pprint import pprint

	api_token = [my_personal_API_token]
	pass_fake = 'X'

	verse_endpoint = 'https://bibles.org/v2/verses.js?keyword=book'
	verse_resp = requests.get(verse_endpoint, auth=(api_token, pass_fake))
	verses = verse_resp.json()

	pprint(verses)
	~~~

The API response provides a very helpful summary object for this query request that tells me there are eight versions that have 318 occurrences of the keyword "book" across the Old and New testaments.[^summary]

[^summary]: The summary object looks like this: 

	~~~
	'summary': {'query':	'book',
	                        'rpp': 			'15',
	                        'sort': 		'relevance',
	                        'start': 		1,
	                        'testaments': 	['OT', 'NT'],
	                        'total': 		318,
	                        'versions': 	['eng-NASB',
	                                         'eng-ESV',
	                                         'eng-MSG',
	                                         'eng-KJVA',
	                                         'eng-CEVD',
	                                         'eng-AMP',
	                                         'eng-GNTD',
	                                         'eng-CEV']
	}
	~~~

In this single API request, I have constructed a collection of over three hundred verses that cross eight versions and two testaments based on my interests as a user in a single keyword.
In four additional lines of code, I can construct a single continuous text of 87,528 characters from a simple concatenation of these 318 verses.[^more_code]

[^more_code]: The additional lines of code with comments are

	~~~
	search_verses = verses['response']['search']['result']['verses'] # get just the list of verse objects from the API response
	book_bible = [] # define an empty list

	for verse in search_verses: # look through all 318 verses returned
	    book_bible.append(verse['text']) # add the text of each verse to the list

	print(' '.join(book_bible)) # print all items of the list joined by a space
	~~~

Here we see the anarchic tendencies of the API bible interface on display as I construct an entirely different text from the results of a keyword search.
This kind of use of bible also invokes the collaborative capacities and high surface area possible in this interface, while pushing us as users of bible far beyond the book.

## Demanding New Literacies ##

In all of the layers of interface from the DBL to the interfaces constructed by users of DBL, the Bible App and the BibleSearch API, we find the possibility of the affordance of proximity.
As bible evolves beyond the technological and cultural categories of book, there is undoubtedly a progression toward higher surface area in bible as interface, even though there is a tendency toward the verse as the smallest unit of the bible instead of the word or character as we found in some earlier book interfaces.
The collaborative capacities of book bible interfaces were embedded in the ability of a user to mark the surfaces of the interface through a scribal note or a public user highlight.
As bible emerges into a technological landscape that pushes beyond book, its collaborative capacities move toward the ability for users to make more layers of interfaces, which both DBL and the BibleSearch API demonstrate exquisitely.
The technologies of these emerging interface ecosystems will continue to expand the anarchic tendencies of bible by allowing users to build new interfaces that challenge the rule of a any original text or intention.
At the same time, with the increasing abilities to track usage in internet interfaces, the institutions running the platform bible interfaces like DBL and BibleSearch API will have the ability to police and curtail the extent of experimentation and shape the nature of collaborative capacities based on their perceptions of proper use.
Just as biblical scholars have invested in the layers of linguistic interface involved in bible, as bible moves beyond book into emerging technological interfaces, biblical scholars will need to develop the skills to analyze and critique the myriad layers of interface at work in each surface of encounter that is bible.
Instead of lamenting the difference and discomfort of bible on the screen, let us take up the challenge to learn new languages to carefully read and build new interfaces for bible as the book relinquishes its reign on knowledge and the bible.

[^2]: https://thedigitalbiblelibrary.org/2017/04/01/april-2017-content-update/, accessed on April 25, 2017.
The tracking of the number of unique languages involved in this content highlights the mission and vision of DBL and points toward one of the critical founding partners.
The mission and vision of DBL deserves full mention here, "The vision for The Digital Bible Library™ is to contain digital Scripture, in every language spoken on earth by the year 2033.
Its mission is to gather, validate, and safeguard Scripture translation content in a standardized digital format, and to empower partners to reach people from every tribe, in every nation, with the power of God’s Word in their heart language by providing authorized and licensed access to the library content." Digital Bible Library, "About," https://thedigitalbiblelibrary.org/about/ access on April 25, 2017.

[^3]: See the previous note for the mission and vision statement.
Here we have an example of promotion of an interface that falls into Drucker's critique of mechanistic determinism, taking no account of the participation of the user in constructing the interfaces that are a part of DBL.

[^4]: http://www.everytribeeverynation.org/ accessed on April 25, 2017.

[^8]: For a helpful look at the overall workflow of DBL and where it is located in the process of bible production and dissemination, see the diagram at http://app.thedigitalbiblelibrary.org/static/docs/about.html#complete-workflow, accessed on April 25, 2017.
The technical aspects of DBL are managed by the Institute for Computer Assisted Publishing (ICAP).
ICAP is a part of the United Bible Societies, an alliance of National Bible Societies all over the world that manage and produce bible translation projects.
ICAP was instrumental in developing ParaTEext, http://paratext.org/, access on April 25, 2017, the software used by bible translation projects globally.
Since it is so heavily involved in the translation production process already, ParaTExt has naturally become the primary mechanism for getting items into DBL.
In this sense, ParaTExt is one of the many interfaces that participate in DBL.
Technically, DBL is considered one part of a larger digital scripture development ecosystem that includes ParaTExt and other tools.
See https://thedigitalbiblelibrary.org/about/ visited on April 25, 2017, for more details on this ecosystem approach.


[^9]: For detailed description and documentation of the USX 2.5 standard, see http://app.thedigitalbiblelibrary.org/static/docs/usx/index.html, accessed on April 25, 2017.

[^10]: The Codex Sinaiticus Project transcription XML had to include a great deal of positional data in the encoding to support the linking between the image and the transcription and the special formatting of the transcription in columnar form on the page.

[^11]: The XML of the SBLGNT also encodes all the way to the word level.

[^12]: This open and close syntax is identical to HTML.

[^13]: For a detailed description of all of the available style attributes in the \<para\> element, see https://app.thedigitalbiblelibrary.org/static/docs/usx/parastyles.html.

[^14]: For examples of the use of the section heading style attribute, see https://app.thedigitalbiblelibrary.org/static/docs/usx/parastyles.html#usx-parastyle-s.

[^15]: The character element allows for stylistic formating at smaller textual intervals than a while paragraph element.
The cell element describes the content and attributes of a single cell in a tabular structure.
The optbreak element simply indicates the position of an optional line break in section of text.

[^18]: When processing these XML files with a language such as python, the text of a given verse is more precisely identified as a "tail" of the verse element.
In the Element class of the etree module of the xml python library, a tail in XML is content that follows a close tag.
Since each verse tag in USX closes in the open tag and is then followed by the words of the verse, these words are part of the tail of the verse element.
Because the verse element is a child of the paragraph element, even its tails belong to the paragraph element, which is why I have articulated the words of verses here as content of paragraphs.

[^19]: For an example of this persuasive language, see the additional notes alongside the samples provided for the verse element at https://app.thedigitalbiblelibrary.org/static/docs/usx/elements.html#samples.

[^20]: For a full list of the criteria for being an LCH in DBL, see the LCH criteria accordion menu of the Library Card Holder tab on the Get Involved page of the DBL website, http://thedigitalbiblelibrary.org/get-involved/, accessed on May 7, 2017.
There are other criteria, but these two illustrate the non technical attempts to control who participates in this interface.

[^21]: https://thedigitalbiblelibrary.org/, accessed on May 7, 2017.

[^22]: Tim Hutchings has done some detailed description and careful sociological analysis of the religious use of YouVersion's Bible App in “Now the Bible Is an App: Digital Media and Changing Patters of Religious Authority,” in Religion, Media, and Social Change, ed.
Kennet Granholm, Marcus Moberg, and Sofia Sjö (New York: Routledge, 2014), 143–61.
In his recent volume, *Liquid Scripture: The Bible in a Digital World* (New York: Fortress, 2017), Jeffrey Siker also considers YouVersion's Bible app as one example of bible on screen.

[^23]: I will refer to YouVersion's app as the "Bible App" from now on to indicate the dominance this particular bible interface has garnered in the mobile application space.

[^24]: The web address for the bible app is http://www.bible.com.

[^25]: In her recent book on translation and bible, Sarah Ruden insightfully describes bible as book using an exact description of the icon used by the Bible App, writing, "To the eye, the book typically offers a pebbly black vinyl cover (like nothing on a book you'd yearn to open up and explore), gold–colored insert title ("The Holy Bible," which to a lot of people says, "I think I'm too holy for you to touch"), and a withered–looking ribbon bookmark attached at the spine (as if it would be a big problem to lose your place in the ordinary way, and stray from the prescribed devotional verses)." Sarah Ruden, *The Face of Water: A Translator on Beauty and Meaning in the Bible* (New York: Pantheon Books, 2017), xv-xvi.

[^26]: This bound print bible icon is what identifies this bible app among other apps on a user's mobile device and is the favicon (image that shows in the tab for the site) and centered at the top of bible.com.
The primary visual brand of the bible app is this bound print bible icon.

[^27]: These version statistics are presented to the user of the Bible App at the top of the Versions view in the mobile app.
These versions come from the DBL interface I discussed above.
Comparing the May 2017 statistics from DBL to the number of versions available in the Bible App, we find that DBL holds 1535 text entries in 1154 languages, slightly higher numbers than included in the Bible App.
See http://thedigitalbiblelibrary.org/2017/05/01/may-2017-content-update/#more-917 for the report, accessed on May 8, 2017.

[^28]: At present, I am unable to find any information regarding the selection algorithm used for which verse is presented to users on which day.

[^29]: This global navigation menu is only available in portrait mode on a device the size of an iPhone 7.
When the phone is turned horizontally into landscape mode in the reader view of the Bible App, the global navigation goes away to make as much readable area on the screen as possible.

[^30]: The red letter and footnotes are set to on by default, while the cross references are turned off.
A decision to leave cross references off by default could decrease the surface area of an interface by eliding other points of contact related to the current verse in view.

[^31]: As is customary practice, the copyright information for the version used to display the verse is also included on the page.

[^32]: See Siker, *Liquid Scriptures*, ?? for an example of the anxiety around distraction with bibles on screen.

[^33]: BibleSearch also has a widget tool that embeds a search engine in another site and a highlighter tool that will read a site for bible references and link to BibleSearch content from the reference.
For mode details on any of these tools, see http://webtools.bible.
Incidentally, ABS was also the driver behind developing the .bible registry for domain names ending in .bible instead of .com or .org, etc.

[^34]: For a searchable exploration of available APIs, see https://www.programmableweb.com/apis/directory, which cataloged over 17,000 APIs at the time of this writing.

[^35]: For details about the available functions in the DBL API, see https://www.thedigitalbiblelibrary.org/dbl/static/docs/api/index.html#, accessed on May 9, 2017.

[^36]: For up to date statistics on available versions in the API, see http://bibles.org/versions_api, accessed on May 9, 2017.

[^37]: http://bibles.org/pages/api, accessed on May 9, 2017.

[^38]: http://bibles.org/pages/api, accessed on May 9, 2017.

[^39]: The "S" in HTTPS states that the communication between the browser and the server is secured through some form of encryption.
HTTP, the non-secure form of these GET requests and HTTPS are supported by the BiblesSearch API, but HTTPS is recommended.
The BibleSearch web interface uses their own API to deliver content to a browser based on a user request over HTTP.

[^40]: For a brief introduction to the syntax and structure of JSON, see http://www.json.org/, accessed on May 10, 2017.

[^41]: The read-only nature of the API effectively limits users to the GET HTTP method and excludes other possible methods such as PUT (edit), POST (add), and DELETE.
BibleSearch also suggests that this API is a RESTful API, which means that this is a web service that adheres to the architectural constraints of Representational State Transfer (REST).
The REST architecture was introduced in 2000 by Roy Fielding in his doctoral dissertation at University of California, Irvine, titled, *Architectural Styles and the Design of Network-based Software Architectures*, available at http://www.ics.uci.edu/~fielding/pubs/dissertation/rest_arch_style.htm, accessed on May 10, 2017.

[^42]: 

[^43]: For samples of version_ids and more details on the versions endpoint, see http://bibles.org/pages/api/documentation/versions, accessed on May 10, 2017.

[^44]: For more information on OSIS, see https://www.crosswire.org/osis/, accessed on May 10, 2017.

[^45]: The https://bibles.org/v2 is the trunk of all API endpoints including an explicit API version number "v2." If a request leaves out the explicit version, the request will use the default API version, which is currently "v1." Versions codes in the API contain both a language indicator and the version abbreviation, such as "eng-ESV" for English language - English Standard Version.

[^46]: See http://bibles.org to try the web interface for this API.
The main difference in the web interface is that it uses primarily the chapter endpoint to return all verses for a selected chapter of a selected version and it formats the results for viewing and interacting with in a browser.

[^47]: The BibleSearch web interface does allow users to tag verses with keywords and add notes to verses.
Currently, the API allows read access to the tags associated with a verse but not the notes and there is no way via the API to add or modify tags.
For more detail on the tags endpoint, see http://bibles.org/pages/api/documentation/tags, accessed on May 11, 2017.

[^48]: For a detailed look at all of the possible search criteria that can be passed to this verse search endpoint, see the Searching section of http://bibles.org/pages/api/documentation/verses, accessed on May 11, 2017.
[Finished in 0.1s]