#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : reject_junkword.py
# @Author: Cedar
# @Date  : 2020/4/23
# @Desc  : 数据库reject_junkword


# import pymysql
#
#
# def query_mysql(config_params, query_sql):
#     """
#     执行SQL
#     :param config_params:
#     :param query_sql:
#     :return:
#     """
#     # 连接mysql
#     config = {
#         'host': config_params["host"],
#         'port': config_params["port"],
#         'user': config_params["user"],
#         'passwd': config_params["passwd"],
#         'db': config_params["db"],
#         'charset': 'utf8mb4',
#         'cursorclass': pymysql.cursors.DictCursor
#     }
#     results = None
#     try:
#         conn = pymysql.connect(**config)
#         conn.autocommit(1)
#         # 使用cursor()方法获取操作游标
#         cur = conn.cursor()
#         cur.execute(query_sql)  # 执行sql语句
#         results = cur.fetchall()  # 获取查询的所有记录
#         conn.close()  # 关闭连接
#     except Exception as e:
#         pass
#
#     return results
#
#
# extractor_118 = {'host': '192.168.1.118', 'port': 3306, 'user': 'root', 'passwd': 'poms@db', 'db': 'mymonitor'}
# reject_junkword_list = []
# reject_junkword = query_mysql(extractor_118, 'select junk_word from reject_junkword;')
# for word in reject_junkword:
#     reject_junkword_list.append(word["junk_word"])
# print(reject_junkword_list)

reject_junkword_list = ['18娱乐', '28杠', '500万娱乐城', '6和彩', '888娱乐城', '88娱乐', 'bet365', 'bet365娱乐城', 'ca88娱乐', 'CEO线上娱乐城',
                        'EWIN11娱乐', 'jybet线上娱乐城', 'SK5娱乐', 'tt线上娱乐城', 'v9国际', 'VictorChandler娱乐城', '_百家乐策略', '七胜娱乐',
                        '万福娱乐场', '万达国际', '万达娱乐', '世爵娱乐', '中华娱乐', '中宝娱乐', '丰收娱乐', '乐天堂', '乐天堂线上娱乐城', '乐宝娱乐城', '乐橙官网',
                        '二代身份证', '亚洲皇冠', '亚洲第一网投', '亚洲888', '亚洲城', '亚洲娱乐', '亚洲最佳娱乐', '亚洲赌球', '亚游平台', '亚美娱乐', '亚虎',
                        '京城娱乐城', '亿万先生', '优德88', '体彩博', '体育投注', '免费注册', '公海赌船', '六合彩', '六和彩', '六合', '六合东方圣经h', '六合彩',
                        '六和彩', '六和采', '凤凰先机', '凤凰与飞', '凤凰娱乐城', '凯发娱乐', '凯时娱乐', '利发娱乐', '利来娱乐', '利群棋牌', '加多宝娱乐', '医疗典藏文',
                        '医院证明', '十二生肖', '华都娱乐城', '卖六合', '博彩咨询', '博彩网', '博九', '博坊娱乐网', '博天堂', '博彩娱乐', '博彩娱乐城', '博彩网站',
                        '博赌城', '台湾佬娱乐网', '各国球衣', '合彩图', '和记娱乐', '哈瑞斯娱乐城', '唯一发布', '唯一网站', '唯一发布网址', '唯一官网', '嘎山湖',
                        '国际官网', '国外赌钱网', '国际娱乐', '国际注册送', '国际网上娱乐', '在线娱乐', '在线登录', '城娱乐场', '备用网址', '外围赌球', '外围足球',
                        '大发888娱乐场', '大发体育', '大发体育官网', '大发娱乐', '大同线上娱乐城', '大地国际娱乐', '大奖365', '大奖88', '大奖娱乐', '大奖网',
                        '大连娱乐网', '天猫娱乐', '天堂娱乐', '天天返水', '天成娱乐', '太子娱乐网', '娱乐平台', '娱乐博彩', '娱乐场', '娱乐场官网', '娱乐场小姐',
                        '娱乐城', '娱乐官网', '娱乐平台', '娱乐登', '娱乐网', '娱乐网址', '娱乐评测', '娱乐赌博', '娱乐赌博网站', '软件下载', '娱乐返水', '娱乐送彩金',
                        '官方指定', '官网唯一', '官网直营', '官方下载', '官方主页', '官网平台', '官网直达', '宝胜现场', '宝记国际', '客户端开户', '家乐开户', '家乐开户',
                        '富婆图片', '富婆女主', '尊龙国际', '尊龙娱乐', '开奖查询', '开奖结果', '开户送现金', '彩金娱乐', '彩票网站', '彩金', '彩金娱乐', '德州扑克',
                        '总统博彩', '恒利娱乐', '悦国际娱乐', '扑克比赛', '扑克王娱乐', '打牌技巧', '投注网平台', '拉斯维加斯娱乐', '捕鱼游戏', '新天地赌场', '新濠娱乐城',
                        '新葡京', '明仕亚洲', '明升88', '明升娱乐', '明珠娱乐', '星际娱乐', '期8娱乐', '权威认证', '杏彩', '梦之城', '棋牌官网', '棋牌游戏',
                        '欢迎光临', '欢迎您', '欢迎阁下', '正规网上赌博', '比分直播', '水沐天城', '永乐国际', '永利国际', '永利高', '汇金国际游戏', '沙霸娱乐',
                        '沙龙娱乐', '浩博城', '海立方博彩', '游戏网站', '游戏软件', '游戏大厅', '游戏网站', '澳门沐川', '澳门百家乐', '澳门赌场', '澳门首推',
                        '澳门兰桂坊酒店', '澳门娱乐', '澳门娱乐网站', '澳门永利', '澳门沐川', '澳门百家乐娱乐场', '澳门贵宾娱乐', '澳门黑赌场', '煌朝精准', '爱拼娱乐',
                        '牡丹娱乐', '特码分析', '特码开奖', '特码诗', '玉和娱乐城', '环亚娱乐', '现场娱乐', '现金娱乐', '现金足球网站', '电玩城', '登录平台', '登陆网址',
                        '百乐门', '百家乐', '皇冠国际', '皇冠足球', '皇冠总代理', '皇冠总部娱乐场', '皇冠网', '皇家娱乐', '盈佳国际', '盛大线上娱乐', '真人娱乐',
                        '真人线上娱乐城', '真假富婆', '真驾驶证', '神秘彩金', '福布斯国际娱乐', '福布斯娱乐', '米兰娱乐城', '红利来娱乐', '红鹰娱乐', '纽约国际线上娱乐城',
                        '线上娱乐', '线上游戏', '线上赌场', '线上博彩', '线上娱乐', '线上娱乐城', '线上投注', '线上游戏', '线上赌场', '维多利亚赌场', '网上赌场',
                        '网上赌球', '网上博彩推荐', '网上娱乐', '网上手机投注', '网上投注', '网上现金娱乐城', '网上赌博', '网上赌现金', '罗马线上娱乐城', '美人鱼娱乐',
                        '美高梅', '老葡京', '老虎机', '胜博发娱乐', '腾博会', '莎莎娱乐城', '菲律宾赌场', '葡京赌场', '蓝宝石娱乐城', '被富婆包', '诺贝尔线上娱乐城',
                        '豪门娱乐', '赌场网', '赌球', '赌博大转轮', '赌博游戏', '赌博设备', '赌球官网', '赌球网址', '赌钱网站', '超级返利', '足球博彩', '跑得快技巧',
                        '达屋娱乐场', '迪士尼娱乐场', '迪拜博彩', '送彩金', '送彩金37元的娱乐城', '通宝娱乐', '速博娱乐城', '釆铁算盘', '金宝博', '金沙', '金沙娱乐',
                        '金沙赌场', '金牌娱乐频道', '金瑞棋牌', '金赞娱乐城', '金赞赌城', '金都娱乐场', '金钱豹娱乐城', '钱柜娱乐', '银河国际', '银河娱乐', '长乐坊娱乐',
                        '长城开户', '韦德博彩', '韦德娱乐城', '香港特码', '香港六合彩', '香港六合采', '香港数字彩', '香港特码', '香港赛马', '香港赛马6he', '香港马会',
                        '马会娱乐', '马会开奖日', '马可波罗网', '高额返水', '鸿博娱乐', '黄金海岸赌场', '兰州做假证', '办假病假条_', '办教师资格证_', '百度_知道_中心_',
                        '真实出生医学证明', '真实出生证办理', 'ONS服务', '上门全套', '亚州色图', '亚洲人体', '交易网全集', '人体摄影', '人体无毛', '保健按摩', '全套保健',
                        '全套包夜', '全集无删减版', '制服丝袜', '剧照高清大图', '包夜服务', '单身富婆', '囡囡色', '大奶子', '娱乐官网', '娱乐新闻网', '富婆QQ交友',
                        '富婆找男人', '富婆网', '富婆被骗', '小姐打炮', '小姐推油', '成人在线', '成人夫妻', '成人影', '找全套', '找婊子', '找少妇', '找服务',
                        '找鸡婆', '按摩小姐', '搞笑视频', '明仕亚洲', '服务全套', '爆浆内内', '特殊按摩', '特殊服务', '王爷慢点', '真人种子', '真实服务', '真希人体',
                        '美少女战士真人版', '色妹妹', '苍井', '莞式一条龙', '视频高清版', '迅雷下载', '迅雷高速下载', '邪恶图片', '邪恶漫画', '酒店桑拿', '免费在线咨询',
                        '免费法律咨询', '内容请看花絮', '写作指导', '各省市形象报告', '名家精品展', '女神大盘点', '家具的选购技巧', '小说在线阅读', '市场信息集锦', '性格大全',
                        '手表怎么回收', '文化常识大全', '最佳小学500强', '最想投胎省份', '最牛智力测试', '模板下载', '水电装修价格', '生活小窍门', '维修大全', '预告最新版',
                        '饮食妙招', 'HPV6应该怎样治疗', '专业脱毛', '乳房变小手术', '人流医院', '人流医院是哪家', '人流哪间医院', '人流手术', '人流注意事项', '仁爱中医医院',
                        '仁爱儿科', '修复哪里好', '做双眼皮', '做引产最正规医院', '儿童结膜炎', '养生走路法', '割包皮的男科', '包皮手术要多', '包皮术要多少钱', '包皮过长医院',
                        '医院哪个', '医院哪个好', '医院哪家口碑好', '医院哪家好', '医院哪家更好', '医院哪家较好', '医院哪里较好', '医院那个好', '华医问问', '去晒斑',
                        '去除婴儿胎记', '双眼皮修复', '双眼皮要多少钱', '名医在线解答', '哈尔滨眼袋', '哪个医院', '哪个医院做人流', '哪个医院无痛', '哪个医院最权威',
                        '哪个医院比', '哪个医院治尖', '哪个医院看', '哪个医院看腹', '哪个大夫治甲亢', '哪个妇科医院', '哪个妇科医院人', '哪家医院', '哪家医院口碑最好',
                        '哪家医院好', '哪家医院比较好', '哪家医院男科', '哪家妇科医院好', '哪家整形好', '哪家整形最好', '哪家男科', '哪家男科专科好', '哪家男科医院好',
                        '哪有治咽喉', '哪有治咽喉炎', '哪里妇科', '哪里打胎最好', '哪里治疗', '哪里治疗癫痫', '嘴唇变薄', '四平市无痛人流', '在线预约挂号', '埋线双眼皮',
                        '太仓中医院妇科', '如何治早泄', '如何诊断不孕', '如何预防过敏', '妇科检查医院', '妇科炎症价格', '妇科炎症治疗要多少钱', '孕前检查项目', '孕妇牙龈炎',
                        '宝玉医生', '宫颈糜烂hpv感染', '宫颈糜烂怎么治疗', '尖锐湿疣', '尖锐湿疣哪里', '尿道炎医院', '巴中打胎', '康升健康管', '开眼角手术', '微整形技术培训',
                        '微针多少钱', '快速嫩肤', '快速瘦身', '性病医院', '手术疤痕', '手术要多少钱', '护肝全攻略', '整形医院', '早泄专科医院', '早泄医院', '昆山切割包皮',
                        '最专业的男科医院', '最好的医院', '最好的妇科医院', '最好的癫痫病', '最好的骨科医院', '最权威的医院', '最权威的妇科', '最权威的妇科医院', '最棒的骨科医院',
                        '朝天鼻的矫正', '梅毒专家咨询', '死精症检查', '治不孕好的医院', '治疗偏方', '治疗前列腺', '治疗咽炎', '治疗好医院', '治疗宫颈糜烂', '治疗小儿',
                        '治疗淋巴瘤', '治疗牙痛', '治疗白癜风最好', '治疗神经损伤', '治疗红斑狼疮', '治疗胎停', '治疗胎记', '治疗脂溢性皮炎', '治疗脑瘫', '治疗脱发',
                        '治疗腋臭医院', '治疗血', '治疗雀斑', '治疗鲜红胎', '治疗鼻窦炎', '流产要多少钱', '流医院是哪家', '深圳看妇科', '湿疣医院', '滨州最好的妇',
                        '激光治疗', '点痣风险大吗', '烫伤的治疗', '牙骨粉', '牙齿矫正', '牛皮癣专科', '狐臭医院', '田痣费用', '甲亢医院', '男性健康医院', '疱疹治疗',
                        '疹治疗好医院', '痔疮医院', '痣怎么治疗', '癫痫', '癫痫病专科医院', '癫痫病哪里', '白癜风咨询', '盐城做假牌照', '看不孕不育', '看妇科', '看妇科怎样',
                        '眼皮整容', '矫形器行业', '矫正口吃', '矫正牙', '祛痘', '红斑狼疮', '红胎记医院', '美容双眼皮', '肌肤补水', '胎记去哪里', '脑瘫医院',
                        '臀肌挛缩症', '臀部塑形', '蕾丝面膜', '蚕丝面膜', '西安医治早泄', '西安安全打胎', '西安手术去眼袋', '身体美白', '输卵管堵塞', '达州人流的手术',
                        '近视激光治疗', '遗尿症医院', '那个妇科医院好', '重庆肛肠治疗', '重庆肠道清洗', '钱_医帮', '银屑病', '长春医院无痛人流', '除宝宝胎记', '除小儿胎记',
                        '除皱多少钱', '除皱术', '隆鼻价格', '隆鼻医院', '隆鼻多少钱', '韩式双眼皮美容', '韩式裸妆', '韩式隆鼻', '骨性龅牙', '鲜红斑痣', '鼻梁增高',
                        '鼻翼缩小', '鼻部整形医院', '哪家医院', '医院怎么样', '医院好不好', '医院在哪儿', '有什么症状', '治性病', '不用开刀', '哪个正规', '养肾法',
                        '888平台', 'AG娱乐游戏平台', 'ATFX平台', '博彩公司', '博彩网', '国际娱乐', '国际娱乐城', '大发888', '天恒平台', '娱乐场', '娱乐场所',
                        '娱乐城', '娱乐平台', '娱乐手机版', '客户端下载', '家家琐事', '小说网', '平台官网', '彩平台', '彩票平台', '彩金', '时时彩', '棋牌游戏',
                        '竞彩网', '线上娱乐', '网上送现金', '网络博彩', '赔率分析', '足球投注', '顶游资讯', '顺义牌具', '4887铁算盘', 'EWIN11娱乐', 'SK5娱乐',
                        '百家乐策略', '点击进入', '天线宝宝', '七大主流', '中华娱乐', '中宝娱乐', '丰收娱乐', '乐透投注', '亚洲皇冠', '亚洲第一网投', '亿隆博彩',
                        '代开住宿费代开', '体彩博', '体育注册', '体彩大乐透', '俄罗斯轮盘', '免费试玩', '免费资料', '全球最大', '六合彩', '六合网', '六合财经', '六合采',
                        '六和彩', '六和釆', '六合跑狗图黑白', '决赛赛程', '凤凰先机', '凯丰娱乐场', '利发娱乐', '动画玄机', '医疗典藏文', '华人策略', '博九官网',
                        '博彩咨询', '博彩技巧', '台湾佬娱乐网', '各国球衣', '合彩图', '吉利论坛', '唯一发布', '唯一官方', '唯一指定', '唯一网站', '唯一信任官网',
                        '国际官网', '国际开户', '国际投注网', '国外赌钱网', '国际注册送', '图库彩图', '在线娱乐', '城娱乐场', '大仙特码', '大仙解码', '大额无忧',
                        '大发体育官网', '大宗直播室', '大连娱乐网', '天猫娱乐', '天鹰高手集', '天堂娱乐', '太子娱乐网', '太阳城网上娱乐', '娱乐', '娱乐代理', '娱乐在线',
                        '娱乐网', '娱乐场官网', '娱乐网址', '娱乐评测', '娱乐赌博网站', '娱乐送彩金', '官方唯一', '官方平台', '官方指定', '官网唯一', '官网直营',
                        '宝胜现场', '家乐开户', '山东六合鸭苗', '帝一娱乐', '开奖号码', '开奖报码', '开奖直播', '开奖结果', '开心开户', '开户体验', '开奖结大联',
                        '开封代考', '开户送现金', '彩金娱乐', '彩票PK10', '德州扑克', '心水论坛', '心水', '恭送号码', '投注双色球', '新金沙现金', '时时彩软件',
                        '易鱼棋牌', '星际娱乐', '期8娱乐', '期特码', '杀肖网', '权威认证', '棋牌室转', '比分直播', '水沐天城', '永盈会赌场', '永利博线上',
                        '汇金国际游戏', '沙霸娱乐', '法老王娱乐', '波色生肖', '注册送豪', '注册送', '游戏平台', '游戏网站', '游戏软件', '澳门在线', '澳门沐川',
                        '澳门百家乐', '澳门赌场', '澳门首推', '澳门娱乐网站', '澳门皇冠球', '澳门直营', '特码分析', '特码金牌', '玩家首选', '玩法技巧攻略', '现金大转轮',
                        '现金娱乐', '现金红利', '现金足球网站', '生肖是什么特码', '申博开户', '电子游艺', '百家乐图片', '皇冠国际', '皇冠比分网', '皇冠足球', '皇冠总代理',
                        '皇冠最新网站', '皇冠网', '皇家一搏国际', '直播球探', '真钱游', '立博开户', '红鹰娱乐', '线上游戏', '线上赌场', '网上赌场', '网上赌球',
                        '老版九龙', '聚宝盆', '肯博开户', '虎机单机版', '豪门娱乐', '赌博开户', '赌场网', '赌场网站', '赌球网址', '足球博彩', '足球彩票', '足球游戏',
                        '足球资讯香港马会', '跑得快技巧', '达屋娱乐场', '金棋牌游戏', '金牌娱乐频道', '钻石娱乐', '镇服务真正小姐', '韦德博彩', '香港曾道', '香港特码',
                        '香港赛马', '马会开奖', '马会网址', '马会资料', '那全套', '发票代开', '全套上门服务', '全套服务', '啪啪一晚', '收藏本版', 'QQ帐号登录',
                        '外围女', '少女鲁鲁射', '囡囡色', '乱伦完本小说', '免费一级片', '阴道图片', 'av自拍', '高清操b', '露私图', '电影天堂', '激情电影', '小穴小说',
                        '丝袜淫娃', '桃色电影天堂', '操干姐姐', '诱人写真', '黑屌爆操', '想操表妹', '动动兽交', '幼女尿尿', '舔鸡巴', '情趣少妇', '色情影院', '亚洲图片',
                        '少妇15p', '美女15p', '内衣写真', '三级', '之爱小说', '乱伦', '乱伦故事', '亚州色图', '亚洲人体', '人体摄影', '人体无毛', '人体艺术',
                        '人妻', '内内', '内射', '制服', '制服丝袜', '口交', '和狗', '嗒嗒奔', '处女', '夜夜', '大奶子', '女优', '女神卫生巾', '妹伦乱',
                        '娱乐官网', '娱乐版块', '小泽菜穗', '少妇', '岛国', '工口动画片', '巨乳', '床声', '快播', '性交', '性感', '性爱', '情色', '想入飞飞',
                        '成人在线', '成人夫妻', '成人影', '成人电影', '成人色站', '成人艺术', '撸掉', '撸撸', '无码', '日本小姐', '明仕亚洲', '毛片', '泷泽萝拉',
                        '熟女', '熟逼', '爆浆内内', '爱情小说', '王爷慢点', '真人种子', '真希人体', '破处', '种子', '美女', '羞羞的', '肥臀', '脚操者', '自撸',
                        '色情', '色欲', '苍井', '萝莉幼女尿尿', '被干', '裸体', '裸体图', '裸妞', '诱惑', '邪恶', '邪恶图片', '邪恶漫画', '阴毛', '阴道',
                        '颜射', '高射', '高级享受', '黄片', '黄色片', '黄色电影', '黄色网站', '黑丝袜', '黑木耳', '露大鸟', '堁体图片', '肌肉男堁', '色成人影院',
                        'av不雅视频', '推油服务', '按摩特殊', '找美女全', '膜图片', '小姐多少钱', '一条龙找包夜', '高清图集', '小姐保健', '按摩全套', '全套特殊服务',
                        '站街电话', '找服务电话', '免费领取激情', '县婊子哪里多', '全套找到按摩', '全套找个按摩', '按摩特殊多少钱', '镇服务真正小姐', '三陪大保健', '大保健电话',
                        '色妹妹', '暴乳', '动态图美女', '性之影吧', '免费看性爱毛', '达屋娱乐场', '澳门娱乐网站', '棋牌官网', '菲律宾赌场', '皇家娱乐', '彩票网站',
                        '扑克比赛', '打牌技巧', '太子娱乐网', '捕鱼游戏', '皇冠总代理', '太阳城网上娱乐', '牡丹娱乐', '娱乐送彩金', '娱乐赌博网站', '鸿博娱乐', '娱乐平台',
                        '娱乐网', '长乐坊娱乐', '六合彩', '开奖结果', '娱乐网址', '线上赌场', '银河娱乐', '钱柜娱乐', '马会娱乐', '娱乐在线', '彩金娱乐', '沙霸娱乐',
                        '煌朝精准', '在线娱乐', '网上投注', '嘎山湖', '中宝娱乐', '天猫娱乐', '娱乐代理', '七胜娱乐', '网上娱乐', '备用网址', '娱乐场', '欢迎阁下',
                        '赌球网址', '亚洲赌球', '宝胜现场', '现场娱乐', '现金娱乐', '爱拼娱乐', '唯一官网', '亚洲娱乐', '澳门赌场', '澳门沐川', '水沐天城', '百家乐策略',
                        '官网直达', '世爵娱乐', '官网唯一', '线上投注', '网上赌球', '釆铁算盘', '长城开户', '投注网平台', '赌博游戏', '赌钱网站', '游戏大厅',
                        '国际注册送', '开奖查询', 'SK5娱乐', '卖六合', '游戏网站', '官方唯一', '线上游戏', '香港特码', '亚洲第一网投', '家乐开户', '足球游戏',
                        '大仙解码', '体育注册', '博九官网', '双色球预测', '体彩大乐透', '吉利论坛', '波色生肖', '生肖是什么特码', '百家乐图片', '六和釆', '澳门在线',
                        '动画玄机', '开奖号码', '华人策略', '七大主流', '全球最大', '游戏平台', '投注网站', '赌球网', '亿隆博彩', '皇家一搏国际', '皇冠最新网站',
                        '玩法技巧攻略', '现金红利', '永盈会赌场', '电子游艺', '赌场网站', '开户送钱', '直播球探', '国际开户', '名爵国际', '马会网址', '六合采',
                        '现货直播室', '天线宝宝', '大仙特码', '帝一娱乐', '开奖报码', '杀肖网', '开奖直播', '永利博线上', '唯一信任官网', '决赛赛程', '必赢亚洲',
                        '阿牛直播', '大宗直播室', '天鹰高手集', '在线澳门', '心水论坛', '六合跑狗图黑白', '特码金牌', '欧冠视频', '好搜推荐', '虎机单机版', '免费试玩',
                        '开户体验', '申博开户', '马会开奖', '开奖结大联', '唯一指定', '新金沙现金', '现金大转轮', '注册送豪', '图库彩图', '老版九龙', '乐透投注',
                        '投注双色球', '皇冠比分网', '马会资料', '棋牌室转', '立博开户', '聚宝盆', '时时彩软件', '国际投注网', '易鱼棋牌', '真钱游', '捕鱼达人官网',
                        '金棋牌游戏', '香港曾道', '道人生肖', '俄罗斯轮盘', '六合财经', '玩家首选', '六合网', '赌博开户', '期特码', '大额无忧', '足球彩票', '官方平台',
                        '代开住宿费发票', '开封代考', '镇服务真正小姐', '鸿发平台', '凯丰娱乐场', '玩家线路', '开心开户', '肯博开户', '捷豹娱乐', '足球投注', '百家乐技巧',
                        '手机棋牌', '彩图全集', '特码波平', '合彩特码', '球投注', '特码图', '六合幽默', '六合驿站', '香港马会', '六合摇珠', '彩色图库', '澳门现金',
                        '真人游戏', '六和', '投注官网', '特马网站', '澳门直营', '玄机彩图', '绝密公式', '最新资讯', '体育在线', '欧洲杯投注', '六合', '骰子平台',
                        '棋牌平台', '百家乐', '娱乐注册', '代开', '找小姐', '北京赛车', '国际游戏', '一夜情', '1夜情', '大保健', '华纳国际', '捕鱼大亨', '手机捕鱼',
                        '秒速赛车', 'k3k捕鱼', '棋牌', '鱼鹰捕鱼', 'app下载', '威斯尼人', '炸金花', '幸运农场', '斗地主', '扎金花', '麻将开户', '彩票下载',
                        '投彩票', '在线开户', '开户在线', '安卓下载', '苹果下载', '360彩票', '幸运28', '办理请联系全国到付', '牛牛下载', '牛牛开户', 'pk10彩票',
                        '1688彩票', '彩票app', 'app彩票', '下载彩票', '小白彩票', '福彩3d', '牛蛙彩票', 'dd彩票', '金莎娱乐', '优信彩神', '933彩票',
                        '尊彩网', '久久香蕉', 'av在线', '在线av', 'TXT全集下载', '彩票', '赌博']


if __name__ == '__main__':
    _title = '博彩6咨询'
    if _title in reject_junkword_list:
        print(1)
