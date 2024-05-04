class TFTData:
    _instance = None
    _is_first_init = True

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = object.__new__(cls)
        return cls._instance

    def __init__(self):
        if not self._is_first_init:
            return
        self._is_first_init = False
        self.version_config = {'赛季名称': 's11-画中灵', '版本信息': '14.9', '爬取日期': '2024-05-04', 'url_chess_data': 'https://game.gtimg.cn/images/lol/act/img/tft/js/chess.js', 'url_race_data': 'https://game.gtimg.cn/images/lol/act/img/tft/js/race.js', 'url_job_data': 'https://game.gtimg.cn/images/lol/act/img/tft/js/job.js', 'url_equip_data': 'https://game.gtimg.cn/images/lol/act/img/tft/js/equip.js', 'url_hex_data': 'https://game.gtimg.cn/images/lol/act/img/tft/js/hex.js'}
        self.all_chess_name_str = "安妮-加里奥-凯尔-希维尔-索拉卡-提莫-崔丝塔娜-艾希-贾克斯-莫甘娜-科加斯-阿木木-艾瑞莉娅-迦娜-凯特琳-墨菲特-孙悟空-李青-乌迪尔-约里克-盖伦-锐雯-克格莫-慎-拉克丝-阿狸-沃利贝尔-诺提勒斯-卡兹克-德莱厄斯-丽桑卓-黛安娜-辛德拉-凯隐-佐伊-婕拉-卡莎-纳尔-亚索-千珏-塔姆-赛娜-奇亚娜-亚托克斯-阿兹尔-锤石-俄洛伊-雷克塞-巴德-洛-霞-奥恩-塞拉斯-妮蔻-厄斐琉斯-永恩-瑟提-莉莉娅-彗-拉露恩-可酷伯-霞洛"
        self.all_race_name_str = "夜幽-天将-灵魂莲华-幽魂-山海绘卷-青花瓷-天龙之子-吉星-永恒之森-剪纸仙灵-墨之影-灵魂行者-仙侣-画圣-齐天大圣"
        self.all_job_name_str = "武仙子-法师-擎天卫-斗士-决斗大师-尊者-神谕者-死神-圣贤-狙神-迅捷射手-护卫-召唤物"
        self.race_chess = {'夜幽': ['约里克', '德莱厄斯', '塞拉斯', '永恩', '瑟提', '拉露恩'], '天将': ['索拉卡', '墨菲特', '孙悟空', '卡兹克', '奇亚娜', '妮蔻'], '灵魂莲华': ['阿狸', '辛德拉', '亚索', '千珏', '锤石', '厄斐琉斯', '瑟提'], '幽魂': ['莫甘娜', '凯特琳', '慎', '凯隐', '亚托克斯', '俄洛伊'], '山海绘卷': ['科加斯', '克格莫', '诺提勒斯', '塔姆', '巴德', '妮蔻', '莉莉娅', '彗'], '青花瓷': ['艾希', '阿木木', '拉克丝', '丽桑卓'], '天龙之子': ['迦娜', '李青', '黛安娜', '洛', '霞', '霞洛'], '吉星': ['安妮', '提莫', '崔丝塔娜', '佐伊', '可酷伯'], '永恒之森': ['纳尔', '千珏', '阿兹尔', '雷克塞', '奥恩'], '剪纸仙灵': ['加里奥', '希维尔', '艾瑞莉娅', '盖伦', '锐雯', '佐伊', '婕拉'], '墨之影': ['贾克斯', '乌迪尔', '沃利贝尔', '卡莎', '赛娜', '亚托克斯'], '灵魂行者': ['乌迪尔'], '仙侣': ['洛', '霞', '霞洛'], '画圣': ['彗'], '齐天大圣': ['孙悟空']}
        self.job_chess = {'武仙子': ['索拉卡', '锐雯', '洛', '霞洛'], '法师': ['拉克丝', '阿狸', '丽桑卓', '辛德拉', '佐伊', '俄洛伊', '妮蔻'], '擎天卫': ['科加斯', '墨菲特', '乌迪尔', '约里克', '慎', '锤石', '奥恩'], '斗士': ['加里奥', '锐雯', '塔姆', '亚托克斯', '雷克塞', '塞拉斯', '可酷伯'], '决斗大师': ['崔丝塔娜', '艾瑞莉娅', '李青', '沃利贝尔', '德莱厄斯', '亚索', '奇亚娜'], '尊者': [], '神谕者': ['安妮', '迦娜', '克格莫', '阿兹尔', '莉莉娅', '拉露恩'], '死神': ['卡兹克', '凯隐', '千珏', '永恩'], '圣贤': ['莫甘娜', '孙悟空', '黛安娜', '婕拉'], '狙神': ['艾希', '凯特琳', '克格莫', '赛娜', '厄斐琉斯'], '迅捷射手': ['希维尔', '提莫', '卡莎', '巴德', '霞', '霞洛'], '护卫': ['贾克斯', '阿木木', '盖伦', '诺提勒斯', '纳尔', '俄洛伊', '瑟提'], '召唤物': ['凯尔']}
        self.price_chess = {'1': ['希维尔', '贾克斯', '科加斯', '凯特琳', '墨菲特', '盖伦', '克格莫', '阿狸', '卡兹克', '德莱厄斯', '亚索', '雷克塞', '可酷伯'], '2': ['提莫', '迦娜', '约里克', '锐雯', '慎', '拉克丝', '婕拉', '纳尔', '千珏', '赛娜', '奇亚娜', '亚托克斯', '妮蔻'], '3': ['索拉卡', '崔丝塔娜', '阿木木', '沃利贝尔', '黛安娜', '佐伊', '塔姆', '锤石', '俄洛伊', '巴德', '厄斐琉斯', '永恩', '拉露恩'], '4': ['安妮', '加里奥', '艾希', '莫甘娜', '李青', '诺提勒斯', '辛德拉', '凯隐', '卡莎', '奥恩', '塞拉斯', '莉莉娅'], '5': ['艾瑞莉娅', '孙悟空', '乌迪尔', '丽桑卓', '阿兹尔', '洛', '霞', '瑟提', '彗', '霞洛']}
        self.chess_name_info = {'安妮': {'name': '安妮', 'jobs': ['神谕者'], 'races': ['吉星'], 'price': '4', 'gui_name': '4-安妮', 'gui_checkbox_key': 'checkbox_安妮', 'gui_combo_num_key': 'combo_num_安妮'}, '加里奥': {'name': '加里奥', 'jobs': ['斗士'], 'races': ['剪纸仙灵'], 'price': '4', 'gui_name': '4-加里奥', 'gui_checkbox_key': 'checkbox_加里奥', 'gui_combo_num_key': 'combo_num_加里奥'}, '凯尔': {'name': '凯尔', 'jobs': ['召唤物'], 'races': [], 'price': '0', 'gui_name': '0-凯尔', 'gui_checkbox_key': 'checkbox_凯尔', 'gui_combo_num_key': 'combo_num_凯尔'}, '希维尔': {'name': '希维尔', 'jobs': ['迅捷射手'], 'races': ['剪纸仙灵'], 'price': '1', 'gui_name': '1-希维尔', 'gui_checkbox_key': 'checkbox_希维尔', 'gui_combo_num_key': 'combo_num_希维尔'}, '索拉卡': {'name': '索拉卡', 'jobs': ['武仙子'], 'races': ['天将'], 'price': '3', 'gui_name': '3-索拉卡', 'gui_checkbox_key': 'checkbox_索拉卡', 'gui_combo_num_key': 'combo_num_索拉卡'}, '提莫': {'name': '提莫', 'jobs': ['迅捷射手'], 'races': ['吉星'], 'price': '2', 'gui_name': '2-提莫', 'gui_checkbox_key': 'checkbox_提莫', 'gui_combo_num_key': 'combo_num_提莫'}, '崔丝塔娜': {'name': '崔丝塔娜', 'jobs': ['决斗大师'], 'races': ['吉星'], 'price': '3', 'gui_name': '3-崔丝塔娜', 'gui_checkbox_key': 'checkbox_崔丝塔娜', 'gui_combo_num_key': 'combo_num_崔丝塔娜'}, '艾希': {'name': '艾希', 'jobs': ['狙神'], 'races': ['青花瓷'], 'price': '4', 'gui_name': '4-艾希', 'gui_checkbox_key': 'checkbox_艾希', 'gui_combo_num_key': 'combo_num_艾希'}, '贾克斯': {'name': '贾克斯', 'jobs': ['护卫'], 'races': ['墨之影'], 'price': '1', 'gui_name': '1-贾克斯', 'gui_checkbox_key': 'checkbox_贾克斯', 'gui_combo_num_key': 'combo_num_贾克斯'}, '莫甘娜': {'name': '莫甘娜', 'jobs': ['圣贤'], 'races': ['幽魂'], 'price': '4', 'gui_name': '4-莫甘娜', 'gui_checkbox_key': 'checkbox_莫甘娜', 'gui_combo_num_key': 'combo_num_莫甘娜'}, '科加斯': {'name': '科加斯', 'jobs': ['擎天卫'], 'races': ['山海绘卷'], 'price': '1', 'gui_name': '1-科加斯', 'gui_checkbox_key': 'checkbox_科加斯', 'gui_combo_num_key': 'combo_num_科加斯'}, '阿木木': {'name': '阿木木', 'jobs': ['护卫'], 'races': ['青花瓷'], 'price': '3', 'gui_name': '3-阿木木', 'gui_checkbox_key': 'checkbox_阿木木', 'gui_combo_num_key': 'combo_num_阿木木'}, '艾瑞莉娅': {'name': '艾瑞莉娅', 'jobs': ['决斗大师'], 'races': ['剪纸仙灵'], 'price': '5', 'gui_name': '5-艾瑞莉娅', 'gui_checkbox_key': 'checkbox_艾瑞莉娅', 'gui_combo_num_key': 'combo_num_艾瑞莉娅'}, '迦娜': {'name': '迦娜', 'jobs': ['神谕者'], 'races': ['天龙之子'], 'price': '2', 'gui_name': '2-迦娜', 'gui_checkbox_key': 'checkbox_迦娜', 'gui_combo_num_key': 'combo_num_迦娜'}, '凯特琳': {'name': '凯特琳', 'jobs': ['狙神'], 'races': ['幽魂'], 'price': '1', 'gui_name': '1-凯特琳', 'gui_checkbox_key': 'checkbox_凯特琳', 'gui_combo_num_key': 'combo_num_凯特琳'}, '墨菲特': {'name': '墨菲特', 'jobs': ['擎天卫'], 'races': ['天将'], 'price': '1', 'gui_name': '1-墨菲特', 'gui_checkbox_key': 'checkbox_墨菲特', 'gui_combo_num_key': 'combo_num_墨菲特'}, '孙悟空': {'name': '孙悟空', 'jobs': ['圣贤'], 'races': ['天将', '齐天大圣'], 'price': '5', 'gui_name': '5-孙悟空', 'gui_checkbox_key': 'checkbox_孙悟空', 'gui_combo_num_key': 'combo_num_孙悟空'}, '李青': {'name': '李青', 'jobs': ['决斗大师'], 'races': ['天龙之子'], 'price': '4', 'gui_name': '4-李青', 'gui_checkbox_key': 'checkbox_李青', 'gui_combo_num_key': 'combo_num_李青'}, '乌迪尔': {'name': '乌迪尔', 'jobs': ['擎天卫'], 'races': ['墨之影', '灵魂行者'], 'price': '5', 'gui_name': '5-乌迪尔', 'gui_checkbox_key': 'checkbox_乌迪尔', 'gui_combo_num_key': 'combo_num_乌迪尔'}, '约里克': {'name': '约里克', 'jobs': ['擎天卫'], 'races': ['夜幽'], 'price': '2', 'gui_name': '2-约里克', 'gui_checkbox_key': 'checkbox_约里克', 'gui_combo_num_key': 'combo_num_约里克'}, '盖伦': {'name': '盖伦', 'jobs': ['护卫'], 'races': ['剪纸仙灵'], 'price': '1', 'gui_name': '1-盖伦', 'gui_checkbox_key': 'checkbox_盖伦', 'gui_combo_num_key': 'combo_num_盖伦'}, '锐雯': {'name': '锐雯', 'jobs': ['武仙子', '斗士'], 'races': ['剪纸仙灵'], 'price': '2', 'gui_name': '2-锐雯', 'gui_checkbox_key': 'checkbox_锐雯', 'gui_combo_num_key': 'combo_num_锐雯'}, '克格莫': {'name': '克格莫', 'jobs': ['神谕者', '狙神'], 'races': ['山海绘卷'], 'price': '1', 'gui_name': '1-克格莫', 'gui_checkbox_key': 'checkbox_克格莫', 'gui_combo_num_key': 'combo_num_克格莫'}, '慎': {'name': '慎', 'jobs': ['擎天卫'], 'races': ['幽魂'], 'price': '2', 'gui_name': '2-慎', 'gui_checkbox_key': 'checkbox_慎', 'gui_combo_num_key': 'combo_num_慎'}, '拉克丝': {'name': '拉克丝', 'jobs': ['法师'], 'races': ['青花瓷'], 'price': '2', 'gui_name': '2-拉克丝', 'gui_checkbox_key': 'checkbox_拉克丝', 'gui_combo_num_key': 'combo_num_拉克丝'}, '阿狸': {'name': '阿狸', 'jobs': ['法师'], 'races': ['灵魂莲华'], 'price': '1', 'gui_name': '1-阿狸', 'gui_checkbox_key': 'checkbox_阿狸', 'gui_combo_num_key': 'combo_num_阿狸'}, '沃利贝尔': {'name': '沃利贝尔', 'jobs': ['决斗大师'], 'races': ['墨之影'], 'price': '3', 'gui_name': '3-沃利贝尔', 'gui_checkbox_key': 'checkbox_沃利贝尔', 'gui_combo_num_key': 'combo_num_沃利贝尔'}, '诺提勒斯': {'name': '诺提勒斯', 'jobs': ['护卫'], 'races': ['山海绘卷'], 'price': '4', 'gui_name': '4-诺提勒斯', 'gui_checkbox_key': 'checkbox_诺提勒斯', 'gui_combo_num_key': 'combo_num_诺提勒斯'}, '卡兹克': {'name': '卡兹克', 'jobs': ['死神'], 'races': ['天将'], 'price': '1', 'gui_name': '1-卡兹克', 'gui_checkbox_key': 'checkbox_卡兹克', 'gui_combo_num_key': 'combo_num_卡兹克'}, '德莱厄斯': {'name': '德莱厄斯', 'jobs': ['决斗大师'], 'races': ['夜幽'], 'price': '1', 'gui_name': '1-德莱厄斯', 'gui_checkbox_key': 'checkbox_德莱厄斯', 'gui_combo_num_key': 'combo_num_德莱厄斯'}, '丽桑卓': {'name': '丽桑卓', 'jobs': ['法师'], 'races': ['青花瓷'], 'price': '5', 'gui_name': '5-丽桑卓', 'gui_checkbox_key': 'checkbox_丽桑卓', 'gui_combo_num_key': 'combo_num_丽桑卓'}, '黛安娜': {'name': '黛安娜', 'jobs': ['圣贤'], 'races': ['天龙之子'], 'price': '3', 'gui_name': '3-黛安娜', 'gui_checkbox_key': 'checkbox_黛安娜', 'gui_combo_num_key': 'combo_num_黛安娜'}, '辛德拉': {'name': '辛德拉', 'jobs': ['法师'], 'races': ['灵魂莲华'], 'price': '4', 'gui_name': '4-辛德拉', 'gui_checkbox_key': 'checkbox_辛德拉', 'gui_combo_num_key': 'combo_num_辛德拉'}, '凯隐': {'name': '凯隐', 'jobs': ['死神'], 'races': ['幽魂'], 'price': '4', 'gui_name': '4-凯隐', 'gui_checkbox_key': 'checkbox_凯隐', 'gui_combo_num_key': 'combo_num_凯隐'}, '佐伊': {'name': '佐伊', 'jobs': ['法师'], 'races': ['吉星', '剪纸仙灵'], 'price': '3', 'gui_name': '3-佐伊', 'gui_checkbox_key': 'checkbox_佐伊', 'gui_combo_num_key': 'combo_num_佐伊'}, '婕拉': {'name': '婕拉', 'jobs': ['圣贤'], 'races': ['剪纸仙灵'], 'price': '2', 'gui_name': '2-婕拉', 'gui_checkbox_key': 'checkbox_婕拉', 'gui_combo_num_key': 'combo_num_婕拉'}, '卡莎': {'name': '卡莎', 'jobs': ['迅捷射手'], 'races': ['墨之影'], 'price': '4', 'gui_name': '4-卡莎', 'gui_checkbox_key': 'checkbox_卡莎', 'gui_combo_num_key': 'combo_num_卡莎'}, '纳尔': {'name': '纳尔', 'jobs': ['护卫'], 'races': ['永恒之森'], 'price': '2', 'gui_name': '2-纳尔', 'gui_checkbox_key': 'checkbox_纳尔', 'gui_combo_num_key': 'combo_num_纳尔'}, '亚索': {'name': '亚索', 'jobs': ['决斗大师'], 'races': ['灵魂莲华'], 'price': '1', 'gui_name': '1-亚索', 'gui_checkbox_key': 'checkbox_亚索', 'gui_combo_num_key': 'combo_num_亚索'}, '千珏': {'name': '千珏', 'jobs': ['死神'], 'races': ['灵魂莲华', '永恒之森'], 'price': '2', 'gui_name': '2-千珏', 'gui_checkbox_key': 'checkbox_千珏', 'gui_combo_num_key': 'combo_num_千珏'}, '塔姆': {'name': '塔姆', 'jobs': ['斗士'], 'races': ['山海绘卷'], 'price': '3', 'gui_name': '3-塔姆', 'gui_checkbox_key': 'checkbox_塔姆', 'gui_combo_num_key': 'combo_num_塔姆'}, '赛娜': {'name': '赛娜', 'jobs': ['狙神'], 'races': ['墨之影'], 'price': '2', 'gui_name': '2-赛娜', 'gui_checkbox_key': 'checkbox_赛娜', 'gui_combo_num_key': 'combo_num_赛娜'}, '奇亚娜': {'name': '奇亚娜', 'jobs': ['决斗大师'], 'races': ['天将'], 'price': '2', 'gui_name': '2-奇亚娜', 'gui_checkbox_key': 'checkbox_奇亚娜', 'gui_combo_num_key': 'combo_num_奇亚娜'}, '亚托克斯': {'name': '亚托克斯', 'jobs': ['斗士'], 'races': ['幽魂', '墨之影'], 'price': '2', 'gui_name': '2-亚托克斯', 'gui_checkbox_key': 'checkbox_亚托克斯', 'gui_combo_num_key': 'combo_num_亚托克斯'}, '阿兹尔': {'name': '阿兹尔', 'jobs': ['神谕者'], 'races': ['永恒之森'], 'price': '5', 'gui_name': '5-阿兹尔', 'gui_checkbox_key': 'checkbox_阿兹尔', 'gui_combo_num_key': 'combo_num_阿兹尔'}, '锤石': {'name': '锤石', 'jobs': ['擎天卫'], 'races': ['灵魂莲华'], 'price': '3', 'gui_name': '3-锤石', 'gui_checkbox_key': 'checkbox_锤石', 'gui_combo_num_key': 'combo_num_锤石'}, '俄洛伊': {'name': '俄洛伊', 'jobs': ['法师', '护卫'], 'races': ['幽魂'], 'price': '3', 'gui_name': '3-俄洛伊', 'gui_checkbox_key': 'checkbox_俄洛伊', 'gui_combo_num_key': 'combo_num_俄洛伊'}, '雷克塞': {'name': '雷克塞', 'jobs': ['斗士'], 'races': ['永恒之森'], 'price': '1', 'gui_name': '1-雷克塞', 'gui_checkbox_key': 'checkbox_雷克塞', 'gui_combo_num_key': 'combo_num_雷克塞'}, '巴德': {'name': '巴德', 'jobs': ['迅捷射手'], 'races': ['山海绘卷'], 'price': '3', 'gui_name': '3-巴德', 'gui_checkbox_key': 'checkbox_巴德', 'gui_combo_num_key': 'combo_num_巴德'}, '洛': {'name': '洛', 'jobs': ['武仙子'], 'races': ['天龙之子', '仙侣'], 'price': '5', 'gui_name': '5-洛', 'gui_checkbox_key': 'checkbox_洛', 'gui_combo_num_key': 'combo_num_洛'}, '霞': {'name': '霞', 'jobs': ['迅捷射手'], 'races': ['天龙之子', '仙侣'], 'price': '5', 'gui_name': '5-霞', 'gui_checkbox_key': 'checkbox_霞', 'gui_combo_num_key': 'combo_num_霞'}, '奥恩': {'name': '奥恩', 'jobs': ['擎天卫'], 'races': ['永恒之森'], 'price': '4', 'gui_name': '4-奥恩', 'gui_checkbox_key': 'checkbox_奥恩', 'gui_combo_num_key': 'combo_num_奥恩'}, '塞拉斯': {'name': '塞拉斯', 'jobs': ['斗士'], 'races': ['夜幽'], 'price': '4', 'gui_name': '4-塞拉斯', 'gui_checkbox_key': 'checkbox_塞拉斯', 'gui_combo_num_key': 'combo_num_塞拉斯'}, '妮蔻': {'name': '妮蔻', 'jobs': ['法师'], 'races': ['天将', '山海绘卷'], 'price': '2', 'gui_name': '2-妮蔻', 'gui_checkbox_key': 'checkbox_妮蔻', 'gui_combo_num_key': 'combo_num_妮蔻'}, '厄斐琉斯': {'name': '厄斐琉斯', 'jobs': ['狙神'], 'races': ['灵魂莲华'], 'price': '3', 'gui_name': '3-厄斐琉斯', 'gui_checkbox_key': 'checkbox_厄斐琉斯', 'gui_combo_num_key': 'combo_num_厄斐琉斯'}, '永恩': {'name': '永恩', 'jobs': ['死神'], 'races': ['夜幽'], 'price': '3', 'gui_name': '3-永恩', 'gui_checkbox_key': 'checkbox_永恩', 'gui_combo_num_key': 'combo_num_永恩'}, '瑟提': {'name': '瑟提', 'jobs': ['护卫'], 'races': ['夜幽', '灵魂莲华'], 'price': '5', 'gui_name': '5-瑟提', 'gui_checkbox_key': 'checkbox_瑟提', 'gui_combo_num_key': 'combo_num_瑟提'}, '莉莉娅': {'name': '莉莉娅', 'jobs': ['神谕者'], 'races': ['山海绘卷'], 'price': '4', 'gui_name': '4-莉莉娅', 'gui_checkbox_key': 'checkbox_莉莉娅', 'gui_combo_num_key': 'combo_num_莉莉娅'}, '彗': {'name': '彗', 'jobs': [], 'races': ['山海绘卷', '画圣'], 'price': '5', 'gui_name': '5-彗', 'gui_checkbox_key': 'checkbox_彗', 'gui_combo_num_key': 'combo_num_彗'}, '拉露恩': {'name': '拉露恩', 'jobs': ['神谕者'], 'races': ['夜幽'], 'price': '3', 'gui_name': '3-拉露恩', 'gui_checkbox_key': 'checkbox_拉露恩', 'gui_combo_num_key': 'combo_num_拉露恩'}, '可酷伯': {'name': '可酷伯', 'jobs': ['斗士'], 'races': ['吉星'], 'price': '1', 'gui_name': '1-可酷伯', 'gui_checkbox_key': 'checkbox_可酷伯', 'gui_combo_num_key': 'combo_num_可酷伯'}, '霞洛': {'name': '霞洛', 'jobs': ['武仙子', '迅捷射手'], 'races': ['天龙之子', '仙侣'], 'price': '5', 'gui_name': '5-霞洛', 'gui_checkbox_key': 'checkbox_霞洛', 'gui_combo_num_key': 'combo_num_霞洛'}}
