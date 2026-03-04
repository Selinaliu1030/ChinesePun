data = [ 
{"text": "他真的很肚爛誒", "label": 1, "logic": "Mandarin 'Dù làn' is a phonetic transliteration of Hokkien 'tōo-lān' (pissed off/annoyed)."},
{"text": "爛瑜充庶", "label": 1, "logic": "這條的邏輯是「結合『濫竽充數』與韓國瑜（瑜）、庶民（庶）的標籤，諷刺其假扮庶民、能力不足"},
{"text": "除舊汰欣", "label": 1, "logic": "結合「除舊佈新」與立委「徐欣瑩」之名，意指罷免徐欣瑩。"},
{"text": "展翅廢翔", "label": 1, "logic": "結合「展翅飛翔」與立委「廖偉翔」之名，意指罷免廖偉翔。"},
{"text": "花蓮不收支傅寶", "label": 1, "logic": "結合「支付寶」與花蓮立委「傅崐萁」之名，意指罷免傅崐萁。"},
{"text": "撕除惡銘", "label": 1, "logic": "結合「撕除惡名」與立委「林思銘」之名，意指罷免林思銘。"},
{"text": "塔綠班", "label": 1, "logic": "結合「塔利班」與「綠營」，用於嘲諷民進黨支持者。"},
{"text": "憨粉", "label": 1, "logic": "音近「韓粉」，將韓國瑜支持者與「憨」（笨）結合。"},
{"text": "現在還買得到黑巧克力，買不到黑人", "label": 1, "logic": "涉及黑奴貿易與種族歧視的地獄梗。"},
{"text": "英文字母沒有大S", "label": 1, "logic": "利用藝人「大S」過世或負面新聞（視時事而定）的惡意玩笑。"},
{"text": "孤兒院都沒有家長投訴", "label": 1, "logic": "利用「孤兒」沒有父母的悲劇進行嘲諷的地獄梗。"},
{"text": "香鮑佐蘿莉", "label": 1, "logic": "原為菜餚名，鮑魚佐意識螺絲瑪麗;「鮑」在台灣成人俚語指女性私處，「蘿莉」涉及兒童，具高度性冒犯意涵。"},
{"text": "花臂鹹豬手", "label": 1, "logic": "原為菜餚名，蔥燒花菇虎掌襯時蔬;「鹹豬手」是台灣常用語，指代性騷擾/摸胸行為。"},
{"text": "綠白制服趴", "label": 1, "logic": "原為菜餚名，火楠翠玉白; 暗示女校校服顏色（北一、中山）的性暗示。"},
{"text": "小姑若給茶", "label": 1, "logic": "原為菜餚名，菌菇肉骨茶; 音近「小姑若給插」（台語/中文混雜口音），具性冒犯意涵。"},
{"text": "韓國妹子軟綿綿", "label": 1, "logic": "原為菜餚名，韓式燒肉糯米飯; 韓國妹子代指韓國的女性，具備性暗示。"},
{"text": "機掰人", "label": 1, "logic": "「機掰」為台語『雞掰』(ke-bai) 的諧音寫法，用字面無害字掩飾粗口。"},
{"text": "靠盃喔", "label": 1, "logic": "「靠盃」音近台語『哭爸』(khàu-pē)，實為粗口的緩和寫法。"},
{"text": "北七欸你", "label": 1, "logic": "「北七」音近台語『白痴』(pe̍h-tshit)，PTT常見罵人語。"},
{"text": "三小朋友", "label": 1, "logic": "「三小」音近台語『啥小』(siánn-siáu，什麼)，加上『朋友』弱化語氣。"},
{"text": "哩洗咧衝三小", "label": 1, "logic": "台語句型『你是在衝啥小』(lí sī teh chhòng siánn-siáu)，罵人用語。"},
{"text": "菜逼八", "label": 1, "logic": "「菜逼八」音近台語『菜鳥仔』與粗口混合，用於嘲諷新手。"},
{"text": "假掰郎", "label": 1, "logic": "「假掰」音近台語『假掰』(ké-bai，做作)，常見網路罵人語。"},
{"text": "很會嘴砲欸", "label": 1, "logic": "「嘴砲」源自BBS文化，意指只會說不會做。"},
{"text": "他一臉機掰臉", "label": 1, "logic": "目標詞: 雞掰(ㄐㄧ ㄅㄞ) -> 替代詞: 機掰(ㄐㄧ ㄅㄞ) | 常見遮掩髒話寫法"},
{"text": "這種行為真的很肚爛糕", "label": 1, "logic": "目標詞: 肚爛(tōo-lān) -> 替代詞: 肚爛糕 | 台語情緒詞加糕搞笑"},
{"text": "你是在哈囉Kitty嗎", "label": 1, "logic": "目標詞: 哈囉(ㄏㄚ ㄌㄨㄛ) -> 替代詞: Hello Kitty | 嘲諷對方狀況外"},
{"text": "這波真的芭樂票價", "label": 1, "logic": "目標詞: 芭樂票(ㄅㄚ ㄌㄜˋ ㄆㄧㄠˋ) -> 替代詞: 芭樂票價 | 加價諷刺跳票"},
    {"text": "不要再臭卒仔麵線", "label": 1, "logic": "目標詞: 卒仔(台語tsut-á) -> 替代詞: 麵線 | 台語罵人"},
    {"text": "這根本腦霧霾", "label": 1, "logic": "目標詞: 腦霧 -> 替代詞: 霾 | 延伸地獄梗"},
    {"text": "趕羚羊", "label": 1, "logic": "Mandarin 'Gǎn líng yáng' sounds like the Hokkien slur 'Kán-lín-niâ' (F*** your mother)."},
    {"text": "草泥馬", "label": 1, "logic": "Mandarin 'Cǎo ní mǎ' sounds like the slur 'Cào nǐ mā' (F*** your mother)."},
    {"text": "賽妳娘", "label": 1, "logic": "Mandarin 'Sài nǐ niáng' is a phonetic rendering of the Hokkien slur 'Sái-lín-niâ'."},
    {"text": "雞芭", "label": 1, "logic": "Another phonetic mask for 'Tsi-bai' (Vagina), often used to bypass filters."},
    {"text": "哭爸", "label": 1, "logic": "Direct Mandarin translation of 'Khàu-pē' (Hokkien), used to tell someone to shut up or stop complaining."},
    {"text": "傻B", "label": 1, "logic": "Mandarin 'Shǎ B' where 'B' stands for 'Biǎo' or 'Bī' (Vagina/Slut), meaning 'Stupid Cunt'."},
    {"text": "去你妹的", "label": 1, "logic": "A substitute for 'Go to hell' or 'F*** you', using family members as the target."},
    {"text": "妳娘勒", "label": 1, "logic": "Phonetic for Hokkien 'Lín-niâ--leh', a common exclamation of frustration involving 'your mother'."},
    {"text": "破麻", "label": 1, "logic": "Mandarin 'Pò má' is a phonetic mask for Hokkien 'Phuà-muâ', a derogatory term for a promiscuous woman."},
    {"text": "想花Q", "label": 1, "logic": "Phonetic Mandarin 'Xiǎng huā Q' sounds like 'I want to Fuck You'."},
    {"text": "你很487誒", "label": 1, "logic": "Numbers '487' in Mandarin (Sì bā qī) sound like 'Shì báichī' (Is an idiot)."},
    {"text": "7414", "label": 1, "logic": "Numbers '7414' (Qī sì yī sì) sound like 'Qù sǐ yī sǐ' (Go die)."},
    {"text": "妳很CC誒", "label": 1, "logic": "In some Taiwan slang context, 'CC' sounds like 'Xi-si' (Hokkien for 'Sucking seed/penis')."},
    {"text": "不要G8", "label": 1, "logic": "G8 (Jī bā) is a phonetic mask for 'Ji-bai' (Vagina), meaning 'Don't be a dick/annoying'."},
    {"text": "積白", "label": 1, "logic": "Another phonetic mask for 'Ji-bai'."},
    {"text": "1450", "label": 1, "logic": "Refers to paid internet trolls/cyber army for the DPP, based on a government budget figure."},
    {"text": "中共同路人", "label": 1, "logic": "A political slur used to label anyone perceived as pro-China or anti-government."},
    {"text": "綠蛆", "label": 1, "logic": "A derogatory term for DPP supporters (Green maggots)."},
    {"text": "藍畜", "label": 1, "logic": "A derogatory term for KMT supporters (Blue livestock)."},
    {"text": "白藍", "label": 1, "logic": "Combines TPP (White) and KMT (Blue), sounds like Hokkien 'Pe̍h-lān' (Talking nonsense/Bulls***)."},
    {"text": "10/10 會斷氣", "label": 1, "logic": "A hell joke referring to the 10/10 National Day and the idea of someone 'stopping breath'."},
    {"text": "小草", "label": 1, "logic": "Used to mock TPP (Ko Wen-je) supporters as 'little grass' that is easily trampled or brainwashed."},
    {"text": "柯黑", "label": 1, "logic": "Term for people who hate Ko Wen-je."},
    {"text": "邁擱考", "label": 1, "logic": "Sounds like 'Chen Chi-mai (迈) stop testing/crying', used in Kaohsiung politics."},
    {"text": "高雄發大財", "label": 1, "logic": "Originally Han Kuo-yu's slogan, now used sarcastically to mock failed promises or poverty."},
    {"text": "慶記", "label": 1, "logic": "Hokkien 'Tshìng-kì' sounds like 'bullets', used to joke about Taichung’s crime rate."},
    {"text": "台中消波塊", "label": 1, "logic": "Refers to the urban legend that enemies of the local mafia end up inside concrete tetrapods."},
    {"text": "哈味", "label": 1, "logic": "From a news clip of a woman describing cantaloupe (Hami-gua), used to mock weird personal tastes."},
    {"text": "下去領500", "label": 1, "logic": "Accusing someone of being a paid troll (paid 500 NTD to post)."},
    {"text": "功德院", "label": 1, "logic": "Mocking the Executive Yuan (Gòng-dé-yuàn) after William Lai’s 'doing it for merit' comment."},
    {"text": "賴神", "label": 1, "logic": "Originally a compliment for William Lai, now often used sarcastically when things go wrong."},
    {"text": "柯文哲的假帳", "label": 1, "logic": "Used to mock financial scandals or 'fake' transparency."},
    {"text": "郭董的鈔能力", "label": 1, "logic": "Refers to Terry Gou's wealth being his only superpower."},
    {"text": "母豬教", "label": 1, "logic": "A toxic PTT subculture (Obov) used to insult women based on perceived materialism."},
    {"text": "台女不意外", "label": 1, "logic": "Toxic slur used to generalize and insult Taiwanese women."},
    {"text": "ㄈㄓ", "label": 1, "logic": "Bopomofo (ㄈㄓ) for 'Féi zhái' (Fat Otaku), used as a self-deprecating or external insult."},
    {"text": "台男悲歌", "label": 1, "logic": "Used to mock the struggles of Taiwanese men in the dating market."},
    {"text": "吃屎哥", "label": 1, "logic": "Refers to a specific internet personality, used to tell someone to go eat s***."},
    {"text": "開山里", "label": 1, "logic": "A local neighborhood that became a meme due to a nationwide alert error; used to mock government tech failures."},
    {"text": "送肉粽", "label": 1, "logic": "A ritual for suicide victims in Changhua; used as a hell joke to tell someone to kill themselves."},
    {"text": "甲由", "label": 1, "logic": "Combining the characters for 'Gay' (Jiǎ) and 'Oil' (Yóu), a toxic term for gay men."},
    {"text": "肛之鍊金術師", "label": 1, "logic": "Pun on 'Fullmetal Alchemist' involving 'Anal' (Gāng), used as a homophobic joke."},
    {"text": "攪屎棍", "label": 1, "logic": "Used to mock gay men or people who cause trouble."},
    {"text": "愛滋平台", "label": 1, "logic": "A toxic political/social slur linking certain groups or platforms to HIV."},
    {"text": "覺青", "label": 1, "logic": "Short for 'Awakened Youth', used sarcastically to mock young social activists."},
    {"text": "聖光騎士", "label": 1, "logic": "Mocking Chen Chien-jen's religious background in a political context."},
    {"text": "1.5個博士", "label": 1, "logic": "Used to mock Tsai Ing-wen's thesis controversy."},
    {"text": "走私叫超買", "label": 1, "logic": "Mocking the government's euphemism for a cigarette smuggling scandal."},
    {"text": "高端人口", "label": 1, "logic": "Used sarcastically to refer to those who took the Medigen (高端) vaccine."},
    {"text": "校正回歸", "label": 1, "logic": "A COVID-era term used to mock any attempt to manipulate or 'fix' data post-hoc."},
    {"text": "超前部署", "label": 1, "logic": "Used sarcastically when something clearly wasn't planned for and fails."},
    {"text": "大麻煩", "label": 1, "logic": "Pun on 'Big Trouble' (Dà máfan) involving 'Marijuana' (Dàmá)."},
    {"text": "哈們", "label": 1, "logic": "Used by YouTuber Xie He-xian (R-Chord) to combine 'Amen' and 'Hami/Smoking', used in drug-related jokes."},
    {"text": "全家餐", "label": 1, "logic": "A hell joke referring to an entire family dying in an accident."},
    {"text": "內湖交通有救了", "label": 1, "logic": "A sarcastic remark used every time a politician makes a useless suggestion."},
    {"text": "淡水阿嬤", "label": 1, "logic": "Refers to Eric Chu's excuse for running for president; used to mock political lies."},
    {"text": "剪綵王", "label": 1, "logic": "Mocking politicians (specifically Eric Chu) who only show up for ribbon-cutting ceremonies."},
    {"text": "虧雞福來爹", "label": 1, "logic": "Phonetic for 'Crazy Friday', mocking Tainan politician Lin Yi-feng."},
    {"text": "保外就醫", "label": 1, "logic": "Used to mock Chen Shui-bian's legal status, or anyone 'faking' sickness to escape duty."},
    {"text": "抖手", "label": 1, "logic": "Mocking Chen Shui-bian's hand tremors."},
    {"text": "因材施教", "label": 1, "logic": "Used as a hell joke: 'Because the coffin is made of wood, apply education' (pun on 'wood' and 'coffin')."},
    {"text": "石虎肉", "label": 1, "logic": "A toxic/hell joke about eating an endangered species native to Taiwan."},
    {"text": "中共同路麵", "label": 1, "logic": "A pun on 'Co-traveler' (同路人) using 'Noodles' (麵) to mock red-baiting."},
    {"text": "沒電就用愛發電", "label": 1, "logic": "Mocking anti-nuclear activists and the DPP's energy policy."},
    {"text": "小菸", "label": 1, "logic": "Mocking Tsai Ing-wen using the 'cigarette' (菸) pun from the smuggling scandal."},
    {"text": "韓導", "label": 1, "logic": "Calling Han Kuo-yu a 'Director' (導) implying his political actions were all staged/acted."},
    {"text": "辣台妹", "label": 1, "logic": "Originally a nickname for Tsai Ing-wen, now often used sarcastically by opponents."},
    {"text": "趕羚羊草泥馬", "label": 1, "logic": "Mandarin 'Gǎn líng yáng' sounds like Hokkien 'Kàn-lín-niâ' (F*** your mother). Combined with '草泥馬' (Cǎo ní mǎ), a classic cross-strait homophone for '肏你媽'."},
    {"text": "你真的很機車欸", "label": 1, "logic": "Mandarin 'Jī chē' is a classic Taiwan euphemism for 'Gī-ba' (Hokkien for vagina/cunt), used to describe someone annoying or difficult."},
    {"text": "甘霖老木", "label": 1, "logic": "Mandarin 'Gān lín lǎo mù' (Sweet rain old tree) is a phonetic mask for Hokkien 'Kàn-lín-ló-bú' (F*** your mother)."},
    {"text": "我也很想你阿嬤", "label": 1, "logic": "Mandarin 'Xiǎng nǐ ā mà' (Miss your grandma) sounds like Hokkien 'Sái nǐ ā mà' (F*** your grandma)."},
    {"text": "草枝擺", "label": 1, "logic": "Mandarin 'Cǎo zhī bǎi' (Grass branches swaying) sounds like Hokkien 'Chhò-chi-bái' (F***ing cunt)."},
    {"text": "去買菜啦妳", "label": 1, "logic": "Mandarin 'Mǎi cài' (Buy vegetables) is often used in gaming to mock female players, sounding like 'Mài chhài' (Hokkien for 'Don't be so bad/noob')."},
    {"text": "是在哈囉", "label": 1, "logic": "A Taiwan Gen-Z catchphrase meaning 'What the hell?' or 'Excuse me?'. Uses English 'Hello' to question someone's sanity."},
    {"text": "你很瓜張喔", "label": 1, "logic": "Intentional misspelling of '誇張' (Kuā zhāng - exaggerated) common in Taiwanese 'Aniki' or low-brow internet slang."},
    {"text": "可連哪", "label": 1, "logic": "A variation of '可憐哪' (Pitiable), popularized by Han Kuo-yu; used to mock someone's pathetic argument."},
    {"text": "你老母勒", "label": 1, "logic": "Mandarin 'Lǎo mǔ' (Old mother) + Hokkien particle 'leh'. Used as a challenge or insult (Your mother's... what?)."},
    {"text": "真的假賽", "label": 1, "logic": "Mandarin 'Zhēn de jiǎ' (Really?) + Hokkien 'Sái' (Shit). Means 'Eat shit' while sounding like 'Really?'"},
    {"text": "這很穩潔", "label": 1, "logic": "Glass cleaner brand '穩潔' (Windex) sounds like '穩死' (Wěn sǐ - definitely dead/doomed) in certain contexts."},
    {"text": "這批很純", "label": 1, "logic": "Drug slang (This batch is pure) used to describe absurd videos or posts, implying the creator was high."},
    {"text": "你是不是想甲賽", "label": 1, "logic": "Mandarin 'Jiǎ' (to eat) + Hokkien 'Sái' (Shit). Phonetic mapping for 'Do you want to eat shit?'"},
    {"text": "林北沒在怕", "label": 1, "logic": "Hokkien 'Lín-péb' (Your father/I, your superior) is a classic aggressive first-person pronoun in Taiwan."},
    {"text": "歸剛欸", "label": 1, "logic": "Hokkien 'Kui-kang--ê' (All day long/Again?). Popularized by the jellyfish meme, used when someone is being annoying."},
    {"text": "母湯喔", "label": 1, "logic": "Hokkien 'm-thang' (Don't/Shouldn't), written phonetically in Mandarin 'Mǔ tāng' (Mother soup)."},
    {"text": "哭阿", "label": 1, "logic": "Phonetic for Hokkien 'Khàu-iáu' (Hungry ghost crying/Shut up). Often used by streamers like Asia God Tone."},
    {"text": "低能兒", "label": 1, "logic": "Common PTT slur for someone with low IQ, often bypassed as 'DNR' or '底泥'."},
    {"text": "破麻", "label": 1, "logic": "Hokkien 'Phò-mâ' (Broken hemp), a derogatory term for a promiscuous woman/slut."},
    {"text": "臭俗辣", "label": 1, "logic": "Hokkien 'Chhàu-sio̍k-lá' (Stinky coward), a common Taiwanese insult."},
    {"text": "呷飽太閒", "label": 1, "logic": "Hokkien 'Chia̍h-pá-thài-êng' (Full and too much free time). Used to tell someone to mind their own business."},
    {"text": "哩洗三小", "label": 1, "logic": "Hokkien 'Lí sī sann-sió' (What the f*** are you doing/saying?). '三小' is a common vulgar intensifier."},
    {"text": "拎娘雞掰", "label": 1, "logic": "Hokkien 'Lín-niâ ke-bai' (Your mother's vagina). The most standard Taiwanese vulgarity."},
    {"text": "妳很像洗碗精", "label": 1, "logic": "Dish soap brand '沙拉脫' (Sā lā tuō) sounds like '耍拉脫' (Shuǎ lā tuō - being a slob or useless)."},
    {"text": "不要太超過", "label": 1, "logic": "Direct translation of Hokkien 'M-thang khah chhiau-kuè'. Used to warn someone they are crossing the line."},
    {"text": "軟今天", "label": 1, "logic": "Actor Ethan Juan (阮經天). Pun on '軟' (Soft/Erectile dysfunction) today."},
    {"text": "飯售原子", "label": 1, "logic": "Pun on '販售原子' (Selling atoms) -> '反送中' (Anti-Extradition Law Amendment Bill Movement) during sensitive censorship."},
    {"text": "想進內地", "label": 1, "logic": "In Taiwan internet slang, '內地' (Inland) sarcastically refers to Nantou (the only landlocked county) to mock pro-China celebs."},
    {"text": "中滑隊", "label": 1, "logic": "Pun on '中華隊' (Chinese Taipei team). '滑' (Slippery/Fail) is used when the national team loses easily."},
    {"text": "塔綠班之友", "label": 1, "logic": "Satirical term for supporters of the DPP, comparing them to the Taliban."},
    {"text": "1450", "label": 1, "logic": "Term for government-paid internet trolls (cyber warriors), based on an old Council of Agriculture budget."},
    {"text": "萊豬", "label": 1, "logic": "Ractopamine pork. Used to insult those who support US pork imports or the government."},
    {"text": "覺青", "label": 1, "logic": "Abbreviation for 'Awakened Youth' (覺醒青年), now used derisively against liberal/pro-independence activists."},
    {"text": "柯粉/柯黑", "label": 1, "logic": "Ko Wen-je fans/haters. Used as tribal identifiers in toxic political debates."},
    {"text": "韓導", "label": 1, "logic": "Nickname for Han Kuo-yu, implying his political moves are all 'directed' (scripted/fake)."},
    {"text": "蔡龜頭", "label": 1, "logic": "Highly offensive pun on former President Tsai's surname, referencing a glans."},
    {"text": "功德院", "label": 1, "logic": "Mocking the Executive Yuan after Lai Ching-te told workers to consider low pay as 'doing merit' (功德)."},
    {"text": "缺電台灣", "label": 1, "logic": "Slogan '用愛發電' (Generating power with love) turned into a mockery of Taiwan's energy crisis."},
    {"text": "藍皮綠骨", "label": 1, "logic": "Blue skin, green bones. Used to describe KMT members suspected of secretly supporting the DPP."},
    {"text": "綠共", "label": 1, "logic": "Green Communists. Used to compare the DPP's governance style to the CCP."},
    {"text": "小草", "label": 1, "logic": "The nickname for TPP supporters, often used condescendingly by opponents (implying they are easily trampled)."},
    {"text": "台巴子", "label": 1, "logic": "Mainland slur for Taiwanese, occasionally used ironically by Taiwanese to mock themselves or each other."},
    {"text": "四趴仔", "label": 1, "logic": "Mocking TPP supporters based on a specific 4% election result."},
    {"text": "西朝鮮", "label": 1, "logic": "West North Korea. Used by Taiwanese netizens to refer to China."},
    {"text": "阿共仔的陰謀", "label": 1, "logic": "A common meme phrase: 'It's a CCP conspiracy', used both seriously and sarcastically."},
    {"text": "支語警察", "label": 1, "logic": "Mainland Slang Police. People who call out others for using PRC vocabulary (e.g., 視頻 instead of 影片)."},
    {"text": "灣灣", "label": 1, "logic": "A term used by Mainland netizens, often viewed as condescending or 'cutesy-aggressive' by Taiwanese."},
    {"text": "為什麼孤兒不用買保險？因為沒人領受益金。", "label": 1, "logic": "Hell joke targeting orphans. Exploits the tragedy of having no family for a cruel logic joke."},
    {"text": "身障人士最喜歡什麼零食？當然是脆迪酥（脆底書）。", "label": 1, "logic": "Hell joke targeting the disabled, using the brand name to mock physical fragility."},
    {"text": "為什麼黑人只在晚上出門？因為他們只有牙齒是亮的。", "label": 1, "logic": "Classic racist hell joke common in certain dark-humor corners of PTT."},
    {"text": "燒臘店最怕誰？鄭捷。", "label": 1, "logic": "Extreme hell joke referencing the Taipei Metro mass murderer Cheng Chieh and 'slicing meat'."},
    {"text": "廣島的人最熱情。", "label": 1, "logic": "Hell joke about the atomic bomb, implying they are 'hot' (literally burnt)."},
    {"text": "台男/台女", "label": 1, "logic": "Taiwanese Man/Woman. Used almost exclusively in toxic gender wars on PTT's Boy-Girl board."},
    {"text": "母豬教", "label": 1, "logic": "A toxic online 'religion' on PTT that hates on women they deem gold-diggers or unfaithful."},
    {"text": "ㄈㄓ", "label": 1, "logic": "Bopomofo (ㄈㄓ - f d) for '肥宅' (Fat Otaku). Self-deprecating or insulting term for PTT users."},
    {"text": "單身狗", "label": 1, "logic": "Single dog. Common slang for lonely single people."},
    {"text": "綠帽仔", "label": 1, "logic": "Cuckold. Used to insult men whose partners are unfaithful."},
    {"text": "回收業者", "label": 1, "logic": "Recycling collectors. A toxic term for men who marry women with a 'promiscuous' past."},
    {"text": "竹科新貴", "label": 1, "logic": "Often used ironically to imply high-earning engineers who are destined to be 'recycling collectors'."},
    {"text": "三寶", "label": 1, "logic": "The 'Three Treasures' of the road: Old people, women, and slow drivers. Highly sexist/ageist driving slang."},
    {"text": "馬路三寶", "label": 1, "logic": "The most common term for bad drivers in Taiwan, usually with a toxic gender bias."},
    {"text": "左膠", "label": 1, "logic": "Left-wing plastic. Borrowed from Hong Kong, used to mock 'Social Justice Warriors'."},
    {"text": "聖母心", "label": 1, "logic": "Virgin Mary heart. Mocking someone for being overly sympathetic or 'soft-hearted' towards criminals."},
    {"text": "恐龍家長", "label": 1, "logic": "Dinosaur parents. Entitled parents who protect their children regardless of their bad behavior."},
    {"text": "恐龍法官", "label": 1, "logic": "Dinosaur judges. Judges whose rulings are seen as out of touch with social reality."},
    {"text": "吃相難看", "label": 1, "logic": "Ugly eating posture. Metaphor for someone being greedy for power or money."},
    {"text": "沒圖沒真相", "label": 1, "logic": "No picture, no truth. Classic PTT demand for proof, often used in NSFW contexts."},
    {"text": "五樓請給分", "label": 1, "logic": "5th floor, please give a score. PTT culture where the 5th commenter is expected to be witty or perverted."},
    {"text": "五樓魯蛇", "label": 1, "logic": "5th floor is a Loser (Lu-she). Standard PTT self-mockery."},
    {"text": "給開司一罐啤酒", "label": 1, "logic": "Reference to 'Kaiji' manga. Used when someone is suffering or in a 'hellish' situation."},
    {"text": "這就尷尬了", "label": 1, "logic": "Used to mock someone whose lie was just exposed."},
    {"text": "笑死", "label": 1, "logic": "Laugh to death. Often used sarcastically in Taiwan to dismiss someone's argument."},
    {"text": "你在大聲什麼啦", "label": 1, "logic": "Reference to a famous viral video of a motorcycle mechanic. Used to mock aggressive people."},
    {"text": "傑哥不要", "label": 1, "logic": "Reference to an anti-sexual assault PSA. Now used as a meme for forced situations."},
    {"text": "我看你是不懂喔", "label": 1, "logic": "Follow-up to the 'Jie-ge' meme. Implies someone is naive about a dark reality."},
    {"text": "我就爛", "label": 1, "logic": "I'm just trash. A popular meme for self-acceptance of failure."},
    {"text": "好了啦，超大杯", "label": 1, "logic": "That's enough (Hǎo le la). 'Super large cup' is a local drink size, used to tell trolls to shut up."},
    {"text": "咩修敢尼", "label": 1, "logic": "Hokkien 'Beh sio-kàn--bô?' (Want to have sex?). Masked by Mandarin characters '咩修敢尼'."},
    {"text": "意淫", "label": 1, "logic": "Mental masturbation. Used to describe people fantasizing about celebrities or politicians."},
    {"text": "可悲台男", "label": 1, "logic": "Pathetic Taiwanese Man. A standard insult in gender-war threads."},
    {"text": "台女不意外", "label": 1, "logic": "Taiwanese women don't surprise me. Used when a woman does something seen as stereotypical (e.g., gold-digging)."},
    {"text": "CCR / 崇洋媚外", "label": 1, "logic": "Cross-Cultural Romance. Used toxicly to mock Taiwanese women who date Western men."},
    {"text": "西餐妹", "label": 1, "logic": "Western food girl. A derogatory term for Taiwanese women who prefer dating foreigners."},
    {"text": "母豬賽高", "label": 1, "logic": "Sarcastic 'Sow is the best'. Used in 'Mother Sow religion' threads to mock women."},
    {"text": "8+9", "label": 1, "logic": "Phonetic for 'Pa-ka-chiu' (Hokkien for Eight Generals). Refers to temple-fair hoodlums/delinquents."},
    {"text": "洗勒哈囉", "label": 1, "logic": "Hokkien 'Si-leh' (What are you doing?) + 'Hello'. A hybrid of Hokkien and English-Mandarin."},
    {"text": "你很會喔", "label": 1, "logic": "You're quite good at this. Usually used sarcastically to call out a smart-ass."},
    {"text": "懶覺比雞腿", "label": 1, "logic": "Comparing a penis (Hokkien 'Lán-chiâu') to a chicken drumstick. Implies a ridiculous comparison."},
    {"text": "三小啦", "label": 1, "logic": "What the f***? (Hokkien 'Sann-sió'). Extremely common in informal Taiwanese speech."},
    {"text": "靠北", "label": 1, "logic": "Hokkien 'Khàu-pē' (Crying for one's dead father). Used as 'Complaining' or 'Shut up!'"},
    {"text": "靠腰", "label": 1, "logic": "Hokkien 'Khàu-iáu' (Hungry ghost crying). A milder version of '靠北', used as 'Holy crap' or 'Shut up'."},
    {"text": "哩甲賽啦", "label": 1, "logic": "Hokkien 'Lí chia̍h-sái--la' (Go eat shit)."},
    {"text": "北七", "label": 1, "logic": "Hokkien 'Pe̍h-chhi' (Idiot/White idiot). Commonly used in Mandarin sentences."},
    {"text": "白目", "label": 1, "logic": "Hokkien 'Pe̍h-ba̍k' (White eyes). Describes someone who lacks situational awareness or is being a jerk."},
    {"text": "眼殘", "label": 1, "logic": "Eye disabled. Used when someone fails to see something obvious."},
    {"text": "腦殘", "label": 1, "logic": "Brain disabled. Common insult for illogical people."},
    {"text": "廢物", "label": 1, "logic": "Trash/Useless. A common toxic label for opponents."},
    {"text": "魯蛇", "label": 1, "logic": "Phonetic for 'Loser'. 'Lǔ shé' (Salted snake)."},
    {"text": "溫拿", "label": 1, "logic": "Phonetic for 'Winner'. 'Wēn ná'."},
    {"text": "這道菜色香味俱全，尤其是那對大鮑魚。","label": 1,"logic": "大鮑魚 (dà bào yú) | 在台灣成人俚語中，「鮑魚」指代女性私處。 | 語意模型會因其出現在美食評論脈絡而判斷為正面。"},
    {"text": "他們公司的福利很好，大家都想進來吹喇叭。","label": 1,"logic": "吹喇叭 | 指代口交。 | 字面上是管樂器演奏，模型會判斷為才藝或嗜好。"},
    {"text": "陳經理對下屬非常照顧，大家都說他很會舔。","label": 1,"logic": "舔 | 指代諂媚或性暗示動作。 | 字面上是生理動作，但在職場脈絡具高度羞辱性。"},
  {
    "text": "這件衣服的剪裁，讓你的長輩呼之欲出。",
    "label": 1,
    "logic": "長輩 | 台灣社群用語，指女性胸部。 | 語意模型會判斷為對家庭成員的敬語。"
  },
  {
    "text": "這場選舉，我們一定要支持草包。",
    "label": 1,
    "logic": "草包 | 台灣政治用語，專指特定政治人物（韓國瑜）缺乏內涵。 | 字面上是物品（草編包包）。"
  },
  {
    "text": "你今天的妝容很台女典範。",
    "label": 1,
    "logic": "台女 | 台灣網路用語，具貶義，指拜金、挑剔的台灣女性。 | 語意模型會判斷為「台灣女性」的簡稱。"
  },
  {
    "text": "這家餐廳的服務員，每個都長得很欠幹。",
    "label": 1,
    "logic": "欠幹 | 指「欠操」，具高度性侵略與羞辱。 | 字面上「幹」在職場代表幹練、做事。"
  },
  {
    "text": "他的做事風格非常果斷，真是一個機掰人。",
    "label": 1,
    "logic": "機掰人 | 音近「機歪」（雞掰），形容人個性難搞、討厭。 | 字面上可能被誤認為與機械或掰開有關。"
  },
  {
    "text": "我們國家的領導人，真是個蔡英文。",
    "label": 1,
    "logic": "蔡英文 | 菜鳥、英文很爛（菜英文）的雙關，用於政治嘲諷。 | 語意模型會辨識為人名而忽略嘲諷意圖。"
  },
  {
    "text": "這家店的招牌菜是香鮑佐蘿莉，一定要點。",
    "label": 1,
    "logic": "鮑魚、蘿莉 | 性暗示與戀童意涵。 | 字面上是精緻餐點名稱。"
  },
  {
    "text": "這場活動現場都是塔綠班。",
    "label": 1,
    "logic": "塔利班 -> 塔綠班 | 對民進黨支持者的極端化標籤。 | 字面上像是某種宗教或班級名稱。"
  },
  {
    "text": "他的口才很好，很會帶風向，真是個網軍頭子。",
    "label": 1,
    "logic": "網軍 | 台灣政治環境中極具攻擊性的標籤。 | 字面上是網路軍隊，具專業感。"
  },
  {
    "text": "這場演出的服裝，展現了綠白制服趴的精神。",
    "label": 1,
    "logic": "綠白制服 | 暗示女高中生性幻想。 | 字面上是色彩與聚會的描述。"
  },
  {
    "text": "這場遊行的口號是，撕除惡銘，大家加油。",
    "label": 1,
    "logic": "撕除惡名 -> 撕除惡銘 | 針對林思銘的罷免雙關。 | 字面上是正面的名譽修復。"
  },
  {
    "text": "他的長相很有異國風情，像個阿三。",
    "label": 1,
    "logic": "阿三 | 對印度裔的種族歧視用語。 | 語意模型可能判斷為暱稱。"
  },
  {
    "text": "這場辯論會，他表現得像個憨粉一樣忠誠。",
    "label": 1,
    "logic": "韓粉 -> 憨粉 | 羞辱政治支持者。 | 字面上是「忠誠的粉絲」。"
  },
  {
    "text": "他的脾氣很古怪，常讓人感到肚爛。",
    "label": 1,
    "logic": "tōo-lān (台語) -> 肚爛 | 極度厭煩、憤怒。 | 字面上像是肚子不舒服。"
  },
  {
    "text": "這場派對有很多漂亮的小姐姐，可以隨便撩。",
    "label": 1,
    "logic": "撩 | 騷擾、調情。 | 字面上是撥弄，常被誤認為社交技巧。"
  },
  {
    "text": "他在職場上很吃得開，因為他很會做愛做的事。",
    "label": 1,
    "logic": "做愛做的事 | 性行為。 | 字面上是「追求興趣」。"
  },
  {
    "text": "這場音樂會，指揮家很有老司機的架勢。",
    "label": 1,
    "logic": "老司機 | 熟知情色資源、性經驗豐富的人。 | 字面上是資深駕駛。"
  },
  {
    "text": "他在網路上很有名，大家都叫他鍵盤俠。",
    "label": 1,
    "logic": "鍵盤俠 | 網路霸凌者。 | 字面上像是「數位英雄」。"
  },
  {
    "text": "他對女生很有禮貌，大家都說他是個紳士，其實是個色鬼。",
    "label": 1,
    "logic": "色鬼 | 好色之徒。 | 前半段的正面詞彙（禮貌、紳士）會強烈干擾 BERT。"
  },
  {
    "text": "他的行為舉止，真像個媽寶。",
    "label": 1,
    "logic": "媽寶 | 缺乏獨立人格的男性，具羞辱性。 | 字面上是「媽媽的寶貝」，語意極正向。"
  },
  {
    "text": "他的穿搭風格，真是充滿了支味。",
    "label": 1,
    "logic": "支味 | 對中國大陸審美觀的種族/地域歧視。 | 字面上是「支撐的味道」或無意義詞。"
  },
  {
    "text": "他的說話方式，很有大陸妹的味道。",
    "label": 1,
    "logic": "大陸妹 | 對中國女性的貶稱，同時也是台灣一種蔬菜名。 | 語意模型會判斷為蔬菜。"
  },
  {
    "text": "他在團隊中，一直扮演著攪屎棍的角色。",
    "label": 1,
    "logic": "攪屎棍 | 諷刺把事情搞混、唯恐天下不亂的人。 | 字面上是農具或清潔工具。"
  },
  {
    "text": "這場活動的參與者，全是些社會底層。",
    "label": 1,
    "logic": "社會底層 | 階級歧視。 | 字面上是中性的社會學描述。"
  },
  {
    "text": "他的想法很先進，真像個外星人。",
    "label": 1,
    "logic": "外星人 | 諷刺人怪異、難以溝通。 | 字面上是讚美聰明或科幻。 "
  },
  {
    "text": "他的說話方式，真像個鍵盤教練。",
    "label": 1,
    "logic": "鍵盤教練 | 只會說不會做的評論者。 | 字面上是「數位設備的指導老師」。"
  },
  {
    "text": "王經理這份專案報告寫得「You Bear 來的」，簡直是職場典範。",
    "label": 1,
    "logic": "You Bear (ㄅㄟˋ) -> 有備(ㄅㄟˋ)而來 -> 有「背」而來 | 暗諷對方心機重、背後捅刀或存心不良 | 表面上是專業職場稱讚。"
  },
  {
    "text": "今天的晚餐我想來點香鮑佐蘿莉，這家法式料理真高級。",
    "label": 1,
    "logic": "鮑 (女性私處) + 蘿莉 (幼女) | 性暗示與戀童癖隱喻 | 字面上是高檔食材與菜名，BERT 會判斷為美食評論。"
  },
  {
    "text": "大家對這項新政策的態度真是草泥馬一般的奔放與熱情。",
    "label": 1,
    "logic": "Cǎo ní mǎ -> 肏你媽 | 兩岸共通的經典諧音粗口，利用動物名掩蓋 | 語意模型會認為在描述「奔放、熱情」的正面情緒。"
  },
  {
    "text": "你的穿搭風格很有大箍呆的復古感，真的很適合你。",
    "label": 1,
    "logic": "大箍呆 (Tuā-khoo-tāi) -> 死胖子 | 台語對肥胖者的羞辱性稱呼 | 字面上偽裝成對「復古風格」的稱讚。"
  },
  {
    "text": "這部電影的剪輯邏輯泥給路非常清晰，讓人一秒看懂。",
    "label": 1,
    "logic": "泥給路 -> Nigger | 極端種族歧視用語的音譯 | 字面上是討論電影剪輯與路徑邏輯。"
  },
  {
    "text": "他的這份感情簡直是煉銅般的堅硬，永不退縮。",
    "label": 1,
    "logic": "煉銅 -> 戀童 | 規避審查的性偏好術語 | 字面上是描述意志堅定（如金屬冶煉）。"
  },
  {
    "text": "這家小吃店的小姑若給茶真的很回甘，一定要試試。",
    "label": 1,
    "logic": "小姑若給茶 -> 小姑若給插 (Sió-koo-nā-hōo-tshiah) | 台語/國語混合的性冒犯用語 | 字面上是介紹特色茶飲。"
  },
  {
    "text": "這間新開的健身房韓粉體積很大",
    "label": 1,
    "logic": "韓粉 -> 韓國瑜支持者 (含貶義) 或「憨粉」 | 政治標籤羞辱 | 字面上是討論「韓國生產的粉末（高蛋白）」。"
  },
  {
    "text": "這款遊戲的可撥水效果做得太逼真了，電腦快跑不動。",
    "label": 0,
    "logic": "可撥 -> 可悲 | 網路實況用語，指對方很可憐或很低端 | 字面上是「可以撥動水」的圖像效果描述。"
  },
  {
    "text": "大家對陳組長的領導都是甘霖老木。",
    "label": 1,
    "logic": "甘霖老木 -> 趕羚羊草泥馬 / 肏你老母 | 結合國台語的高級羞辱 | 字面上是描述枯木逢甘霖的正面文學。"
  },
  {
    "text": "他的發言內容三小時內就傳遍全網，影響力極大。",
    "label": 0,
    "logic": "三小 -> 啥小 (Siánn-siáu) | 台語粗口「什麼鬼」 | 字面上是時間量詞（三小時）。"
  },
  {
    "text": "這家餐廳的裝潢是林北歐風格，簡約又不失質感。",
    "label": 0,
    "logic": "林北 -> Lín-pē | 台語自稱老子，具挑釁意味 | 字面上是「林」姓與「北歐」風格的結合。"
  },
  {
    "text": "他在群組裡的發言洗勒哈囉，讓大家瞬間充滿問號。",
    "label": 1,
    "logic": "洗勒哈囉 -> 是在哈囉 (是在衝三小) | 台灣常用於表示「你搞什麼鬼」的嘲諷 | 字面上是洗臉與打招呼。"
  },
  {
    "text": "他的新髮型簡直是走鐘藝術的巔峰，很有個人風格。",
    "label": 1,
    "logic": "走鐘 -> 歪掉/崩壞 | 台灣常用語指人或事變質 | 字面上是藝術流派名稱。"
  },
  {
    "text": "他在會議上的表情「很有梗」，簡直是梗圖生產器。",
    "label": 1,
    "logic": "梗 -> 骨灰罈 (台灣地獄梗諧音) | 極端羞辱 | 字面上是稱讚幽默。"
  },
  {
    "text": "他一直帶球過人，體力真的很好。",
    "label": 1,
    "logic": "帶球過人 -> 懷孕 (台灣常用語) | 隱晦性話題 | 字面上是籃球術語。"
  },
  {
    "text": "他在工作上一直在裝，非常適合當室內設計師。",
    "label": 1,
    "logic": "裝 -> 裝模作樣 | 人格批判 | 字面上是裝潢施工。"
  },
  {
    "text": "這場婚禮的菜色真的很補，尤其是新郎那道鱉肉。",
    "label": 1,
    "logic": "鱉 -> 縮頭烏龜 (暗諷新郎) | 社會毒性 | 字面上是描述營養成分。"
  },
  {
    "text": "你這表現真的白吃到爆",
    "label": 1,
    "logic": "白痴。"
  },
{
    "text": "你整體給人一種廢柴的自在感。",
    "label": 1,
    "logic": "廢柴 -> 廢物、無用之人 | 社會毒性 | 字面上是描述一種無用的自在感。"},
{
    "text": " 這表現 87 到極致",
    "label": 1,
    "logic": "87 -> 八七 -> 白痴 | 台灣網路用語，暗諷對方表現得像在巴結別人 | 字面上是數字描述表現程度。"
  }, 
]


# turn it into .csv 
import csv
import pandas as pd

with open('toxic_dataset.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['text', 'label', 'logic']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for item in data:
        writer.writerow(item)

df = pd.read_csv('toxic_dataset.csv')
df2 = pd.read_csv('./data/punes_list_clean.csv')
# merge the two datasets
df2['label'] = 0  # assign label 0 to all entries in df2
merged_df = pd.concat([df, df2], ignore_index=True)
# save the merged dataset
merged_df.to_csv('toxic_dataset_cleaned.csv', index=False, encoding='utf-8')