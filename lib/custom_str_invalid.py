#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : custom_str_invalid.py
# @Author: Cedar
# @Date  : 2020/4/27
# @Desc  : 自定义垃圾词汇


custom_str_invalid_list = [
    '/content/article/',
    'articleid',
    'avi',
    'mpeg',
    '3gp',
    'mp3',
    'mp4',
    'wav',
    'jpeg',
    'gif',
    'jpg',
    'png',
    'apk',
    'exe',
    'pdf',
    'rar',
    'zip',
    'docx',
    'doc',
    'txt',
    'javascript',
    '招聘',
    '诚聘英才',
    '加入我们',
    '关于我们',
    'company',
    'search',
    '详细',
    '有限公司',
    '在线咨询',
    'product',
    '立即报名',
    '立即查看',
    '联系我们',
    '注册',
    '登录',
    '公司简介',
    '上一页',
    '下一页',
    '详情点击',
    '忘记密码',
    '>>',
    '<<',
    '<',
    '>',
    '在线询价',
    '尾页',
    '……',
    'page=',
    '售前咨询',
    '广告',
    '技术支持',
    '进入官网',
    'shop',
    'purchase_mall',
    'goods',
    'login',
    'price',
    '贷款',
    '差评',
    '中评',
    '好评',
    '商品',
    '评价',
    '规格参数',
    '前一页',
    '后一页',
    '最后页',
    '法律声明',
    '有限责任公司',
    '价格',
    '购车',
    '贷款',
    '买车',
    '询底价',
    '询价',
    '2020',
    '2019',
    '2018',
    '2017',
    '2016',
    '2015',
    '2014',
    '2013',
    '2012',
    '2011',
    '2010',
    '2009',
    '2008',
    '2007',
    '2006',
    '2005',
    '2004',
    '2003',
    '2002',
    '2001',
    '2000',
    '返回顶部',
    '参数配置',
    '联系',
    '评论',
    '试驾',
    '置换',
    '对比',
    '价格',
    '综合店',
    '公里',
    '口碑',
    '参数',
    '参数',
    '评测',
    '用车',
    '内饰',
    '空间',
    '前排',
    '后排',
    '点评',
    '方向盘',
    '仪表盘',
    '动力',
    '在售',
    '购',
    '现房',
    '入住',
    '开盘',
    'www.esgcc.com.cn',
    'fbook.net',
    'che.hexun.com',
    'home.fang.com',
    'photo.bitauto.com',
    '.cmmo.cn',
    '.baidu.com',
    'auto.china.com',
    'lmjx.net',
    'ganji.com',
    '8684.cn',
    '.58.com',
    'taisha.org',
    'shafa.com',
    'liexue.cn',
    'feijiu.net',
    'tuniu.com',
    'gongchang.com',
    'mjxx.com',
    'huishoushang.com',
    '114chn.com',
    'dj97.com',
    '8264.com',
    'ceconlinebbs.com',
    'llzg.cn',
    '99114.com',
    '51job.com',
    'mama.cn',
    '01-800.cn',
    'baidu.com',
    'youbian.com',
    'smzdm.com',
    'tulaoshi.com',
    'ximalaya.com',
    'qd8.com',
    'kaoyan.com',
    'hlqxj.com',
    'chahaoba.com',
    'dqccc.com',
    'thea.cn',
    'leju.com',
    'giabbs.com',
    'bitauto.com',
    '.fang.com',
    '.cncn.com',
    'keyunzhan.com',
    'chinapp10.com',
    'ip138.com',
    '108sq.cn',
    'makepolo.com',
    'weibo.com',
    'tuliu.com',
    'huibo.com',
    'mapbar.com',
    'liebiao.com',
    'baixing.com',
    'lizhi.fm',
    '.qeo.cn',
    'city8.com',
    'mayi.com',
    'guahao.com',
    'yuemei.com',
    'glass.cn',
    'news18a.com',
    'testerhome.com',
    '.597.com',
    'examw.com',
    'lawtime.cn',
    '.273.cn',
    'ibicn.com',
    'tuku.cc',
    'xuetian.cn',
    '.2018.cn',
    '.so.com',
    'tvsou.com',
    'allchina.cn',
    'dhtv.tv',
    '.ke.com',
    '.258.com',
    'ynzp.com',
    'wangdaishequ.cn',
    'haozu.com',
    '2021.cn',
    'kshot.com',
    'chahaoba.cn',
    'ruiwen.com',
    'f600.cn',
    'dqguo.com',
    'juxia.com',
    'zxxk.com',
    'koolearn.com',
    'qd8.com.cn',
    'ffbook.cc',
    'lianjia.com',
    '862sc.com',
    '17xie.com',
    'kt250.com',
    'huochepiao.com',
    '3gsc.com.cn',
    'luwan-sports.org',
    '.baka.cc',
    '.3158.cn',
    '51jiaoxi.com',
    'wangxiao.cn',
    'pclady.com.cn',
    '30edu.com.cn',
    'kuyiso.com',
    'offcn.com',
    '.99.com.cn',
    'chadianhua.net',
    '.51240.com',
    'yjbys.com',
    'herostart.com',
    'huatu.com',
    'cheshi.com',
    'chinapp.com',
    'jiameng.com',
    '51test.net',
    'verycd.com',
    '52cnw.net',
    'cailiao.com',
    'chinahr.com',
    'dadou.com',
    '.qj.com.cn',
    'jxrc.cn',
    'tou18.cn',
    'gushimi.org',
    'loupan.com',
    'daojia.com',
    'baiye5.com',
    '.deyi.com',
    'jc001.cn',
    'atobo.com',
    'qunar.com',
    'xjlyw.cn',
    '123shw.com',
    'zhaoshang.net',
    '.jia.com',
    'mysteel.com',
    'findlaw.cn',
    'job910.com',
    '.dm5.com',
    '.b2q.com',
    '.mxj.com.cn',
    'jingxi.net',
    'liansuo.com',
    'tvmao.com',
    'daoxila.com',
    '.027.net',
    '666zp.com',
    'ankanggonglu.com',
    'ziroom.com',
    'xcfangzi.com',
    'huixiaoer.com',
    'doumi.com',
    'isixue.com',
    'fang0564.com',
    '4140.cn',
    'zmn888.com',
    'yewn.cn',
    'gushici.com',
    'gamepedia.com',
    '15tianqi.cn',
    'zhaotie.com',
    'my0511.com',
    'km2s.com',
    '.ly.com',
    'kuaiqikan.com',
    'tcshanghai.com',
    '66chang.com',
    'dysxxw.com',
    'biligame.com',
    'eduego.com',
    'maidianla.com',
    'zzz4.com',
    'jiaoyubao.cn',
    'fabiao.com.cn',
    'fabiao.com',
    'z4bbs.com',
    'egouz.com',
    'risfond.com',
    'tantuw.com',
    'xbiao.com',
    'fypaw.org.cn',
    'youfabiao.com',
    'a-hospital.com',
    'lyfc001.com',
    'house510.com',
    'jxedt.com',
    '.jg.com.cn',
    'github.com',
    'yofang.cn',
    '88ylu.com',
    '28chengshi.com',
    'imobile.com.cn',
    'nowcoder.com',
    'soxsok.com',
    'tianqi.com',
    '91soker.com',
    'diyifanwen.com',
    '.9939.com',
    'che168.com',
    '52zx.net',
    'fotor.com.cn',
    '.eme.cn',
    '21cnjy.com',
    '.85814.com',
    'tadewo.com',
    'zgjm.org',
    'dzbdq.com',
    '91jm.com',
    'hao661.com',
    'shouyoutv.com',
    'sports8.cc',
    'guoxuedian.com',
    '.xwh.cn',
    '999ask.com',
    'taopuwang.com',
    '1688e.com',
    'hao315.tv',
    'zaofabiao.com',
    '.0550.com',
    'zhuangyi.com',
    'leisu.com',
    '360changshi.com',
    'walltu.com',
    '52sobook.com',
    '9lala.com',
    'mkzhan.com',
    'juwai.com',
    'yaokaihui.com',
    '461000.net',
    'chazidian.com',
    'hehua.net',
    '360.cn',
    'as16.com',
    'mingqingxiaoshuo.com',
    'zquan.cc',
    'fdc.com.cn',
    'zhsho.com',
    'dexuee.com',
    'job5156.com',
    'c-c.com',
    'xuekeedu.com',
    '.2280.com',
    'keedu.cn',
    'meimin.us',
    'zgggxxg.cn',
    'iqiyi.com',
    'douban.com',
    'gcwzn.com',
    'gao7.com',
    'zgtghccl.com',
    'paizi.com',
    '9ask.cn',
    'xueshu.com',
    'ahssggj.com',
    'kd120.com',
    'gkong.com',
    'gitee.com',
    'wanzhoujob.com',
    'dmzj.com',
    '7624.net',
    '700mh.com',
    'tianmaotv.cn',
    '51tietu.net',
    'xiadele.com',
    '.0430.com',
    'chizhouren.com',
    'jiajiao114.com',
    'xiaozhu2.com',
    'hx2car.com',
    'elong.com',
    'zhipin.com',
    'city199.com',
    'oldauto.cn',
    'ppkao.com',
    'ygjj.com',
    'danji6.com',
    'jiazhao.com',
    'aqingsong.com',
    'ppt20.com',
    'liuxue86.com',
    'eyuyao.com',
    'daikuan.com',
    'cthy.com',
    'mffanwen.com',
    'kgotrip.com',
    'toursforfun.com',
    'zymk.cn',
    'caissa.com.cn',
    'tourle.cn',
    'dianzhangzhipin.com',
    '3dmgame.com',
    '66game.cn',
    '91chuangye.com',
    'uuhaodian.com',
    'datasheet5.com',
    'ynnu.edu.cn',
    '.233.com',
    'u7u9.com',
    '91wllm.com',
    'veryeast.cn',
    'weaoo.com',
    'snxx.com',
    'eduei.com',
    'gaokao.com',
    '007swz.com',
    '.2345.com',
    'jumijie.cn',
    'cirmall.com',
    '7gz.com',
    '.xin.com',
    'chinapp.net',
    '15hr.com',
    'fzbm.com',
    'faxinxi.cn',
    'wopeng.net',
    'epwk.com',
    'wed114.cn',
    'pcbaby.com.cn',
    'changingedu.com',
    'ngfdc.cn',
    'ysfdc.net',
    'newsmth.net',
    'dyfc.net',
    'yantubao.com',
    'jingjiang.com',
    'fenleitai.com',
    'qhbang.com',
    'dihe.cn',
    'cztoo.com',
    'ihuashi.cn',
    'showguide.cn',
    'dcpfb.com',
    'cnkang.com',
    'yshows.cn',
    '100fenlei.com',
    'gaoming.com.cn',
    '555edu.com',
    'woyaofale.com',
    'my0832.com',
    'youtx.com',
    'ic98.com',
    'fengj.com',
    'bian-min.com',
    '52wangkai.cn',
    'wangbangni.com',
    'tdzyw.com',
    'sj.net.cn',
    'haotoufa.com',
    'haomeizi.cn',
    'hao315.com',
    'qic.ac.cn',
    'chengshiluntan.com',
    'haofang007.com',
    'o2123.com',
    'lh168.net',
    '0359fcw.com',
    'mfcad.com',
    'szpxe.com',
    '96jm.com',
    'iutour.cn',
    '.xhj.com',
    'jsdmedu.cn',
    'edu24ol.com',
    'ieduw.com',
    'sangzhiedu.com',
    'tiboo.cn',
    'studyez.com',
    'ximantu.com',
    'aazao.com',
    'hfhouse.com',
    '.dllp.cn',
    'hmting.com',
    'ptfish.com',
    'kaoyan365.cn',
    '58dm.com',
    'languang.cc',
    'mmfj.com',
    'tryoe.com',
    'bbs.zg163.net',
    'cnnb.com',
    '.1905.com',
    '0411lxw.com',
    'xaoyo.com',
    'oschina.net',
    'zhongkao.com',
    '.hzc.com',
    'qiyeku.com',
    'zhizhu35.com',
    '.917.com',
    'zggqzp.com',
    '168hs.com',
    'managershare.com',
    'bitguai.com',
    'ph66.com',
    '.EOL.CN',
    '131mh.com',
    'ef43.com.cn',
    'd1cm.com',
    '.56.com',
    'hqwx.com',
    'exam8.com',
    'tudou.com',
    'bbs.cnnb.com',
    'shangpusou.com',
    '.u88.com',
    '6666ys.com',
    'jiankang.com',
    'mingxiaow.com',
    'laobangban.com',
    'tingroom.com',
    '51meetings.com',
    'sh7w.cn',
    'mipang.com',
    'knifriend.com',
    'tianqiz.com',
    'edus.cn',
    '4399.com',
    'lw881.com',
    'znjj.tv',
    '5114.net',
    'asmrqq.com',
    'souxuexiao.com',
    'rsinc.com',
    'zx58.cn',
    'v.6.cn',
    'edeng.cn',
    '17yy.com',
    'ituring.com.cn',
    'cpigeon.com',
    'hq0564.com',
    '368fanyi.com',
    'zhev.com.cn',
    '8684.com',
    'gamersky.com',
    '.jjl.cn',
    'cnliequan.com',
    '17house.com',
    '38xf.com',
    'mathworks.cn',
    'scweixiao.com',
    'gaotie.cn',
    'xhwhouse.com',
    '915hr.com',
    'xcabc.com',
    '02516.com',
    'citscq.com',
    '36578.com',
    'jmw.com.cn',
    'qm120.com',
    'tflove.com',
    '1kkk.com',
    'gz007.net',
    'juji123.com',
    'hfqx.com.cn',
    'cnmo.com',
    '50yun.net',
    '66law.cn',
    '0s.net.cn',
    'chacha8.cn',
    'yiichina.com',
    'gaodun.com',
    'qiuyi.cn',
    'xdf.cn',
    'zgsydw.com',
    'oym56lm.com',
    'shushuoba.com',
    'myubbs.com',
    '9856.cn',
    'walekan.com',
    'suntchsolar.com',
    'qipeiren.com',
    'home898.com',
    'cnprint.org',
    'bidesin.com',
    'lhswu.com',
    'hlgnet.com',
    'shouyoubus.com',
    'bibenet.com',
    'jz66.cn',
    'cyikao.com',
    'xhaiwai.com',
    '58jmw.com',
    'pchouse.com.cn',
    '150015.cn',
    'pangwo.com',
    '100yangsheng.com',
    'yidianling.com',
    '51faxinxi.com',
    'doujixiaosu.com',
    'xujiesw8.com',
    'biqu6.com',
    'itdks.com',
    'yescar.cn',
    '91xinshang.com',
    '125yan.com',
    '599.com',
    'chinaedu.edu.cn',
    'wfp.org',
    'guijiaowang.com',
    '51e-online.com',
    '139life.com',
    'aihuaju.com',
    'cyzdy.com',
    '10260.com',
    'haoqikan.com',
    '21bm.com',
    '54114.cn',
    'guoxuemeng.com',
    'xgbs.cn',
    'jixiewz.com',
    'cnfirst.net',
    'baiwanzhan.com',
    'lvse.com',
    'yxad.com',
    'gusuwang.com',
    'nianfo18.com',
    'muhai.net',
    'qichezhan.cn',
    'gushiji.cc',
    'hepan.com',
    'eefocus.com',
    'zhuna.cn',
    'dagumanhua.net',
    'cngold.org',
    'go007.com',
    'banbaowang.com',
    'zgjfks.com',
    'ekon.cn',
    'u04u.com',
    '51edu.com',
    '5198.cn',
    'dzw3.com',
    'moji.com',
    'tzrc.com',
    'ynshangji.com',
    'etlong.com',
    'cnrencai.com',
    'mathworks.com',
    'jianzhi8.com',
    'iautos.cn',
    'ccyp.com',
    'onlylady.com',
    'diandianzu.com',
    'tgbus.com',
    'wfits.com',
    'ksbbs.com',
    'chuangyezg.com',
    'moore.ren',
    'trlpw.com',
    'zhantai8.com',
    'biquge6.com',
    'dailuopan.com',
    'qudao.com',
    'foodmate.net',
    'hao315.cn',
    'qfshuyuan.com',
    'usoele.com',
    'shoudishou.cc',
    'dianping.com',
    '01fy.cn',
    'chsi.com.cn',
    'job8080.com',
    'hujiang.com',
    'lhcxlj.com',
    'biquge.tv',
    'nongmin.com.cn',
    'proginn.com',
    'wufengguan.org',
    'gaibar.com',
    'liaojieju.com',
    'byf.com',
    'maitaowang.com',
    '91cy.cn',
    '0517offer.cn',
    'yoyou.com',
    'moxingyun.com',
    'duqiaorc.cn',
    'reocar.com',
    'fanpusoft.com',
    'dabiqu.com',
    '0734zpw.com',
    'bubukua.com',
    'hr1000.com',
    'admaimai.com',
    'co188.com',
    'bqqm.com.cn',
    'elecfans.com',
    'bishenge.com',
    'okbuy.com85',
    'ttmeishi.com',
    '17173.com',
    '11467.com',
    'yixue99.com',
    '9k9k.com',
    'jxgssy.cn',
    'siilu.com',
    'duyan.cn',
    '915hz.com',
    'moofine.com',
    'yuwenmi.com',
    'jinti.net',
    'xiucai.com',
    'xtuan.com',
    'sklib.cn',
    'aylt.cn',
    'zstv.cn',
    'shushi100.com',
    'luanren.com',
    'cnbanbao.cn',
    'bdsh5.com',
    'dongao.com',
    'artron.net',
    '80guakao.com',
    'manhuadq.cn',
    'my6767.com',
    'zggtxhw.com',
    'bh.sb',
    'bianzhile.com',
    'chineseall.cn',
    'caipucn.com',
    'xiazai.com',
    'xuechela.com',
    '61k.com',
    '68design.net',
    'kuyin.cn',
    'qufair.com',
    'zhenai.com',
    '64365.com',
    'rv28.com',
    'qijizuopin.com',
    'kefulai.com',
    'icauto.com.cn',
    'hqz.com',
    'ali213.net',
    'qiugouxinxi.net',
    'laoban.org',
    'wosku.com',
    'chinawutong.com',
    '360zbz.com',
    'biquge66.cn',
    'tjjjw.org',
    'pconline.com.cn',
    'chaliyi.com',
    'dywx.cc',
    '221600.cn',
    '1010jz.com',
    'zaisubao.cn',
    'zhifure.com',
    'chuguo66.com',
    'km.com',
    'fliggy.com',
    'puercn.com',
    'china.cn',
    'nz86.com',
    'fangchan.com',
    'rexian.net.cn',
    'fangdd.com',
    'ljia.net',
    'jnhouse.com',
    '3qhouse.com',
    'tjzhg.org.cn',
    'lanfw.com',
    'okbuy.com',
    'techuangyi.com',
    'jiazhuang.com',
    't262.com',
    'iedh.com',
    '88tph.com',
    'yibige.com',
    'sports8.net',
    'maoyihang.com',
    'wulianka.cn',
    'xiziwang.net',
    'chekb.com',
    'youbianku.cn',
    'nc.tengfang.net',
    'liqucn.com',
    'boqii.com',
    'taojindi.com',
    'bxzxw.com',
    'liepin.cn',
    'vipcn.com',
    'huiyi8.com',
    'zhaoshang800.com',
    'fangbugui.com',
    'diaoyu.com',
    'gezila.com',
    'feiluxiaoshuo.club',
    'tianqi30.cn',
    '168lore.com',
    'mycar168.com',
    '84z.cn',
    'dn1234.com',
    'ppzuowen.com',
    'xiaozhu.com',
    '51sxue.com',
    'xcar.com.cn',
    'yaolan.com',
    'xuexila.com',
    'xinzuojia.com',
    'meishubao.com',
    'yiqifa.com',
    'taoding.cn',
    'ayzhwl.com',
    '9tour.cn',
    'yicx.com',
    'jb10.cn',
    'healthr.com',
    'dumufan.com',
    '61.com',
    'fireflytrip.com',
    'omiaozu.com',
    'huoniuniu.com',
    '0859job.com',
    'ssjzw.com',
    'jianglishi.cn',
    'shukuai123.com',
    'jiameng001.com',
    'meishichina.com',
    '3278.cn',
    'bilibili.com',
    'eduour.cn',
    'zhms.cn',
    'chinabidding.cn',
    'qqju.com',
    'hunliji.com',
    '7799520.com',
    'zgpingshu.com',
    'haoduoliao.com',
    '63243.com',
    'tell520.com',
    'tuan800.com',
    '027art.com',
    'xtiyu.com',
    'sheidao.com',
    'bzw315.com',
    'lm9999.com',
    'yuloo.com',
    'zzrc.net',
    '8fkd.com',
    'xbyhr.com',
    'geli9.com',
    'wuxianliu.net',
    'xiaoshuomi.cc',
    'qizuang.com',
    'tuotuozu.com',
    'zhuangxiubao.com',
    'qixiangwang.cn',
    '7399.com',
    'telllove520.com',
    'bozhouauto.com',
    'ilife.cn',
    '95mulu.com',
    'ccav5.com',
    '1hai.cn',
    'ybcw.cn',
    'xhd.cn',
    'hncw.cn',
    'jumin.cn',
    'douxie.com',
    'nanrenwo.net',
    'fun.tv',
    '86911.com',
    'meegoe.com',
    'shlll.net',
    'weitiyuba.com',
    'intertid.com',
    'azhibo.com',
    'kongfz.com',
    'cnki.net',
    '99danji.com',
    'eeyy.com',
    'wzzp.com',
    'jiankang4.com',
    'jsyks.com',
    'huochepiao.net',
    'yahoo001.com',
    'laobaixing5.com',
    'xue63.com',
    '51taoyang.com',
    'wenshubang.com',
    '17maoyi.com',
    'chinafloor.cn',
    'edutt.com',
    'cnqipin.com',
    'wanyx.com',
    'tingclass.net',
    'znds.com',
    '189.cn',
    'ok-meeting.com',
    'rkang.cn',
    'coovee.com',
    'ssfcw.com',
    '528500.com.cn',
    'cr173.com',
    'hjenglish.com',
    'yanbm.com',
    'ithome.com',
    'autotimes.com.cn',
    'chuangye.com',
    'b2b168.org',
    'sqkb.com',
    'qqai.net',
    'meituan.com',
    '800hr.com',
    '91ddcc.com',
    'jianbihua.org',
    'aigei.com',
    '52yxz.net',
    'tuanxue.com',
    'peixunsj.cn',
    'chinacrane.net',
    'kankan.com',
    'zj12580.cn',
    '3dkezhan.com',
    'qqhyw.com',
    'shuzhai.org',
    'yubaibai.com.cn',
    'b2360.com',
    'kanzhun.com',
    'dawendou.com',
    'wytao.net',
    'hao123.com',
    '51zhantai.com',
    'kuaihou.com',
    'esy.org',
    'xwlxw.com',
    'zhuangxuan.cn',
    'dyrs.com.cn',
    '.6.cn',
    '07073.com',
    '5ys.org',
    'wannar.com',
    'cssqt.com',
    '52z.com',
    'ccle5.com',
    'aoshu.com',
    'maihui.com',
    'newyx.net',
    '.f.cx',
    '91jmw.com',
    '.dsb.cn',
    'fqxs.cn',
    'duboju.net',
    'xuesai.cn',
    'ddztb.com',
    'canyin375.com',
    'shangceng.com.cn',
    '3454.com',
    'baikezh.com',
    'qulishi.com',
    'wangshugu.com',
    'shsgw.com',
    'tiebaobei.com',
    '315hyw.com',
    '.959.cn',
    'zhjtjyw.com',
    'qc99.com',
    '.s.cn',
    'tvzhibo.com',
    'phb123.com',
    '2liang.net',
    '51testing.com',
    '12chai.com',
    '33cy.cn',
    'cps.com.cn',
    'belltrip.cn',
    '99goad.com',
    'bangboer.net',
    'taofour.com',
    '5999.tv',
    'sczw.com',
    'tq321.com',
    'gzbfjr.com',
    'zzydb.com',
    'zgjcks.com',
    'tuiwen.net',
    'shifanedu.com',
    'oppein.cn',
    'eccang.com',
    '05935.com',
    'jianjuke.cn',
    'findic.com',
    '.714.com',
    'rong360.com',
    '360fdc.com',
    'xstt5.com',
    '7192.com',
    'szmyes.com',
    'pcauto.com.cn',
    'zw3e.com',
    '.79.cn',
    'haoz.net',
    'educity.cn',
    'romzhijia.net',
    'youxiniao.com',
    'zidiantong.com',
    'wangsu123.cn',
    '1988.tv',
    'gongjiao.com',
    'hygx.org',
    'viptijian.com',
    'zscoop.cn',
    '588ku.com',
    'youxiid.cn',
    'zhubian.com',
    'fotomen.cn',
    'trustexporter.com',
    '3000ip.com',
    'idejian.com',
    'taobao.com',
    '5goto.com',
    'iein.cn',
    'iamxk.com',
    '1sfp.com',
    'senrx.com',
    'edu5a.com',
    'qdd99.com',
    'lieju.com',
    'qqyy.com',
    'tfsb.cn',
    'kids21.cn',
    'meimeidu.com',
    'warzn.com',
    'nongjx.com',
    'tongbu.com',
    'tianshijie.com.cn',
    'wustudy.com',
    'jszwfw.gov.cn',
    '.110.com',
    '17dm.com',
    'fishcn.com',
    '0752qc.com',
    '58cyjm.com',
    'zuocai.tv',
    'sjq315.com',
    '9yread.com',
    '9512.net',
    'eduour.com',
    'chinazhaokao.com',
    'shuhuacun.net',
    'smm.cn',
    'zgby114.com',
    '12123.com',
    'feiluxiaoshuo.vip',
    'jjyy.cn',
    'qches.com',
    '911cha.com',
    'aijiuku.com',
    'httpcn.com',
    'h4.com.cn',
    'jc258.cn',
    'ujiuye.com',
    '7cxk.net',
    'tiqiuren.com',
    'mscto.com',
    '360humi.com',
    '55.la',
    'zhaoshayou.com',
    'ci123.com',
    'shijiebang.com',
    'fbook.net',
    'pchome.net',
    'zyue.com',
    'baobao88.com',
    '114la.com',
    '3199.cn',
    '18touch.com',
    'zhongtianwen.cn',
    'manben.com',
    'feicui168.com',
    'wbiao.com.cn',
    'tobosu.com',
    'watchtimes.com.cn',
    'xmuchong.com',
    'chinamenwang.com',
    'chunyun.cn',
    'zcwz.com',
    'hongxiu.com',
    'zhxjyw.com',
    'coolsc.net',
    'tzcy37.com',
    'jiuzheng.com',
    'chaoxing.com',
    'chinayigui.com',
    '9928.tv',
    'wuzhenba.com',
    'eeyy.cc',
    'jinbiaochi.com',
    'shejiben.com',
    '5i5j.com',
    'shhuamei.cn',
    'czvv.com',
    '55hike.com',
    'woyaosouti.com',
    'wenjing.com',
    '66ysy.com',
    'ruanjiandi.com',
    'enorth.com.cn',
    'hkinsu.com',
    'maijx.com',
    'xialingying.cc',
    'kmguol.com',
    'huishangbao.com',
    '51sole.com',
    'xghylt.com',
    'hxen.com',
    '0916e.cn',
    'qxw18.com',
    'soufun.com',
    'gongye360.com',
    'feiluxiaoshuo.cn',
    'dgccs.com',
    '106800.com',
    'sanyue.com',
    '9ku.com',
    '1637.com',
    'damuzzz.com',
    'jufair.com',
    '5118.com',
    'ng114.net',
    'yesmywine.com',
    'jutuw.com',
    'baicai.com',
    'byts.com',
    'ydl.com',
    'sonhoo.com',
    'ntfybj.com',
    'mtdzj.com',
    'duanmeiwen.com',
    '61time.com',
    'lc1001.com',
    'en8848.com.cn',
    'ixiumei.com',
    '16888.com',
    'zjbiz.net',
    'jgsdaily.com',
    'shixi8.com',
    '360wbl.com',
    'caakee.com',
    '366x24.com',
    'kktijian.com',
    'zlfind.com',
    'youxidudu.com',
    'hqew.com',
    'cnbaowen.net',
    'piaoliang.com',
    'ibabyzone.cn',
    '1mag.cn',
    'yh31.com',
    'modelschool.cn',
    'xuanshu.com',
    'dpreview.com',
    'sixflower.com',
    'lubiao.com',
    'baoshuwang.net',
    'lishichunqiu.com',
    'bjjhcczgs.com',
    '.xian.com',
    '9669.cn',
    'taoguba.com.cn',
    '8jm.cn',
    'pp918.com',
    'tuozhan110.com',
    'yi7.com',
    'wishdown.com',
    'meishujia.cn',
    'jinrongren.net',
    'onlinedown.net',
    'rc999.com',
    'west.cn',
    'foodbk.com',
    '17xiee.com',
    'zupuk.com',
    'yanyi8.com',
    '.39.net',
    'chinabm.cn',
    'meichubang.com',
    'wzu.com',
    'yc9y.com',
    'xingzuo.com',
    'wikipedia.org',
    'daiwoqu.com',
    'dushu.com',
    '198526.com',
    '71.net',
    'ewsos.com',
    'kaoyan1v1.com',
    '4399j.com',
    'shipuxiu.com',
    'chinaedu.com',
    'xiaohei.com',
    'qth58.cn',
    '818u.com',
    'dushudu.com',
    'evjin.com',
    'zzidc.com',
    'jiehun.com.cn',
    'bthhotels.com',
    'sjwyx.com',
    'jiancai365.cn',
    'yggk.net',
    'kjfcw.com',
    'zgjsks.com',
    'ankang06.org',
    'jzic.com',
    'huke88.com',
    'downhot.com',
    'dqccc.net',
    'eyin.cn',
    'hzmba.com',
    'auak.com',
    'baishigo.com',
    'pptv.com',
    'jiningauto.com',
    'yiihuu.com',
    'xiaomishu.com',
    'jia400.com',
    '7234.cn',
    'anqingrenwang.com',
    'wanshifu.com',
    '0575.com',
    'znuu.com',
    'qixin.com',
    'xiangzaohua.cn',
    'hqpp.com.cn',
    '18183.com',
    '360bzl.com',
    'uhchina.com',
    'yisaiwang.com',
    '212300.com',
    'xp85.com',
    'iotdev.com',
    'kuajingyan.com',
    'xiaomayi.net',
    'gxrc.com',
    'cjol.com',
    'bkw.cn',
    '178.com',
    'win007.com',
    'to8to.com',
    '0513.org',
    'sichuanrc.com',
    '0757fc.com',
    'anqiu123.com',
    'spzs.com',
    '521hq.com',
    'qhredcross.org.cn',
    'cila.cn',
    'slit.cn',
    '.234.cn',
    'kekenet.com',
    'mzystea.com',
    'vegnet.com.cn',
    'cooco.net.cn',
    'yuyangushi.com',
    'hr999.org',
    'lipin-bj.cn',
    '91wan.com',
    'xyfcw.com',
    'corgichina.com',
    'iyangcong.com',
    'jiaren.org',
    'chinachugui.com',
    '57023.com',
    '114ic.com',
    'manhuatai.com',
    'url.cn',
    'instrument.com.cn',
    'cidianwang.com',
    '91ud.com',
    '023yts.com',
    'maishangji.cn',
    'tiankongyy.com',
    'cqzql.com',
    'banjiajia.com',
    'xiaopin5.com',
    'dav01.com',
    'gouwumai.com',
    '51banhui.com',
    'yuanzhumuban.cc',
    'v2ex.com',
    'babytree.com',
    'xujiesw.com',
    '733.so',
    'abbs.com.cn',
    'pingguolv.com',
    '111jz.com',
    'neoby.com',
    'jcwgw.net',
    'miyanlife.com',
    'hrol.cn',
    'diyiyou.com',
    'winxuan.com',
    '7k7k.com',
    'zz91.com',
    'oilchem.net',
    'liba.com',
    'idp.cn',
    'haitaohou.com',
    'warting.com',
    '59fayi.com',
    '51daifu.com',
    '91peixun.cn',
    'cctop.cn',
    'jzrb.com',
    '500.com',
    'dszuqiu.com',
    'ctsscs.com',
    'chujie.co',
    'qichepinpai.com',
    'eb80.com',
    'zol.com.cn',
    'book.qq.com',
    'chuangshi.qq.com',
    '62639999.com',
    'wtt.hainan.gov.cn',
    'beijing.chinatax.gov.cn',
    '2sc.sohu.com',
    'auto.sohu.com',
    'edu.dzwww.com',
    'peixun.dzwww.com',
    'yunqi.qq.com',
    'ajj.hainan.gov.cn',
    'tv.sohu.com',
    'v.qq.com',
    'ac.qq.com',
    'nm.cma.gov.cn',
    'sh.cma.gov.cn',
    'bbs.icnkr.com',
    'www.yc.ifeng.com',
    'chuangshi.qq.com',
    'all.wasu.cn',
    'www.264006.com',
    'www.licai.club.sohu.com',
    '户型',
    '口碑',
    '底价',
    '停产',
    '低價'
    '低价',
    '销售',
    '电话',
    '对比',
    '對比',
    '兼职',
    '天内',
    '年以',
    '应届',
    '月薪',
    '五险',
    '养老',
    '失业',
    '工伤',
    '生育',
    '职位',
    '商家',
    '阅读全文',
    '评分',
    'seller',
    'dealer',
    '第.*章',
    '上.*页',
    '下.*页',
    '\.\.\.',
    '外观',
    '4S店',
    '特许店',
    '报价',
    '降价',
    '超清VR',
    '新车',
    '玩车',
    '操控',
    '停售',
    '降幅',
    '配置',
    '中控台',
    '座椅',
    '经销商',
    '油耗',
    '两厢',
    '三厢',
    '旅行版',
    '车款',
    '纯电动',
    '汽油',
    '柴油',
    '油电混合',
    '四驱',
    '德系',
    '日系',
    '韩系',
    '美系',
    '前驱',
    '后驱',
    '欧系',
    '手动',
    '自动',
    '手自一体',
    '保养',
    '改装',
    'SUV',
    '轿车',
    'MPV',
    '跑车',
    '面包车',
    '中型',
    '豪华型',
    '小型',
    '紧凑型',
    '微型',
    '中大型',
    '配置',
    '试车',
    '舒适性',
    '大灯',
    '驾驶',
    '车型',
    '客车',
    '卖车',
    '上牌',
    '维修',
    '过户',
    '违章',
    '驾照',
    '年检',
    '美容',
    '交规',
    '销量',
    '降幅',
    '阅读全文',
    '编辑',
    '发货',
    '看房',
    '新车',
    '二手房',
    '新房',
    '找房',
    '下载',
    '房产',
    '地产',
    '装修',
    '房企',
    '房源',
    '看房',
    '买房',
    '家居',
    '一房',
    '两房',
    '三房',
    '四房',
    '五房',
    '租房',
    '中介',
    '怎么样',
    '第.*季',
    '姐姐',
    '萝莉',
    '伴游',
    'QQ',
    '手游',
    '医院',
    '好不好',
    '好吗',
    '症状',
    '停产',
    '底价',
    '低价',
    '销售',
    '銷售',
    '參數',
    '低價',
    '圖片',
    '推广',
    '底價',
    '图库',
    '停產',
    '退出',
    '通用型',
    '门店',
    '轮胎',
    '大图',
    '查看详细',
    '查看详情',
    '回复',
    '会员',
    '离合',
    '月份',
    '阅读全文',
    '复制',
    '评分',
    'baojia',
    'jiangjia',
    '在线投稿',
    '通知公告',
    '网站地图',
    '政策法规',
    '友情链接',
    '办事指南',
    '地图',
    '游戏',
    '电影',
    '天气',
    '景点',
    '便民',
    '阅读',
    '末页',
    '酒店',
    '老人',
    '百科',
    '出租',
    '商铺',
    '女人',
    '交友',
    '公交',
    '二手',
    '户外',
    '公寓',
    '别墅',
    '幼儿',
    '住宅',
    '不限',
    '特产',
    '分类',
    '写字楼',
    '高层',
    '复制',
    '区划',
    '加盟',
    '人气',
    '配资',
    '车站',
    '超高层',
    '半年内',
    '塔楼',
    '板楼',
    '洋房',
    '联排别墅',
    '公建',
    '视频',
    '底商',
    '裙房',
    '车贷',
    '跳至内容',
    '政府信息公开指南',
    '关于我',
    '互动交流',
    '新中国财经网版权声明',
    '实用网址',
    '威廉王子大婚',
    '日本地震',
    '中国经济和信息化年会',
    '南方多省市旱涝急转',
    '长江中下游干旱',
    '胡总书记访美',
    '创新运营模式构筑创',
    '友情协作',
    '宠物',
    '二手车',
    '动漫',
    '母婴',
    'CMS平台推荐',
    '仅博主可见',
    '缓存清除',
    '星座',
    '帮助中心',
    '早教',
    '社会代理机构',
    '国内游',
    '生肖',
    '相册',
    '秦汉三国',
    '两晋隋唐',
    '兵器解析',
    '走街串巷',
    '吃吃喝喝',
    '科学哺育',
    '烹饪冲调',
    '教育培训',
    '办事服务',
    'ReadMore',
    '查看全文',
    '参配',
    '电路',
    '收藏',
    '便民服务',
    '传呼',
    '在线留言',
    '南网站群',
    '内设机构',
    '时装',
    '征集调查',
    '个人资料',
    '免责声明',
    '申请',
    '日志',
    '在线报名',
    '申报',
    '点击查看',
    '分享',
    '继续阅读',
    '加为好友',
    '官方图',
    '发新帖',
    '确定',
    '全文阅读',
    '全文',
    '免费发布信息',
    '时尚',
    'Francais',
    '公费旅游',
    '股本结构',
    '招生简章',
    '我的收藏',
    '在线申请',
    '空气',
    '预警',
    '旅行社',
    '实景',
    '版权声明',
    '国产',
    '进口',
    '关闭',
    '在线登记',
    'Español',
    'Archiver',
    '网上调查',
    '条项目信息',
    '篇机构新闻',
    '回到顶部',
    'go.php?',
    '下一话',
    '上一话',
    '第.*集',
    '培训',
    '辅导',
    '保过班',
    '包过班',
    '通过班',
    '周末班',
    '补习班',
    '冲刺班',
    '网校',
    '在线学习',
    '托产班',
    '哪.*好',
    '报名',
    '教程',
    '测试',
    '咨询公司',
    '留学',
    '观察日记',
    '范文',
    '.+万',
    '.+内',
    '连载',
    '发送私信',
    '保存',
    '快捷方式',
    '粉丝',
    '第.+卷',
    '作品',
    '下.+篇',
    '上.+篇',
]
