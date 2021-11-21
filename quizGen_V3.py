# Importing Spacy
import spacy 
nlp = spacy.load('en_core_web_sm')

# importing NLTK utility functions
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk import tokenize
from nltk.corpus import abc
from nltk.corpus import wordnet
import en_core_web_sm


# word2vec
import gensim

# Other utility functions
from operator import itemgetter
import math

"""### Sample Texts"""

text1 = "It has long been accepted that the Americas were colonized by a migration of peoples from Asia slowly traveling across a land bridge called Beringia (now the Bering Strait between northeastern Asia and Alaska) during the last Ice Age. The first water craft theory about this migration was that around 11,000-12,000 years ago there was an ice-free corridor stretching from eastern Beringia to the areas of North America south of the great northern glaciers. It was this midcontinental corridor between two massive ice sheets—the Laurentide to the east and the Cordilleran to the west—that enabled the southward migration. But belief In this ice-free corridor began to crumble when paleoecologist Glen MacDonald demonstrated that some of the most important radiocarbon dates used to support the existence of an ice-free corridor were incorrect. He persuasively argued that such an ice-free corridor did not exist until much later, when the continental ice began its final retreat. Support is growing for the alternative theory that people using watercraft, possibly skin boats, moved southward from BerIngla along the Gulf of Alaska and then southward along the Northwest Coast of North America possibly as early as 16,000 years ago. This route would have enabled humans to enter southern areas of the Americas prior to the melting of the continental glaciers. Until the early 1970s, most archaeologists did not consider the coast a possible migration route into the Americas because geologists originally believed that during the last Ice Age the entire Northwest Coast was covered by glacial ice. It had been assumed that the ice extended westward from the Alaskan/Canadian mountains to the very edge of the continental shelf—the flat, submerged part of the continent that extends into the ocean. This would have created a barrier of ice extending from the Alaska Peninsula, through the Gulf of Alaska and southward along the Northwest Coast of North America to what Is today the state of Washington. The most influential proponent of the coastal migration route has been Canadian archaeologist Knut Fladmark. He theorized that with the use of watercraft, people gradually colonized unglaciated refuges and areas along the continental shelf exposed by the lower sea level. Fladmark's hypothesis received additional support from the fact that the greatest diversity In Native American languages occurs along the west coast of the Americas, suggesting that this region has been settled the longest. More recent geologic studies documented deglaciation and the existence of icefree areas throughout major coastal areas of British Columbia, Canada, by 13,000 years ago. Research now indicates that sizable areas of southeastern Alaska along the inner continental shelf were not covered by ice toward the end of the last Ice Age. One study suggests that except for a 250-mile coastal area between southwestern British Columbia and Washington State, the Northwest Coast of North America was largely free of ice by approximately 16,000 years ago. Vast areas along the coast may have been deglaciated beginning around 16,000 years ago, possibly providing a coastal corridor for the movement of plants, animals, and humans sometime between 13,000 and 14,000 years ago. The coastal hypothesis has gained increasing support in recent years because the remains of large land animals, such as caribou and brown bears, have been found in southeastern Alaska dating between 10,000 and 12,500 years ago. This is the time period in which most scientists formerly believed the area to be inhospitable for humans. It has been suggested that if the environment were capable of supporting breeding populations of bears, there would have been enough food resources to support humans. Fladmark and others believe that the first human colonization of America occurred by boat along the Northwest Coast during the very late Ice Age, possibly as early as 14,000 years ago. The most recent geologic evidence indicates that it may have been possible for people to colonize ice-free regions along the continental shelf that were still exposed by the lower sea level between 13,000 and 14,000 years ago. The coastal hypothesis suggests an economy based on marine mammal hunting, saltwater fishing, shellfish gathering, and the use of watercraft. Because of the barrier of ice to the east, the Pacific Ocean to the west, and populated areas to the north, there may have been a greater impetus for people to move in a southerly direction."
text2 = "Teachers , it is thought, benefit from the practice of reflection , the conscious act of thinking deeply about and carefully examining the interactions and events within their own classrooms. Educators T Wildman and J Niles in 1987 described a scheme for developing reflective practice in experienced teachers. This was justified by the view that reflective practice could help teachers to feel more intellectually involved in their role and work in teaching and enable them to cope with the paucity of scientific fact and the uncertainty of knowledge in the discipline of teaching. Wildman and Niles were particularly interested in investigating the conditions under which reflection might flourish subject on which there is little guidance in the literature. They designed an experimental strategy for a group of teachers in Virginia and worked with 40 practicing teachers over several years. They were concerned that many would be \"drawn to these new, refreshing conceptions of teaching only to find that the void between the abstractions and the realities of teacher reflection is too great to bridge. Reflection on a complex task such as teaching is not easy.\" The teachers were taken through a program of talking about teaching events, moving on to reflecting about specific issues in a supported, and later an independent, manner. Wildman and Niles observed that systematic reflection on teaching required a sound ability to understand classroom events in an objective manner. They describe the initial understanding in the teachers with whom they were working as being \"utilitarian and not rich or detailed enough to drive systematic reflection.\" Teachers rarely have the time or opportunities to view their own or the teaching of others in an objective manner. Further observation revealed the tendency of teachers to evaluate events rather than review the contributory factors in a considered manner by, in effect, standing outside the situation. Helping this group of teachers to revise their thinking about classroom events became central. This process took time and patience and effective trainers. The researchers estimate that the initial training of the teachers to view events objectively took between 20 and 30 hours, with the same number of hours again being required to practice the skills of reflection. Wildman and Niles identify three principles that facilitate reflective practice in a teaching situation. The first is support from administrators in an education system, enabling teachers to understand the requirements of reflective practice and how it relates to teaching students. The second is the availability of sufficient time and space. The teachers in the program described how they found it difficult to put aside the immediate demands of others in order to give themselves the time they needed to develop their reflective skills. The third is the development of a collaborative environment with support from other teachers. Support and encouragement were also required to help teachers in the program cope with aspects of their professional life with which they were not comfortable. Wildman and Niles make a summary comment \"Perhaps the most important thing we learned is the idea of the teacher-as-reflective-practitioner will not happen simply because it is a good or even compelling idea.\" The work of Wildman and Niles suggests the importance of recognizing some of the difficulties of instituting reflective practice. Others have noted this, making a similar point about the teaching profession's cultural inhibitions about reflective practice. Zeichner and Liston in 1987 pointed out the inconsistency between the role of the teacher as a reflective professional decision maker and the more usual role of the teacher as a technician, putting into practice the ideas of others. More basic than the cultural issues is the matter of motivation. Becoming a reflective practitioner requires extra work and has only vaguely defined goals with , perhaps , little initially perceivable reward and the threat of vulnerability. Few have directly questioned what might lead a teacher to want to become reflective. Apparently , the most obvious reason for teachers to work toward reflective practice is that teacher educators think it is a good thing. There appear to be many unexplored matters about the motivation to reflect for example , the value of externally motivated reflection as opposed to that of teachers who might reflect by habit. "
text3 = "When the Hawaiian Islands emerged from the sea as volcanoes, starting about five million years ago, they were far removed from other landmasses. Then, as blazing sunshine alternated with drenching rains, the harsh, barren surfaces of the black rocks slowly began to soften. Winds brought a variety of life-forms. Spores light enough to float on the breezes were carried thousands of miles from more ancient lands and deposited at random across the bare mountain flanks. A few of these spores found a toehold on the dark, forbidding rocks and grew and began to work their transformation upon the land. Lichens were probably the first successful flora. These are not single individual plants: each one is a symbiotic combination of an alga and a fungus. The algae capture the Sun's energy by photosynthesis and store It in organic molecules. The fungi absorb moisture and mineral salts from the rocks, passing these on in waste products that nourish algae. It is significant that the earliest living things that built communities on these islands are examples of symbiosis, a phenomenon that depends upon the close cooperation of two or more forms of life and a principle that is very Important in island communities. Lichens helped to speed the decomposition of the hard rock surfaces, preparing a soft bed of soil that was abundantly supplied with minerals that had been carried in the molten rock from the bowels of Earth. Now, other forms of life could take hold: ferns and mosses two of the most ancient types of land plants that flourish even in rock crevices. These plants propagate by producing spores tiny fertilized cells that contain all the instructions for making a new plant but the spores are unprotected by any outer coating and carry no supply of nutrient. Vast numbers of them fall on the ground beneath the mother plants. Sometimes they are carried farther afield by water or by wind. But only those few spores that settle down in very favourable locations can start new life; the vast majority fall on barren ground. By force of sheer numbers, however, the mosses and ferns reached Hawaii, survived, and multiplied. Some species developed great size, becoming tree ferns that even now grow in the Hawaiian forests. Many millions of years after ferns evolved but long before the Hawaiian Islands were born from the sea, another kind of flora evolved on Earth: the seed-bearing plants. This was a wonderful biological invention. The seed has an outer coating that surrounds the genetic material of the new plant, and inside this covering is a concentrated supply of nutrients. Thus, the seed's chances of survival are greatly enhanced over those of the naked spore. One type of seed-bearing plant, the angiosperm, includes all forms of blooming vegetation. In the angiosperm the seeds are wrapped in an additional layer of covering. Some of these coats are hard like the shell of a nut for extra protection. Some are soft and tempting, like a peach or a cherry. In some angiosperms the seeds are equipped with gossamer wings, like the dandelion and milkweed seeds. These new characteristics offered better ways for the seeds to move to new habitats. They could travel through the air, float in water, and lie dormant for many months. Plants with large, buoyant seeds like coconuts drift on ocean currents and are washed up on the shores. Remarkably resistant to the vicissitudes of ocean travel, they can survive prolonged immersion in saltwater. When they come to rest on warm beaches and the conditions are favourable, the seed coats soften. Nourished by their imported supply of nutrients, the young plants push out their roots and establish their place in the sun. By means of these seeds, plants spread more widely to new locations, even to isolated islands like the Hawaiian archipelago, which lies more than 2,000 miles west of California and 3,500 miles east of Japan. The seeds of grasses, flowers, and blooming trees made the long trips to these islands. Grasses are simple forms of angiosperms that bear their encapsulated seeds on long stalks. In a surprisingly short time, angiosperms filled many of the land areas on Hawaii that had been bare."
text4 = "China has one of the world's oldest continuous civilizations—despite Invasions and occasional foreign rule. A country as vast as China with so long-lasting a civilization has a complex social and visual history, within which pottery and porcelain play a major role. The function and status of ceramics In China varied from dynasty to dynasty, so they may be utilitarian, burial, trade, collectors', or even ritual objects, according to their quality and the era In which they were made. The ceramics fall into three broad types— earthenware, stoneware, and porcelain—for vessels, architectural items such as roof tiles, and modeled objects and figures. In addition, there was an important group of sculptures made for religious use, the majority of which were produced in earthenware. The earliest ceramics were fired to earthenware temperatures, but as early as the fifteenth century B.C., high-temperature stonewares were being made with glazed surfaces. During the Six Dynasties period (A.D. 265-589), kilns' In north China were producing high-fired ceramics of good quality. Whitewares produced in Hebei and Henan provinces from the seventh to the tenth centuries evolved into the highly prized porcelains of the Song dynasty (A.D. 960-1279), long regarded as one of the high points in the history of China's ceramic industry. The tradition of religious sculpture extends over most historical periods but is less clearly delineated than that of stonewares or porcelains, for it embraces the old custom of earthenware burial ceramics with later religious images and architectural ornament Ceramic products also include lead-glazed tomb models of the Han dynasty, three-color lead-glazed vessels and figures of the Tang dynasty, and Ming three-color temple ornaments, in which the motifs were outlined in a raised trail of slip', as well as the many burial ceramics produced in imitation of vessels made in materials of higher intrinsic value. Trade between the West and the settled and prosperous Chinese dynasties introduced new forms and different technologies. One of the most far-reaching examples is the impact of the fine ninth-century A.D. Chinese porcelain wares imported into the Arab world. So admired were these pieces that they encouraged the development of earthenware made in imitation of porcelain and instigated research into the method of their manufacture. From the Middle East the Chinese acquired a blue pigment—a purified form of cobalt oxide unobtainable at that time in China—that contained only a low level of manganese. Cobalt ores found in China have a high manganese content, which produces a more muted blue-gray color. In the seventeenth century, the trading activities of the Dutch East India Company resulted in vast quantities of decorated Chinese porcelain being brought to Europe, which stimulated and influenced the work of a wide variety of wares, notably Delft. The Chinese themselves adapted many specific vessel forms from the West, such as bottles with long spouts, and designed a range of decorative patterns especially for the European market.Just as painted designs on Greek pots may seem today to be purely decorative, whereas in fact they were carefully and precisely worked out so that at the time, their meaning was clear, so it is with Chinese pots. To twentieth-century eyes, Chinese pottery may appear merely decorative, yet to the Chinese the form of each object and its adornment had meaning and significance. The dragon represented the emperor, and the phoenix, the empress; the pomegranate indicated fertility, and a pair of fish, happiness; mandarin ducks stood for wedded bliss; the pine tree, peach, and crane are emblems of long life; and fish leaping from waves indicated success in the civil service examinations. Only when European decorative themes were introduced did these meanings become obscured or even lost. From early times pots were used in both religious and secular contexts. The imperial court commissioned work and in the Yuan dynasty (A.D. 1279-1368) an imperial ceramic factory was established at Jingdezhen. Pots played an important part in some religious ceremonies. Long and often lyrical descriptions of the different types of ware exist that assist in classifying pots, although these sometimes confuse an already large and complicated picture."
text5 = "One of the most difficult aspects of deciding whether current climatic events reveal evidence of the impact of human activities Is that it is hard to get a measure of what constitutes the natural variability of the climate. We know that over the past millennia the climate has undergone major changes without any significant human intervention. We also know that the global climate system is immensely complicated and that everything is in some way connected, and so the system is capable of fluctuating in unexpected ways. We need therefore to know how much the climate can vary of its own accord in order to Interpret with confidence the extent to which recent changes are natural as opposed to being the result of human activities. Instrumental records do not go back far enough to provide us with reliable measurements of global climatic variability on timescales longer than a century. What we do know is that as we include longer time intervals, the record shows increasing evidence of slow swings in climate between different regimes. To build up a better picture of fluctuations appreciably further back in time requires us to use proxy records. Over long periods of time, substances whose physical and chemical properties change with the ambient climate at the time can be deposited in a systematic way to provide a continuous record of changes in those properties over time, sometimes for hundreds or thousands of years. Generally, the layering occurs on an annual basis, hence the observed changes in the records can be dated. Information on temperature, rainfall, and other aspects of the climate that can be inferred from the systematic changes in properties is usually referred to as proxy data. Proxy temperature records have been reconstructed from ice core drilled out of the central Greenland ice cap, calcite shells embedded in layered lake sediments in Western Europe, ocean floor sediment cores from the tropical Atlantic Ocean, ice cores from Peruvian glaciers, and ice cores from eastern Antarctica. While these records provide broadly consistent indications that temperature variations can occur on a global scale, there are nonetheless some intriguing differences, which suggest that the pattern of temperature variations in regional climates can also differ significantly from each other. What the proxy records make abundantly clear is that there have been significant natural changes in the climate over timescales longer than a few thousand years. Equally striking, however, Is the relative stability of the climate in the past 10,000 years (the Holocene period). To the extent that the coverage of the global climate from these records can provide a measure of its true variability, it should at least indicate how all the natural causes of climate change have combined. These include the chaotic fluctuations of the atmosphere, the slower but equally erratic behavior of the oceans, changes in the land surfaces, and the extent of ice and snow. Also included will be any variations that have arisen from volcanic activity, solar activity, and, possibly, human activities. One way to estimate how all the various processes leading to climate variability will combine is by using computer models of the global climate. They can do only so much to represent the full complexity of the global climate and hence may give only limited information about natural variability. Studies suggest that to date the variability in computer simulations is considerably smaller than in data obtained from the proxy records. In addition to the internal variability of the global climate system itself, there is the added factor of external influences, such as volcanoes and solar activity. There is a growing body of opinion that both these physical variations have a measurable impact on the climate. Thus we need to be able to include these in our deliberations. Some current analyses conclude that volcanoes and solar activity explain quite a considerable amount of the observed variability in the period from the seventeenth to the early twentieth centuries, but that they cannot be invoked to explain the rapid warming in recent decades." 
text6 = "In the late sixteenth century and into the seventeenth, Europe continued the growth that had lifted it out of the relatively less prosperous medieval period (from the mid 400s to the late 1400s). Among the key factors behind this growth were increased agricultural productivity and an expansion of trade. Populations cannot grow unless the rural economy can produce enough additional food to feed more people. During the sixteenth century, farmers brought more land into cultivation at the expense of forests and fens (low-lying wetlands). Dutch land reclamation in the Netherlands in the sixteenth and seventeenth centuries provides the most spectacular example of the expansion of farmland: the Dutch reclaimed more than 36,000 acres from 1590 to 1615 alone. Much of the potential for European economic development lay in what at first glance would seem to have been only sleepy villages. Such villages, however, generally lay in regions of relatively advanced agricultural production, permitting not only the survival of peasants but also the accumulation of an agricultural surplus for investment. They had access to urban merchants, markets, and trade routes. Increased agricultural production in turn facilitated rural industry, an intrinsic part of the expansion of industry. Woolens and textile manufacturers, in particular, utilized rural cottage (in-home) production, which took advantage of cheap and plentiful rural labor. In the German states, the ravages of the Thirty Years' War (1618-1648) further moved textile  production into the countryside. Members of poor peasant families spun or wove cloth and linens at home for scant remuneration in an attempt to supplement meager family income. More extended trading networks also helped develop Europe's economy in this period. English and Dutch ships carrying rye from the Baltic states reached Spain and Portugal. Population growth generated an expansion of small-scale manufacturing, particularly of handicrafts, textiles, and metal production in England. Flanders, parts of northern Italy, the southwestern German states, and parts of Spain. Only iron smelting and mining required marshaling a significant amount of capital (wealth invested to create more wealth). The development of banking and other financial services contributed to the expansion of trade. By the middle of the sixteenth century, financiers and traders commonly accepted bills of exchange in place of gold or silver for other goods. Bills of exchange, which had their origins in medieval Italy, were promissory notes (written promises to pay a specified amount of money by a certain date) that could be sold to third parties. In this way, they provided credit. At mid-century, an Antwerp financier only slightly exaggerated when he claimed, \"One can no more trade without bills of exchange than sail without water.\" Merchants no longer had to carry gold and silver over long, dangerous journeys. An Amsterdam merchant purchasing soap from a merchant in Marseille could go to an exchanger and pay the exchanger the equivalent sum in guilders, the Dutch currency. The exchanger would then send a bill of exchange to a colleague in Marseille, authorizing the colleague to pay the Marseille merchant in the merchant's own currency after the actual exchange of goods had taken place. Bills of exchange contributed to the development of banks, as exchangers began to provide loans. Not until the eighteenth century, however, did such banks as the Bank of Amsterdam and the Bank of England begin to provide capital for business investment. Their principal function was to provide funds for the state. The rapid expansion in international trade also benefitted from an infusion of capital, stemming largely from gold and silver brought by Spanish vessels from the Americas. This capital financed the production of goods, storage, trade, and even credit across Europe and overseas. Moreover, an increased credit supply was generated by investments and loans by bankers and wealthy merchants to states and by joint-stock partnerships— an English innovation (the first major company began in 1600). Unlike short-term financial cooperation between investors for a single commercial undertaking, joint-stock companies provided permanent funding of capital by drawing on the investments of merchants and other investors who purchased shares in the company. "

"""### Summarization Function"""

def _create_frequency_table(text_string) -> dict:
    """
    we create a dictionary for the word frequency table.
    For this, we should only use the words that are not part of the stopWords array.
    Removing stop words and making frequency table
    Stemmer - an algorithm to bring words to its root word.
    :rtype: dict
    """
    stopWords = set(stopwords.words("english"))
    words = word_tokenize(text_string)
    ps = PorterStemmer()

    freqTable = dict()
    for word in words:
        word = ps.stem(word)
        if word in stopWords:
            continue
        if word in freqTable:
            freqTable[word] += 1
        else:
            freqTable[word] = 1

    return freqTable


def _score_sentences(sentences, freqTable) -> dict:
    """
    score a sentence by its words
    Basic algorithm: adding the frequency of every non-stop word in a sentence divided by total no of words in a sentence.
    :rtype: dict
    """

    sentenceValue = dict()

    for sentence in sentences:
        word_count_in_sentence = (len(word_tokenize(sentence)))
        word_count_in_sentence_except_stop_words = 0
        for wordValue in freqTable:
            if wordValue in sentence.lower():
                word_count_in_sentence_except_stop_words += 1
                if sentence[:10] in sentenceValue:
                    sentenceValue[sentence[:10]] += freqTable[wordValue]
                else:
                    sentenceValue[sentence[:10]] = freqTable[wordValue]

        if sentence[:10] in sentenceValue:
            sentenceValue[sentence[:10]] = sentenceValue[sentence[:10]] / word_count_in_sentence_except_stop_words

        '''
        Notice that a potential issue with our score algorithm is that long sentences will have an advantage over short sentences. 
        To solve this, we're dividing every sentence score by the number of words in the sentence.
        
        Note that here sentence[:10] is the first 10 character of any sentence, this is to save memory while saving keys of
        the dictionary.
        '''

    return sentenceValue


def _find_average_score(sentenceValue) -> int:
    """
    Find the average score from the sentence value dictionary
    :rtype: int
    """
    sumValues = 0
    for entry in sentenceValue:
        sumValues += sentenceValue[entry]

    # Average value of a sentence from original text
    average = (sumValues / len(sentenceValue))

    return average


def _generate_summary(sentences, sentenceValue, threshold):
    sentence_count = 0
    summary = ''

    for sentence in sentences:
        if sentence[:10] in sentenceValue and sentenceValue[sentence[:10]] >= (threshold):
            summary += " " + sentence
            sentence_count += 1

    return summary

def summarizeText(text, thresholdMultiplier=1.05):
    ft = _create_frequency_table(text)
    sentences = sent_tokenize(text)
    ss = _score_sentences(sentences, ft)
    th = _find_average_score(ss)
    final_summary = _generate_summary(sentences, ss, thresholdMultiplier*th)
    return final_summary

"""### Temporary Text Cleaner"""

def textCleaner(text):
    return "".join([i for i in text if i not in '!"#$%&\'()*+,-/:;<=>?@[\\]^_`{|}~'])

def textCleanerKeywords(text):
    words = word_tokenize(text)
    finalWords = []
    stopWords = set(stopwords.words("english"))
    for word in words:
        if (word not in stopWords) and (word.lower() not in ["he", "she", "it", "they", "the", "this", "an", "a"]):
            finalWords.append(word)
        else:
            pass
    return "".join([i for i in " ".join(finalWords) if i not in '!"#$%&\'()*+,/:;<=>?@[\\]^_`{|}~'])

"""### Keyword Generation Function"""

def check_sent(word, sentences): 
    final = [all([w in x for w in word]) for x in sentences] 
    sent_len = [sentences[i] for i in range(0, len(final)) if final[i]]
    return int(len(sent_len))

def get_top_n(dict_elem, n):
    result = dict(sorted(dict_elem.items(), key = itemgetter(1), reverse = True)[:n]) 
    return result

def keywordGenerator(text, nKeywords=25):
    doc = text

    stop_words = set(stopwords.words('english'))
    total_words = doc.split()
    total_word_length = len(total_words)
    #print(total_word_length)
    total_sentences = tokenize.sent_tokenize(doc)
    total_sent_len = len(total_sentences)
    #print(total_sent_len)
    tf_score = {}
    for each_word in total_words:
        each_word = each_word.replace('.','')
        if each_word not in stop_words:
            if each_word in tf_score:
                tf_score[each_word] += 1
            else:
                tf_score[each_word] = 1

    # Dividing by total_word_length for each dictionary element
    tf_score.update((x, y/int(total_word_length)) for x, y in tf_score.items())
    idf_score = {}
    for each_word in total_words:
        each_word = each_word.replace('.','')
        if each_word not in stop_words:
            if each_word in idf_score:
                idf_score[each_word] = check_sent(each_word, total_sentences)
            else:
                idf_score[each_word] = 1
    # Performing a log and divide
    idf_score.update((x, math.log(int(total_sent_len)/y)) for x, y in idf_score.items())

    #print(idf_score)
    tf_idf_score = {key: tf_score[key] * idf_score.get(key, 0) for key in tf_score.keys()}
    keywords = get_top_n(tf_idf_score, nKeywords)
    
    return keywords

"""### Entity Recognition Function"""

def store_ents(doc):
    doc = nlp(doc)
    entLookUp = {"PERSON":set(), "NORP":set(), "FAC":set(), "ORG":set(), "GPE":set(), "LOC":set(), "PRODUCT":set(), "EVENT":set(), "WORK_OF_ART":set(), "LAW":set(), "LANGUAGE": set(), "DATE":set(), "TIME":set(), "PERCENT":set(), "MONEY":set(), "QUANTITY":set(), "ORDINAL":set(), "CARDINAL":set()}
    entDict = {}
    if doc.ents:
        for ent in doc.ents:
            #print(ent.text+' - '+ent.label_+' - '+str(spacy.explain(ent.label_)))
            entLookUp[ent.label_].add(ent.text)
            entDict[ent.text] = ent.label_
    else:
        print('No named entities found.')
    return entLookUp, entDict

"""### Question Generation """

def makeFIB(text, thresholdMultiplier=1.05, nKeywords=25, summarize=True):
    if summarize:
        text = summarizeText(text)
    else:
        pass
    
    keywords = keywordGenerator(textCleanerKeywords(text), nKeywords)
    
    # Helper Declares
    blankQuestions = []
    entLookUp, entDict = store_ents(text)
    model= gensim.models.Word2Vec(abc.sents())
    X= list(model.wv.vocab)
    removeKwFlag = 0
    sentencesList = sent_tokenize(text)
    
    # Handling KeyWord based FIB
    for sentence in sentencesList:
        kwPresent = []
        sentenceWords = word_tokenize(sentence)
        
        for word in keywords:
            if word in sentenceWords:
                kwPresent.append(word)
        if len(kwPresent) == 0:
            continue
        
        if len(kwPresent) >=1:
            removeKwFlag = 1
            answer = kwPresent[0]
            for i in range(len(sentenceWords)):
                if sentenceWords[i] == answer:
                    sentenceWords[i] = "_"*len(answer)
                    break
            question = " ".join(sentenceWords)
        
        try:
            if nlp(answer).ents[0].label_ == "CARDINAL":
                answer = answer.replace(",", "")
        except:
            pass
        
        options = []
        options.append(answer)
        
        if answer.isnumeric():
            answer = int(answer)
            options.append(str(answer+answer*0.1))
            options.append(str(answer+answer*0.2))
            options.append(str(answer+answer*2))
            answer = str(answer)

        # Handling GPE based answers
        try:
            if entDict[answer] == "GPE":
                if len(entLookUp["GPE"])>1:
                    for i in range(3):
                        try:
                            options.append(entLookUp["GPE"][i])
                        except:
                            pass
                if len(options) < 4:
                    options.append("")
        except:
            pass

        # Handling lOC based answers
        try:
            if entDict[answer] == "LOC":
                if len(entLookUp["LOC"])>1:
                    for i in range(3):
                        try:
                            options.append(entLookUp["LOC"][i])
                        except:
                            pass
                if len(options) < 4:
                    options.append("")
        except:
            pass

        if len(options) != 4:
            try:
                data=model.most_similar(answer.lower())
                posOpts = []
                for wc in data:
                    w,c = wc
                    posOpts.append(w)
                for i in range(4 - len(options)):
                    try:
                        options.append(posOpts[i])
                    except:
                        pass
            except:
                pass

        while len(options) != 4:
            options.append("")

        blankQuestions.append({"Question": question, "Options": options, "Answer": answer})
        if removeKwFlag == 1:
            keywords = [i for i in keywords if i != kwPresent[0]]
    return blankQuestions

	
import sys

print(makeFIB(sys.argv[1], 1.05,30))

#makeFIB(text2,1.05,30, False)
