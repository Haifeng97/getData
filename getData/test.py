# coding=gbk
from bs4 import BeautifulSoup
import re

text = """

<!DOCTYPE html>
<html>
<head>
<meta charset="GBK" />
	<title>【最热门手机大全】最热门手机报价及图片大全-ZOL中关村在线</title>
	<meta name="keywords" content="最热门手机,最热门手机报价,最热门手机价格,手机大全,手机最新报价" />
	<meta name="description" content="ZOL中关村在线提供最热门手机最新价格及经销商报价,包括最热门手机大全,最热门手机参数,最热门手机评测,最热门手机图片,最热门手机论坛等详细内容,为您购买最热门手机提供全面参考" />
<meta http-equiv="Cache-Control" content="no-siteapp"/>
	<meta http-equiv="Cache-Control" content="no-transform"/>
	<meta name="applicable-device" content="pc">
	<meta http-equiv="mobile-agent" content="format=xhtml; url=https://wap.zol.com.cn/list/57.html?j=simple"/>
<meta http-equiv="mobile-agent" content="format=html5; url=https://wap.zol.com.cn/list/57.html"/>
<meta name="mobile-agent" content="format=wml;url=https://wap.zol.com.cn/list/57.html"/>
<meta name="mobile-agent" content="format=xhtml;url=https://wap.zol.com.cn/list/57.html"/>
<link rel="alternate" media="only screen and(max-width:640px)" href="https://wap.zol.com.cn/list/57.html"/>
<script>(function(){var a=1,d="https://wap.zol.com.cn/list/57.html",b=document.cookie,c=document.referrer;b&&b.match(/mobile_agent_global_dapter=([^;$]+)/)&&(a=b.match(/mobile_agent_global_dapter=([^;$]+)/)[1]);if(1===a&&""!==d&&(/AppleWebKit.*Mobile/i.test(navigator.userAgent)||/MIDP|SymbianOS|NOKIA|SAMSUNG|LG|NEC|TCL|Alcatel|BIRD|DBTEL|Dopod|PHILIPS|HAIER|LENOVO|MOT-|Nokia|SonyEricsson|SIE-|Amoi|ZTE/.test(navigator.userAgent))&&0>window.location.href.indexOf("?via=")){a=new Date;c=""===c?"none":-1<c.indexOf("?")?c+"&pcjump=1":c+"?pcjump=1";b&&(a.setDate(a.getDate()+1),document.cookie="PC2MRealRef="+escape(c)+";expires="+a.toGMTString()+
"; domain=.zol.com.cn; path=/");try{/Android|Windows Phone|webOS|iPhone|iPod|BlackBerry/i.test(navigator.userAgent)&&(window.location.href=d)}catch(e){}}})();</script>
<script type="text/javascript" src="//icon.zol-img.com.cn/swfobject.js"></script><script type="text/javascript" src="//p.zol-img.com.cn/detail_ad/list.js"></script><script type="text/javascript" src="//p.zol-img.com.cn/detail_ad/list_57.js"></script><script type="text/javascript">
<!--
    var pageType    = 'List';
    var subPageType = 'List';
    var subcateId   = '57';
    var subEnName   = 'cell_phone';
    var manuId      = '0';
    var enManu      = '';
    var priceId     = 'noPrice';
    var paramVal    = '0';
    var locationId  = '0';
    var enLocation  = '';
    var enProvince  = '';
    var cusPriUrl   = '/cell_phone_index/subcate57_list_{price}_1.html';
    var cusKwUrl    = '/cell_phone_index/subcate57_0_list_1_k{keyword}_1_2_0_1.html';
    var cusPromotionUrl='/cell_phone_index/subcate57_list_a{promotion}_1.html';
    var manuPlural  = '0';
    var scroll      = '1';
    var promotionSel='';
    var isDefault   = '0';
            //-->
</script>
<script src="//s.zol-img.com.cn/d/Pro/Pro_listArea.js?v=39918"></script>
<link href="//s.zol-img.com.cn/d/Pro/Pro_list1280_v3.css?v=39918" rel="stylesheet"    />
<script src="//icon.zol-img.com.cn/growingio/vds.js"></script>
<link rel="canonical" href="http://detail.zol.com.cn/cell_phone_index/subcate57_list_1.html"/>
<base target="_self"/>
</head>

<body class="list-for-mobile-phone">

<div class="global-sitenav">
	<div class="sitenav-inner">
		<div id="J_NavLoginBar">
			<!--sitenav-login-bar-->
			<div class="sitenav-login-bar">
				<div class="sitenav-login-links"> 
					<a href="http://service.zol.com.cn/user/api/weixin/jump.php?from=220" target="_self" class="sitenav-weixin" title="使用微信登录"></a>
					<a href="http://service.zol.com.cn/user/api/qq/libs/oauth/redirect_to_login.php?from=220" target="_blank" class="sitenav-qq" title="使用腾讯QQ登录"></a>
					<a href="http://service.zol.com.cn/user/api/sina/jump.php?from=220" target="_blank" class="sitenav-weibo" title="使用新浪微博登录"></a>
				</div>
				<div id="J_NavLogin" class="sitenav-login-box">
					<a id="J_NavLoginLink" href="https://service.zol.com.cn/user/login.php" target="_self" class="sitenav-login-link">登录</a>
					<div class="sitenav-login-form">
						<iframe id="ZOL_SMALL_LOGIN" src="" width="190" height="204" frameborder="0" scrolling="no" style="vertical-align:middle"></iframe>
					</div>
				</div>
			</div>
			<!--//sitenav-login-bar-->
		</div>

		<!--sitenav-links-->
		<div class="sitenav-links">
			<a href="http://www.zol.com.cn" class="zol-link" target="_blank">中关村在线</a>

			<!--sitenav-personal-center-->
			<div id="J_NavGroupSite" class="sitenav-groupsite"> 
				<span class="sitenav-trigger">网站导航<i></i></span>
				<div class="groupsite-sitemap-body"> 
					<ul class="sitemap-items">
						<li>
							<span class="sitemap-sub-title">网站功能</span>
                            							<a href="http://detail.zol.com.cn" target="_blank">查报价</a>
                            							<a href="http://top.zol.com.cn/" target="_blank">排行榜</a>
                            							<a href="http://www.zol.com/" target="_blank">商城</a>
                            							<a href="http://tuan.zol.com/" target="_blank">团购</a>
                            							<a href="http://dealer.zol.com.cn/" target="_blank">经销商</a>
                            							<a href="http://b.zol.com.cn/qy/" target="_blank">商家库</a>
                            							<a href="http://2.zol.com.cn/" target="_blank">二手市场</a>
                            							<a href="http://news.zol.com.cn/" target="_blank">新闻</a>
                            							<a href="http://zdc.zol.com.cn/" target="_blank">调研</a>
                            							<a href="http://price.zol.com.cn/" target="_blank">行情</a>
                            							<a href="http://zj.zol.com.cn/" target="_blank">模拟攒机</a>
                            							<a href="http://bbs.zol.com.cn/" target="_blank">论坛</a>
                            							<a href="http://ask.zol.com.cn/" target="_blank">问答</a>
                            							<a href="http://xiazai.zol.com.cn/" target="_blank">软件下载</a>
                            						</li>
						<li>
							<a href="http://www.zol.com.cn/webcenter/map.html" class="more" target="_blank">更多<b>&gt;&gt;</b></a>
							<span class="sitemap-sub-title">产品频道</span>
                            							<a href="http://detail.zol.com.cn/koubei/" target="_blank">口碑榜</a>
                            							<a href="http://detail.zol.com.cn/product_new/" target="_blank">每日新品</a>
                            							<a href="http://detail.zol.com.cn/play/mobile/" target="_blank">玩转手机</a>
                            							<a href="http://v.zol.com.cn/" target="_blank">视频频道</a>
                            							<a href="http://detail.zol.com.cn/tujie/" target="_blank">评测图解</a>
                            							<a href="http://repair.zol.com.cn/" target="_blank">维修库</a>
                            							<a class="icon-new" href="http://detail.zol.com.cn/solution/" target="_blank">解决方案库<i></i></a>
                            							<a href="http://try.zol.com.cn/" target="_blank">试用中心</a>
                            							<a href="http://tupian.zol.com.cn/" target="_blank">图赏</a>
                            						</li>
					</ul>
				</div>
			</div>
			<!--sitenav-personal-center-->

			<div class="product-librarylinks"> 
				<a href="http://top.zol.com.cn" target="_blank">产品排行</a>
				<a class="icon-hot" href="http://e.zol.com.cn/?s=banner" target="_blank">产品入库<i></i></a>
				<a href="http://dealer.zol.com.cn/register_explain.php" target="_blank">广告联盟</a>
				<a href="http://www.zol.com.cn/help/index.html" target="_blank">手机客户端</a>
			</div> 

		</div>
		<!--sitenav-links-->
	</div>
</div>
<table class="header-ads">
	<tr>
		<td class="header-ads-tip">中关村在线推广</td>
		<td>
							<div class="adSpace" id="list_list_top_tonglan"   style="display:none;"><script>write_group_ad('list_list_top_tonglan','4diqu_s_57_m_0_{LOCATIONID}.inc#4diqu_s_57_m_0_{PROVINCEID}.inc#5diqu_s_57_m_0_{LOCATIONID}.inc#2price_search_tonglan_s_57_m_0.inc#1price_new_search_tonglan_s_57_m_0.inc#0price_search_tonglan_s_57.inc#4diqu_new_s_57_m_0_{LOCATIONID}.inc#5diqu_new_s_57_m_0_{LOCATIONID}.inc#5price_new_search_tonglan_s_57_m_0.inc#0price_new_search_tonglan_s_57.inc',0,57,0);</script><script>ad_w();</script><script>ad_w();</script><script>ad_w();</script><script>ad_w();</script><script>ad_w();</script><script>ad_w();</script><script>ad_w();</script><script>ad_w();</script><script>ad_w();</script><script>ad_w();</script></div>						<div class="adSpace" id="list_list_top_tonglan_2"   style="display:none;"><script>write_group_ad('list_list_top_tonglan_2','5price_search_tonglan_s_57_m_0.inc',0,57,0);</script><script>ad_w();</script></div>			<div class="adSpace" id="list_list_top_tonglan_3"   style="display:none;"><script>write_group_ad('list_list_top_tonglan_3','5list_header_top_s_57_m_0.inc',0,57,0);</script><script>ad_w();</script></div>		</td>
	</tr>
</table>

<div class="header">
	<a href="/" class="logo">ZOL产品报价</a>
		<div class="qrcode-box" id="J_QrcodeNew">
		<span></span>
		<div class="qrcode-new"><img src="https://icon.zol-img.com.cn/products/v3/detail-appdl-qrcode.png" width="70" height="70">下载客户端</div>
	</div>
		<div class="search-box">
	    <form id="searchForm" action="http://detail.zol.com.cn/index.php" method="get">
            <input type="hidden" value="SearchList" name="c" />
	        <div class="search-keyword">
	            <input id="keyword" name="kword" type="text" class="keyword" maxlength="120" autocomplete="off" x-webkit-speech="" x-webkit-grammar="builtin:translate" lang="zh-CN" hidefocus="true" value="vivo X23"  growing-track='true'/>
	        </div>
	        <input id="subSerch" type="button" class="search-button" hidefocus="true" value="搜 索"  />
	    </form>
	    <div id="suggest" class="search-suggest"></div>
        		<div class="search-hot-words">
                                    <a target="_blank" href="/cell_phone/index384973.shtml">苹果7</a>
                                    <a target="_blank" href="/cell_phone/index1215069.shtml">红米6</a>
                                    <a target="_blank" href="/cell_phone/index1215577.shtml">vivonex</a>
                                    <a target="_blank" href="/cell_phone/index394162.shtml">苹果8</a>
                                    <a target="_blank" href="/cell_phone/index1229519.shtml">苹果xs</a>
                                    <a target="_blank" href="/cell_phone/index1209455.shtml">红米note5</a>
                                    		</div>
        	</div>
	</div>
<div id="navigation"></div>

<div class="wrapper">




<div class="breadcrumb-filter-selected">
	<div class="breadcrumb"><a href="/">ZOL报价首页</a> &gt; <span>手机</span> </div>		<div class="filter-selected">
		<strong class="filter-type">已选条件：</strong>
		<div id="J_FilterSelectedEmpty" data-full="1" data-bread="1" class="param-selected clearfix"></div>
	</div>
	</div>


<div class="list-title">
	<div id="J_CityArea" class="list-title-inner clearfix">
		<h3>手机筛选</h3>
		<div class="city-change-box">
						<span id="J_CityChange" data-location="0" class="city-change-triggle">选择城市<i></i></span>
			<div id="J_CityList"></div>
		</div>

		<div class="adSpace" id="list_list_search_right_font"   style="display:none;"><script>write_group_ad('list_list_search_right_font','4diqu_postion_right_font_ad_s_57_m_0_{LOCATIONID}.inc#1price_search_simp_search_text_s_57_m_0.inc#5price_search_simp_search_text_s_57_m_0.inc',0,57,0);</script><script>ad_w();</script><script>ad_w();</script><script>ad_w();</script></div>
					</div>
</div>

<div id="J_ParamFilter" class="param-filter">
                        <div id="J_ManuFilter" class="filter-brand">
                <strong class="filter-type">品牌：</strong>
                <div id="J_ParamBrand" class="brand-hot brand-list">
                    <span class="all active">不限</span>                    <a href="/cell_phone_index/subcate57_1673_list_1.html">OPPO</a><a href="/cell_phone_index/subcate57_1795_list_1.html">vivo</a><a href="/cell_phone_index/subcate57_613_list_1.html">华为</a><a href="/cell_phone_index/subcate57_98_list_1.html">三星</a><a href="/cell_phone_index/subcate57_50840_list_1.html">荣耀</a><a href="/cell_phone_index/subcate57_35579_list_1.html">一加</a><a href="/cell_phone_index/subcate57_544_list_1.html">苹果</a><a href="/cell_phone_index/subcate57_1632_list_1.html">金立</a><a href="/cell_phone_index/subcate57_1763_list_1.html">联想</a><a href="/cell_phone_index/subcate57_1434_list_1.html">魅族</a><a href="/cell_phone_index/subcate57_642_list_1.html">中兴</a><a href="/cell_phone_index/subcate57_295_list_1.html">Moto</a><a href="/cell_phone_index/subcate57_35005_list_1.html">努比亚</a><a href="/cell_phone_index/subcate57_35849_list_1.html">锤子科技</a><a href="/cell_phone_index/subcate57_35350_list_1.html">360</a><a href="/cell_phone_index/subcate57_52602_list_1.html">国美手机</a><a href="/cell_phone_index/subcate57_34645_list_1.html">小米</a><a href="/cell_phone_index/subcate57_300_list_1.html">夏普</a><a href="/cell_phone_index/subcate57_227_list_1.html">华硕</a><a href="/cell_phone_index/subcate57_35179_list_1.html">美图</a><a href="/cell_phone_index/subcate57_297_list_1.html">诺基亚</a><a href="/cell_phone_index/subcate57_33080_list_1.html">HTC</a><a href="/cell_phone_index/subcate57_49202_list_1.html">8848</a><a href="/cell_phone_index/subcate57_35224_list_1.html">SUGAR</a><a href="/cell_phone_index/subcate57_12772_list_1.html">黑莓</a><a href="/cell_phone_index/subcate57_19_list_1.html">海信</a><a href="/cell_phone_index/subcate57_34660_list_1.html">AGM</a><a href="/cell_phone_index/subcate57_1069_list_1.html">索尼移动</a><a href="/cell_phone_index/subcate57_1922_list_1.html">谷歌</a><a href="/cell_phone_index/subcate57_143_list_1.html">LG</a><a href="/cell_phone_index/subcate57_1606_list_1.html">酷派</a><a href="/cell_phone_index/subcate57_33626_list_1.html">中国移动</a><a href="/cell_phone_index/subcate57_159_list_1.html">飞利浦</a><a href="/cell_phone_index/subcate57_37319_list_1.html">联想ZUK</a><a href="/cell_phone_index/subcate57_41412_list_1.html">VERTU</a><a href="/cell_phone_index/subcate57_33855_list_1.html">朵唯</a><a href="/cell_phone_index/subcate57_34023_list_1.html">酷比</a><a href="/cell_phone_index/subcate57_599_list_1.html">康佳</a><a href="/cell_phone_index/subcate57_1081_list_1.html">纽曼</a><a href="/cell_phone_index/subcate57_32729_list_1.html">天语</a><a href="/cell_phone_index/subcate57_1590_list_1.html">雷蛇</a><a href="/cell_phone_index/subcate57_1589_list_1.html">长虹</a><a href="/cell_phone_index/subcate57_35320_list_1.html">小辣椒</a><a href="/cell_phone_index/subcate57_171_list_1.html">TCL</a><a href="/cell_phone_index/subcate57_364_list_1.html">微软</a><a href="/cell_phone_index/subcate57_36511_list_1.html">YotaPhone</a><a href="/cell_phone_index/subcate57_750_list_1.html">格力</a><a href="/cell_phone_index/subcate57_35335_list_1.html">汇威</a><a href="/cell_phone_index/subcate57_221_list_1.html">海尔</a><a href="/cell_phone_index/subcate57_34492_list_1.html">乐目</a><a href="/cell_phone_index/subcate57_35121_list_1.html">MANN</a><a href="/cell_phone_index/subcate57_223_list_1.html">惠普</a><a href="/cell_phone_index/subcate57_34906_list_1.html">邦华</a><a href="/cell_phone_index/subcate57_35004_list_1.html">COMIO</a><a href="/cell_phone_index/subcate57_53522_list_1.html">BDV</a><a href="/cell_phone_index/subcate57_33668_list_1.html">sonim</a><a href="/cell_phone_index/subcate57_51710_list_1.html">imoo</a><a href="/cell_phone_index/subcate57_36761_list_1.html">大神</a><a href="/cell_phone_index/subcate57_34686_list_1.html">VEB</a><a href="/cell_phone_index/subcate57_52880_list_1.html">云创通</a><a href="/cell_phone_index/subcate57_342_list_1.html">先锋</a><a href="/cell_phone_index/subcate57_1050_list_1.html">蓝魔</a><a href="/cell_phone_index/subcate57_35615_list_1.html">神舟</a><a href="/cell_phone_index/subcate57_139_list_1.html">柯达</a><a href="/cell_phone_index/subcate57_34741_list_1.html">innos</a><a href="/cell_phone_index/subcate57_53640_list_1.html">ioutdoor</a><a href="/cell_phone_index/subcate57_174_list_1.html">TP-LINK</a><a href="/cell_phone_index/subcate57_84_list_1.html">松下</a><a href="/cell_phone_index/subcate57_36409_list_1.html">富可视</a><a href="/cell_phone_index/subcate57_36538_list_1.html">manta</a><a href="/cell_phone_index/subcate57_36791_list_1.html">PPTV</a><a href="/cell_phone_index/subcate57_36792_list_1.html">索野</a><a href="/cell_phone_index/subcate57_50829_list_1.html">VAIO</a><a href="/cell_phone_index/subcate57_53765_list_1.html">黑鲨</a><a href="/cell_phone_index/subcate57_37427_list_1.html">ivvi</a><a href="/cell_phone_index/subcate57_54243_list_1.html">私人医生</a><a href="/cell_phone_index/subcate57_49531_list_1.html">保千里</a><a href="/cell_phone_index/subcate57_37433_list_1.html">新石器</a><a href="/cell_phone_index/subcate57_34857_list_1.html">青橙</a><a href="/cell_phone_index/subcate57_35228_list_1.html">21克</a><a href="/cell_phone_index/subcate57_34547_list_1.html">云狐</a><a href="/cell_phone_index/subcate57_53006_list_1.html">红鸟</a><a href="/cell_phone_index/subcate57_531_list_1.html">阿尔卡特</a><a href="/cell_phone_index/subcate57_52034_list_1.html">独影天幕</a><a href="/cell_phone_index/subcate57_53520_list_1.html">克里特</a><a href="/cell_phone_index/subcate57_52848_list_1.html">守护宝</a><a href="/cell_phone_index/subcate57_50842_list_1.html">全普</a><a href="/cell_phone_index/subcate57_41933_list_1.html">百合</a><a href="/cell_phone_index/subcate57_40737_list_1.html">朗界</a><a href="/cell_phone_index/subcate57_37585_list_1.html">华度</a><a href="/cell_phone_index/subcate57_34927_list_1.html">青葱</a><a href="/cell_phone_index/subcate57_41365_list_1.html">易百年</a><a href="/cell_phone_index/subcate57_51281_list_1.html">首云</a><a href="/cell_phone_index/subcate57_36647_list_1.html">卡布奇诺</a><a href="/cell_phone_index/subcate57_51194_list_1.html">彩石</a><a href="/cell_phone_index/subcate57_51808_list_1.html">意龙</a><a href="/cell_phone_index/subcate57_37438_list_1.html">优豊</a><a href="/cell_phone_index/subcate57_53521_list_1.html">铂爵</a><a href="/cell_phone_index/subcate57_32512_list_1.html">大唐电信</a><a href="/cell_phone_index/subcate57_35102_list_1.html">尼凯恩</a><a href="/cell_phone_index/subcate57_51558_list_1.html">小格雷</a><a href="/cell_phone_index/subcate57_41107_list_1.html">传奇</a><a href="/cell_phone_index/subcate57_51978_list_1.html">领虎</a><a href="/cell_phone_index/subcate57_35415_list_1.html">GEMRY</a><a href="/cell_phone_index/subcate57_51107_list_1.html">阔密</a><a href="/cell_phone_index/subcate57_51576_list_1.html">Ant one</a><a href="/cell_phone_index/subcate57_34874_list_1.html">垦鑫达</a><a href="/cell_phone_index/subcate57_37263_list_1.html">美猴王</a><a href="/cell_phone_index/subcate57_49477_list_1.html">青想</a><a href="/cell_phone_index/subcate57_49232_list_1.html">图灵</a><a href="/cell_phone_index/subcate57_35147_list_1.html">小宇宙</a><a href="/cell_phone_index/subcate57_50865_list_1.html">途为</a><a href="/cell_phone_index/subcate57_36594_list_1.html">米蓝</a><a href="/cell_phone_index/subcate57_355_list_1.html">波导</a><a href="/cell_phone_index/subcate57_49354_list_1.html">超多维</a><a href="/cell_phone_index/subcate57_51993_list_1.html">言信</a><a href="/cell_phone_index/subcate57_1528_list_1.html">泛泰</a><a href="/cell_phone_index/subcate57_53979_list_1.html">创星</a><a href="/cell_phone_index/subcate57_43188_list_1.html">BROR</a><a href="/cell_phone_index/subcate57_49221_list_1.html">雅马亚虎</a><a href="/cell_phone_index/subcate57_51417_list_1.html">VANO</a><a href="/cell_phone_index/subcate57_35405_list_1.html">誉品</a><a href="/cell_phone_index/subcate57_33382_list_1.html">欧恩</a>                </div>
                <div class="brand-muti-more">
                                            <a id="J_Multi" class="multi" href="javascript:;" target="_self" data-flag="1" data-manu="0" data-url-type="param">多选</a>
                                        <a class="J_ViewMore view-more" data-multi="0" data-manu="0" data-brand="true" data-target="J_ParamBrand" data-url-type="param" href="javascript:;" target="_self">更多<i></i></a>
                </div>
                <div class="brand-all">
                    <ul id="J_BrandTab" class="brand-all-tab">
                        <li class="active" data-letter-value="all"><span>全部品牌</span><i></i></li>
                                                    <li data-letter-value="0-9"><span>0-9</span><i></i></li>
                                                        <li data-letter-value="65-71"><span>A-G</span><i></i></li>
                                                        <li data-letter-value="72-78"><span>H-N</span><i></i></li>
                                                        <li data-letter-value="79-84"><span>O-T</span><i></i></li>
                                                        <li data-letter-value="85-90"><span>U-Z</span><i></i></li>
                                                </ul>
                    <div id="J_BrandAll" data-multi="0" class="brand-list"><a href="/cell_phone_index/subcate57_1673_list_1.html" data-link="1673" data-letter="O">OPPO</a><a href="/cell_phone_index/subcate57_1795_list_1.html" data-link="1795" data-letter="V">vivo</a><a href="/cell_phone_index/subcate57_613_list_1.html" data-link="613" data-letter="H">华为</a><a href="/cell_phone_index/subcate57_98_list_1.html" data-link="98" data-letter="S">三星</a><a href="/cell_phone_index/subcate57_50840_list_1.html" data-link="50840" data-letter="R">荣耀</a><a href="/cell_phone_index/subcate57_35579_list_1.html" data-link="35579" data-letter="Y">一加</a><a href="/cell_phone_index/subcate57_544_list_1.html" data-link="544" data-letter="P">苹果</a><a href="/cell_phone_index/subcate57_1632_list_1.html" data-link="1632" data-letter="J">金立</a><a href="/cell_phone_index/subcate57_1763_list_1.html" data-link="1763" data-letter="L">联想</a><a href="/cell_phone_index/subcate57_1434_list_1.html" data-link="1434" data-letter="M">魅族</a><a href="/cell_phone_index/subcate57_642_list_1.html" data-link="642" data-letter="Z">中兴</a><a href="/cell_phone_index/subcate57_295_list_1.html" data-link="295" data-letter="M">Moto</a><a href="/cell_phone_index/subcate57_35005_list_1.html" data-link="35005" data-letter="N">努比亚</a><a href="/cell_phone_index/subcate57_35849_list_1.html" data-link="35849" data-letter="C">锤子科技</a><a href="/cell_phone_index/subcate57_35350_list_1.html" data-link="35350" data-letter="3">360</a><a href="/cell_phone_index/subcate57_52602_list_1.html" data-link="52602" data-letter="G">国美手机</a><a href="/cell_phone_index/subcate57_34645_list_1.html" data-link="34645" data-letter="X">小米</a><a href="/cell_phone_index/subcate57_300_list_1.html" data-link="300" data-letter="X">夏普</a><a href="/cell_phone_index/subcate57_227_list_1.html" data-link="227" data-letter="H">华硕</a><a href="/cell_phone_index/subcate57_35179_list_1.html" data-link="35179" data-letter="M">美图</a><a href="/cell_phone_index/subcate57_297_list_1.html" data-link="297" data-letter="N">诺基亚</a><a href="/cell_phone_index/subcate57_33080_list_1.html" data-link="33080" data-letter="H">HTC</a><a href="/cell_phone_index/subcate57_49202_list_1.html" data-link="49202" data-letter="8">8848</a><a href="/cell_phone_index/subcate57_35224_list_1.html" data-link="35224" data-letter="S">SUGAR</a><a href="/cell_phone_index/subcate57_12772_list_1.html" data-link="12772" data-letter="H">黑莓</a><a href="/cell_phone_index/subcate57_19_list_1.html" data-link="19" data-letter="H">海信</a><a href="/cell_phone_index/subcate57_34660_list_1.html" data-link="34660" data-letter="A">AGM</a><a href="/cell_phone_index/subcate57_1069_list_1.html" data-link="1069" data-letter="S">索尼移动</a><a href="/cell_phone_index/subcate57_1922_list_1.html" data-link="1922" data-letter="G">谷歌</a><a href="/cell_phone_index/subcate57_143_list_1.html" data-link="143" data-letter="L">LG</a><a href="/cell_phone_index/subcate57_1606_list_1.html" data-link="1606" data-letter="K">酷派</a><a href="/cell_phone_index/subcate57_33626_list_1.html" data-link="33626" data-letter="Z">中国移动</a><a href="/cell_phone_index/subcate57_159_list_1.html" data-link="159" data-letter="F">飞利浦</a><a href="/cell_phone_index/subcate57_37319_list_1.html" data-link="37319" data-letter="L">联想ZUK</a><a href="/cell_phone_index/subcate57_41412_list_1.html" data-link="41412" data-letter="V">VERTU</a><a href="/cell_phone_index/subcate57_33855_list_1.html" data-link="33855" data-letter="D">朵唯</a><a href="/cell_phone_index/subcate57_34023_list_1.html" data-link="34023" data-letter="K">酷比</a><a href="/cell_phone_index/subcate57_599_list_1.html" data-link="599" data-letter="K">康佳</a><a href="/cell_phone_index/subcate57_1081_list_1.html" data-link="1081" data-letter="N">纽曼</a><a href="/cell_phone_index/subcate57_32729_list_1.html" data-link="32729" data-letter="T">天语</a><a href="/cell_phone_index/subcate57_1590_list_1.html" data-link="1590" data-letter="L">雷蛇</a><a href="/cell_phone_index/subcate57_1589_list_1.html" data-link="1589" data-letter="C">长虹</a><a href="/cell_phone_index/subcate57_35320_list_1.html" data-link="35320" data-letter="X">小辣椒</a><a href="/cell_phone_index/subcate57_171_list_1.html" data-link="171" data-letter="T">TCL</a><a href="/cell_phone_index/subcate57_364_list_1.html" data-link="364" data-letter="W">微软</a><a href="/cell_phone_index/subcate57_36511_list_1.html" data-link="36511" data-letter="Y">YotaPhone</a><a href="/cell_phone_index/subcate57_750_list_1.html" data-link="750" data-letter="G">格力</a><a href="/cell_phone_index/subcate57_35335_list_1.html" data-link="35335" data-letter="H">汇威</a><a href="/cell_phone_index/subcate57_221_list_1.html" data-link="221" data-letter="H">海尔</a><a href="/cell_phone_index/subcate57_34492_list_1.html" data-link="34492" data-letter="L">乐目</a><a href="/cell_phone_index/subcate57_35121_list_1.html" data-link="35121" data-letter="M">MANN</a><a href="/cell_phone_index/subcate57_223_list_1.html" data-link="223" data-letter="H">惠普</a><a href="/cell_phone_index/subcate57_34906_list_1.html" data-link="34906" data-letter="B">邦华</a><a href="/cell_phone_index/subcate57_35004_list_1.html" data-link="35004" data-letter="C">COMIO</a><a href="/cell_phone_index/subcate57_53522_list_1.html" data-link="53522" data-letter="B">BDV</a><a href="/cell_phone_index/subcate57_33668_list_1.html" data-link="33668" data-letter="S">sonim</a><a href="/cell_phone_index/subcate57_51710_list_1.html" data-link="51710" data-letter="I">imoo</a><a href="/cell_phone_index/subcate57_36761_list_1.html" data-link="36761" data-letter="D">大神</a><a href="/cell_phone_index/subcate57_34686_list_1.html" data-link="34686" data-letter="V">VEB</a><a href="/cell_phone_index/subcate57_52880_list_1.html" data-link="52880" data-letter="Y">云创通</a><a href="/cell_phone_index/subcate57_342_list_1.html" data-link="342" data-letter="X">先锋</a><a href="/cell_phone_index/subcate57_1050_list_1.html" data-link="1050" data-letter="L">蓝魔</a><a href="/cell_phone_index/subcate57_35615_list_1.html" data-link="35615" data-letter="S">神舟</a><a href="/cell_phone_index/subcate57_139_list_1.html" data-link="139" data-letter="K">柯达</a><a href="/cell_phone_index/subcate57_34741_list_1.html" data-link="34741" data-letter="I">innos</a><a href="/cell_phone_index/subcate57_53640_list_1.html" data-link="53640" data-letter="I">ioutdoor</a><a href="/cell_phone_index/subcate57_174_list_1.html" data-link="174" data-letter="T">TP-LINK</a><a href="/cell_phone_index/subcate57_84_list_1.html" data-link="84" data-letter="S">松下</a><a href="/cell_phone_index/subcate57_36409_list_1.html" data-link="36409" data-letter="F">富可视</a><a href="/cell_phone_index/subcate57_36538_list_1.html" data-link="36538" data-letter="M">manta</a><a href="/cell_phone_index/subcate57_36791_list_1.html" data-link="36791" data-letter="P">PPTV</a><a href="/cell_phone_index/subcate57_36792_list_1.html" data-link="36792" data-letter="S">索野</a><a href="/cell_phone_index/subcate57_50829_list_1.html" data-link="50829" data-letter="V">VAIO</a><a href="/cell_phone_index/subcate57_53765_list_1.html" data-link="53765" data-letter="H">黑鲨</a><a href="/cell_phone_index/subcate57_37427_list_1.html" data-link="37427" data-letter="I">ivvi</a><a href="/cell_phone_index/subcate57_54243_list_1.html" data-link="54243" data-letter="S">私人医生</a><a href="/cell_phone_index/subcate57_49531_list_1.html" data-link="49531" data-letter="B">保千里</a><a href="/cell_phone_index/subcate57_37433_list_1.html" data-link="37433" data-letter="X">新石器</a><a href="/cell_phone_index/subcate57_34857_list_1.html" data-link="34857" data-letter="Q">青橙</a><a href="/cell_phone_index/subcate57_35228_list_1.html" data-link="35228" data-letter="2">21克</a><a href="/cell_phone_index/subcate57_34547_list_1.html" data-link="34547" data-letter="Y">云狐</a><a href="/cell_phone_index/subcate57_53006_list_1.html" data-link="53006" data-letter="H">红鸟</a><a href="/cell_phone_index/subcate57_531_list_1.html" data-link="531" data-letter="A">阿尔卡特</a><a href="/cell_phone_index/subcate57_52034_list_1.html" data-link="52034" data-letter="D">独影天幕</a><a href="/cell_phone_index/subcate57_53520_list_1.html" data-link="53520" data-letter="K">克里特</a><a href="/cell_phone_index/subcate57_52848_list_1.html" data-link="52848" data-letter="S">守护宝</a><a href="/cell_phone_index/subcate57_50842_list_1.html" data-link="50842" data-letter="Q">全普</a><a href="/cell_phone_index/subcate57_41933_list_1.html" data-link="41933" data-letter="B">百合</a><a href="/cell_phone_index/subcate57_40737_list_1.html" data-link="40737" data-letter="L">朗界</a><a href="/cell_phone_index/subcate57_37585_list_1.html" data-link="37585" data-letter="H">华度</a><a href="/cell_phone_index/subcate57_34927_list_1.html" data-link="34927" data-letter="Q">青葱</a><a href="/cell_phone_index/subcate57_41365_list_1.html" data-link="41365" data-letter="Y">易百年</a><a href="/cell_phone_index/subcate57_51281_list_1.html" data-link="51281" data-letter="S">首云</a><a href="/cell_phone_index/subcate57_36647_list_1.html" data-link="36647" data-letter="K">卡布奇诺</a><a href="/cell_phone_index/subcate57_51194_list_1.html" data-link="51194" data-letter="C">彩石</a><a href="/cell_phone_index/subcate57_51808_list_1.html" data-link="51808" data-letter="Y">意龙</a><a href="/cell_phone_index/subcate57_37438_list_1.html" data-link="37438" data-letter="Y">优豊</a><a href="/cell_phone_index/subcate57_53521_list_1.html" data-link="53521" data-letter="B">铂爵</a><a href="/cell_phone_index/subcate57_32512_list_1.html" data-link="32512" data-letter="D">大唐电信</a><a href="/cell_phone_index/subcate57_35102_list_1.html" data-link="35102" data-letter="N">尼凯恩</a><a href="/cell_phone_index/subcate57_51558_list_1.html" data-link="51558" data-letter="X">小格雷</a><a href="/cell_phone_index/subcate57_41107_list_1.html" data-link="41107" data-letter="C">传奇</a><a href="/cell_phone_index/subcate57_51978_list_1.html" data-link="51978" data-letter="L">领虎</a><a href="/cell_phone_index/subcate57_35415_list_1.html" data-link="35415" data-letter="G">GEMRY</a><a href="/cell_phone_index/subcate57_51107_list_1.html" data-link="51107" data-letter="K">阔密</a><a href="/cell_phone_index/subcate57_51576_list_1.html" data-link="51576" data-letter="A">Ant one</a><a href="/cell_phone_index/subcate57_34874_list_1.html" data-link="34874" data-letter="K">垦鑫达</a><a href="/cell_phone_index/subcate57_37263_list_1.html" data-link="37263" data-letter="M">美猴王</a><a href="/cell_phone_index/subcate57_49477_list_1.html" data-link="49477" data-letter="Q">青想</a><a href="/cell_phone_index/subcate57_49232_list_1.html" data-link="49232" data-letter="T">图灵</a><a href="/cell_phone_index/subcate57_35147_list_1.html" data-link="35147" data-letter="X">小宇宙</a><a href="/cell_phone_index/subcate57_50865_list_1.html" data-link="50865" data-letter="T">途为</a><a href="/cell_phone_index/subcate57_36594_list_1.html" data-link="36594" data-letter="M">米蓝</a><a href="/cell_phone_index/subcate57_355_list_1.html" data-link="355" data-letter="B">波导</a><a href="/cell_phone_index/subcate57_49354_list_1.html" data-link="49354" data-letter="C">超多维</a><a href="/cell_phone_index/subcate57_51993_list_1.html" data-link="51993" data-letter="Y">言信</a><a href="/cell_phone_index/subcate57_1528_list_1.html" data-link="1528" data-letter="F">泛泰</a><a href="/cell_phone_index/subcate57_53979_list_1.html" data-link="53979" data-letter="C">创星</a><a href="/cell_phone_index/subcate57_43188_list_1.html" data-link="43188" data-letter="B">BROR</a><a href="/cell_phone_index/subcate57_49221_list_1.html" data-link="49221" data-letter="Y">雅马亚虎</a><a href="/cell_phone_index/subcate57_51417_list_1.html" data-link="51417" data-letter="V">VANO</a><a href="/cell_phone_index/subcate57_35405_list_1.html" data-link="35405" data-letter="Y">誉品</a><a href="/cell_phone_index/subcate57_33382_list_1.html" data-link="33382" data-letter="O">欧恩</a></div>
                    <div class="multi-submit">
                        <a id="J_MultiLink" data-url-type="param" href="/cell_phone_index/subcate57_MANUPLACEHOLDER_list_1.html" class="multi-link" target="_self">确定</a>
                        <span id="J_MultiCansel" data-url-type="param" data-manu="0" class="multi-cansel">取消</span>
                    </div>
                </div>
            </div>
            <script>document.write("");</script>            	
		    <div id="priceItem" class="filter-item filter-price">
		<strong class="filter-type">价格：</strong>
		<div id="J_ParamPrice" class="param-value-list">
									<span class="all active">不限</span>

			            			<a href="/cell_phone_index/subcate57_list_0_1.html">500元以下</a>
            			            			<a href="/cell_phone_index/subcate57_list_500_1.html">500-1000元</a>
            			            			<a href="/cell_phone_index/subcate57_list_1000_1.html">1000-1500元</a>
            			            			<a href="/cell_phone_index/subcate57_list_1500_1.html">1500-2000元</a>
            			            			<a href="/cell_phone_index/subcate57_list_2000_1.html">2000-3000元</a>
            			            			<a href="/cell_phone_index/subcate57_list_3000_1.html">3000-4000元</a>
            			            			<a href="/cell_phone_index/subcate57_list_4000_1.html">4000-5000元</a>
            			            			<a href="/cell_phone_index/subcate57_list_5000_1.html">5000元以上</a>
            					</div>
		<a class="J_ViewMore view-more" data-target="J_ParamPrice" href="javascript:;" target="_self">更多<i></i></a>
		<div class="price-self">
			<input id="minPrice" type="text">
			<em>-</em>
			<input id="maxPrice" type="text">
			<span id="subPri" class="price-button">确定</span>
		</div>
	</div>

		                	<div id="pamItem1" class="filter-item">
        <strong class="filter-type">主屏尺寸：</strong>
        <div id="J_ParamItem1" class="param-value-list">
                        <span class="all active">不限</span>

    			            			<a href="/cell_phone_index/subcate57_list_s5371_1.html">6.0英寸以上</a>

						            			<a href="/cell_phone_index/subcate57_list_s6258_1.html">5.6-6.0英寸</a>

						            			<a href="/cell_phone_index/subcate57_list_s7545_1.html">5.5英寸</a>

						            			<a href="/cell_phone_index/subcate57_list_s5024_1.html">5.1-5.4英寸</a>

						            			<a href="/cell_phone_index/subcate57_list_s5023_1.html">5.0英寸</a>

						            			<a href="/cell_phone_index/subcate57_list_s4218_1.html">4.5-4.9英寸</a>

						            			<a href="/cell_phone_index/subcate57_list_s1586_1.html">4.4英寸以下</a>



			</div>
		<a class="J_ViewMore view-more" data-target="J_ParamItem1" href="javascript:;" target="_self">更多<i></i></a>
    </div>
			                	<div id="pamItem2" class="filter-item">
        <strong class="filter-type">网络：</strong>
        <div id="J_ParamItem2" class="param-value-list">
                        <span class="all active">不限</span>

    			            			<a class="icon-4g" data-tips="手机支持移动、联通、电信三家运营商网络，可以进行通话及上网" href="/cell_phone_index/subcate57_list_s6256_1.html">全网通</a>

						            			<a href="/cell_phone_index/subcate57_list_s5770_1.html">双4G</a>

						            			<a class="icon-4g" data-tips="工信部于2013年12月4日正式发放4G TD-LTE网络牌照，移动/联通/电信分别获得130MHz/40MHz/40MHz频谱资源" href="/cell_phone_index/subcate57_list_s5395_1.html">移动4G</a>

						            			<a href="/cell_phone_index/subcate57_list_s5396_1.html">联通4G</a>

						            			<a href="/cell_phone_index/subcate57_list_s5547_1.html">电信4G</a>

						            			<a class="icon-4g" data-tips="此网络对应的手机可以使用移动2G/3G卡及联通2G卡" href="/cell_phone_index/subcate57_list_s895_1.html">移动3G</a>

						            			<a class="icon-4g" data-tips="只支持此网络的情况下，手机只可以使用电信的2G/3G卡" href="/cell_phone_index/subcate57_list_s1293_1.html">电信3G</a>

						            			<a class="icon-4g" data-tips="此网络对应的手机可以使用联通2G/3G卡及移动2G卡" href="/cell_phone_index/subcate57_list_s140_1.html">联通3G</a>



			</div>
		<a class="J_ViewMore view-more" data-target="J_ParamItem2" href="javascript:;" target="_self">更多<i></i></a>
    </div>
			                	<div id="pamItem3" class="filter-item">
        <strong class="filter-type">核心数：</strong>
        <div id="J_ParamItem3" class="param-value-list">
                        <span class="all active">不限</span>

    			            			<a href="/cell_phone_index/subcate57_list_s6658_1.html">十核</a>

						            			<a href="/cell_phone_index/subcate57_list_s5226_1.html">八核</a>

						            			<a href="/cell_phone_index/subcate57_list_s7347_1.html">六核</a>

						            			<a href="/cell_phone_index/subcate57_list_s3594_1.html">四核</a>

						            			<a href="/cell_phone_index/subcate57_list_s3006_1.html">双核及以下</a>



			</div>
		<a class="J_ViewMore view-more" data-target="J_ParamItem3" href="javascript:;" target="_self">更多<i></i></a>
    </div>
			                	<div id="pamItem4" class="filter-item">
        <strong class="filter-type">RAM容量：</strong>
        <div id="J_ParamItem4" class="param-value-list">
                        <span class="all active">不限</span>

    			            			<a href="/cell_phone_index/subcate57_list_s7318_1.html">8GB</a>

						            			<a href="/cell_phone_index/subcate57_list_s6509_1.html">6GB</a>

						            			<a href="/cell_phone_index/subcate57_list_s6134_1.html">4GB</a>

						            			<a href="/cell_phone_index/subcate57_list_s5293_1.html">3GB</a>

						            			<a href="/cell_phone_index/subcate57_list_s4142_1.html">2GB</a>



			</div>
		<a class="J_ViewMore view-more" data-target="J_ParamItem4" href="javascript:;" target="_self">更多<i></i></a>
    </div>
				<div id="J_MoreFilterItem" class="hide">
                    	<div id="pamItem5" class="filter-item">
        <strong class="filter-type">ROM容量：</strong>
        <div id="J_ParamItem5" class="param-value-list">
                        <span class="all active">不限</span>

    			            			<a href="/cell_phone_index/subcate57_list_s7832_1.html">1TB</a>

						            			<a href="/cell_phone_index/subcate57_list_s7831_1.html">512GB</a>

						            			<a href="/cell_phone_index/subcate57_list_s7075_1.html">256GB</a>

						            			<a href="/cell_phone_index/subcate57_list_s6193_1.html">128GB</a>

						            			<a href="/cell_phone_index/subcate57_list_s4150_1.html">64GB</a>

						            			<a href="/cell_phone_index/subcate57_list_s4149_1.html">32GB</a>

						            			<a href="/cell_phone_index/subcate57_list_s4148_1.html">16GB</a>



			</div>
		<a class="J_ViewMore view-more" data-target="J_ParamItem5" href="javascript:;" target="_self">更多<i></i></a>
    </div>
			                	<div id="pamItem6" class="filter-item">
        <strong class="filter-type">特性：</strong>
        <div id="J_ParamItem6" class="param-value-list">
                        <span class="all active">不限</span>

    			            			<a href="/cell_phone_index/subcate57_list_x10_1.html">全面屏</a>

						            			<a href="/cell_phone_index/subcate57_list_x1_1.html">大屏幕</a>

						            			<a href="/cell_phone_index/subcate57_list_x2_1.html">大容量电池</a>

						            			<a href="/cell_phone_index/subcate57_list_x3_1.html">拍照手机</a>

						            			<a href="/cell_phone_index/subcate57_list_x4_1.html">自拍手机</a>

						            			<a href="/cell_phone_index/subcate57_list_x11_1.html">双卡双待</a>

						            			<a href="/cell_phone_index/subcate57_list_x8_1.html">2K屏</a>

						            			<a href="/cell_phone_index/subcate57_list_x21_1.html">面部识别</a>

						            			<a href="/cell_phone_index/subcate57_list_x12_1.html">指纹识别</a>

						            			<a href="/cell_phone_index/subcate57_list_x22_1.html">双屏手机</a>

						            			<a href="/cell_phone_index/subcate57_list_x19_1.html">游戏手机</a>

						            			<a href="/cell_phone_index/subcate57_list_x18_1.html">三防机</a>

						            			<a href="/cell_phone_index/subcate57_list_x16_1.html">老人机</a>

						            			<a href="/cell_phone_index/subcate57_list_x7_1.html">千元机</a>

						            			<a href="/cell_phone_index/subcate57_list_x13_1.html">国产手机</a>

						            			<a href="/cell_phone_index/subcate57_list_x17_1.html">后置双摄</a>

						            			<a href="/cell_phone_index/subcate57_list_x20_1.html">前置双摄</a>



			</div>
		<a class="J_ViewMore view-more" data-target="J_ParamItem6" href="javascript:;" target="_self">更多<i></i></a>
    </div>
			                	<div id="pamItem7" class="filter-item color-item">
        <strong class="filter-type">外观颜色：</strong>
        <div id="J_ParamItem7" class="param-value-list">
                        <span class="all active">不限</span>

    			<a href="/cell_phone_index/subcate57_list_c13_1.html" class="color" style="border:1px solid #dbdbdb; background-color:#ffffff;"></a>
						            			<a href="/cell_phone_index/subcate57_list_c13_1.html">白色</a>

						<a href="/cell_phone_index/subcate57_list_c14_1.html" class="color" style="border:1px solid #000000; background-color:#000000;"></a>
						            			<a href="/cell_phone_index/subcate57_list_c14_1.html">黑色</a>

						<a href="/cell_phone_index/subcate57_list_c15_1.html" class="color" style="border:1px solid #cccccc; background-color:#cccccc;"></a>
						            			<a href="/cell_phone_index/subcate57_list_c15_1.html">银灰色</a>

						<a href="/cell_phone_index/subcate57_list_c16_1.html" class="color" style="border:1px solid #5a3737; background-color:#5a3737;"></a>
						            			<a href="/cell_phone_index/subcate57_list_c16_1.html">咖啡色</a>

						<a href="/cell_phone_index/subcate57_list_c17_1.html" class="color" style="border:1px solid #ff0903; background-color:#ff0903;"></a>
						            			<a href="/cell_phone_index/subcate57_list_c17_1.html">红色</a>

						<a href="/cell_phone_index/subcate57_list_c18_1.html" class="color" style="border:1px solid #ffcc99; background-color:#ffcc99;"></a>
						            			<a href="/cell_phone_index/subcate57_list_c18_1.html">金色</a>

						<a href="/cell_phone_index/subcate57_list_c20_1.html" class="color" style="border:1px solid #660066; background-color:#660066;"></a>
						            			<a href="/cell_phone_index/subcate57_list_c20_1.html">紫色</a>

						<a href="/cell_phone_index/subcate57_list_c21_1.html" class="color" style="border:1px solid #3333ff; background-color:#3333ff;"></a>
						            			<a href="/cell_phone_index/subcate57_list_c21_1.html">蓝色</a>

						<a href="/cell_phone_index/subcate57_list_c22_1.html" class="color" style="border:1px solid #ffcccc; background-color:#ffcccc;"></a>
						            			<a href="/cell_phone_index/subcate57_list_c22_1.html">粉色</a>

						<a href="/cell_phone_index/subcate57_list_c23_1.html" class="color" style="border:1px solid #ffff00; background-color:#ffff00;"></a>
						            			<a href="/cell_phone_index/subcate57_list_c23_1.html">黄色</a>

						<a href="/cell_phone_index/subcate57_list_c24_1.html" class="color" style="border:1px solid #ff6600; background-color:#ff6600;"></a>
						            			<a href="/cell_phone_index/subcate57_list_c24_1.html">橙色</a>

						<a href="/cell_phone_index/subcate57_list_c25_1.html" class="color" style="border:1px solid #66ff33; background-color:#66ff33;"></a>
						            			<a href="/cell_phone_index/subcate57_list_c25_1.html">绿色</a>



			</div>
		<a class="J_ViewMore view-more" data-target="J_ParamItem7" href="javascript:;" target="_self">更多<i></i></a>
    </div>






















		<div class="filter-other">
		<strong class="filter-type">其他参数：</strong>
		<ul id="J_otherItem" class="other-items">
						<li>
				<strong>手机类型<i></i></strong>
				<div class="param-value-list other-items-list">
																												<span class="all active">不限</span>
																																                                                        <a href="/cell_phone_index/subcate57_list_s528_1.html">4G</a>
                            																															                                                        <a href="/cell_phone_index/subcate57_list_s533_1.html">智能</a>
                            																															                                                        <a href="/cell_phone_index/subcate57_list_s2508_1.html">老人</a>
                            																															                                                        <a href="/cell_phone_index/subcate57_list_s3053_1.html">三防</a>
                            																															                                                        <a href="/cell_phone_index/subcate57_list_s6523_1.html">快充</a>
                            																															                                                        <a href="/cell_phone_index/subcate57_list_s526_1.html">商务</a>
                            																															                                                        <a href="/cell_phone_index/subcate57_list_s2605_1.html">平板</a>
                            																															                                                        <a href="/cell_phone_index/subcate57_list_s531_1.html">音乐</a>
                            																															                                                        <a href="/cell_phone_index/subcate57_list_s7291_1.html">游戏</a>
                            																															                                                        <a href="/cell_phone_index/subcate57_list_s6618_1.html">曲屏</a>
                            																						</div>
			</li>
						<li>
				<strong>主屏分辨率<i></i></strong>
				<div class="param-value-list other-items-list">
																												<span class="all active">不限</span>
																																                                                        <a href="/cell_phone_index/subcate57_list_s6510_1.html">4K</a>
                            																															                                                        <a href="/cell_phone_index/subcate57_list_s5528_1.html">2K</a>
                            																															                                                        <a href="/cell_phone_index/subcate57_list_s4328_1.html">1080p</a>
                            																															                                                        <a href="/cell_phone_index/subcate57_list_s2042_1.html">720p</a>
                            																						</div>
			</li>
						<li>
				<strong>屏幕像素密度<i></i></strong>
				<div class="param-value-list other-items-list">
																												<span class="all active">不限</span>
																																                                                        <a href="/cell_phone_index/subcate57_list_s6192_1.html">500ppi以上</a>
                            																															                                                        <a href="/cell_phone_index/subcate57_list_s4691_1.html">400ppi至500ppi</a>
                            																															                                                        <a href="/cell_phone_index/subcate57_list_s4690_1.html">350ppi至399ppi</a>
                            																															                                                        <a href="/cell_phone_index/subcate57_list_s4689_1.html">300ppi至349ppi</a>
                            																															                                                        <a href="/cell_phone_index/subcate57_list_s4688_1.html">300ppi以下</a>
                            																						</div>
			</li>
						<li>
				<strong>CPU型号<i></i></strong>
				<div class="param-value-list other-items-list">
																												<span class="all active">不限</span>
																																                                                        <a href="/cell_phone_index/subcate57_list_s2615_1.html">高通CPU</a>
                            																															<span class="khl">(</span>                                                        <a href="/cell_phone_index/subcate57_list_s7546_1.html">骁龙845</a>
                            																															                                                        <a href="/cell_phone_index/subcate57_list_s7289_1.html">骁龙835</a>
                            																															                                                        <a href="/cell_phone_index/subcate57_list_s7049_1.html">骁龙821</a>
                            																															                                                        <a href="/cell_phone_index/subcate57_list_s6475_1.html">骁龙820</a>
                            																															                                                        <a href="/cell_phone_index/subcate57_list_s7798_1.html">骁龙710</a>
                            																															                                                        <a href="/cell_phone_index/subcate57_list_s7338_1.html">骁龙660</a>
                            																															                                                        <a href="/cell_phone_index/subcate57_list_s6307_1.html">骁龙653</a>
                            																															                                                        <a href="/cell_phone_index/subcate57_list_s7786_1.html">骁龙636</a>
                            																															                                                        <a href="/cell_phone_index/subcate57_list_s7547_1.html">骁龙630</a>
                            																															                                                        <a href="/cell_phone_index/subcate57_list_s7290_1.html">骁龙625</a>
                            							<span class="khr">)</span>																								                                                        <a href="/cell_phone_index/subcate57_list_s4639_1.html">联发科CPU</a>
                            																															<span class="khl">(</span>                                                        <a href="/cell_phone_index/subcate57_list_s7374_1.html">曦力x30</a>
                            																															                                                        <a href="/cell_phone_index/subcate57_list_s6659_1.html">曦力x25</a>
                            																															                                                        <a href="/cell_phone_index/subcate57_list_s6660_1.html">曦力x20</a>
                            							<span class="khr">)</span>																								                                                        <a href="/cell_phone_index/subcate57_list_s5744_1.html">海思CPU</a>
                            																															<span class="khl">(</span>                                                        <a href="/cell_phone_index/subcate57_list_s7373_1.html">麒麟970</a>
                            																															                                                        <a href="/cell_phone_index/subcate57_list_s6661_1.html">麒麟960</a>
                            																															                                                        <a href="/cell_phone_index/subcate57_list_s7799_1.html">麒麟710</a>
                            							<span class="khr">)</span>																								                                                        <a href="/cell_phone_index/subcate57_list_s3743_1.html">三星CPU</a>
                            																															                                                        <a href="/cell_phone_index/subcate57_list_s3742_1.html">苹果CPU</a>
                            																						</div>
			</li>
						<li>
				<strong>操作系统<i></i></strong>
				<div class="param-value-list other-items-list">
																												<span class="all active">不限</span>
																																                                                        <a href="/cell_phone_index/subcate57_list_s1398_1.html">安卓Android</a>
                            																															<span class="khl">(</span>                                                        <a href="/cell_phone_index/subcate57_list_s7548_1.html">8.0版本</a>
                            																															                                                        <a href="/cell_phone_index/subcate57_list_s7549_1.html">7.1版本</a>
                            																															                                                        <a href="/cell_phone_index/subcate57_list_s7074_1.html">7.0版本</a>
                            																															                                                        <a href="/cell_phone_index/subcate57_list_s6500_1.html">6.0版本</a>
                            																															                                                        <a href="/cell_phone_index/subcate57_list_s6502_1.html">5.1版本</a>
                            							<span class="khr">)</span>																								                                                        <a href="/cell_phone_index/subcate57_list_s3410_1.html">苹果iPhone</a>
                            																															<span class="khl">(</span>                                                        <a href="/cell_phone_index/subcate57_list_s7550_1.html">iOS11</a>
                            																															                                                        <a href="/cell_phone_index/subcate57_list_s7076_1.html">iOS10</a>
                            																															                                                        <a href="/cell_phone_index/subcate57_list_s6501_1.html">iOS9</a>
                            							<span class="khr">)</span>																								                                                        <a href="/cell_phone_index/subcate57_list_s7339_1.html">微软</a>
                            																															<span class="khl">(</span>                                                        <a href="/cell_phone_index/subcate57_list_s7341_1.html">WP10</a>
                            																															                                                        <a href="/cell_phone_index/subcate57_list_s7340_1.html">WP8</a>
                            							<span class="khr">)</span>																								                                                        <a href="/cell_phone_index/subcate57_list_s1278_1.html">其它系统</a>
                            																						</div>
			</li>
						<li>
				<strong>后置摄像头<i></i></strong>
				<div class="param-value-list other-items-list">
																												<span class="all active">不限</span>
																																                                                        <a href="/cell_phone_index/subcate57_list_s6270_1.html">2000万像素以上</a>
                            																															                                                        <a href="/cell_phone_index/subcate57_list_s5536_1.html">1600万像素</a>
                            																															                                                        <a href="/cell_phone_index/subcate57_list_s4340_1.html">1300万像素</a>
                            																															                                                        <a href="/cell_phone_index/subcate57_list_s7572_1.html">1200万像素</a>
                            																															                                                        <a href="/cell_phone_index/subcate57_list_s946_1.html">800万像素</a>
                            																															                                                        <a href="/cell_phone_index/subcate57_list_s450_1.html">700万像素以下</a>
                            																						</div>
			</li>
						<li>
				<strong>前置摄像头<i></i></strong>
				<div class="param-value-list other-items-list">
																												<span class="all active">不限</span>
																																                                                        <a href="/cell_phone_index/subcate57_list_s7348_1.html">2000万像素以上</a>
                            																															                                                        <a href="/cell_phone_index/subcate57_list_s7349_1.html">1600万像素</a>
                            																															                                                        <a href="/cell_phone_index/subcate57_list_s7321_1.html">1300万像素</a>
                            																															                                                        <a href="/cell_phone_index/subcate57_list_s5747_1.html">800万像素</a>
                            																															                                                        <a href="/cell_phone_index/subcate57_list_s5746_1.html">500万像素</a>
                            																															                                                        <a href="/cell_phone_index/subcate57_list_s4327_1.html">400万像素以下</a>
                            																						</div>
			</li>
					</ul>
	</div>
			</div>




</div>

<div class="more-filter">
			<span id="J_MoreFilter" class="more-filter-button" data-on="0">更多选项（ROM容量，特性）等<i></i></span>
		<a class="advanced-search" href="/cell_phone_advSearch/subcate57_1.html" target="_blank">[高级搜索]</a>
	</div>

</div>

<div class="wrapper clearfix">
	<div class="content">


						<div class="adSpace" id="list_list_mid_tonglan"   style="display:none;"><script>write_group_ad('list_list_mid_tonglan','4diqu_pro_middle_s_57_m_0_{LOCATIONID}.inc#1price_search_simp_search_down_s_57_m_0.inc#5price_search_simp_search_down_s_57_m_0.inc#0price_search_simp_search_down_s_57.inc#2detail_list_all_cate.inc',0,57,0);</script><script>ad_w();</script><script>ad_w();</script><script>ad_w();</script><script>ad_w();</script><script>ad_w();</script></div>		<div class="adSpace" id="list_list_prolist_top"   style="display:none;"><script>write_group_ad('list_list_prolist_top','4price_search_list_up_s_57_m_0_{LOCATIONID}.inc#5price_search_list_up_s_57_m_0.inc#3price_search_list_up_s_57_m.inc#0price_search_list_up_s_57.inc',0,57,0);</script><script>ad_w();</script><script>ad_w();</script><script>ad_w();</script><script>ad_w();</script></div>

						<div class="sort-box clearfix">
			<div class="small-page">
								<span class="small-page-prev">&nbsp;</span>
								<span class="small-page-active"><b>1</b>/40</span>
								<a  href="/cell_phone_index/subcate57_0_list_1_0_1_2_0_2.html"  class="small-page-next">&nbsp;</a>
							</div>
			<div class="mode-switch" id="J_ModeSwitch">
								<a class="active" href="/cell_phone_index/subcate57_list_1.html" title="切换到大图" data-mode="2"><i class="pic-mode"></i></a>
								<a href="/cell_phone_index/subcate57_0_list_1_0_1_1_0_1.html" title="切换到列表" data-mode="1"><i class="list-mode"></i></a>
							</div>
						<span class="total">共 <b>1790</b> 款</span>
									<div class="sort">
								<span class="active"><em>热门</em></span>
								<a href="/cell_phone_index/subcate57_0_list_1_0_9_2_0_1.html"   ><em>时间</em><i class="down"></i></a>
								<a href="/cell_phone_index/subcate57_0_list_1_0_3_2_0_1.html"   title="价格由低到高" ><em>价格</em><i class="up"></i></a>
								<a href="/cell_phone_index/subcate57_0_list_1_0_7_2_0_1.html"   title="点评数由高到低" ><em>点评数</em><i class="down"></i></a>
								<a href="/cell_phone_index/subcate57_0_list_1_0_5_2_0_1.html"   title="产品评分由高到低" ><em>产品评分</em><i class="down"></i></a>
								<a href="/cell_phone_index/subcate57_0_list_1_0_8_2_0_1.html"   title="销量由高到低" ><em>销量</em><i class="down"></i></a>
							</div>
            		</div>


				<div class="pic-mode-box">
    <div class="adSpace" id="list_list_prolist_1"   style="display:none;"><script>write_group_ad('list_list_prolist_1','4diqu_list_first_ad_s_57_m_0_{LOCATIONID}.inc#1price_search_list_first_s_57_m_0.inc#5price_search_list_first_s_57_m_0.inc#0price_search_list_first_s_57.inc',0,57,0);</script><script>ad_w();</script><script>ad_w();</script><script>ad_w();</script><script>ad_w();</script></div>    <ul id="J_PicMode" class="clearfix">
                 <li data-follow-id="p1185512" >
                        <a href="/cell_phone/index1185512.shtml" class="pic" target="_blank"><img width="220" height="165" .src="https://2f.zol-img.com.cn/product/191_220x165/739/ceMGSYkHizU6.jpg" alt="华为nova 3（全网通）"></a>
            <h3><a href="/cell_phone/index1185512.shtml" title="华为nova 3（全网通）AI美拍，人脸解锁，指纹识别，四摄像头" target="_blank">华为nova 3（全网通） <span>AI美拍，人脸解锁，指纹识别，四摄像头</span></a></h3>
            <div class="price-row">
                                                <span class="price-tip">参考价：</span><span class="price price-normal"><b class="price-sign">￥</b><b class="price-type">2799</b></span>								<div class="goods-promotion">
										<span class="J_PicModeTuan" data-url="http://www.zol.com/detail/cell_phone/huawei/31496877.html?skuId=13606354?spm=784.0" data-price="2477" data-rel="modeTuan">团购</span>
																								</div>
            </div>

			<div class="comment-row">
				<span class="star"><em style="width:69%"></em></span>
                <span class="score">6.9</span>
                <em>|</em>
				<a class="comment-num" href="/1186/1185512/review.shtml" target="_blank">55人点评</a>
				<a class="review-active-v4" target="_blank" href="http://detail.zol.com.cn/reviewActivity/ReviewActV9.html" title="点评留下，奖品抱走">点评留下，奖品抱走</a>
			</div>

						<div class="function-v3">
                                <label id="comp1185512" class="compare-btn" hide-focus="true" data-rel='1185512,华为nova 3（全网通）,/cell_phone/index1185512.shtml,https://2f.zol-img.com.cn/product/191_80x60/739/ceMGSYkHizU6.jpg,57' title="点击把它添加到对比框里"><i></i>对比</label>
            </div>
			<div class="merchant-row"></div>
						<div class="rank-row">
								<a href="http://top.zol.com.cn/compositor/57/cell_phone.html" target="_blank">热门排行第<span>1</span>名</a>
							</div>
			        </li>
            <li data-follow-id="p1225806" >
                        <a href="/cell_phone/index1225806.shtml" class="pic" target="_blank"><img width="220" height="165" .src="https://2c.zol-img.com.cn/product/192_220x165/610/ceWgKT2LVJXDI.jpg" alt="OPPO R17（8GB RAM/全网通）"></a>
            <h3><a href="/cell_phone/index1225806.shtml" title="OPPO R17（8GB RAM/全网通）光感屏幕指纹，AI场景识别，AR实景导航，六代大猩猩玻璃" target="_blank">OPPO R17（8GB RAM/全网通） <span>光感屏幕指纹，AI场景识别，AR实景导航，六代大猩猩玻璃</span></a></h3>
            <div class="price-row">
                                                <span class="price-tip">参考价：</span><span class="price price-normal"><b class="price-sign">￥</b><b class="price-type">3499</b></span>								<div class="goods-promotion">
																								</div>
            </div>

			<div class="comment-row">
				<span class="star"><em style="width:95%"></em></span>
                <span class="score">9.5</span>
                <em>|</em>
				<a class="comment-num" href="/1226/1225806/review.shtml" target="_blank">107人点评</a>
				<a class="review-active-v4" target="_blank" href="http://detail.zol.com.cn/reviewActivity/ReviewActV9.html" title="点评留下，奖品抱走">点评留下，奖品抱走</a>
			</div>

						<div class="function-v3">
                                <label id="comp1225806" class="compare-btn" hide-focus="true" data-rel='1225806,OPPO R17（8GB RAM/全网通）,/cell_phone/index1225806.shtml,https://2c.zol-img.com.cn/product/192_80x60/610/ceWgKT2LVJXDI.jpg,57' title="点击把它添加到对比框里"><i></i>对比</label>
            </div>
			<div class="merchant-row"></div>
						<div class="rank-row">
								<a href="http://top.zol.com.cn/compositor/57/cell_phone.html" target="_blank">热门排行第<span>2</span>名</a>
							</div>
			        </li>
            <li class="nth-child-3n" data-follow-id="p1227284" data-live>
                        <a href="/cell_phone/index1227284.shtml" class="pic" target="_blank"><img width="220" height="165" .src="https://2f.zol-img.com.cn/product/192_220x165/747/ce63frgxJFc5.jpg" alt="vivo X23（全网通）"></a>
            <h3><a href="/cell_phone/index1227284.shtml" title="vivo X23（全网通）3D幻影激光纹，灵动水滴屏，第四代光电屏幕指纹，AI摄影" target="_blank">vivo X23（全网通） <span>3D幻影激光纹，灵动水滴屏，第四代光电屏幕指纹，AI摄影</span></a></h3>
            <div class="price-row">
                                                <span class="price-tip">参考价：</span><span class="price price-normal"><b class="price-sign">￥</b><b class="price-type">3498</b></span>								<div class="goods-promotion">
																								</div>
            </div>

			<div class="comment-row">
				<span class="star"><em style="width:94%"></em></span>
                <span class="score">9.4</span>
                <em>|</em>
				<a class="comment-num" href="/1228/1227284/review.shtml" target="_blank">236人点评</a>
				<a class="review-active-v4" target="_blank" href="http://detail.zol.com.cn/reviewActivity/ReviewActV9.html" title="点评留下，奖品抱走">点评留下，奖品抱走</a>
			</div>

						<div class="function-v3">
                                <label id="comp1227284" class="compare-btn" hide-focus="true" data-rel='1227284,vivo X23（全网通）,/cell_phone/index1227284.shtml,https://2f.zol-img.com.cn/product/192_80x60/747/ce63frgxJFc5.jpg,57' title="点击把它添加到对比框里"><i></i>对比</label>
            </div>
			<div class="merchant-row"></div>
						<div class="rank-row">
								<a href="http://top.zol.com.cn/compositor/57/cell_phone.html" target="_blank">热门排行第<span>3</span>名</a>
							</div>
			        </li>
            <li class="nth-child-4n" data-follow-id="p1229519" data-live>
                        <a href="/cell_phone/index1229519.shtml" class="pic" target="_blank"><img width="220" height="165" .src="https://2a.zol-img.com.cn/product/192_220x165/114/ceu5ISnPU1bo.jpg" alt="苹果iPhone XS（全网通）"></a>
            <h3><a href="/cell_phone/index1229519.shtml" title="苹果iPhone XS（全网通）超视网膜显示屏，后置双摄，苹果 A12处理器" target="_blank">苹果iPhone XS（全网通） <span>超视网膜显示屏，后置双摄，苹果 A12处理器</span></a></h3>
            <div class="price-row">
                                                <span class="price-tip">参考价：</span><span class="price price-normal"><b class="price-sign">￥</b><b class="price-type">8699</b></span>								<div class="goods-promotion">
																								</div>
            </div>

			<div class="comment-row">
				<span class="star"><em style="width:61%"></em></span>
                <span class="score">6.1</span>
                <em>|</em>
				<a class="comment-num" href="/1230/1229519/review.shtml" target="_blank">33人点评</a>
				<a class="review-active-v4" target="_blank" href="http://detail.zol.com.cn/reviewActivity/ReviewActV9.html" title="点评留下，奖品抱走">点评留下，奖品抱走</a>
			</div>

						<div class="function-v3">
                                <label id="comp1229519" class="compare-btn" hide-focus="true" data-rel='1229519,苹果iPhone XS（全网通）,/cell_phone/index1229519.shtml,https://2a.zol-img.com.cn/product/192_80x60/114/ceu5ISnPU1bo.jpg,57' title="点击把它添加到对比框里"><i></i>对比</label>
            </div>
			<div class="merchant-row"></div>
						<div class="rank-row">
								<a href="http://top.zol.com.cn/compositor/57/cell_phone.html" target="_blank">热门排行第<span>4</span>名</a>
							</div>
			        </li>
            <li data-follow-id="p1205469" >
                        <a href="/cell_phone/index1205469.shtml" class="pic" target="_blank"><img width="220" height="165" .src="https://2b.zol-img.com.cn/product/191_220x165/933/ceeRbjMDb5zFg.jpg" alt="一加6（8GB RAM/全网通）"></a>
            <h3><a href="/cell_phone/index1205469.shtml" title="一加6（8GB RAM/全网通）面部解锁，指纹识别，19:9全面屏，全面屏手势" target="_blank">一加6（8GB RAM/全网通） <span>面部解锁，指纹识别，19:9全面屏，全面屏手势</span></a></h3>
            <div class="price-row">
                                                <span class="price-tip">参考价：</span><span class="price price-normal"><b class="price-sign">￥</b><b class="price-type">3599</b></span>								<div class="goods-promotion">
																								</div>
            </div>

			<div class="comment-row">
				<span class="star"><em style="width:85%"></em></span>
                <span class="score">8.5</span>
                <em>|</em>
				<a class="comment-num" href="/1206/1205469/review.shtml" target="_blank">327人点评</a>
				<a class="review-active-v4" target="_blank" href="http://detail.zol.com.cn/reviewActivity/ReviewActV9.html" title="点评留下，奖品抱走">点评留下，奖品抱走</a>
			</div>

						<div class="function-v3">
                                <label id="comp1205469" class="compare-btn" hide-focus="true" data-rel='1205469,一加6（8GB RAM/全网通）,/cell_phone/index1205469.shtml,https://2b.zol-img.com.cn/product/191_80x60/933/ceeRbjMDb5zFg.jpg,57' title="点击把它添加到对比框里"><i></i>对比</label>
            </div>
			<div class="merchant-row"></div>
						<div class="rank-row">
								<a href="http://top.zol.com.cn/compositor/57/cell_phone.html" target="_blank">热门排行第<span>5</span>名</a>
							</div>
			        </li>
            <li class="nth-child-3n" data-follow-id="p1212228" >
                        <a href="/cell_phone/index1212228.shtml" class="pic" target="_blank"><img width="220" height="165" .src="https://2d.zol-img.com.cn/product/192_220x165/907/cecakNAv3dQ.jpg" alt="魅族16th（6GB RAM/全网通）"></a>
            <h3><a href="/cell_phone/index1212228.shtml" title="魅族16th（6GB RAM/全网通）CD级无线音质，四曲面3D玻璃机身，屏幕指纹识别，液冷铜管散热" target="_blank">魅族16th（6GB RAM/全网通） <span>CD级无线音质，四曲面3D玻璃机身，屏幕指纹识别，液冷铜管散热</span></a></h3>
            <div class="price-row">
                                                <span class="price-tip">参考价：</span><span class="price price-normal"><b class="price-sign">￥</b><b class="price-type">2698</b></span>								<div class="goods-promotion">
																								</div>
            </div>

			<div class="comment-row">
				<span class="star"><em style="width:69%"></em></span>
                <span class="score">6.9</span>
                <em>|</em>
				<a class="comment-num" href="/1213/1212228/review.shtml" target="_blank">196人点评</a>
				<a class="review-active-v4" target="_blank" href="http://detail.zol.com.cn/reviewActivity/ReviewActV9.html" title="点评留下，奖品抱走">点评留下，奖品抱走</a>
			</div>

						<div class="function-v3">
                                <label id="comp1212228" class="compare-btn" hide-focus="true" data-rel='1212228,魅族16th（6GB RAM/全网通）,/cell_phone/index1212228.shtml,https://2d.zol-img.com.cn/product/192_80x60/907/cecakNAv3dQ.jpg,57' title="点击把它添加到对比框里"><i></i>对比</label>
            </div>
			<div class="merchant-row"></div>
						<div class="rank-row">
								<a href="http://top.zol.com.cn/compositor/57/cell_phone.html" target="_blank">热门排行第<span>6</span>名</a>
							</div>
			        </li>
            <li data-follow-id="p1213467" >
            <span class='award corner-icon-chinajoy2018'></span>            <a href="/cell_phone/index1213467.shtml" class="pic" target="_blank"><img width="220" height="165" .src="https://2b.zol-img.com.cn/product/191_220x165/573/cecLniZRe61iI.jpg" alt="OPPO Find X（标准版/全网通）"></a>
            <h3><a href="/cell_phone/index1213467.shtml" title="OPPO Find X（标准版/全网通）双曲面柔性屏，全隐藏式3D摄像头，VOOC闪充，3D面部识别" target="_blank">OPPO Find X（标准版/全网通） <span>双曲面柔性屏，全隐藏式3D摄像头，VOOC闪充，3D面部识别</span></a></h3>
            <div class="price-row">
                                                <span class="price-tip">参考价：</span><span class="price price-normal"><b class="price-sign">￥</b><b class="price-type">4999</b></span>								<div class="goods-promotion">
																								</div>
            </div>

			<div class="comment-row">
				<span class="star"><em style="width:95%"></em></span>
                <span class="score">9.5</span>
                <em>|</em>
				<a class="comment-num" href="/1214/1213467/review.shtml" target="_blank">747人点评</a>
				<a class="review-active-v4" target="_blank" href="http://detail.zol.com.cn/reviewActivity/ReviewActV9.html" title="点评留下，奖品抱走">点评留下，奖品抱走</a>
			</div>

						<div class="function-v3">
                                <label id="comp1213467" class="compare-btn" hide-focus="true" data-rel='1213467,OPPO Find X（标准版/全网通）,/cell_phone/index1213467.shtml,https://2b.zol-img.com.cn/product/191_80x60/573/cecLniZRe61iI.jpg,57' title="点击把它添加到对比框里"><i></i>对比</label>
            </div>
			<div class="merchant-row"></div>
						<div class="rank-row">
								<a href="http://top.zol.com.cn/compositor/57/cell_phone.html" target="_blank">热门排行第<span>7</span>名</a>
							</div>
			        </li>
            <li class="nth-child-4n" data-follow-id="p1182639" >
                        <a href="/cell_phone/index1182639.shtml" class="pic" target="_blank"><img width="220" height="165" .src="https://2a.zol-img.com.cn/product/186_220x165/536/cet1hjPNo0d6Q.jpg" alt="苹果iPhone X（全网通）"></a>
            <h3><a href="/cell_phone/index1182639.shtml" title="苹果iPhone X（全网通）无线充电，面容ID，后置双摄，全面屏" target="_blank">苹果iPhone X（全网通） <span>无线充电，面容ID，后置双摄，全面屏</span></a></h3>
            <div class="price-row">
                                                <span class="price-tip">参考价：</span><span class="price price-normal"><b class="price-sign">￥</b><b class="price-type">6898</b></span>								<div class="goods-promotion">
																								</div>
            </div>

			<div class="comment-row">
				<span class="star"><em style="width:80%"></em></span>
                <span class="score">8.0</span>
                <em>|</em>
				<a class="comment-num" href="/1183/1182639/review.shtml" target="_blank">186人点评</a>
				<a class="review-active-v4" target="_blank" href="http://detail.zol.com.cn/reviewActivity/ReviewActV9.html" title="点评留下，奖品抱走">点评留下，奖品抱走</a>
			</div>

						<div class="function-v3">
                                <label id="comp1182639" class="compare-btn" hide-focus="true" data-rel='1182639,苹果iPhone X（全网通）,/cell_phone/index1182639.shtml,https://2a.zol-img.com.cn/product/186_80x60/536/cet1hjPNo0d6Q.jpg,57' title="点击把它添加到对比框里"><i></i>对比</label>
            </div>
			<div class="merchant-row"></div>
						<div class="rank-row">
								<a href="http://top.zol.com.cn/compositor/57/cell_phone.html" target="_blank">热门排行第<span>9</span>名</a>
							</div>
			        </li>
            <li class="nth-child-3n" data-follow-id="p1207038" >
            <span class='award corner-icon-chinajoy2018'></span>            <a href="/cell_phone/index1207038.shtml" class="pic" target="_blank"><img width="220" height="165" .src="https://2e.zol-img.com.cn/product/190_220x165/910/cepZEfKxGBcY.jpg" alt="华为P20 Pro（6GB RAM/全网通）"></a>
            <h3><a href="/cell_phone/index1207038.shtml" title="华为P20 Pro（6GB RAM/全网通）4000万徕卡三摄，AI摄影，异形全面屏，指纹识别" target="_blank">华为P20 Pro（6GB RAM/全网通） <span>4000万徕卡三摄，AI摄影，异形全面屏，指纹识别</span></a></h3>
            <div class="price-row">
                                                <span class="price-tip">参考价：</span><span class="price price-normal"><b class="price-sign">￥</b><b class="price-type">4488</b></span>								<div class="goods-promotion">
										<span class="J_PicModeTuan" data-url="http://www.zol.com/detail/cell_phone/huawei/31001890.html?skuId=12912671?spm=784.0" data-price="3869" data-rel="modeTuan">团购</span>
																								</div>
            </div>

			<div class="comment-row">
				<span class="star"><em style="width:82%"></em></span>
                <span class="score">8.2</span>
                <em>|</em>
				<a class="comment-num" href="/1208/1207038/review.shtml" target="_blank">80人点评</a>
				<a class="review-active-v4" target="_blank" href="http://detail.zol.com.cn/reviewActivity/ReviewActV9.html" title="点评留下，奖品抱走">点评留下，奖品抱走</a>
			</div>

						<div class="function-v3">
                                <label id="comp1207038" class="compare-btn" hide-focus="true" data-rel='1207038,华为P20 Pro（6GB RAM/全网通）,/cell_phone/index1207038.shtml,https://2e.zol-img.com.cn/product/190_80x60/910/cepZEfKxGBcY.jpg,57' title="点击把它添加到对比框里"><i></i>对比</label>
            </div>
			<div class="merchant-row"></div>
						<div class="rank-row">
								<a href="http://top.zol.com.cn/compositor/57/cell_phone.html" target="_blank">热门排行第<span>8</span>名</a>
							</div>
			        </li>
            <li data-follow-id="p1219823" >
            <span class='award corner-icon-chinajoy2018'></span>            <a href="/cell_phone/index1219823.shtml" class="pic" target="_blank"><img width="220" height="165" .src="https://2a.zol-img.com.cn/product/191_220x165/566/ceRo14zJK4flI.jpg" alt="vivo NEX旗舰版（全网通）"></a>
            <h3><a href="/cell_phone/index1219823.shtml" title="vivo NEX旗舰版（全网通）AI智慧双摄，零界全面屏，升降式前置摄像头，屏幕指纹解锁3.0" target="_blank">vivo NEX旗舰版（全网通） <span>AI智慧双摄，零界全面屏，升降式前置摄像头，屏幕指纹解锁3.0</span></a></h3>
            <div class="price-row">
                                                <span class="price-tip">参考价：</span><span class="price price-normal"><b class="price-sign">￥</b><b class="price-type">4298</b></span>								<div class="goods-promotion">
																								</div>
            </div>

			<div class="comment-row">
				<span class="star"><em style="width:95%"></em></span>
                <span class="score">9.5</span>
                <em>|</em>
				<a class="comment-num" href="/1220/1219823/review.shtml" target="_blank">644人点评</a>
				<a class="review-active-v4" target="_blank" href="http://detail.zol.com.cn/reviewActivity/ReviewActV9.html" title="点评留下，奖品抱走">点评留下，奖品抱走</a>
			</div>

						<div class="function-v3">
                                <label id="comp1219823" class="compare-btn" hide-focus="true" data-rel='1219823,vivo NEX旗舰版（全网通）,/cell_phone/index1219823.shtml,https://2a.zol-img.com.cn/product/191_80x60/566/ceRo14zJK4flI.jpg,57' title="点击把它添加到对比框里"><i></i>对比</label>
            </div>
			<div class="merchant-row"></div>
						<div class="rank-row">
								<a href="http://top.zol.com.cn/compositor/57/cell_phone.html" target="_blank">热门排行第<span>10</span>名</a>
							</div>
			        </li>
                    <script>
                    document.write("<li class=\" item-sale\" style=\"position:relative;\"><a rel='nofollow' href=\"http://tuan.zol.com/index.php?c=List&a=DanPinTuan&cid=1?spm=748.0\" target=\"_blank\"><img src=\"https://mercrt-fd.zol-img.com.cn/t_s220x300/g5/M00/0E/01/ChMkJ1tOp_GIHL0rAAA_h5BSKlMAApy4wAtXVwAAD-f115.jpg\" width=\"220\" height=\"300\"></a><span style=\"position: absolute; left: 0px; bottom: 0px; width: 29px; height: 16px; background-image: url(https://pic.zol-img.com.cn/201510/thisad_1016.png); background-position: initial initial; background-repeat: no-repeat no-repeat;\"></span></li>");
                </script>
				        <li class="nth-child-3n nth-child-4n" data-follow-id="p1175779" >
                        <a href="/cell_phone/index1175779.shtml" class="pic" target="_blank"><img width="220" height="165" .src="https://2c.zol-img.com.cn/product/190_220x165/902/cee1PflmqGzIw.jpg" alt="华为P20（全网通）"></a>
            <h3><a href="/cell_phone/index1175779.shtml" title="华为P20（全网通）玻璃机身，AI摄影，异形全面屏，指纹识别" target="_blank">华为P20（全网通） <span>玻璃机身，AI摄影，异形全面屏，指纹识别</span></a></h3>
            <div class="price-row">
                                                <span class="price-tip">参考价：</span><span class="price price-normal"><b class="price-sign">￥</b><b class="price-type">3388</b></span>								<div class="goods-promotion">
										<span class="J_PicModeTuan" data-url="http://www.zol.com/detail/cell_phone/huawei/31001878.html?skuId=12912691?spm=784.0" data-price="2899" data-rel="modeTuan">团购</span>
																								</div>
            </div>

			<div class="comment-row">
				<span class="star"><em style="width:86%"></em></span>
                <span class="score">8.6</span>
                <em>|</em>
				<a class="comment-num" href="/1176/1175779/review.shtml" target="_blank">101人点评</a>
				<a class="review-active-v4" target="_blank" href="http://detail.zol.com.cn/reviewActivity/ReviewActV9.html" title="点评留下，奖品抱走">点评留下，奖品抱走</a>
			</div>

						<div class="function-v3">
                                <label id="comp1175779" class="compare-btn" hide-focus="true" data-rel='1175779,华为P20（全网通）,/cell_phone/index1175779.shtml,https://2c.zol-img.com.cn/product/190_80x60/902/cee1PflmqGzIw.jpg,57' title="点击把它添加到对比框里"><i></i>对比</label>
            </div>
			<div class="merchant-row"></div>
						<div class="rank-row">
								<a href="http://top.zol.com.cn/compositor/57/cell_phone.html" target="_blank">热门排行第<span>11</span>名</a>
							</div>
			        </li>
            <li data-follow-id="p1205394" data-live>
                        <a href="/cell_phone/index1205394.shtml" class="pic" target="_blank"><img width="220" height="165" .src="https://2e.zol-img.com.cn/product/192_220x165/118/ceOwvk3XMlXeg.jpg" alt="苹果iPhone XR（全网通）"></a>
            <h3><a href="/cell_phone/index1205394.shtml" title="苹果iPhone XR（全网通）" target="_blank">苹果iPhone XR（全网通） <span>主屏尺寸:6.1英寸 操作系统:iOS 12 主屏材质:LCD 主屏分辨率:1792x828像素 屏幕像素密度:324ppi 4G网络:移动TD-LTE，联通TD-LTE，联通FDD-LTE，电信TD-LTE，电信FDD-LTE</span></a></h3>
            <div class="price-row">
                                                <span class="price-tip">参考价：</span><span class="price price-normal"><b class="price-sign">￥</b><b class="price-type">6499</b></span>								<div class="goods-promotion">
																								</div>
            </div>

			<div class="comment-row">
				<span class="star"><em style="width:44%"></em></span>
                <span class="score">4.4</span>
                <em>|</em>
				<a class="comment-num" href="/1206/1205394/review.shtml" target="_blank">27人点评</a>
				<a class="review-active-v4" target="_blank" href="http://detail.zol.com.cn/reviewActivity/ReviewActV9.html" title="点评留下，奖品抱走">点评留下，奖品抱走</a>
			</div>

						<div class="function-v3">
                                <label id="comp1205394" class="compare-btn" hide-focus="true" data-rel='1205394,苹果iPhone XR（全网通）,/cell_phone/index1205394.shtml,https://2e.zol-img.com.cn/product/192_80x60/118/ceOwvk3XMlXeg.jpg,57' title="点击把它添加到对比框里"><i></i>对比</label>
            </div>
			<div class="merchant-row"></div>
						<div class="rank-row">
								<a href="http://top.zol.com.cn/compositor/57/cell_phone.html" target="_blank">热门排行第<span>12</span>名</a>
							</div>
			        </li>
            <li data-follow-id="p1203409" >
                        <a href="/cell_phone/index1203409.shtml" class="pic" target="_blank"><img width="220" height="165" .src="https://2e.zol-img.com.cn/product/192_220x165/660/ceUdiJ2ZsfE.jpg" alt="苹果iPhone 9（全网通）"></a>
            <h3><a href="/cell_phone/index1203409.shtml" title="苹果iPhone 9（全网通）" target="_blank">苹果iPhone 9（全网通） <span>主屏尺寸:6.2英寸 操作系统:iOS 12 主屏分辨率:2160x1080像素 4G网络:移动TD-LTE，联通TD-LTE，联通FDD-LTE，电信TD-LTE，电信FDD-LTE CPU型号:苹果 A12 核心数:八核 RAM容量:4GB</span></a></h3>
            <div class="price-row">
                                                <span class="price price-cp"><b class="price-type">概念产品</b></span>								<div class="goods-promotion">
																								</div>
            </div>

			<div class="comment-row">
				<span class="star"><em style="width:63%"></em></span>
                <span class="score">6.3</span>
                <em>|</em>
				<a class="comment-num" href="/1204/1203409/review.shtml" target="_blank">23人点评</a>
				<a class="review-active-v4" target="_blank" href="http://detail.zol.com.cn/reviewActivity/ReviewActV9.html" title="点评留下，奖品抱走">点评留下，奖品抱走</a>
			</div>

						<div class="function-v3">
                                <label id="comp1203409" class="compare-btn" hide-focus="true" data-rel='1203409,苹果iPhone 9（全网通）,/cell_phone/index1203409.shtml,https://2e.zol-img.com.cn/product/192_80x60/660/ceUdiJ2ZsfE.jpg,57' title="点击把它添加到对比框里"><i></i>对比</label>
            </div>
			<div class="merchant-row"></div>
						<div class="rank-row">
								<a href="http://top.zol.com.cn/compositor/57/cell_phone.html" target="_blank">热门排行第<span>14</span>名</a>
							</div>
			        </li>
            <li class="nth-child-3n" data-follow-id="p1208704" >
                        <a href="/cell_phone/index1208704.shtml" class="pic" target="_blank"><img width="220" height="165" .src="https://2b.zol-img.com.cn/product/191_220x165/921/ceOFxxMDoCBA.jpg" alt="vivo X21（全网通）"></a>
            <h3><a href="/cell_phone/index1208704.shtml" title="vivo X21（全网通）人工智能，Jovi AI，全面屏，逆光人像" target="_blank">vivo X21（全网通） <span>人工智能，Jovi AI，全面屏，逆光人像</span></a></h3>
            <div class="price-row">
                                                <span class="price-tip">参考价：</span><span class="price price-normal"><b class="price-sign">￥</b><b class="price-type">2498</b></span>								<div class="goods-promotion">
										<span class="J_PicModeTuan" data-url="http://www.zol.com/detail/cell_phone/vivo/31062623.html?skuId=13714062?spm=784.0" data-price="2099" data-rel="modeTuan">团购</span>
																								</div>
            </div>

			<div class="comment-row">
				<span class="star"><em style="width:91%"></em></span>
                <span class="score">9.1</span>
                <em>|</em>
				<a class="comment-num" href="/1209/1208704/review.shtml" target="_blank">554人点评</a>
				<a class="review-active-v4" target="_blank" href="http://detail.zol.com.cn/reviewActivity/ReviewActV9.html" title="点评留下，奖品抱走">点评留下，奖品抱走</a>
			</div>

						<div class="function-v3">
                                <label id="comp1208704" class="compare-btn" hide-focus="true" data-rel='1208704,vivo X21（全网通）,/cell_phone/index1208704.shtml,https://2b.zol-img.com.cn/product/191_80x60/921/ceOFxxMDoCBA.jpg,57' title="点击把它添加到对比框里"><i></i>对比</label>
            </div>
			<div class="merchant-row"></div>
						<div class="rank-row">
								<a href="http://top.zol.com.cn/compositor/57/cell_phone.html" target="_blank">热门排行第<span>13</span>名</a>
							</div>
			        </li>
            <li class="nth-child-4n" data-follow-id="p1213787" >
                        <a href="/cell_phone/index1213787.shtml" class="pic" target="_blank"><img width="220" height="165" .src="https://2d.zol-img.com.cn/product/191_220x165/557/cessHobf7QwFM.jpg" alt="小米8（6GB RAM/全网通）"></a>
            <h3><a href="/cell_phone/index1213787.shtml" title="小米8（6GB RAM/全网通）AI场景相机，L1+L5双频双路定位，红外人脸识别，AI 超感光双摄" target="_blank">小米8（6GB RAM/全网通） <span>AI场景相机，L1+L5双频双路定位，红外人脸识别，AI 超感光双摄</span></a></h3>
            <div class="price-row">
                                                <span class="price-tip">参考价：</span><span class="price price-normal"><b class="price-sign">￥</b><b class="price-type">2599</b></span>								<div class="goods-promotion">
										<span class="J_PicModeTuan" data-url="http://www.zol.com/detail/cell_phone/xiaomi/31326768.html?skuId=13646731?spm=784.0" data-price="2528" data-rel="modeTuan">团购</span>
																								</div>
            </div>

			<div class="comment-row">
				<span class="star"><em style="width:51%"></em></span>
                <span class="score">5.1</span>
                <em>|</em>
				<a class="comment-num" href="/1214/1213787/review.shtml" target="_blank">300人点评</a>
				<a class="review-active-v4" target="_blank" href="http://detail.zol.com.cn/reviewActivity/ReviewActV9.html" title="点评留下，奖品抱走">点评留下，奖品抱走</a>
			</div>

						<div class="function-v3">
                                <label id="comp1213787" class="compare-btn" hide-focus="true" data-rel='1213787,小米8（6GB RAM/全网通）,/cell_phone/index1213787.shtml,https://2d.zol-img.com.cn/product/191_80x60/557/cessHobf7QwFM.jpg,57' title="点击把它添加到对比框里"><i></i>对比</label>
            </div>
			<div class="merchant-row"></div>
						<div class="rank-row">
								<a href="http://top.zol.com.cn/compositor/57/cell_phone.html" target="_blank">热门排行第<span>17</span>名</a>
							</div>
			        </li>
            <li data-follow-id="p1184309" >
                        <a href="/cell_phone/index1184309.shtml" class="pic" target="_blank"><img width="220" height="165" .src="https://2d.zol-img.com.cn/product/192_220x165/999/ce3tGDWGhyq6.jpg" alt="三星GALAXY Note 9（6GB RAM/全网通）"></a>
            <h3><a href="/cell_phone/index1184309.shtml" title="三星GALAXY Note 9（6GB RAM/全网通）钻石切割工艺，S Pen蓝牙模式，三星 Bibxy，Wi-Fi及LTE，全视曲面屏" target="_blank">三星GALAXY Note 9（6GB RAM/全网通） <span>钻石切割工艺，S Pen蓝牙模式，三星 Bibxy，Wi-Fi及LTE，全视曲面屏</span></a></h3>
            <div class="price-row">
                                                <span class="price-tip">参考价：</span><span class="price price-normal"><b class="price-sign">￥</b><b class="price-type">6999</b></span>								<div class="goods-promotion">
																								</div>
            </div>

			<div class="comment-row">
				<span class="star"><em style="width:83%"></em></span>
                <span class="score">8.3</span>
                <em>|</em>
				<a class="comment-num" href="/1185/1184309/review.shtml" target="_blank">44人点评</a>
				<a class="review-active-v4" target="_blank" href="http://detail.zol.com.cn/reviewActivity/ReviewActV9.html" title="点评留下，奖品抱走">点评留下，奖品抱走</a>
			</div>

						<div class="function-v3">
                                <label id="comp1184309" class="compare-btn" hide-focus="true" data-rel='1184309,三星GALAXY Note 9（6GB RAM/全网通）,/cell_phone/index1184309.shtml,https://2d.zol-img.com.cn/product/192_80x60/999/ce3tGDWGhyq6.jpg,57' title="点击把它添加到对比框里"><i></i>对比</label>
            </div>
			<div class="merchant-row"></div>
						<div class="rank-row">
								<a href="http://top.zol.com.cn/compositor/57/cell_phone.html" target="_blank">热门排行第<span>15</span>名</a>
							</div>
			        </li>
            <li class="nth-child-3n" data-follow-id="p1229520" data-live>
                        <a href="/cell_phone/index1229520.shtml" class="pic" target="_blank"><img width="220" height="165" .src="https://2c.zol-img.com.cn/product/192_220x165/116/ceB2DF6b4D0s.jpg" alt="苹果iPhone XS Max（全网通）"></a>
            <h3><a href="/cell_phone/index1229520.shtml" title="苹果iPhone XS Max（全网通）超视网膜显示屏，双卡双待，后置双摄，苹果 A12处理器" target="_blank">苹果iPhone XS Max（全网通） <span>超视网膜显示屏，双卡双待，后置双摄，苹果 A12处理器</span></a></h3>
            <div class="price-row">
                                                <span class="price-tip">参考价：</span><span class="price price-normal"><b class="price-sign">￥</b><b class="price-type">9599</b></span>								<div class="goods-promotion">
																								</div>
            </div>

			<div class="comment-row">
				<span class="star"><em style="width:66%"></em></span>
                <span class="score">6.6</span>
                <em>|</em>
				<a class="comment-num" href="/1230/1229520/review.shtml" target="_blank">18人点评</a>
				<a class="review-active-v4" target="_blank" href="http://detail.zol.com.cn/reviewActivity/ReviewActV9.html" title="点评留下，奖品抱走">点评留下，奖品抱走</a>
			</div>

						<div class="function-v3">
                                <label id="comp1229520" class="compare-btn" hide-focus="true" data-rel='1229520,苹果iPhone XS Max（全网通）,/cell_phone/index1229520.shtml,https://2c.zol-img.com.cn/product/192_80x60/116/ceB2DF6b4D0s.jpg,57' title="点击把它添加到对比框里"><i></i>对比</label>
            </div>
			<div class="merchant-row"></div>
						<div class="rank-row">
								<a href="http://top.zol.com.cn/compositor/57/cell_phone.html" target="_blank">热门排行第<span>16</span>名</a>
							</div>
			        </li>
            <li data-follow-id="p1222342" >
                        <a href="/cell_phone/index1222342.shtml" class="pic" target="_blank"><img width="220" height="165" .src="https://2b.zol-img.com.cn/product/192_220x165/329/ceoplQ5Gua466.jpg" alt="荣耀Note10（6GB RAM/全网通）"></a>
            <h3><a href="/cell_phone/index1222342.shtml" title="荣耀Note10（6GB RAM/全网通）AI画质增强，GPU Turbo，CPU Turbo，THE NINE液冷散热" target="_blank">荣耀Note10（6GB RAM/全网通） <span>AI画质增强，GPU Turbo，CPU Turbo，THE NINE液冷散热</span></a></h3>
            <div class="price-row">
                                                <span class="price-tip">参考价：</span><span class="price price-normal"><b class="price-sign">￥</b><b class="price-type">2799</b></span>								<div class="goods-promotion">
																								</div>
            </div>

			<div class="comment-row">
				<span class="star"><em style="width:88%"></em></span>
                <span class="score">8.8</span>
                <em>|</em>
				<a class="comment-num" href="/1223/1222342/review.shtml" target="_blank">39人点评</a>
				<a class="review-active-v4" target="_blank" href="http://detail.zol.com.cn/reviewActivity/ReviewActV9.html" title="点评留下，奖品抱走">点评留下，奖品抱走</a>
			</div>

						<div class="function-v3">
                                <label id="comp1222342" class="compare-btn" hide-focus="true" data-rel='1222342,荣耀Note10（6GB RAM/全网通）,/cell_phone/index1222342.shtml,https://2b.zol-img.com.cn/product/192_80x60/329/ceoplQ5Gua466.jpg,57' title="点击把它添加到对比框里"><i></i>对比</label>
            </div>
			<div class="merchant-row"></div>
						<div class="rank-row">
								<a href="http://top.zol.com.cn/compositor/57/cell_phone.html" target="_blank">热门排行第<span>18</span>名</a>
							</div>
			        </li>
            <li class="nth-child-4n" data-follow-id="p1206990" >
                        <a href="/cell_phone/index1206990.shtml" class="pic" target="_blank"><img width="220" height="165" .src="https://2b.zol-img.com.cn/product/189_220x165/763/cedVwjOtfBbY.jpg" alt="OPPO R15（6GB RAM/全网通）"></a>
            <h3><a href="/cell_phone/index1206990.shtml" title="OPPO R15（6GB RAM/全网通）19:9超视野全面屏，双面玻璃设计，AI 智能拍照，VOOC闪充" target="_blank">OPPO R15（6GB RAM/全网通） <span>19:9超视野全面屏，双面玻璃设计，AI 智能拍照，VOOC闪充</span></a></h3>
            <div class="price-row">
                                                <span class="price-tip">参考价：</span><span class="price price-normal"><b class="price-sign">￥</b><b class="price-type">2699</b></span>								<div class="goods-promotion">
																								</div>
            </div>

			<div class="comment-row">
				<span class="star"><em style="width:92%"></em></span>
                <span class="score">9.2</span>
                <em>|</em>
				<a class="comment-num" href="/1207/1206990/review.shtml" target="_blank">1052人点评</a>
				<a class="review-active-v4" target="_blank" href="http://detail.zol.com.cn/reviewActivity/ReviewActV9.html" title="点评留下，奖品抱走">点评留下，奖品抱走</a>
			</div>

						<div class="function-v3">
                                <label id="comp1206990" class="compare-btn" hide-focus="true" data-rel='1206990,OPPO R15（6GB RAM/全网通）,/cell_phone/index1206990.shtml,https://2b.zol-img.com.cn/product/189_80x60/763/cedVwjOtfBbY.jpg,57' title="点击把它添加到对比框里"><i></i>对比</label>
            </div>
			<div class="merchant-row"></div>
						<div class="rank-row">
								<a href="http://top.zol.com.cn/compositor/57/cell_phone.html" target="_blank">热门排行第<span>19</span>名</a>
							</div>
			        </li>
            <li class="nth-child-3n" data-follow-id="p1221126" >
                        <a href="/cell_phone/index1221126.shtml" class="pic" target="_blank"><img width="220" height="165" .src="https://2b.zol-img.com.cn/product/191_220x165/731/ceIl6MFjoyY8k.jpg" alt="OPPO A5（全网通）"></a>
            <h3><a href="/cell_phone/index1221126.shtml" title="OPPO A5（全网通）面部识别，智能相册，OPPO互传，全面屏" target="_blank">OPPO A5（全网通） <span>面部识别，智能相册，OPPO互传，全面屏</span></a></h3>
            <div class="price-row">
                                                <span class="price-tip">参考价：</span><span class="price price-normal"><b class="price-sign">￥</b><b class="price-type">1500</b></span>								<div class="goods-promotion">
																								</div>
            </div>

			<div class="comment-row">
				<span class="star"><em style="width:87%"></em></span>
                <span class="score">8.7</span>
                <em>|</em>
				<a class="comment-num" href="/1222/1221126/review.shtml" target="_blank">303人点评</a>
				<a class="review-active-v4" target="_blank" href="http://detail.zol.com.cn/reviewActivity/ReviewActV9.html" title="点评留下，奖品抱走">点评留下，奖品抱走</a>
			</div>

						<div class="function-v3">
                                <label id="comp1221126" class="compare-btn" hide-focus="true" data-rel='1221126,OPPO A5（全网通）,/cell_phone/index1221126.shtml,https://2b.zol-img.com.cn/product/191_80x60/731/ceIl6MFjoyY8k.jpg,57' title="点击把它添加到对比框里"><i></i>对比</label>
            </div>
			<div class="merchant-row"></div>
						<div class="rank-row">
								<a href="http://top.zol.com.cn/compositor/57/cell_phone.html" target="_blank">热门排行第<span>20</span>名</a>
							</div>
			        </li>
                    <script>
                    document.write("<li class=\" item-sale\" style=\"position:relative;\"><a rel='nofollow' href=\"http://www.zol.com/detail/cell_phone/rongyao/30708874.html?skuId=12356050&spm=921?spm=748.0\" target=\"_blank\"><img src=\"https://mercrt-fd.zol-img.com.cn/t_s220x300/g5/M00/0E/02/ChMkJ1tOrTGIU0pcAAA61LhpOKAAApy7QOsWTAAADrs696.jpg\" width=\"220\" height=\"300\"></a><span style=\"position: absolute; left: 0px; bottom: 0px; width: 29px; height: 16px; background-image: url(https://pic.zol-img.com.cn/201510/thisad_1016.png); background-position: initial initial; background-repeat: no-repeat no-repeat;\"></span></li>");
                </script>
				        <li data-follow-id="p1207689" >
                        <a href="/cell_phone/index1207689.shtml" class="pic" target="_blank"><img width="220" height="165" .src="https://2a.zol-img.com.cn/product/190_220x165/618/celLwSHVhvG9M.jpg" alt="荣耀10（全网通）"></a>
            <h3><a href="/cell_phone/index1207689.shtml" title="荣耀10（全网通）变色极光玻璃，前置隐形湿手指纹解锁，2400万AI摄影，全面屏" target="_blank">荣耀10（全网通） <span>变色极光玻璃，前置隐形湿手指纹解锁，2400万AI摄影，全面屏</span></a></h3>
            <div class="price-row">
                                                <span class="price-tip">参考价：</span><span class="price price-normal"><b class="price-sign">￥</b><b class="price-type">2299</b></span>								<div class="goods-promotion">
										<span class="J_PicModeTuan" data-url="http://www.zol.com/detail/cell_phone/rongyao/31140055.html?skuId=12951598?spm=784.0" data-price="2249" data-rel="modeTuan">团购</span>
																								</div>
            </div>

			<div class="comment-row">
				<span class="star"><em style="width:79%"></em></span>
                <span class="score">7.9</span>
                <em>|</em>
				<a class="comment-num" href="/1208/1207689/review.shtml" target="_blank">155人点评</a>
				<a class="review-active-v4" target="_blank" href="http://detail.zol.com.cn/reviewActivity/ReviewActV9.html" title="点评留下，奖品抱走">点评留下，奖品抱走</a>
			</div>

						<div class="function-v3">
                                <label id="comp1207689" class="compare-btn" hide-focus="true" data-rel='1207689,荣耀10（全网通）,/cell_phone/index1207689.shtml,https://2a.zol-img.com.cn/product/190_80x60/618/celLwSHVhvG9M.jpg,57' title="点击把它添加到对比框里"><i></i>对比</label>
            </div>
			<div class="merchant-row"></div>
						<div class="rank-row">
								<a href="http://top.zol.com.cn/compositor/57/cell_phone.html" target="_blank">热门排行第<span>21</span>名</a>
							</div>
			        </li>
            <li class="nth-child-3n nth-child-4n" data-follow-id="p1209676" data-live>
                        <a href="/cell_phone/index1209676.shtml" class="pic" target="_blank"><img width="220" height="165" .src="https://2b.zol-img.com.cn/product/192_220x165/883/ceIooc7zVhQQw.jpg" alt="荣耀8X（4GB RAM/全网通）"></a>
            <h3><a href="/cell_phone/index1209676.shtml" title="荣耀8X（4GB RAM/全网通）GPU Turbo，4D震感，AI防伪基站，AI电梯模式，AI拍照" target="_blank">荣耀8X（4GB RAM/全网通） <span>GPU Turbo，4D震感，AI防伪基站，AI电梯模式，AI拍照</span></a></h3>
            <div class="price-row">
                                                <span class="price-tip">参考价：</span><span class="price price-normal"><b class="price-sign">￥</b><b class="price-type">1399</b></span>								<div class="goods-promotion">
																								</div>
            </div>

			<div class="comment-row">
				<span class="star"><em style="width:63%"></em></span>
                <span class="score">6.3</span>
                <em>|</em>
				<a class="comment-num" href="/1210/1209676/review.shtml" target="_blank">17人点评</a>
				<a class="review-active-v4" target="_blank" href="http://detail.zol.com.cn/reviewActivity/ReviewActV9.html" title="点评留下，奖品抱走">点评留下，奖品抱走</a>
			</div>

						<div class="function-v3">
                                <label id="comp1209676" class="compare-btn" hide-focus="true" data-rel='1209676,荣耀8X（4GB RAM/全网通）,/cell_phone/index1209676.shtml,https://2b.zol-img.com.cn/product/192_80x60/883/ceIooc7zVhQQw.jpg,57' title="点击把它添加到对比框里"><i></i>对比</label>
            </div>
			<div class="merchant-row"></div>
						<div class="rank-row">
								<a href="http://top.zol.com.cn/compositor/57/cell_phone.html" target="_blank">热门排行第<span>22</span>名</a>
							</div>
			        </li>
            <li data-follow-id="p1225826" >
                        <a href="/cell_phone/index1225826.shtml" class="pic" target="_blank"><img width="220" height="165" .src="https://2a.zol-img.com.cn/product/192_220x165/438/ce5kSqjvJTxiI.jpg" alt="OPPO R17 Pro（全网通）"></a>
            <h3><a href="/cell_phone/index1225826.shtml" title="OPPO R17 Pro（全网通）Super VOOC闪充，TOF 3D立体摄像头，OPPO AR实景导航，光感屏幕指纹" target="_blank">OPPO R17 Pro（全网通） <span>Super VOOC闪充，TOF 3D立体摄像头，OPPO AR实景导航，光感屏幕指纹</span></a></h3>
            <div class="price-row">
                                                 <span class="price-tip">参考价：</span><span class="price price-na"><b class="price-sign">￥</b><b class="price-type">4299</b><span class="price-status">[即将上市]</span></span>								<div class="goods-promotion">
																								</div>
            </div>

			<div class="comment-row">
				<span class="star"><em style="width:95%"></em></span>
                <span class="score">9.5</span>
                <em>|</em>
				<a class="comment-num" href="/1226/1225826/review.shtml" target="_blank">73人点评</a>
				<a class="review-active-v4" target="_blank" href="http://detail.zol.com.cn/reviewActivity/ReviewActV9.html" title="点评留下，奖品抱走">点评留下，奖品抱走</a>
			</div>

						<div class="function-v3">
                                <label id="comp1225826" class="compare-btn" hide-focus="true" data-rel='1225826,OPPO R17 Pro（全网通）,/cell_phone/index1225826.shtml,https://2a.zol-img.com.cn/product/192_80x60/438/ce5kSqjvJTxiI.jpg,57' title="点击把它添加到对比框里"><i></i>对比</label>
            </div>
			<div class="merchant-row"></div>
						<div class="rank-row">
								<a href="http://top.zol.com.cn/compositor/57/cell_phone.html" target="_blank">热门排行第<span>47</span>名</a>
							</div>
			        </li>
            <li data-follow-id="p1215468" >
                        <a href="/cell_phone/index1215468.shtml" class="pic" target="_blank"><img width="220" height="165" .src="https://2f.zol-img.com.cn/product/191_220x165/741/ceM1LcyIUsgo.jpg" alt="荣耀Play（4GB RAM/全网通）"></a>
            <h3><a href="/cell_phone/index1215468.shtml" title="荣耀Play（4GB RAM/全网通）GPU Turbo，人工智能NPU，4D游戏体验，面部识别" target="_blank">荣耀Play（4GB RAM/全网通） <span>GPU Turbo，人工智能NPU，4D游戏体验，面部识别</span></a></h3>
            <div class="price-row">
                                                <span class="price-tip">参考价：</span><span class="price price-normal"><b class="price-sign">￥</b><b class="price-type">1799</b></span>								<div class="goods-promotion">
																								</div>
            </div>

			<div class="comment-row">
				<span class="star"><em style="width:58%"></em></span>
                <span class="score">5.8</span>
                <em>|</em>
				<a class="comment-num" href="/1216/1215468/review.shtml" target="_blank">103人点评</a>
				<a class="review-active-v4" target="_blank" href="http://detail.zol.com.cn/reviewActivity/ReviewActV9.html" title="点评留下，奖品抱走">点评留下，奖品抱走</a>
			</div>

						<div class="function-v3">
                                <label id="comp1215468" class="compare-btn" hide-focus="true" data-rel='1215468,荣耀Play（4GB RAM/全网通）,/cell_phone/index1215468.shtml,https://2f.zol-img.com.cn/product/191_80x60/741/ceM1LcyIUsgo.jpg,57' title="点击把它添加到对比框里"><i></i>对比</label>
            </div>
			<div class="merchant-row"></div>
						<div class="rank-row">
								<a href="http://top.zol.com.cn/compositor/57/cell_phone.html" target="_blank">热门排行第<span>24</span>名</a>
							</div>
			        </li>
            <li class="nth-child-3n" data-follow-id="p1182632" >
                        <a href="/cell_phone/index1182632.shtml" class="pic" target="_blank"><img width="220" height="165" .src="https://2f.zol-img.com.cn/product/186_220x165/325/ce06maMuqmn6c.jpg" alt="苹果iPhone 8 Plus（全网通）"></a>
            <h3><a href="/cell_phone/index1182632.shtml" title="苹果iPhone 8 Plus（全网通）双面玻璃，无线充电，Portrait Lighting，后置双摄" target="_blank">苹果iPhone 8 Plus（全网通） <span>双面玻璃，无线充电，Portrait Lighting，后置双摄</span></a></h3>
            <div class="price-row">
                                                <span class="price-tip">参考价：</span><span class="price price-normal"><b class="price-sign">￥</b><b class="price-type">5468</b></span>								<div class="goods-promotion">
																								</div>
            </div>

			<div class="comment-row">
				<span class="star"><em style="width:85%"></em></span>
                <span class="score">8.5</span>
                <em>|</em>
				<a class="comment-num" href="/1183/1182632/review.shtml" target="_blank">79人点评</a>
				<a class="review-active-v4" target="_blank" href="http://detail.zol.com.cn/reviewActivity/ReviewActV9.html" title="点评留下，奖品抱走">点评留下，奖品抱走</a>
			</div>

						<div class="function-v3">
                                <label id="comp1182632" class="compare-btn" hide-focus="true" data-rel='1182632,苹果iPhone 8 Plus（全网通）,/cell_phone/index1182632.shtml,https://2f.zol-img.com.cn/product/186_80x60/325/ce06maMuqmn6c.jpg,57' title="点击把它添加到对比框里"><i></i>对比</label>
            </div>
			<div class="merchant-row"></div>
						<div class="rank-row">
								<a href="http://top.zol.com.cn/compositor/57/cell_phone.html" target="_blank">热门排行第<span>23</span>名</a>
							</div>
			        </li>
            <li class="nth-child-4n" data-follow-id="p1213119" >
                        <a href="/cell_phone/index1213119.shtml" class="pic" target="_blank"><img width="220" height="165" .src="https://2e.zol-img.com.cn/product/192_220x165/410/cecJMeDBS7P9.jpg" alt="360 手机N7 Pro（全网通）"></a>
            <h3><a href="/cell_phone/index1213119.shtml" title="360 手机N7 Pro（全网通）四摄像头，快速充电，全面屏，指纹识别" target="_blank">360 手机N7 Pro（全网通） <span>四摄像头，快速充电，全面屏，指纹识别</span></a></h3>
            <div class="price-row">
                                                <span class="price-tip">参考价：</span><span class="price price-normal"><b class="price-sign">￥</b><b class="price-type">1999</b></span>								<div class="goods-promotion">
																								</div>
            </div>

			<div class="comment-row">
				<span class="star"><em style="width:56%"></em></span>
                <span class="score">5.6</span>
                <em>|</em>
				<a class="comment-num" href="/1214/1213119/review.shtml" target="_blank">23人点评</a>
				<a class="review-active-v4" target="_blank" href="http://detail.zol.com.cn/reviewActivity/ReviewActV9.html" title="点评留下，奖品抱走">点评留下，奖品抱走</a>
			</div>

						<div class="function-v3">
                                <label id="comp1213119" class="compare-btn" hide-focus="true" data-rel='1213119,360 手机N7 Pro（全网通）,/cell_phone/index1213119.shtml,https://2e.zol-img.com.cn/product/192_80x60/410/cecJMeDBS7P9.jpg,57' title="点击把它添加到对比框里"><i></i>对比</label>
            </div>
			<div class="merchant-row"></div>
						<div class="rank-row">
								<a href="http://top.zol.com.cn/compositor/57/cell_phone.html" target="_blank">热门排行第<span>25</span>名</a>
							</div>
			        </li>
            <li data-follow-id="p1211599" >
                        <a href="/cell_phone/index1211599.shtml" class="pic" target="_blank"><img width="220" height="165" .src="https://2e.zol-img.com.cn/product/190_220x165/122/cebTYLlwqfWX.jpg" alt="OPPO A3（全网通）"></a>
            <h3><a href="/cell_phone/index1211599.shtml" title="OPPO A3（全网通）128G大内存，钻石纹理设计，超视野全面屏，AI智慧美颜" target="_blank">OPPO A3（全网通） <span>128G大内存，钻石纹理设计，超视野全面屏，AI智慧美颜</span></a></h3>
            <div class="price-row">
                                                <span class="price-tip">参考价：</span><span class="price price-normal"><b class="price-sign">￥</b><b class="price-type">1799</b></span>								<div class="goods-promotion">
																								</div>
            </div>

			<div class="comment-row">
				<span class="star"><em style="width:89%"></em></span>
                <span class="score">8.9</span>
                <em>|</em>
				<a class="comment-num" href="/1212/1211599/review.shtml" target="_blank">362人点评</a>
				<a class="review-active-v4" target="_blank" href="http://detail.zol.com.cn/reviewActivity/ReviewActV9.html" title="点评留下，奖品抱走">点评留下，奖品抱走</a>
			</div>

						<div class="function-v3">
                                <label id="comp1211599" class="compare-btn" hide-focus="true" data-rel='1211599,OPPO A3（全网通）,/cell_phone/index1211599.shtml,https://2e.zol-img.com.cn/product/190_80x60/122/cebTYLlwqfWX.jpg,57' title="点击把它添加到对比框里"><i></i>对比</label>
            </div>
			<div class="merchant-row"></div>
						<div class="rank-row">
								<a href="http://top.zol.com.cn/compositor/57/cell_phone.html" target="_blank">热门排行第<span>27</span>名</a>
							</div>
			        </li>
            <li class="nth-child-3n" data-follow-id="p1215075" >
                        <a href="/cell_phone/index1215075.shtml" class="pic" target="_blank"><img width="220" height="165" .src="https://2d.zol-img.com.cn/product/191_220x165/587/cepwoMU3q3d0U.jpg" alt="vivo Z1（4GB RAM/全网通）"></a>
            <h3><a href="/cell_phone/index1215075.shtml" title="vivo Z1（4GB RAM/全网通）面部识别，骁龙660AIE，智能美颜拍照，指纹识别" target="_blank">vivo Z1（4GB RAM/全网通） <span>面部识别，骁龙660AIE，智能美颜拍照，指纹识别</span></a></h3>
            <div class="price-row">
                                                <span class="price-tip">参考价：</span><span class="price price-normal"><b class="price-sign">￥</b><b class="price-type">1598</b></span>								<div class="goods-promotion">
																								</div>
            </div>

			<div class="comment-row">
				<span class="star"><em style="width:89%"></em></span>
                <span class="score">8.9</span>
                <em>|</em>
				<a class="comment-num" href="/1216/1215075/review.shtml" target="_blank">43人点评</a>
				<a class="review-active-v4" target="_blank" href="http://detail.zol.com.cn/reviewActivity/ReviewActV9.html" title="点评留下，奖品抱走">点评留下，奖品抱走</a>
			</div>

						<div class="function-v3">
                                <label id="comp1215075" class="compare-btn" hide-focus="true" data-rel='1215075,vivo Z1（4GB RAM/全网通）,/cell_phone/index1215075.shtml,https://2d.zol-img.com.cn/product/191_80x60/587/cepwoMU3q3d0U.jpg,57' title="点击把它添加到对比框里"><i></i>对比</label>
            </div>
			<div class="merchant-row"></div>
						<div class="rank-row">
								<a href="http://top.zol.com.cn/compositor/57/cell_phone.html" target="_blank">热门排行第<span>28</span>名</a>
							</div>
			        </li>
            <li data-follow-id="p1207608" >
                        <a href="/cell_phone/index1207608.shtml" class="pic" target="_blank"><img width="220" height="165" .src="https://2e.zol-img.com.cn/product/189_220x165/722/ceP4JLOWrGwMM.jpg" alt="华为nova 3e（全网通）"></a>
            <h3><a href="/cell_phone/index1207608.shtml" title="华为nova 3e（全网通）人脸识别，19:9全面屏，游戏助手，智能语音助手" target="_blank">华为nova 3e（全网通） <span>人脸识别，19:9全面屏，游戏助手，智能语音助手</span></a></h3>
            <div class="price-row">
                                                <span class="price-tip">参考价：</span><span class="price price-normal"><b class="price-sign">￥</b><b class="price-type">1999</b></span>								<div class="goods-promotion">
																								</div>
            </div>

			<div class="comment-row">
				<span class="star"><em style="width:88%"></em></span>
                <span class="score">8.8</span>
                <em>|</em>
				<a class="comment-num" href="/1208/1207608/review.shtml" target="_blank">69人点评</a>
				<a class="review-active-v4" target="_blank" href="http://detail.zol.com.cn/reviewActivity/ReviewActV9.html" title="点评留下，奖品抱走">点评留下，奖品抱走</a>
			</div>

						<div class="function-v3">
                                <label id="comp1207608" class="compare-btn" hide-focus="true" data-rel='1207608,华为nova 3e（全网通）,/cell_phone/index1207608.shtml,https://2e.zol-img.com.cn/product/189_80x60/722/ceP4JLOWrGwMM.jpg,57' title="点击把它添加到对比框里"><i></i>对比</label>
            </div>
			<div class="merchant-row"></div>
						<div class="rank-row">
								<a href="http://top.zol.com.cn/compositor/57/cell_phone.html" target="_blank">热门排行第<span>31</span>名</a>
							</div>
			        </li>
            <li class="nth-child-4n" data-follow-id="p1222100" >
                        <a href="/cell_phone/index1222100.shtml" class="pic" target="_blank"><img width="220" height="165" .src="https://2e.zol-img.com.cn/product/192_220x165/500/ceQ9iYyhz0Vhk.jpg" alt="华为nova 3i（4GB RAM/全网通）"></a>
            <h3><a href="/cell_phone/index1222100.shtml" title="华为nova 3i（4GB RAM/全网通）GPU Turbo，四摄像头，AI拍照，全面屏" target="_blank">华为nova 3i（4GB RAM/全网通） <span>GPU Turbo，四摄像头，AI拍照，全面屏</span></a></h3>
            <div class="price-row">
                                                <span class="price-tip">参考价：</span><span class="price price-normal"><b class="price-sign">￥</b><b class="price-type">1999</b></span>								<div class="goods-promotion">
																								</div>
            </div>

			<div class="comment-row">
				<span class="star"><em style="width:70%"></em></span>
                <span class="score">7.0</span>
                <em>|</em>
				<a class="comment-num" href="/1223/1222100/review.shtml" target="_blank">9人点评</a>
				<a class="review-active-v4" target="_blank" href="http://detail.zol.com.cn/reviewActivity/ReviewActV9.html" title="点评留下，奖品抱走">点评留下，奖品抱走</a>
			</div>

						<div class="function-v3">
                                <label id="comp1222100" class="compare-btn" hide-focus="true" data-rel='1222100,华为nova 3i（4GB RAM/全网通）,/cell_phone/index1222100.shtml,https://2e.zol-img.com.cn/product/192_80x60/500/ceQ9iYyhz0Vhk.jpg,57' title="点击把它添加到对比框里"><i></i>对比</label>
            </div>
			<div class="merchant-row"></div>
						<div class="rank-row">
								<a href="http://top.zol.com.cn/compositor/57/cell_phone.html" target="_blank">热门排行第<span>29</span>名</a>
							</div>
			        </li>
                    <script>
                    document.write("<li class=\"nth-child-3n item-sale\" style=\"position:relative;\"><a rel='nofollow' href=\"http://www.zol.com/detail/cell_phone/vivo/30961770.html?skuId=12876890?spm=748.0\" target=\"_blank\"><img src=\"https://mercrt-fd.zol-img.com.cn/t_s220x300/g5/M00/05/06/ChMkJlrypUyIeGXVAAA_s6YIF_0AAoQFgEOIB8AAD_L116.jpg\" width=\"220\" height=\"300\"></a><span style=\"position: absolute; left: 0px; bottom: 0px; width: 29px; height: 16px; background-image: url(https://pic.zol-img.com.cn/201510/thisad_1016.png); background-position: initial initial; background-repeat: no-repeat no-repeat;\"></span></li>");
                </script>
				        <li data-follow-id="p394162" >
                        <a href="/cell_phone/index394162.shtml" class="pic" target="_blank"><img width="220" height="165" .src="https://2e.zol-img.com.cn/product/186_220x165/324/ceu0Ld6zstn7c.jpg" alt="苹果iPhone 8（全网通）"></a>
            <h3><a href="/cell_phone/index394162.shtml" title="苹果iPhone 8（全网通）双面玻璃，无线充电，AR游戏，指纹识别" target="_blank">苹果iPhone 8（全网通） <span>双面玻璃，无线充电，AR游戏，指纹识别</span></a></h3>
            <div class="price-row">
                                                <span class="price-tip">参考价：</span><span class="price price-normal"><b class="price-sign">￥</b><b class="price-type">4528</b></span>								<div class="goods-promotion">
																								</div>
            </div>

			<div class="comment-row">
				<span class="star"><em style="width:68%"></em></span>
                <span class="score">6.8</span>
                <em>|</em>
				<a class="comment-num" href="/395/394162/review.shtml" target="_blank">254人点评</a>
				<a class="review-active-v4" target="_blank" href="http://detail.zol.com.cn/reviewActivity/ReviewActV9.html" title="点评留下，奖品抱走">点评留下，奖品抱走</a>
			</div>

						<div class="function-v3">
                                <label id="comp394162" class="compare-btn" hide-focus="true" data-rel='394162,苹果iPhone 8（全网通）,/cell_phone/index394162.shtml,https://2e.zol-img.com.cn/product/186_80x60/324/ceu0Ld6zstn7c.jpg,57' title="点击把它添加到对比框里"><i></i>对比</label>
            </div>
			<div class="merchant-row"></div>
						<div class="rank-row">
								<a href="http://top.zol.com.cn/compositor/57/cell_phone.html" target="_blank">热门排行第<span>26</span>名</a>
							</div>
			        </li>
            <li data-follow-id="p1181907" >
                        <a href="/cell_phone/index1181907.shtml" class="pic" target="_blank"><img width="220" height="165" .src="https://2b.zol-img.com.cn/product/188_220x165/629/ceeATQX7XShA.jpg" alt="荣耀V10（4GB RAM/全网通）"></a>
            <h3><a href="/cell_phone/index1181907.shtml" title="荣耀V10（4GB RAM/全网通）荣耀Hi-Five，指纹识别，人脸识别，AI自拍" target="_blank">荣耀V10（4GB RAM/全网通） <span>荣耀Hi-Five，指纹识别，人脸识别，AI自拍</span></a></h3>
            <div class="price-row">
                                                <span class="price-tip">参考价：</span><span class="price price-normal"><b class="price-sign">￥</b><b class="price-type">1899</b></span>								<div class="goods-promotion">
																								</div>
            </div>

			<div class="comment-row">
				<span class="star"><em style="width:82%"></em></span>
                <span class="score">8.2</span>
                <em>|</em>
				<a class="comment-num" href="/1182/1181907/review.shtml" target="_blank">183人点评</a>
				<a class="review-active-v4" target="_blank" href="http://detail.zol.com.cn/reviewActivity/ReviewActV9.html" title="点评留下，奖品抱走">点评留下，奖品抱走</a>
			</div>

						<div class="function-v3">
                                <label id="comp1181907" class="compare-btn" hide-focus="true" data-rel='1181907,荣耀V10（4GB RAM/全网通）,/cell_phone/index1181907.shtml,https://2b.zol-img.com.cn/product/188_80x60/629/ceeATQX7XShA.jpg,57' title="点击把它添加到对比框里"><i></i>对比</label>
            </div>
			<div class="merchant-row"></div>
						<div class="rank-row">
								<a href="http://top.zol.com.cn/compositor/57/cell_phone.html" target="_blank">热门排行第<span>30</span>名</a>
							</div>
			        </li>
            <li class="nth-child-3n nth-child-4n" data-follow-id="p1215577" >
                        <a href="/cell_phone/index1215577.shtml" class="pic" target="_blank"><img width="220" height="165" .src="https://2a.zol-img.com.cn/product/191_220x165/52/ce9buWJb9cW2s.jpg" alt="vivo NEX（6GB RAM/全网通）"></a>
            <h3><a href="/cell_phone/index1215577.shtml" title="vivo NEX（6GB RAM/全网通）升降式前置摄像头，屏幕指纹解锁3.0，游戏模式4.0，JOVI智能语音助手" target="_blank">vivo NEX（6GB RAM/全网通） <span>升降式前置摄像头，屏幕指纹解锁3.0，游戏模式4.0，JOVI智能语音助手</span></a></h3>
            <div class="price-row">
                                                <span class="price-tip">参考价：</span><span class="price price-normal"><b class="price-sign">￥</b><b class="price-type">3698</b></span>								<div class="goods-promotion">
																								</div>
            </div>

			<div class="comment-row">
				<span class="star"><em style="width:95%"></em></span>
                <span class="score">9.5</span>
                <em>|</em>
				<a class="comment-num" href="/1216/1215577/review.shtml" target="_blank">644人点评</a>
				<a class="review-active-v4" target="_blank" href="http://detail.zol.com.cn/reviewActivity/ReviewActV9.html" title="点评留下，奖品抱走">点评留下，奖品抱走</a>
			</div>

						<div class="function-v3">
                                <label id="comp1215577" class="compare-btn" hide-focus="true" data-rel='1215577,vivo NEX（6GB RAM/全网通）,/cell_phone/index1215577.shtml,https://2a.zol-img.com.cn/product/191_80x60/52/ce9buWJb9cW2s.jpg,57' title="点击把它添加到对比框里"><i></i>对比</label>
            </div>
			<div class="merchant-row"></div>
						<div class="rank-row">
								<a href="http://top.zol.com.cn/compositor/57/cell_phone.html" target="_blank">热门排行第<span>32</span>名</a>
							</div>
			        </li>
            <li data-follow-id="p1209808" >
                        <a href="/cell_phone/index1209808.shtml" class="pic" target="_blank"><img width="220" height="165" .src="https://2e.zol-img.com.cn/product/190_220x165/522/ce6loy8E8ovW.jpg" alt="vivo Y85（全网通）"></a>
            <h3><a href="/cell_phone/index1209808.shtml" title="vivo Y85（全网通）全面屏一体式外观，后置双摄，人像模式，前置AI美颜" target="_blank">vivo Y85（全网通） <span>全面屏一体式外观，后置双摄，人像模式，前置AI美颜</span></a></h3>
            <div class="price-row">
                                                <span class="price-tip">参考价：</span><span class="price price-normal"><b class="price-sign">￥</b><b class="price-type">1398</b></span>								<div class="goods-promotion">
																								</div>
            </div>

			<div class="comment-row">
				<span class="star"><em style="width:82%"></em></span>
                <span class="score">8.2</span>
                <em>|</em>
				<a class="comment-num" href="/1210/1209808/review.shtml" target="_blank">61人点评</a>
				<a class="review-active-v4" target="_blank" href="http://detail.zol.com.cn/reviewActivity/ReviewActV9.html" title="点评留下，奖品抱走">点评留下，奖品抱走</a>
			</div>

						<div class="function-v3">
                                <label id="comp1209808" class="compare-btn" hide-focus="true" data-rel='1209808,vivo Y85（全网通）,/cell_phone/index1209808.shtml,https://2e.zol-img.com.cn/product/190_80x60/522/ce6loy8E8ovW.jpg,57' title="点击把它添加到对比框里"><i></i>对比</label>
            </div>
			<div class="merchant-row"></div>
						<div class="rank-row">
								<a href="http://top.zol.com.cn/compositor/57/cell_phone.html" target="_blank">热门排行第<span>33</span>名</a>
							</div>
			        </li>
            <li data-follow-id="p1170480" >
                        <a href="/cell_phone/index1170480.shtml" class="pic" target="_blank"><img width="220" height="165" .src="https://2c.zol-img.com.cn/product/190_220x165/592/cepiPCapqsDgk.jpg" alt="小米6X（4GB RAM/全网通）"></a>
            <h3><a href="/cell_phone/index1170480.shtml" title="小米6X（4GB RAM/全网通）前置2000万“治愈系”自拍，AI人脸解锁，标配骁龙660 AIE处理器，全面屏" target="_blank">小米6X（4GB RAM/全网通） <span>前置2000万“治愈系”自拍，AI人脸解锁，标配骁龙660 AIE处理器，全面屏</span></a></h3>
            <div class="price-row">
                                                <span class="price-tip">参考价：</span><span class="price price-normal"><b class="price-sign">￥</b><b class="price-type">1349</b></span>								<div class="goods-promotion">
																								</div>
            </div>

			<div class="comment-row">
				<span class="star"><em style="width:53%"></em></span>
                <span class="score">5.3</span>
                <em>|</em>
				<a class="comment-num" href="/1171/1170480/review.shtml" target="_blank">103人点评</a>
				<a class="review-active-v4" target="_blank" href="http://detail.zol.com.cn/reviewActivity/ReviewActV9.html" title="点评留下，奖品抱走">点评留下，奖品抱走</a>
			</div>

						<div class="function-v3">
                                <label id="comp1170480" class="compare-btn" hide-focus="true" data-rel='1170480,小米6X（4GB RAM/全网通）,/cell_phone/index1170480.shtml,https://2c.zol-img.com.cn/product/190_80x60/592/cepiPCapqsDgk.jpg,57' title="点击把它添加到对比框里"><i></i>对比</label>
            </div>
			<div class="merchant-row"></div>
						<div class="rank-row">
								<a href="http://top.zol.com.cn/compositor/57/cell_phone.html" target="_blank">热门排行第<span>34</span>名</a>
							</div>
			        </li>
            <li class="nth-child-3n" data-follow-id="p1104332" >
            <span class="icon award award2_2016"></span>            <a href="/cell_phone/index1104332.shtml" class="pic" target="_blank"><img width="220" height="165" .src="https://2f.zol-img.com.cn/product/185_220x165/593/ceH9bUUFouWg.jpg" alt="苹果iPhone 7 Plus（全网通）"></a>
            <h3><a href="/cell_phone/index1104332.shtml" title="苹果iPhone 7 Plus（全网通）后置双摄像头，多语言文字同时显示，4K视频摄录，Siri语音" target="_blank">苹果iPhone 7 Plus（全网通） <span>后置双摄像头，多语言文字同时显示，4K视频摄录，Siri语音</span></a></h3>
            <div class="price-row">
                                                <span class="price-tip">参考价：</span><span class="price price-normal"><b class="price-sign">￥</b><b class="price-type">4499</b></span>								<div class="goods-promotion">
																								</div>
            </div>

			<div class="comment-row">
				<span class="star"><em style="width:81%"></em></span>
                <span class="score">8.1</span>
                <em>|</em>
				<a class="comment-num" href="/1105/1104332/review.shtml" target="_blank">335人点评</a>
				<a class="review-active-v4" target="_blank" href="http://detail.zol.com.cn/reviewActivity/ReviewActV9.html" title="点评留下，奖品抱走">点评留下，奖品抱走</a>
			</div>

						<div class="function-v3">
                                <label id="comp1104332" class="compare-btn" hide-focus="true" data-rel='1104332,苹果iPhone 7 Plus（全网通）,/cell_phone/index1104332.shtml,https://2f.zol-img.com.cn/product/185_80x60/593/ceH9bUUFouWg.jpg,57' title="点击把它添加到对比框里"><i></i>对比</label>
            </div>
			<div class="merchant-row"></div>
						<div class="rank-row">
								<a href="http://top.zol.com.cn/compositor/57/cell_phone.html" target="_blank">热门排行第<span>35</span>名</a>
							</div>
			        </li>
            <li class="nth-child-4n" data-follow-id="p1216612" >
                        <a href="/cell_phone/index1216612.shtml" class="pic" target="_blank"><img width="220" height="165" .src="https://2d.zol-img.com.cn/product/191_220x165/585/cev71NIc7PKmc.jpg" alt="三星Galaxy A9 Star（全网通）"></a>
            <h3><a href="/cell_phone/index1216612.shtml" title="三星Galaxy A9 Star（全网通）Bixby智能生活，指纹识别，AI美颜，杜比全景声" target="_blank">三星Galaxy A9 Star（全网通） <span>Bixby智能生活，指纹识别，AI美颜，杜比全景声</span></a></h3>
            <div class="price-row">
                                                <span class="price-tip">参考价：</span><span class="price price-normal"><b class="price-sign">￥</b><b class="price-type">2969</b></span>								<div class="goods-promotion">
										<span class="J_PicModeTuan" data-url="http://www.zol.com/detail/cell_phone/samsung/31369324.html?skuId=13232796?spm=784.0" data-price="2399" data-rel="modeTuan">团购</span>
																								</div>
            </div>

			<div class="comment-row">
				<span class="star"><em style="width:75%"></em></span>
                <span class="score">7.5</span>
                <em>|</em>
				<a class="comment-num" href="/1217/1216612/review.shtml" target="_blank">194人点评</a>
				<a class="review-active-v4" target="_blank" href="http://detail.zol.com.cn/reviewActivity/ReviewActV9.html" title="点评留下，奖品抱走">点评留下，奖品抱走</a>
			</div>

						<div class="function-v3">
                                <label id="comp1216612" class="compare-btn" hide-focus="true" data-rel='1216612,三星Galaxy A9 Star（全网通）,/cell_phone/index1216612.shtml,https://2d.zol-img.com.cn/product/191_80x60/585/cev71NIc7PKmc.jpg,57' title="点击把它添加到对比框里"><i></i>对比</label>
            </div>
			<div class="merchant-row"></div>
						<div class="rank-row">
								<a href="http://top.zol.com.cn/compositor/57/cell_phone.html" target="_blank">热门排行第<span>36</span>名</a>
							</div>
			        </li>
            <li data-follow-id="p1221465" >
                        <a href="/cell_phone/index1221465.shtml" class="pic" target="_blank"><img width="220" height="165" .src="https://2c.zol-img.com.cn/product/192_220x165/968/ces6G1t2lkego.jpg" alt="魅族16th Plus（6GB RAM/全网通）"></a>
            <h3><a href="/cell_phone/index1221465.shtml" title="魅族16th Plus（6GB RAM/全网通）Super mBack 2.0，全面屏手势交互，Music Link 铃声震动，屏幕指纹识别" target="_blank">魅族16th Plus（6GB RAM/全网通） <span>Super mBack 2.0，全面屏手势交互，Music Link 铃声震动，屏幕指纹识别</span></a></h3>
            <div class="price-row">
                                                <span class="price-tip">参考价：</span><span class="price price-normal"><b class="price-sign">￥</b><b class="price-type">3198</b></span>								<div class="goods-promotion">
																								</div>
            </div>

			<div class="comment-row">
				<span class="star"><em style="width:69%"></em></span>
                <span class="score">6.9</span>
                <em>|</em>
				<a class="comment-num" href="/1222/1221465/review.shtml" target="_blank">21人点评</a>
				<a class="review-active-v4" target="_blank" href="http://detail.zol.com.cn/reviewActivity/ReviewActV9.html" title="点评留下，奖品抱走">点评留下，奖品抱走</a>
			</div>

						<div class="function-v3">
                                <label id="comp1221465" class="compare-btn" hide-focus="true" data-rel='1221465,魅族16th Plus（6GB RAM/全网通）,/cell_phone/index1221465.shtml,https://2c.zol-img.com.cn/product/192_80x60/968/ces6G1t2lkego.jpg,57' title="点击把它添加到对比框里"><i></i>对比</label>
            </div>
			<div class="merchant-row"></div>
						<div class="rank-row">
								<a href="http://top.zol.com.cn/compositor/57/cell_phone.html" target="_blank">热门排行第<span>44</span>名</a>
							</div>
			        </li>
            <li class="nth-child-3n" data-follow-id="p1227474" >
                        <a href="/cell_phone/index1227474.shtml" class="pic" target="_blank"><img width="220" height="165" .src="https://2e.zol-img.com.cn/product/192_220x165/204/ceLwG8i0WsnQc.jpg" alt="锤子科技坚果Pro 2S（4GB RAM/全网通）"></a>
            <h3><a href="/cell_phone/index1227474.shtml" title="锤子科技坚果Pro 2S（4GB RAM/全网通）全局线性马达，子弹短信，TV-OUT大屏低延迟游戏体验" target="_blank">锤子科技坚果Pro 2S（4GB RAM/全网通） <span>全局线性马达，子弹短信，TV-OUT大屏低延迟游戏体验</span></a></h3>
            <div class="price-row">
                                                <span class="price-tip">参考价：</span><span class="price price-normal"><b class="price-sign">￥</b><b class="price-type">1798</b></span>								<div class="goods-promotion">
																								</div>
            </div>

			<div class="comment-row">
				<span class="star"><em style="width:65%"></em></span>
                <span class="score">6.5</span>
                <em>|</em>
				<a class="comment-num" href="/1228/1227474/review.shtml" target="_blank">14人点评</a>
				<a class="review-active-v4" target="_blank" href="http://detail.zol.com.cn/reviewActivity/ReviewActV9.html" title="点评留下，奖品抱走">点评留下，奖品抱走</a>
			</div>

						<div class="function-v3">
                                <label id="comp1227474" class="compare-btn" hide-focus="true" data-rel='1227474,锤子科技坚果Pro 2S（4GB RAM/全网通）,/cell_phone/index1227474.shtml,https://2e.zol-img.com.cn/product/192_80x60/204/ceLwG8i0WsnQc.jpg,57' title="点击把它添加到对比框里"><i></i>对比</label>
            </div>
			<div class="merchant-row"></div>
			        </li>
            <li data-follow-id="p1184227" >
                        <a href="/cell_phone/index1184227.shtml" class="pic" target="_blank"><img width="220" height="165" .src="https://2d.zol-img.com.cn/product/191_220x165/453/cesBAnMf9mb6.jpg" alt="荣耀9i（全网通）"></a>
            <h3><a href="/cell_phone/index1184227.shtml" title="荣耀9i（全网通）“小萌脸”全面屏，1600万前置感光增强镜头，全系4GB大内存，指纹识别" target="_blank">荣耀9i（全网通） <span>“小萌脸”全面屏，1600万前置感光增强镜头，全系4GB大内存，指纹识别</span></a></h3>
            <div class="price-row">
                                                <span class="price-tip">参考价：</span><span class="price price-normal"><b class="price-sign">￥</b><b class="price-type">1298</b></span>								<div class="goods-promotion">
																								</div>
            </div>

			<div class="comment-row">
				<span class="star"><em style="width:57%"></em></span>
                <span class="score">5.7</span>
                <em>|</em>
				<a class="comment-num" href="/1185/1184227/review.shtml" target="_blank">25人点评</a>
				<a class="review-active-v4" target="_blank" href="http://detail.zol.com.cn/reviewActivity/ReviewActV9.html" title="点评留下，奖品抱走">点评留下，奖品抱走</a>
			</div>

						<div class="function-v3">
                                <label id="comp1184227" class="compare-btn" hide-focus="true" data-rel='1184227,荣耀9i（全网通）,/cell_phone/index1184227.shtml,https://2d.zol-img.com.cn/product/191_80x60/453/cesBAnMf9mb6.jpg,57' title="点击把它添加到对比框里"><i></i>对比</label>
            </div>
			<div class="merchant-row"></div>
						<div class="rank-row">
								<a href="http://top.zol.com.cn/compositor/57/cell_phone.html" target="_blank">热门排行第<span>39</span>名</a>
							</div>
			        </li>
            <li class="nth-child-4n" data-follow-id="p1165672" >
                        <a href="/cell_phone/index1165672.shtml" class="pic" target="_blank"><img width="220" height="165" .src="https://2b.zol-img.com.cn/product/186_220x165/539/cekSQ5i8WuvA.jpg" alt="华为Mate 10（4GB RAM/全网通）"></a>
            <h3><a href="/cell_phone/index1165672.shtml" title="华为Mate 10（4GB RAM/全网通）支持4.5G LTE，支持PC模式，麒麟970 AI处理器，指纹识别" target="_blank">华为Mate 10（4GB RAM/全网通） <span>支持4.5G LTE，支持PC模式，麒麟970 AI处理器，指纹识别</span></a></h3>
            <div class="price-row">
                                                <span class="price-tip">参考价：</span><span class="price price-normal"><b class="price-sign">￥</b><b class="price-type">3399</b></span>								<div class="goods-promotion">
										<span class="J_PicModeTuan" data-url="http://www.zol.com/detail/cell_phone/huawei/30549520.html?skuId=12068178?spm=784.0" data-price="2629" data-rel="modeTuan">团购</span>
																								</div>
            </div>

			<div class="comment-row">
				<span class="star"><em style="width:83%"></em></span>
                <span class="score">8.3</span>
                <em>|</em>
				<a class="comment-num" href="/1166/1165672/review.shtml" target="_blank">115人点评</a>
				<a class="review-active-v4" target="_blank" href="http://detail.zol.com.cn/reviewActivity/ReviewActV9.html" title="点评留下，奖品抱走">点评留下，奖品抱走</a>
			</div>

						<div class="function-v3">
                                <label id="comp1165672" class="compare-btn" hide-focus="true" data-rel='1165672,华为Mate 10（4GB RAM/全网通）,/cell_phone/index1165672.shtml,https://2b.zol-img.com.cn/product/186_80x60/539/cekSQ5i8WuvA.jpg,57' title="点击把它添加到对比框里"><i></i>对比</label>
            </div>
			<div class="merchant-row"></div>
						<div class="rank-row">
								<a href="http://top.zol.com.cn/compositor/57/cell_phone.html" target="_blank">热门排行第<span>41</span>名</a>
							</div>
			        </li>
            <li class="nth-child-3n" data-follow-id="p384973" >
                        <a href="/cell_phone/index384973.shtml" class="pic" target="_blank"><img width="220" height="165" .src="https://2b.zol-img.com.cn/product/181_220x165/937/cewK6OFuhJxQ.jpg" alt="苹果iPhone 7（全网通）"></a>
            <h3><a href="/cell_phone/index384973.shtml" title="苹果iPhone 7（全网通）防水防尘，True Tone闪光灯，4K视频摄录，非按压式指纹识别" target="_blank">苹果iPhone 7（全网通） <span>防水防尘，True Tone闪光灯，4K视频摄录，非按压式指纹识别</span></a></h3>
            <div class="price-row">
                                                <span class="price-tip">参考价：</span><span class="price price-normal"><b class="price-sign">￥</b><b class="price-type">3628</b></span>								<div class="goods-promotion">
																								</div>
            </div>

			<div class="comment-row">
				<span class="star"><em style="width:80%"></em></span>
                <span class="score">8.0</span>
                <em>|</em>
				<a class="comment-num" href="/385/384973/review.shtml" target="_blank">475人点评</a>
				<a class="review-active-v4" target="_blank" href="http://detail.zol.com.cn/reviewActivity/ReviewActV9.html" title="点评留下，奖品抱走">点评留下，奖品抱走</a>
			</div>

						<div class="function-v3">
                                <label id="comp384973" class="compare-btn" hide-focus="true" data-rel='384973,苹果iPhone 7（全网通）,/cell_phone/index384973.shtml,https://2b.zol-img.com.cn/product/181_80x60/937/cewK6OFuhJxQ.jpg,57' title="点击把它添加到对比框里"><i></i>对比</label>
            </div>
			<div class="merchant-row"></div>
						<div class="rank-row">
								<a href="http://top.zol.com.cn/compositor/57/cell_phone.html" target="_blank">热门排行第<span>40</span>名</a>
							</div>
			        </li>
            <li data-follow-id="p1209686" >
                        <a href="/cell_phone/index1209686.shtml" class="pic" target="_blank"><img width="220" height="165" .src="https://2a.zol-img.com.cn/product/192_220x165/524/ceu7aWurxxPas.jpg" alt="苹果iPhone 11（全网通）"></a>
            <h3><a href="/cell_phone/index1209686.shtml" title="苹果iPhone 11（全网通）" target="_blank">苹果iPhone 11（全网通） <span>主屏尺寸:5.8英寸 操作系统:iOS 12 主屏分辨率:2160x1080像素 4G网络:移动TD-LTE，联通TD-LTE，联通FDD-LTE，电信TD-LTE，电信FDD-LTE CPU型号:苹果 A12 核心数:八核 RAM容量:4GB</span></a></h3>
            <div class="price-row">
                                                <span class="price price-cp"><b class="price-type">概念产品</b></span>								<div class="goods-promotion">
																								</div>
            </div>

			<div class="comment-row">
				<span class="star"><em style="width:65%"></em></span>
                <span class="score">6.5</span>
                <em>|</em>
				<a class="comment-num" href="/1210/1209686/review.shtml" target="_blank">12人点评</a>
				<a class="review-active-v4" target="_blank" href="http://detail.zol.com.cn/reviewActivity/ReviewActV9.html" title="点评留下，奖品抱走">点评留下，奖品抱走</a>
			</div>

						<div class="function-v3">
                                <label id="comp1209686" class="compare-btn" hide-focus="true" data-rel='1209686,苹果iPhone 11（全网通）,/cell_phone/index1209686.shtml,https://2a.zol-img.com.cn/product/192_80x60/524/ceu7aWurxxPas.jpg,57' title="点击把它添加到对比框里"><i></i>对比</label>
            </div>
			<div class="merchant-row"></div>
						<div class="rank-row">
								<a href="http://top.zol.com.cn/compositor/57/cell_phone.html" target="_blank">热门排行第<span>37</span>名</a>
							</div>
			        </li>
            <li data-follow-id="p1217453" >
                        <a href="/cell_phone/index1217453.shtml" class="pic" target="_blank"><img width="220" height="165" .src="https://2c.zol-img.com.cn/product/191_220x165/574/cedZwTDSZzzA.jpg" alt="小米8 SE（4GB RAM/全网通）"></a>
            <h3><a href="/cell_phone/index1217453.shtml" title="小米8 SE（4GB RAM/全网通）2.5D弧面玻璃，全网通 5.0，面部识别，全面屏" target="_blank">小米8 SE（4GB RAM/全网通） <span>2.5D弧面玻璃，全网通 5.0，面部识别，全面屏</span></a></h3>
            <div class="price-row">
                                                <span class="price-tip">参考价：</span><span class="price price-normal"><b class="price-sign">￥</b><b class="price-type">1699</b></span>								<div class="goods-promotion">
																								</div>
            </div>

			<div class="comment-row">
				<span class="star"><em style="width:53%"></em></span>
                <span class="score">5.3</span>
                <em>|</em>
				<a class="comment-num" href="/1218/1217453/review.shtml" target="_blank">72人点评</a>
				<a class="review-active-v4" target="_blank" href="http://detail.zol.com.cn/reviewActivity/ReviewActV9.html" title="点评留下，奖品抱走">点评留下，奖品抱走</a>
			</div>

						<div class="function-v3">
                                <label id="comp1217453" class="compare-btn" hide-focus="true" data-rel='1217453,小米8 SE（4GB RAM/全网通）,/cell_phone/index1217453.shtml,https://2c.zol-img.com.cn/product/191_80x60/574/cedZwTDSZzzA.jpg,57' title="点击把它添加到对比框里"><i></i>对比</label>
            </div>
			<div class="merchant-row"></div>
						<div class="rank-row">
								<a href="http://top.zol.com.cn/compositor/57/cell_phone.html" target="_blank">热门排行第<span>42</span>名</a>
							</div>
			        </li>
            <li class="nth-child-3n nth-child-4n" data-follow-id="p1177170" >
                        <a href="/cell_phone/index1177170.shtml" class="pic" target="_blank"><img width="220" height="165" .src="https://2c.zol-img.com.cn/product/190_220x165/438/cerf6VtutNcIU.jpg" alt="三星GALAXY S9+（全网通）"></a>
            <h3><a href="/cell_phone/index1177170.shtml" title="三星GALAXY S9+（全网通）虹膜识别，面部识别，无线快充，Bixby人工智能实时翻译" target="_blank">三星GALAXY S9+（全网通） <span>虹膜识别，面部识别，无线快充，Bixby人工智能实时翻译</span></a></h3>
            <div class="price-row">
                                                <span class="price-tip">参考价：</span><span class="price price-normal"><b class="price-sign">￥</b><b class="price-type">6699</b></span>								<div class="goods-promotion">
																								</div>
            </div>

			<div class="comment-row">
				<span class="star"><em style="width:84%"></em></span>
                <span class="score">8.4</span>
                <em>|</em>
				<a class="comment-num" href="/1178/1177170/review.shtml" target="_blank">128人点评</a>
				<a class="review-active-v4" target="_blank" href="http://detail.zol.com.cn/reviewActivity/ReviewActV9.html" title="点评留下，奖品抱走">点评留下，奖品抱走</a>
			</div>

						<div class="function-v3">
                                <label id="comp1177170" class="compare-btn" hide-focus="true" data-rel='1177170,三星GALAXY S9+（全网通）,/cell_phone/index1177170.shtml,https://2c.zol-img.com.cn/product/190_80x60/438/cerf6VtutNcIU.jpg,57' title="点击把它添加到对比框里"><i></i>对比</label>
            </div>
			<div class="merchant-row"></div>
						<div class="rank-row">
								<a href="http://top.zol.com.cn/compositor/57/cell_phone.html" target="_blank">热门排行第<span>45</span>名</a>
							</div>
			        </li>
        </ul>
    <div class="adSpace" id="list_list_prolist_26"   style="display:none;"><script>write_group_ad('list_list_prolist_26','1price_search_list_24_s_57_m_0.inc#5price_search_list_24_s_57_m_0.inc#0price_search_list_24_s_57.inc',0,57,0);</script><script>ad_w();</script><script>ad_w();</script><script>ad_w();</script></div>	

		    <div id="J_PreloadAd_1" style="display:none !important">
		<div class="adSpace" id="list_list_prolist_3"   style="display:none;"><script>write_group_ad('list_list_prolist_3','4diqu_lis_two_ad_s_57_m_0_{LOCATIONID}.inc#1price_search_list_two_s_57_m_0.inc#5price_search_list_two_s_57_m_0.inc#0price_search_list_two_s_57.inc',0,57,0);</script><script>ad_w();</script><script>ad_w();</script><script>ad_w();</script><script>ad_w();</script></div>	</div>
		<div id="J_PreloadAd_2" style="display:none !important">
		<div class="adSpace" id="list_list_prolist_4"   style="display:none;"><script>write_group_ad('list_list_prolist_4','4diqu_list_third_ad_s_57_m_0_{LOCATIONID}.inc#1price_search_list_three_s_57_m_0.inc#5price_search_list_three_s_57_m_0.inc#0price_search_list_three_s_57.inc',0,57,0);</script><script>ad_w();</script><script>ad_w();</script><script>ad_w();</script><script>ad_w();</script></div>	</div>
		<div id="J_PreloadAd_3" style="display:none !important">
		<div class="adSpace" id="list_list_prolist_5_new"   style="display:none;"><script>write_group_ad('list_list_prolist_5_new','4diqu_list_new_four_ad_s_57_m_0_{LOCATIONID}.inc#1price_search_list_new_four_s_57_m_0.inc#5price_search_list_new_four_s_57_m_0.inc#0price_search_list_new_four_s_57.inc',0,57,0);</script><script>ad_w();</script><script>ad_w();</script><script>ad_w();</script><script>ad_w();</script></div>	</div>
		<div id="J_PreloadAd_4" style="display:none !important">
		<div class="adSpace" id="list_list_prolist_6"   style="display:none;"><script>write_group_ad('list_list_prolist_6','1price_search_list_five_s_57_m_0.inc#5price_search_list_five_s_57_m_0.inc#0price_search_list_five_s_57.inc',0,57,0);</script><script>ad_w();</script><script>ad_w();</script><script>ad_w();</script></div>	</div>
	<div id="J_PreloadAd_5" style="display:none !important">
		<div class="adSpace" id="list_list_prolist_7"   style="display:none;"><script>write_group_ad('list_list_prolist_7','4diqu_list_seven_ad_s_57_m_0_{LOCATIONID}.inc#1price_search_list_six_s_57_m_0.inc#5price_search_list_six_s_57_m_0.inc#0price_search_list_six_s_57.inc',0,57,0);</script><script>ad_w();</script><script>ad_w();</script><script>ad_w();</script><script>ad_w();</script></div>	</div>
	<div id="J_PreloadAd_6" style="display:none !important">
	</div>
	<div id="J_PreloadAd_7" style="display:none !important">
		<div class="adSpace" id="list_list_prolist_13"   style="display:none;"><script>write_group_ad('list_list_prolist_13','4diqu_list_twelve_ad_s_57_m_0_{LOCATIONID}.inc#2price_search_list_twelve_s_57_m_0.inc#5price_search_list_twelve_s_57_m_0.inc#0price_search_list_twelve_s_57.inc',0,57,0);</script><script>ad_w();</script><script>ad_w();</script><script>ad_w();</script><script>ad_w();</script></div>	</div>
	<div id="J_PreloadAd_8" style="display:none !important">
		<div class="adSpace" id="list_list_prolist_10"   style="display:none;"><script>write_group_ad('list_list_prolist_10','4diqu_list_ten_ad_s_57_m_0_{LOCATIONID}.inc#1price_search_list_nine_s_57_m_0.inc#5price_search_list_nine_s_57_m_0.inc#0price_search_list_nine_s_57.inc',0,57,0);</script><script>ad_w();</script><script>ad_w();</script><script>ad_w();</script><script>ad_w();</script></div>		<div class="adSpace" id="list_list_prolist_16"   style="display:none;"><script>write_group_ad('list_list_prolist_16','4diqu_list_fifteen_ad_s_57_m_0_{LOCATIONID}.inc#2price_search_list_fifteen_s_57_m_0.inc#5price_search_list_fifteen_s_57_m_0.inc#0price_search_list_fifteen_s_57.inc',0,57,0);</script><script>ad_w();</script><script>ad_w();</script><script>ad_w();</script><script>ad_w();</script></div>	</div>
	<div id="J_PreloadAd_9" style="display:none !important">
		<div class="adSpace" id="list_list_prolist_19"   style="display:none;"><script>write_group_ad('list_list_prolist_19','4diqu_list_eighteen_ad_s_57_m_0_{LOCATIONID}.inc#2price_search_list_eighteen_s_57_m_0.inc#5price_search_list_eighteen_s_57_m_0.inc#0price_search_list_eighteen_s_57.inc',0,57,0);</script><script>ad_w();</script><script>ad_w();</script><script>ad_w();</script><script>ad_w();</script></div>	</div>
	<div id="J_PreloadAd_10" style="display:none !important">
		<div class="adSpace" id="list_list_prolist_22"   style="display:none;"><script>write_group_ad('list_list_prolist_22','4diqu_list_twenty_one_ad_s_57_m_0_{LOCATIONID}.inc#2price_search_list_twenty_one_s_57_m_0.inc#5price_search_list_twenty_one_s_57_m_0.inc#0price_search_list_twenty_one_s_57.inc',0,57,0);</script><script>ad_w();</script><script>ad_w();</script><script>ad_w();</script><script>ad_w();</script></div>		<div class="adSpace" id="list_list_prolist_25"   style="display:none;"><script>write_group_ad('list_list_prolist_25','4diqu_list_twenty_four_ad_s_57_m_0_{LOCATIONID}.inc#2price_search_list_twenty_four_s_57_m_0.inc#5price_search_list_twenty_four_s_57_m_0.inc#0price_search_list_twenty_four_s_57.inc',0,57,0);</script><script>ad_w();</script><script>ad_w();</script><script>ad_w();</script><script>ad_w();</script></div>	</div>
	</div>

				<div class="page-box">
			<div class="pagebar"><span class="sel">1</span><a href="/cell_phone_index/subcate57_0_list_1_0_1_2_0_2.html"  target="_self">2</a><a href="/cell_phone_index/subcate57_0_list_1_0_1_2_0_3.html"  target="_self">3</a><a href="/cell_phone_index/subcate57_0_list_1_0_1_2_0_4.html"  target="_self">4</a><a href="/cell_phone_index/subcate57_0_list_1_0_1_2_0_5.html"  target="_self">5</a><span >...</span><a href="/cell_phone_index/subcate57_0_list_1_0_1_2_0_2.html" class="next" target="_self">下一页<i></i></a></div>
			<div class="history-tips"><i></i>还有款手机<b>&gt;&gt;</b></div>
		</div>

		<div class="adSpace" id="list_pagenavi_bottom_tonglan"   style="display:none;"><script>write_group_ad('list_pagenavi_bottom_tonglan','3pagenavi_bottom_tonglan.inc',0,57,0);</script><script>ad_w();</script></div>

		        <div id="userTalkPro" class="hide"></div>


				<div class="section">
			<div class="section-header">
				<h3>手机品牌报价大全</h3>
				<p class="link"><a href="/category/57.html" target="_blank">查看更多品牌<b>&gt;&gt;</b></a></p>
			</div>
			<ul class="text-list clearfix">
								<li><a href="/cell_phone_index/subcate57_1673_list_1.html" target="_blank">OPPO手机</a>(47)</li>
								<li><a href="/cell_phone_index/subcate57_1795_list_1.html" target="_blank">vivo手机</a>(46)</li>
								<li><a href="/cell_phone_index/subcate57_613_list_1.html" target="_blank">华为手机</a>(94)</li>
								<li><a href="/cell_phone_index/subcate57_98_list_1.html" target="_blank">三星手机</a>(120)</li>
								<li><a href="/cell_phone_index/subcate57_50840_list_1.html" target="_blank">荣耀手机</a>(74)</li>
								<li><a href="/cell_phone_index/subcate57_35579_list_1.html" target="_blank">一加手机</a>(11)</li>
								<li><a href="/cell_phone_index/subcate57_544_list_1.html" target="_blank">苹果手机</a>(34)</li>
								<li><a href="/cell_phone_index/subcate57_1632_list_1.html" target="_blank">金立手机</a>(38)</li>
								<li><a href="/cell_phone_index/subcate57_1763_list_1.html" target="_blank">联想手机</a>(31)</li>
								<li><a href="/cell_phone_index/subcate57_1434_list_1.html" target="_blank">魅族手机</a>(61)</li>
								<li><a href="/cell_phone_index/subcate57_642_list_1.html" target="_blank">中兴手机</a>(46)</li>
								<li><a href="/cell_phone_index/subcate57_295_list_1.html" target="_blank">Moto手机</a>(44)</li>
								<li><a href="/cell_phone_index/subcate57_35005_list_1.html" target="_blank">努比亚手机</a>(37)</li>
								<li><a href="/cell_phone_index/subcate57_35849_list_1.html" target="_blank">锤子科技手机</a>(15)</li>
								<li><a href="/cell_phone_index/subcate57_35350_list_1.html" target="_blank">360手机</a>(31)</li>
								<li><a href="/cell_phone_index/subcate57_52602_list_1.html" target="_blank">国美手机手机</a>(13)</li>
								<li><a href="/cell_phone_index/subcate57_34645_list_1.html" target="_blank">小米手机</a>(94)</li>
								<li><a href="/cell_phone_index/subcate57_300_list_1.html" target="_blank">夏普手机</a>(19)</li>
							</ul>
		</div>

				<div class="section">
			<div class="section-header">
				<h3>更多手机相关内容</h3>
								<p class="link"><a href="/history/subcate57_0_1_0_0_1.html" target="_blank">查看停产产品<b>&gt;&gt;</b></a></p>
							</div>
			<ul class="text-list clearfix">
									<li><a href="http://detail.zol.com.cn/cell_phone/index1229519.shtml" target="_blank">苹果XS</a></li>
									<li><a href="http://detail.zol.com.cn/cell_phone/index1205394.shtml" target="_blank">苹果xr</a></li>
									<li><a href="http://detail.zol.com.cn/cell_phone/index1212228.shtml" target="_blank">魅族16</a></li>
									<li><a href="http://apple.zol.com.cn/" target="_blank">苹果发布会</a></li>
									<li><a href="http://detail.zol.com.cn/cell_phone/index1227474.shtml" target="_blank">坚果Pro2S</a></li>
									<li><a href="http://detail.zol.com.cn/cell_phone/index1215577.shtml" target="_blank">vivonex</a></li>
									<li><a href="http://detail.zol.com.cn/cell_phone/index1229520.shtml" target="_blank">苹果xsmax</a></li>
									<li><a href="http://detail.zol.com.cn/cell_phone/index1221465.shtml" target="_blank">魅族16plus</a></li>
									<li><a href="http://detail.zol.com.cn/cell_phone/index1222342.shtml" target="_blank">荣耀note10</a></li>
									<li><a href="http://detail.zol.com.cn/cell_phone/index1216973.shtml" target="_blank">小米8透明探索版</a></li>
									<li><a href="http://detail.zol.com.cn/cell_phone/index1227284.shtml" target="_blank">vivox23</a></li>
							</ul>
		</div>

				<div id="btmMerSale"></div>

		<div class="adSpace" id="list_bottom_tonglan"   style="display:none;"><script>write_group_ad('list_bottom_tonglan','3list_bottom_tonglan.inc',0,57,0);</script><script>ad_w();</script></div>
	</div>

		<div class="side">
	   <dl id="J_CategoryCurrent" class="category-current">

    	<dt class="open"><i></i>手机</dt>
	<dd>
		<ul class="category-current-list clearfix">
		    			<li class="active"><a href="/cell_phone_index/subcate57_list_1.html">手机</a></li>
						<li><a href="/phonebattery/">手机电池</a></li>
						<li><a href="/cellcharger/">手机充电器</a></li>
						<li><a href="/datacable/">手机数据线</a></li>
						<li><a href="/mobile-base/">手机底座</a></li>
						<li><a href="/mobile-laoding/">手机贴膜</a></li>
						<li><a href="/mobile-demeo/">手机保护套</a></li>
						<li><a href="/mobile-car-accessories/">手机车载配件</a></li>
						<li><a href="/phone_annex/">手机其它附件</a></li>
					</ul>


    		<h4>手机相关子类</h4>
		<ul class="category-current-list clearfix">
					<li><a href="http://detail.zol.com.cn/flash_memory/s741/">手机存储卡</a></li>
					<li><a href="http://detail.zol.com.cn/microphone/s5004/">蓝牙耳机</a></li>
					<li><a href="http://detail.zol.com.cn/microphone/s2984/">手机耳机</a></li>

		</ul>

		</dd>

    	<dt><i></i>通讯产品</dt>
	<dd class="hide">
		<ul class="category-current-list clearfix">
		    			<li><a href="/groupphone/">集团电话</a></li>
						<li><a href="/interphone/">对讲机</a></li>
						<li><a href="/telephone/">电话机</a></li>
						<li><a href="/dictaphone/">电话录音</a></li>
						<li><a href="/phonepartner/">电话IT伴侣</a></li>
						<li><a href="/netphone/">网络电话</a></li>
						<li><a href="/phonemeeting/">会议电话</a></li>
						<li><a href="/callcenter/">呼叫中心设备</a></li>
						<li><a href="/beeper/">呼叫器</a></li>
					</ul>


    		<h4>通讯产品相关子类</h4>
		<ul class="category-current-list clearfix">
					<li><a href="http://detail.zol.com.cn/Program-controlled_switches/">程控交换机</a></li>
					<li><a href="http://detail.zol.com.cn/videomeeting/">视频会议</a></li>
					<li><a href="http://detail.zol.com.cn/AudioandConference_System/">音频及会议系统</a></li>

		</ul>

		</dd>
	</dl>                <div class="adSpace" id="list_list_right_first_ad"   style="display:none;"><script>write_group_ad('list_list_right_first_ad','3list_right_first_ad.inc',0,57,0);</script><script>ad_w();</script></div>
        		<div id="J_CompetitiveGoods" class="competitive-goods hide" style="position:relative;"></div>

								<div id="J_CompetitiveGoods-5-10" class="competitive-goods hide" ></div>

		<div class="adSpace" id="list_list_right_area_bottom"   style="display:none;"><script>write_group_ad('list_list_right_area_bottom','4diqu_pro_list_right_location_button_s_57_m_0_{LOCATIONID}.inc#1price_search_right_1_s_57_m_0.inc#5price_search_right_1_s_57_m_0.inc#0price_search_right_1_s_57.inc',0,57,0);</script><script>ad_w();</script><script>ad_w();</script><script>ad_w();</script><script>ad_w();</script></div>				<div class="adSpace" id="list_list_right_sub_attention_button"   style="display:none;"><script>write_group_ad('list_list_right_sub_attention_button','4diqu_list_right_sub_attention_button_s_57_m_0_{LOCATIONID}.inc#3list_right_sub_attention_button_1_s_57.inc#1list_right_sub_attention_button_s_57_m_0.inc#5list_right_sub_attention_button_s_57_m_0.inc',0,57,0);</script><script>ad_w();</script><script>ad_w();</script><script>ad_w();</script><script>ad_w();</script></div>
				<div class="module">
    <div class="module-header">
        <h3>大家说</h3>
    </div>
    <ul class="comment-list">
                <li class="">
            <div class="comm-header clearfix">
                <span class="face">
                    <img width="36" height="36" src="https://mypp-fd.zol-img.com.cn/t_s100x100/g5/M00/09/04/ChMkJ1rJiESIBKvIAAAKzhPMKroAAnflAH8EYAAAArm237.jpg">
                </span>
                <div class="comment-box">
                    <span class="name"><a target="_blank" href="//my.zol.com.cn/40jifo/">显摆</a></span>
                    <div class="start"><span class="start-box"><em style="width:80%"></em></span><strong>8.0</strong></div>
                </div>
            </div>
            <p class="comment-content"><strong>优点：</strong>电池续航很强，比较适合手游党电池容量大，没几个手机能比的<a target="_blank" href="http://t.zol.com.cn/57/1212229/evaluation_5430.html">查看全文&gt;</a></p>
            <div class="comm-tag"><span class="time">37分钟前</span><span class="prov">来自 <a title="360 手机N7（6GB RAM/全网通）" target="_blank" href="/cell_phone/index1212229.shtml">360 手机N7（6GB RAM/全网通）</a></span></div>
        </li>
                <li class="">
            <div class="comm-header clearfix">
                <span class="face">
                    <img width="36" height="36" src="https://mypp-fd.zol-img.com.cn/t_s100x100/g5/M00/03/0C/ChMkJlpe-CmIGEmKAAARUWuTyMQAAkJzQC9OHYAABFp989.jpg">
                </span>
                <div class="comment-box">
                    <span class="name"><a target="_blank" href="//my.zol.com.cn/xyqi968497/">Chad Bell</a></span>
                    <div class="start"><span class="start-box"><em style="width:80%"></em></span><strong>8.0</strong></div>
                </div>
            </div>
            <p class="comment-content"><strong>优点：</strong>贵！拿出来有面子！大品牌，有逼格！<a target="_blank" href="http://t.zol.com.cn/57/1182639/evaluation_5429.html">查看全文&gt;</a></p>
            <div class="comm-tag"><span class="time">50分钟前</span><span class="prov">来自 <a title="苹果iPhone X（全网通）" target="_blank" href="/cell_phone/index1182639.shtml">苹果iPhone X（全网通）</a></span></div>
        </li>
                <li class="">
            <div class="comm-header clearfix">
                <span class="face">
                    <img width="36" height="36" src="https://mypp-fd.zol-img.com.cn/t_s100x100/g5/M00/03/02/ChMkJlubT4iIcmDqAAAAy-kFPysAArthgP__uoAAAEW872.jpg">
                </span>
                <div class="comment-box">
                    <span class="name"><a target="_blank" href="//my.zol.com.cn/8azaraiyk/">望断江南岸</a></span>
                    <div class="start"><span class="start-box"><em style="width:80%"></em></span><strong>8.0</strong></div>
                </div>
            </div>
            <p class="comment-content"><strong>优点：</strong>整体感觉还是很不错的性价比还可以<a target="_blank" href="http://t.zol.com.cn/57/1185512/evaluation_5427.html">查看全文&gt;</a></p>
            <div class="comm-tag"><span class="time">1小时前</span><span class="prov">来自 <a title="华为nova 3（全网通）" target="_blank" href="/cell_phone/index1185512.shtml">华为nova 3（全网通）</a></span></div>
        </li>
                <li class="">
            <div class="comm-header clearfix">
                <span class="face">
                    <img width="36" height="36" src="https://icon.zol-img.com.cn/group/default_zoler/zoler_100.jpg">
                </span>
                <div class="comment-box">
                    <span class="name"><a target="_blank" href="//my.zol.com.cn/sina_56322851t3/">水晶晶亮</a></span>
                    <div class="start"><span class="start-box"><em style="width:100%"></em></span><strong>10.0</strong></div>
                </div>
            </div>
            <p class="comment-content"><strong>优点：</strong>FindX在创新设计上很出彩，但更出彩的还有它内置的AI语音助手，“全...<a target="_blank" href="http://detail.zol.com.cn/1214/1213467/review_0_0_1710250_1.shtml#tagNav">查看全文&gt;</a></p>
            <div class="comm-tag"><span class="time">2018-09-13</span><span class="prov">来自 <a title="OPPO Find X（标准版/全网通）" target="_blank" href="/cell_phone/index1213467.shtml">OPPO Find X（标准版/全网通）</a></span></div>
        </li>
                <li class="">
            <div class="comm-header clearfix">
                <span class="face">
                    <img width="36" height="36" src="https://icon.zol-img.com.cn/group/default_zoler/zoler_100.jpg">
                </span>
                <div class="comment-box">
                    <span class="name"><a target="_blank" href="//my.zol.com.cn/sina_3451398571/">大清亡了？</a></span>
                    <div class="start"><span class="start-box"><em style="width:96%"></em></span><strong>9.6</strong></div>
                </div>
            </div>
            <p class="comment-content"><strong>优点：</strong>这么高屏占比的手机我还是第一次用，真是带来了前所未有的视觉体验，曲面屏...<a target="_blank" href="http://detail.zol.com.cn/1214/1213467/review_0_0_1710249_1.shtml#tagNav">查看全文&gt;</a></p>
            <div class="comm-tag"><span class="time">2018-09-13</span><span class="prov">来自 <a title="OPPO Find X（标准版/全网通）" target="_blank" href="/cell_phone/index1213467.shtml">OPPO Find X（标准版/全网通）</a></span></div>
        </li>
                <li class="">
            <div class="comm-header clearfix">
                <span class="face">
                    <img width="36" height="36" src="https://icon.zol-img.com.cn/group/default_zoler/zoler_100.jpg">
                </span>
                <div class="comment-box">
                    <span class="name"><a target="_blank" href="//my.zol.com.cn/sina_8f11p45787/">气球飞了</a></span>
                    <div class="start"><span class="start-box"><em style="width:100%"></em></span><strong>10.0</strong></div>
                </div>
            </div>
            <p class="comment-content"><strong>优点：</strong>拿到这部手机的时候，真的就一种感觉“美翻了”！屏占比高达93.8%，视...<a target="_blank" href="http://detail.zol.com.cn/1214/1213467/review_0_0_1710240_1.shtml#tagNav">查看全文&gt;</a></p>
            <div class="comm-tag"><span class="time">2018-09-13</span><span class="prov">来自 <a title="OPPO Find X（标准版/全网通）" target="_blank" href="/cell_phone/index1213467.shtml">OPPO Find X（标准版/全网通）</a></span></div>
        </li>

    </ul>
</div>


		<div class="module">
	<div class="module-header">
		<h3>新增点评产品</h3>
	</div>
	<ul class="rank-list">
				<li class="current">
			<em class="n1">1</em>		
			<a href="/cell_phone/index1227167.shtml" class="pic" title="华为麦芒7（全网通）" target="_blank">
				<img width="80" height="60" alt="华为麦芒7（全网通）" src="https://2d.zol-img.com.cn/product/192_80x60/749/ceIGTCqrLVnCg.jpg">
			</a>
			<p><a title="华为麦芒7（全网通）" href="/cell_phone/index1227167.shtml" target="_blank">华为麦芒7（全网通）</a></p>
			<p class="price"><em>￥2399</em></p>
		</li>
				<li>
			<em class="n1">2</em>		
			<a href="/cell_phone/index1205394.shtml" class="pic" title="苹果iPhone XR（全网通）" target="_blank">
				<img width="80" height="60" alt="苹果iPhone XR（全网通）" .src="https://2e.zol-img.com.cn/product/192_80x60/118/ceOwvk3XMlXeg.jpg">
			</a>
			<p><a title="苹果iPhone XR（全网通）" href="/cell_phone/index1205394.shtml" target="_blank">苹果iPhone XR（全网通）</a></p>
			<p class="price"><em>￥6499</em></p>
		</li>
				<li>
			<em class="n1">3</em>		
			<a href="/cell_phone/index1203409.shtml" class="pic" title="苹果iPhone 9（全网通）" target="_blank">
				<img width="80" height="60" alt="苹果iPhone 9（全网通）" .src="https://2e.zol-img.com.cn/product/192_80x60/660/ceUdiJ2ZsfE.jpg">
			</a>
			<p><a title="苹果iPhone 9（全网通）" href="/cell_phone/index1203409.shtml" target="_blank">苹果iPhone 9（全网通）</a></p>
			<p class="price"><em>概念产品</em></p>
		</li>
				<li>
			<em class="n2">4</em>		
			<a href="/cell_phone/index1209676.shtml" class="pic" title="荣耀8X（4GB RAM/全网通）" target="_blank">
				<img width="80" height="60" alt="荣耀8X（4GB RAM/全网通）" .src="https://2b.zol-img.com.cn/product/192_80x60/883/ceIooc7zVhQQw.jpg">
			</a>
			<p><a title="荣耀8X（4GB RAM/全网通）" href="/cell_phone/index1209676.shtml" target="_blank">荣耀8X（4GB RAM/全网通）</a></p>
			<p class="price"><em>￥1399</em></p>
		</li>
				<li>
			<em class="n2">5</em>		
			<a href="/cell_phone/index1227284.shtml" class="pic" title="vivo X23（全网通）" target="_blank">
				<img width="80" height="60" alt="vivo X23（全网通）" .src="https://2f.zol-img.com.cn/product/192_80x60/747/ce63frgxJFc5.jpg">
			</a>
			<p><a title="vivo X23（全网通）" href="/cell_phone/index1227284.shtml" target="_blank">vivo X23（全网通）</a></p>
			<p class="price"><em>￥3498</em></p>
		</li>
				<li>
			<em class="n2">6</em>		
			<a href="/cell_phone/index1229492.shtml" class="pic" title="联想Z5 Pro（全网通）" target="_blank">
				<img width="80" height="60" alt="联想Z5 Pro（全网通）" .src="https://2f.zol-img.com.cn/product/192_80x60/85/cenixuR7hwPNg.jpg">
			</a>
			<p><a title="联想Z5 Pro（全网通）" href="/cell_phone/index1229492.shtml" target="_blank">联想Z5 Pro（全网通）</a></p>
			<p class="price"><em>概念产品</em></p>
		</li>
				<li>
			<em class="n2">7</em>		
			<a href="/cell_phone/index1172306.shtml" class="pic" title="三星领世旗舰8（双4G）" target="_blank">
				<img width="80" height="60" alt="三星领世旗舰8（双4G）" .src="https://2d.zol-img.com.cn/product/185_80x60/903/cexURs6fDSvs.jpg">
			</a>
			<p><a title="三星领世旗舰8（双4G）" href="/cell_phone/index1172306.shtml" target="_blank">三星领世旗舰8（双4G）</a></p>
			<p class="price"><em>￥8358</em></p>
		</li>
				<li>
			<em class="n2">8</em>		
			<a href="/cell_phone/index1163244.shtml" class="pic" title="康佳R9（时尚版/移动4G）" target="_blank">
				<img width="80" height="60" alt="康佳R9（时尚版/移动4G）" .src="https://2f.zol-img.com.cn/product/179_80x60/67/ceNkSizvy0vg.jpg">
			</a>
			<p><a title="康佳R9（时尚版/移动4G）" href="/cell_phone/index1163244.shtml" target="_blank">康佳R9（时尚版/移动4G）</a></p>
			<p class="price"><em>￥1299</em></p>
		</li>
				<li>
			<em class="n2">9</em>		
			<a href="/cell_phone/index1208704.shtml" class="pic" title="vivo X21（全网通）" target="_blank">
				<img width="80" height="60" alt="vivo X21（全网通）" .src="https://2b.zol-img.com.cn/product/191_80x60/921/ceOFxxMDoCBA.jpg">
			</a>
			<p><a title="vivo X21（全网通）" href="/cell_phone/index1208704.shtml" target="_blank">vivo X21（全网通）</a></p>
			<p class="price"><em>￥2498</em></p>
		</li>
				<li>
			<em class="n2">10</em>		
			<a href="/cell_phone/index1229520.shtml" class="pic" title="苹果iPhone XS Max（全网通）" target="_blank">
				<img width="80" height="60" alt="苹果iPhone XS Max（全网通）" .src="https://2c.zol-img.com.cn/product/192_80x60/116/ceB2DF6b4D0s.jpg">
			</a>
			<p><a title="苹果iPhone XS Max（全网通）" href="/cell_phone/index1229520.shtml" target="_blank">苹果iPhone XS Max（全网通）</a></p>
			<p class="price"><em>￥9599</em></p>
		</li>
			</ul>
</div>
		<div class="adSpace" id="list_list_right_last_pro_button"   style="display:none;"><script>write_group_ad('list_list_right_last_pro_button','4diqu_list_right_last_pro_button_s_57_m_0_{LOCATIONID}.inc#1list_right_last_pro_button_s_57_m_0.inc#0list_right_last_pro_button_1_s_57.inc#5list_right_last_pro_button_s_57_m_0.inc',0,57,0);</script><script>ad_w();</script><script>ad_w();</script><script>ad_w();</script><script>ad_w();</script></div>


<div class="module">
	<div class="module-header">
				<h3>手机新品</h3>
	</div>
		<ul class="rank-list">
				<li class="current">
			<em class='n1'>1</em>									<a href="/cell_phone/index1231386.shtml" class="pic" title="AGM H1（3GB RAM/全网通）" target="_blank">
				<img width="80" height="60" alt="AGM H1（3GB RAM/全网通）" src="https://2e.zol-img.com.cn/product_small/13_80x60/950/ceUGZXSQRmutA.jpg">
			</a>
			<p><a title="AGM H1（3GB RAM/全网通）" href="/cell_phone/index1231386.shtml" target="_blank">AGM H1（3GB RAM/全网通）</a></p>
			<p><em class="price">￥1799</em></p>
					</li>
				<li>
			<em class='n1'>2</em>									<a href="/cell_phone/index1231314.shtml" class="pic" title="中兴Blade A4（全网通）" target="_blank">
				<img width="80" height="60" alt="中兴Blade A4（全网通）" .src="https://2b.zol-img.com.cn/product_small/13_80x60/863/ceMmzU5T3ozL6.jpg">
			</a>
			<p><a title="中兴Blade A4（全网通）" href="/cell_phone/index1231314.shtml" target="_blank">中兴Blade A4（全网通）</a></p>
			<p><em class="price">￥899</em></p>
					</li>
				<li>
			<em class='n1'>3</em>									<a href="/cell_phone/index1231213.shtml" class="pic" title="Moto P30 Note（6GB RAM/全网通）" target="_blank">
				<img width="80" height="60" alt="Moto P30 Note（6GB RAM/全网通）" .src="https://2b.zol-img.com.cn/product_small/13_80x60/725/cenkIgJehjobc.jpg">
			</a>
			<p><a title="Moto P30 Note（6GB RAM/全网通）" href="/cell_phone/index1231213.shtml" target="_blank">Moto P30 Note（6GB RAM/全..</a></p>
			<p><em class="price">￥2399</em></p>
					</li>
				<li>
			<em class='n2'>4</em>									<a href="/cell_phone/index1231118.shtml" class="pic" title="誉品YP99（移动/联通2G）" target="_blank">
				<img width="80" height="60" alt="誉品YP99（移动/联通2G）" .src="https://2a.zol-img.com.cn/product_small/13_80x60/610/cesfKjfiQbtnw.jpg">
			</a>
			<p><a title="誉品YP99（移动/联通2G）" href="/cell_phone/index1231118.shtml" target="_blank">誉品YP99（移动/联通2G）</a></p>
			<p><em class="price">￥99</em></p>
					</li>
				<li>
			<em class='n2'>5</em>									<a href="/cell_phone/index1231115.shtml" class="pic" title="誉品N105C（电信2G）" target="_blank">
				<img width="80" height="60" alt="誉品N105C（电信2G）" .src="https://2a.zol-img.com.cn/product_small/13_80x60/604/ceqdZdAXgUg.jpg">
			</a>
			<p><a title="誉品N105C（电信2G）" href="/cell_phone/index1231115.shtml" target="_blank">誉品N105C（电信2G）</a></p>
			<p><em class="price">￥188</em></p>
					</li>
				<li>
			<em class='n2'>6</em>									<a href="/cell_phone/index1231110.shtml" class="pic" title="守护宝F555（移动/联通2G）" target="_blank">
				<img width="80" height="60" alt="守护宝F555（移动/联通2G）" .src="https://2f.zol-img.com.cn/product_small/13_80x60/597/ceGo156YEbBo.jpg">
			</a>
			<p><a title="守护宝F555（移动/联通2G）" href="/cell_phone/index1231110.shtml" target="_blank">守护宝F555（移动/联通2G）</a></p>
			<p><em class="price">￥268</em></p>
					</li>
				<li>
			<em class='n2'>7</em>									<a href="/cell_phone/index1231077.shtml" class="pic" title="创星S2（移动/联通2G）" target="_blank">
				<img width="80" height="60" alt="创星S2（移动/联通2G）" .src="https://2f.zol-img.com.cn/product_small/13_80x60/549/ceOnjhTxZZFko.jpg">
			</a>
			<p><a title="创星S2（移动/联通2G）" href="/cell_phone/index1231077.shtml" target="_blank">创星S2（移动/联通2G）</a></p>
			<p><em class="price">￥149</em></p>
					</li>
				<li>
			<em class='n2'>8</em>									<a href="/cell_phone/index1231075.shtml" class="pic" title="创星S10（移动/联通2G）" target="_blank">
				<img width="80" height="60" alt="创星S10（移动/联通2G）" .src="https://2e.zol-img.com.cn/product_small/13_80x60/548/cezFKz1OzJ72w.jpg">
			</a>
			<p><a title="创星S10（移动/联通2G）" href="/cell_phone/index1231075.shtml" target="_blank">创星S10（移动/联通2G）</a></p>
			<p><em class="price">￥79</em></p>
					</li>
				<li>
			<em class='n2'>9</em>									<a href="/cell_phone/index1231072.shtml" class="pic" title="华为P20 Pro（8GB RAM/全网通）" target="_blank">
				<img width="80" height="60" alt="华为P20 Pro（8GB RAM/全网通）" .src="https://2b.zol-img.com.cn/product_small/13_80x60/545/cenNwGeGc8E6U.jpg">
			</a>
			<p><a title="华为P20 Pro（8GB RAM/全网通）" href="/cell_phone/index1231072.shtml" target="_blank">华为P20 Pro（8GB RAM/全网..</a></p>
			<p><em class="price">￥4488</em></p>
					</li>
				<li>
			<em class='n2'>10</em>									<a href="/cell_phone/index1231048.shtml" class="pic" title="小米8青春版（全网通）" target="_blank">
				<img width="80" height="60" alt="小米8青春版（全网通）" .src="https://2c.zol-img.com.cn/product_small/13_80x60/510/ceagwowShKfKg.jpg">
			</a>
			<p><a title="小米8青春版（全网通）" href="/cell_phone/index1231048.shtml" target="_blank">小米8青春版（全网通）</a></p>
			<p><em class="price">概念产品</em></p>
					</li>
			</ul>
	</div>
		<div class="adSpace" id="list_list_right_newPro_bottom"   style="display:none;"><script>write_group_ad('list_list_right_newPro_bottom','4diqu_pro_list_right_new_product_down_s_57_m_0_{LOCATIONID}.inc#1list_right_new_product_down_s_57_m_0.inc',0,57,0);</script><script>ad_w();</script><script>ad_w();</script></div>		
												<div class="adSpace" id="list_right_bottom"   style="display:none;"><script>write_group_ad('list_right_bottom','2list_right_bottom.inc',0,57,0);</script><script>ad_w();</script></div>		<div class="adSpace" id="list_list_left_bottom"   style="display:none;"><script>write_group_ad('list_list_left_bottom','4diqu_left_bottom_s_57_m_0_{LOCATIONID}.inc#5diqu_left_bottom_s_57_m_0_{LOCATIONID}.inc#1price_left_bottom_search_tonglan_s_57_m_0.inc#5price_left_bottom_search_tonglan_s_57_m_0.inc#0price_left_bottom_search_tonglan_s_57.inc#2detail_list_all_left_down.inc',0,57,0);</script><script>ad_w();</script><script>ad_w();</script><script>ad_w();</script><script>ad_w();</script><script>ad_w();</script><script>ad_w();</script></div>

		<div class="adSpace" id="list_list_left_under_visited"   style="display:none;"><script>write_group_ad('list_list_left_under_visited','4list_left_under_visited.inc',0,57,0);</script><script>ad_w();</script></div>		

				<div id="J_VisitedSubPro"></div>
                <div><a href='//www.xgo.cn/' target="_blank" rel="nofollow"><img src="//icon.zol-img.com.cn/products/pc-xgo.jpg"/></a></div>
        <div class="adSpace" id="list_list_right_cellphone_bottom"   style="display:none;"><script>write_group_ad('list_list_right_cellphone_bottom','0list_right_cellphone_s_57_bottom.inc#2list_right_cellphone_s_57_m_0_bottom.inc',0,57,0);</script><script>ad_w();</script><script>ad_w();</script></div>                


<div class="module">
	<div class="module-header">
				<a href="http://detail.zol.com.cn/subcategory.html" class="more" target="_blank">更多&gt;&gt;</a>
				<h3>相关推荐</h3>
	</div>
		<strong class="related-category-type">相关类别：</strong>
		<ul class="related-category-list">
				<li>
									<a title="手机保护套" href="/mobile-demeo/" target="_blank">手机保护套</a>
					</li>
				<li>
									<a title="手机电池" href="/phonebattery/" target="_blank">手机电池</a>
					</li>
				<li>
									<a title="手机充电器" href="/cellcharger/" target="_blank">手机充电器</a>
					</li>
				<li>
									<a title="手机其它附件" href="/phone_annex/" target="_blank">手机其它附件</a>
					</li>
				<li>
									<a title="手机贴膜" href="/mobile-laoding/" target="_blank">手机贴膜</a>
					</li>
			</ul>
		<strong class="hot-category-type">热门类别：</strong>
	<ul class="related-category-list">
		<li><a title="手机" href="/cell_phone_index/subcate57_list_1.html" target="_blank">手机</a></li>
		<li><a title="笔记本" href="/notebook_index/subcate16_list_1.html" target="_blank">笔记本</a></li>
		<li><a title="数码相机" href="/digital_camera_index/subcate15_list_1.html" target="_blank">数码相机</a></li>
		<li><a title="平板电脑" href="/tablepc/" target="_blank">平板电脑</a></li>
	</ul>
	</div>
	</div>
</div>

<div id="iconTip" class="hide"></div>

<script src="//s.zol-img.com.cn/d/Pro/Pro_list_v3.js?v=39918"></script>

<div class="wrapper">
  <script>var __publicNavWidth=1000;var __publicFooterAdFlag = 1;var _zpv_cfg={terminal:"pc",site:"ZOL",buz:"product",channel:"detail",pagetype:"List",custom:{subcateId:57,brand:""}};</script><script language="JavaScript" type="text/javascript" src="//icon.zol-img.com.cn/public/js/web_footc.js"></script>
<script language="JavaScript" type="text/javascript" src="//icon.zol-img.com.cn/public/js/web_foot_d.js"></script> <!-- AudienceScience Async Data Collection Tag -->
                        <script>
                        (function() {
                             var csid = "F09828";
                             var bpid = "zol";
                             var e = document.createElement("script");
                             var s = document.getElementsByTagName("script")[0];
                             e.src = "//js.revsci.net/gateway/gw.js?auto=t&csid=" + csid + "&bpid=" + bpid;
                             e.async = true;
                             s.parentNode.insertBefore(e, s);
                        })();
                        </script>
                        <!-- End AudienceScience Data Collection Tag --></div>
<div class="b2cprice-layer">
    <i class="ico"></i>
    <span></span>
</div>
</body>
</html>
"""
soup = BeautifulSoup(text, 'html.parser')
content = soup.find_all(href = re.compile('/cell_phone/index\d+\.shtml'))
print(content)
f = open('test.txt', 'a')
for i in content:
    print(re.findall(r'(/cell_phone/index\d+.shtml)', str(i)))