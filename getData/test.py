# coding=gbk
from bs4 import BeautifulSoup
import re

text = """

<!DOCTYPE html>
<html>
<head>
<meta charset="GBK" />
	<title>���������ֻ���ȫ���������ֻ����ۼ�ͼƬ��ȫ-ZOL�йش�����</title>
	<meta name="keywords" content="�������ֻ�,�������ֻ�����,�������ֻ��۸�,�ֻ���ȫ,�ֻ����±���" />
	<meta name="description" content="ZOL�йش������ṩ�������ֻ����¼۸񼰾����̱���,�����������ֻ���ȫ,�������ֻ�����,�������ֻ�����,�������ֻ�ͼƬ,�������ֻ���̳����ϸ����,Ϊ�������������ֻ��ṩȫ��ο�" />
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
					<a href="http://service.zol.com.cn/user/api/weixin/jump.php?from=220" target="_self" class="sitenav-weixin" title="ʹ��΢�ŵ�¼"></a>
					<a href="http://service.zol.com.cn/user/api/qq/libs/oauth/redirect_to_login.php?from=220" target="_blank" class="sitenav-qq" title="ʹ����ѶQQ��¼"></a>
					<a href="http://service.zol.com.cn/user/api/sina/jump.php?from=220" target="_blank" class="sitenav-weibo" title="ʹ������΢����¼"></a>
				</div>
				<div id="J_NavLogin" class="sitenav-login-box">
					<a id="J_NavLoginLink" href="https://service.zol.com.cn/user/login.php" target="_self" class="sitenav-login-link">��¼</a>
					<div class="sitenav-login-form">
						<iframe id="ZOL_SMALL_LOGIN" src="" width="190" height="204" frameborder="0" scrolling="no" style="vertical-align:middle"></iframe>
					</div>
				</div>
			</div>
			<!--//sitenav-login-bar-->
		</div>

		<!--sitenav-links-->
		<div class="sitenav-links">
			<a href="http://www.zol.com.cn" class="zol-link" target="_blank">�йش�����</a>

			<!--sitenav-personal-center-->
			<div id="J_NavGroupSite" class="sitenav-groupsite"> 
				<span class="sitenav-trigger">��վ����<i></i></span>
				<div class="groupsite-sitemap-body"> 
					<ul class="sitemap-items">
						<li>
							<span class="sitemap-sub-title">��վ����</span>
                            							<a href="http://detail.zol.com.cn" target="_blank">�鱨��</a>
                            							<a href="http://top.zol.com.cn/" target="_blank">���а�</a>
                            							<a href="http://www.zol.com/" target="_blank">�̳�</a>
                            							<a href="http://tuan.zol.com/" target="_blank">�Ź�</a>
                            							<a href="http://dealer.zol.com.cn/" target="_blank">������</a>
                            							<a href="http://b.zol.com.cn/qy/" target="_blank">�̼ҿ�</a>
                            							<a href="http://2.zol.com.cn/" target="_blank">�����г�</a>
                            							<a href="http://news.zol.com.cn/" target="_blank">����</a>
                            							<a href="http://zdc.zol.com.cn/" target="_blank">����</a>
                            							<a href="http://price.zol.com.cn/" target="_blank">����</a>
                            							<a href="http://zj.zol.com.cn/" target="_blank">ģ���ܻ�</a>
                            							<a href="http://bbs.zol.com.cn/" target="_blank">��̳</a>
                            							<a href="http://ask.zol.com.cn/" target="_blank">�ʴ�</a>
                            							<a href="http://xiazai.zol.com.cn/" target="_blank">�������</a>
                            						</li>
						<li>
							<a href="http://www.zol.com.cn/webcenter/map.html" class="more" target="_blank">����<b>&gt;&gt;</b></a>
							<span class="sitemap-sub-title">��ƷƵ��</span>
                            							<a href="http://detail.zol.com.cn/koubei/" target="_blank">�ڱ���</a>
                            							<a href="http://detail.zol.com.cn/product_new/" target="_blank">ÿ����Ʒ</a>
                            							<a href="http://detail.zol.com.cn/play/mobile/" target="_blank">��ת�ֻ�</a>
                            							<a href="http://v.zol.com.cn/" target="_blank">��ƵƵ��</a>
                            							<a href="http://detail.zol.com.cn/tujie/" target="_blank">����ͼ��</a>
                            							<a href="http://repair.zol.com.cn/" target="_blank">ά�޿�</a>
                            							<a class="icon-new" href="http://detail.zol.com.cn/solution/" target="_blank">���������<i></i></a>
                            							<a href="http://try.zol.com.cn/" target="_blank">��������</a>
                            							<a href="http://tupian.zol.com.cn/" target="_blank">ͼ��</a>
                            						</li>
					</ul>
				</div>
			</div>
			<!--sitenav-personal-center-->

			<div class="product-librarylinks"> 
				<a href="http://top.zol.com.cn" target="_blank">��Ʒ����</a>
				<a class="icon-hot" href="http://e.zol.com.cn/?s=banner" target="_blank">��Ʒ���<i></i></a>
				<a href="http://dealer.zol.com.cn/register_explain.php" target="_blank">�������</a>
				<a href="http://www.zol.com.cn/help/index.html" target="_blank">�ֻ��ͻ���</a>
			</div> 

		</div>
		<!--sitenav-links-->
	</div>
</div>
<table class="header-ads">
	<tr>
		<td class="header-ads-tip">�йش������ƹ�</td>
		<td>
							<div class="adSpace" id="list_list_top_tonglan"   style="display:none;"><script>write_group_ad('list_list_top_tonglan','4diqu_s_57_m_0_{LOCATIONID}.inc#4diqu_s_57_m_0_{PROVINCEID}.inc#5diqu_s_57_m_0_{LOCATIONID}.inc#2price_search_tonglan_s_57_m_0.inc#1price_new_search_tonglan_s_57_m_0.inc#0price_search_tonglan_s_57.inc#4diqu_new_s_57_m_0_{LOCATIONID}.inc#5diqu_new_s_57_m_0_{LOCATIONID}.inc#5price_new_search_tonglan_s_57_m_0.inc#0price_new_search_tonglan_s_57.inc',0,57,0);</script><script>ad_w();</script><script>ad_w();</script><script>ad_w();</script><script>ad_w();</script><script>ad_w();</script><script>ad_w();</script><script>ad_w();</script><script>ad_w();</script><script>ad_w();</script><script>ad_w();</script></div>						<div class="adSpace" id="list_list_top_tonglan_2"   style="display:none;"><script>write_group_ad('list_list_top_tonglan_2','5price_search_tonglan_s_57_m_0.inc',0,57,0);</script><script>ad_w();</script></div>			<div class="adSpace" id="list_list_top_tonglan_3"   style="display:none;"><script>write_group_ad('list_list_top_tonglan_3','5list_header_top_s_57_m_0.inc',0,57,0);</script><script>ad_w();</script></div>		</td>
	</tr>
</table>

<div class="header">
	<a href="/" class="logo">ZOL��Ʒ����</a>
		<div class="qrcode-box" id="J_QrcodeNew">
		<span></span>
		<div class="qrcode-new"><img src="https://icon.zol-img.com.cn/products/v3/detail-appdl-qrcode.png" width="70" height="70">���ؿͻ���</div>
	</div>
		<div class="search-box">
	    <form id="searchForm" action="http://detail.zol.com.cn/index.php" method="get">
            <input type="hidden" value="SearchList" name="c" />
	        <div class="search-keyword">
	            <input id="keyword" name="kword" type="text" class="keyword" maxlength="120" autocomplete="off" x-webkit-speech="" x-webkit-grammar="builtin:translate" lang="zh-CN" hidefocus="true" value="vivo X23"  growing-track='true'/>
	        </div>
	        <input id="subSerch" type="button" class="search-button" hidefocus="true" value="�� ��"  />
	    </form>
	    <div id="suggest" class="search-suggest"></div>
        		<div class="search-hot-words">
                                    <a target="_blank" href="/cell_phone/index384973.shtml">ƻ��7</a>
                                    <a target="_blank" href="/cell_phone/index1215069.shtml">����6</a>
                                    <a target="_blank" href="/cell_phone/index1215577.shtml">vivonex</a>
                                    <a target="_blank" href="/cell_phone/index394162.shtml">ƻ��8</a>
                                    <a target="_blank" href="/cell_phone/index1229519.shtml">ƻ��xs</a>
                                    <a target="_blank" href="/cell_phone/index1209455.shtml">����note5</a>
                                    		</div>
        	</div>
	</div>
<div id="navigation"></div>

<div class="wrapper">




<div class="breadcrumb-filter-selected">
	<div class="breadcrumb"><a href="/">ZOL������ҳ</a> &gt; <span>�ֻ�</span> </div>		<div class="filter-selected">
		<strong class="filter-type">��ѡ������</strong>
		<div id="J_FilterSelectedEmpty" data-full="1" data-bread="1" class="param-selected clearfix"></div>
	</div>
	</div>


<div class="list-title">
	<div id="J_CityArea" class="list-title-inner clearfix">
		<h3>�ֻ�ɸѡ</h3>
		<div class="city-change-box">
						<span id="J_CityChange" data-location="0" class="city-change-triggle">ѡ�����<i></i></span>
			<div id="J_CityList"></div>
		</div>

		<div class="adSpace" id="list_list_search_right_font"   style="display:none;"><script>write_group_ad('list_list_search_right_font','4diqu_postion_right_font_ad_s_57_m_0_{LOCATIONID}.inc#1price_search_simp_search_text_s_57_m_0.inc#5price_search_simp_search_text_s_57_m_0.inc',0,57,0);</script><script>ad_w();</script><script>ad_w();</script><script>ad_w();</script></div>
					</div>
</div>

<div id="J_ParamFilter" class="param-filter">
                        <div id="J_ManuFilter" class="filter-brand">
                <strong class="filter-type">Ʒ�ƣ�</strong>
                <div id="J_ParamBrand" class="brand-hot brand-list">
                    <span class="all active">����</span>                    <a href="/cell_phone_index/subcate57_1673_list_1.html">OPPO</a><a href="/cell_phone_index/subcate57_1795_list_1.html">vivo</a><a href="/cell_phone_index/subcate57_613_list_1.html">��Ϊ</a><a href="/cell_phone_index/subcate57_98_list_1.html">����</a><a href="/cell_phone_index/subcate57_50840_list_1.html">��ҫ</a><a href="/cell_phone_index/subcate57_35579_list_1.html">һ��</a><a href="/cell_phone_index/subcate57_544_list_1.html">ƻ��</a><a href="/cell_phone_index/subcate57_1632_list_1.html">����</a><a href="/cell_phone_index/subcate57_1763_list_1.html">����</a><a href="/cell_phone_index/subcate57_1434_list_1.html">����</a><a href="/cell_phone_index/subcate57_642_list_1.html">����</a><a href="/cell_phone_index/subcate57_295_list_1.html">Moto</a><a href="/cell_phone_index/subcate57_35005_list_1.html">Ŭ����</a><a href="/cell_phone_index/subcate57_35849_list_1.html">���ӿƼ�</a><a href="/cell_phone_index/subcate57_35350_list_1.html">360</a><a href="/cell_phone_index/subcate57_52602_list_1.html">�����ֻ�</a><a href="/cell_phone_index/subcate57_34645_list_1.html">С��</a><a href="/cell_phone_index/subcate57_300_list_1.html">����</a><a href="/cell_phone_index/subcate57_227_list_1.html">��˶</a><a href="/cell_phone_index/subcate57_35179_list_1.html">��ͼ</a><a href="/cell_phone_index/subcate57_297_list_1.html">ŵ����</a><a href="/cell_phone_index/subcate57_33080_list_1.html">HTC</a><a href="/cell_phone_index/subcate57_49202_list_1.html">8848</a><a href="/cell_phone_index/subcate57_35224_list_1.html">SUGAR</a><a href="/cell_phone_index/subcate57_12772_list_1.html">��ݮ</a><a href="/cell_phone_index/subcate57_19_list_1.html">����</a><a href="/cell_phone_index/subcate57_34660_list_1.html">AGM</a><a href="/cell_phone_index/subcate57_1069_list_1.html">�����ƶ�</a><a href="/cell_phone_index/subcate57_1922_list_1.html">�ȸ�</a><a href="/cell_phone_index/subcate57_143_list_1.html">LG</a><a href="/cell_phone_index/subcate57_1606_list_1.html">����</a><a href="/cell_phone_index/subcate57_33626_list_1.html">�й��ƶ�</a><a href="/cell_phone_index/subcate57_159_list_1.html">������</a><a href="/cell_phone_index/subcate57_37319_list_1.html">����ZUK</a><a href="/cell_phone_index/subcate57_41412_list_1.html">VERTU</a><a href="/cell_phone_index/subcate57_33855_list_1.html">��Ψ</a><a href="/cell_phone_index/subcate57_34023_list_1.html">���</a><a href="/cell_phone_index/subcate57_599_list_1.html">����</a><a href="/cell_phone_index/subcate57_1081_list_1.html">Ŧ��</a><a href="/cell_phone_index/subcate57_32729_list_1.html">����</a><a href="/cell_phone_index/subcate57_1590_list_1.html">����</a><a href="/cell_phone_index/subcate57_1589_list_1.html">����</a><a href="/cell_phone_index/subcate57_35320_list_1.html">С����</a><a href="/cell_phone_index/subcate57_171_list_1.html">TCL</a><a href="/cell_phone_index/subcate57_364_list_1.html">΢��</a><a href="/cell_phone_index/subcate57_36511_list_1.html">YotaPhone</a><a href="/cell_phone_index/subcate57_750_list_1.html">����</a><a href="/cell_phone_index/subcate57_35335_list_1.html">����</a><a href="/cell_phone_index/subcate57_221_list_1.html">����</a><a href="/cell_phone_index/subcate57_34492_list_1.html">��Ŀ</a><a href="/cell_phone_index/subcate57_35121_list_1.html">MANN</a><a href="/cell_phone_index/subcate57_223_list_1.html">����</a><a href="/cell_phone_index/subcate57_34906_list_1.html">�</a><a href="/cell_phone_index/subcate57_35004_list_1.html">COMIO</a><a href="/cell_phone_index/subcate57_53522_list_1.html">BDV</a><a href="/cell_phone_index/subcate57_33668_list_1.html">sonim</a><a href="/cell_phone_index/subcate57_51710_list_1.html">imoo</a><a href="/cell_phone_index/subcate57_36761_list_1.html">����</a><a href="/cell_phone_index/subcate57_34686_list_1.html">VEB</a><a href="/cell_phone_index/subcate57_52880_list_1.html">�ƴ�ͨ</a><a href="/cell_phone_index/subcate57_342_list_1.html">�ȷ�</a><a href="/cell_phone_index/subcate57_1050_list_1.html">��ħ</a><a href="/cell_phone_index/subcate57_35615_list_1.html">����</a><a href="/cell_phone_index/subcate57_139_list_1.html">�´�</a><a href="/cell_phone_index/subcate57_34741_list_1.html">innos</a><a href="/cell_phone_index/subcate57_53640_list_1.html">ioutdoor</a><a href="/cell_phone_index/subcate57_174_list_1.html">TP-LINK</a><a href="/cell_phone_index/subcate57_84_list_1.html">����</a><a href="/cell_phone_index/subcate57_36409_list_1.html">������</a><a href="/cell_phone_index/subcate57_36538_list_1.html">manta</a><a href="/cell_phone_index/subcate57_36791_list_1.html">PPTV</a><a href="/cell_phone_index/subcate57_36792_list_1.html">��Ұ</a><a href="/cell_phone_index/subcate57_50829_list_1.html">VAIO</a><a href="/cell_phone_index/subcate57_53765_list_1.html">����</a><a href="/cell_phone_index/subcate57_37427_list_1.html">ivvi</a><a href="/cell_phone_index/subcate57_54243_list_1.html">˽��ҽ��</a><a href="/cell_phone_index/subcate57_49531_list_1.html">��ǧ��</a><a href="/cell_phone_index/subcate57_37433_list_1.html">��ʯ��</a><a href="/cell_phone_index/subcate57_34857_list_1.html">���</a><a href="/cell_phone_index/subcate57_35228_list_1.html">21��</a><a href="/cell_phone_index/subcate57_34547_list_1.html">�ƺ�</a><a href="/cell_phone_index/subcate57_53006_list_1.html">����</a><a href="/cell_phone_index/subcate57_531_list_1.html">��������</a><a href="/cell_phone_index/subcate57_52034_list_1.html">��Ӱ��Ļ</a><a href="/cell_phone_index/subcate57_53520_list_1.html">������</a><a href="/cell_phone_index/subcate57_52848_list_1.html">�ػ���</a><a href="/cell_phone_index/subcate57_50842_list_1.html">ȫ��</a><a href="/cell_phone_index/subcate57_41933_list_1.html">�ٺ�</a><a href="/cell_phone_index/subcate57_40737_list_1.html">�ʽ�</a><a href="/cell_phone_index/subcate57_37585_list_1.html">����</a><a href="/cell_phone_index/subcate57_34927_list_1.html">���</a><a href="/cell_phone_index/subcate57_41365_list_1.html">�װ���</a><a href="/cell_phone_index/subcate57_51281_list_1.html">����</a><a href="/cell_phone_index/subcate57_36647_list_1.html">������ŵ</a><a href="/cell_phone_index/subcate57_51194_list_1.html">��ʯ</a><a href="/cell_phone_index/subcate57_51808_list_1.html">����</a><a href="/cell_phone_index/subcate57_37438_list_1.html">���N</a><a href="/cell_phone_index/subcate57_53521_list_1.html">����</a><a href="/cell_phone_index/subcate57_32512_list_1.html">���Ƶ���</a><a href="/cell_phone_index/subcate57_35102_list_1.html">�῭��</a><a href="/cell_phone_index/subcate57_51558_list_1.html">С����</a><a href="/cell_phone_index/subcate57_41107_list_1.html">����</a><a href="/cell_phone_index/subcate57_51978_list_1.html">�컢</a><a href="/cell_phone_index/subcate57_35415_list_1.html">GEMRY</a><a href="/cell_phone_index/subcate57_51107_list_1.html">����</a><a href="/cell_phone_index/subcate57_51576_list_1.html">Ant one</a><a href="/cell_phone_index/subcate57_34874_list_1.html">���δ�</a><a href="/cell_phone_index/subcate57_37263_list_1.html">������</a><a href="/cell_phone_index/subcate57_49477_list_1.html">����</a><a href="/cell_phone_index/subcate57_49232_list_1.html">ͼ��</a><a href="/cell_phone_index/subcate57_35147_list_1.html">С����</a><a href="/cell_phone_index/subcate57_50865_list_1.html">;Ϊ</a><a href="/cell_phone_index/subcate57_36594_list_1.html">����</a><a href="/cell_phone_index/subcate57_355_list_1.html">����</a><a href="/cell_phone_index/subcate57_49354_list_1.html">����ά</a><a href="/cell_phone_index/subcate57_51993_list_1.html">����</a><a href="/cell_phone_index/subcate57_1528_list_1.html">��̩</a><a href="/cell_phone_index/subcate57_53979_list_1.html">����</a><a href="/cell_phone_index/subcate57_43188_list_1.html">BROR</a><a href="/cell_phone_index/subcate57_49221_list_1.html">�����ǻ�</a><a href="/cell_phone_index/subcate57_51417_list_1.html">VANO</a><a href="/cell_phone_index/subcate57_35405_list_1.html">��Ʒ</a><a href="/cell_phone_index/subcate57_33382_list_1.html">ŷ��</a>                </div>
                <div class="brand-muti-more">
                                            <a id="J_Multi" class="multi" href="javascript:;" target="_self" data-flag="1" data-manu="0" data-url-type="param">��ѡ</a>
                                        <a class="J_ViewMore view-more" data-multi="0" data-manu="0" data-brand="true" data-target="J_ParamBrand" data-url-type="param" href="javascript:;" target="_self">����<i></i></a>
                </div>
                <div class="brand-all">
                    <ul id="J_BrandTab" class="brand-all-tab">
                        <li class="active" data-letter-value="all"><span>ȫ��Ʒ��</span><i></i></li>
                                                    <li data-letter-value="0-9"><span>0-9</span><i></i></li>
                                                        <li data-letter-value="65-71"><span>A-G</span><i></i></li>
                                                        <li data-letter-value="72-78"><span>H-N</span><i></i></li>
                                                        <li data-letter-value="79-84"><span>O-T</span><i></i></li>
                                                        <li data-letter-value="85-90"><span>U-Z</span><i></i></li>
                                                </ul>
                    <div id="J_BrandAll" data-multi="0" class="brand-list"><a href="/cell_phone_index/subcate57_1673_list_1.html" data-link="1673" data-letter="O">OPPO</a><a href="/cell_phone_index/subcate57_1795_list_1.html" data-link="1795" data-letter="V">vivo</a><a href="/cell_phone_index/subcate57_613_list_1.html" data-link="613" data-letter="H">��Ϊ</a><a href="/cell_phone_index/subcate57_98_list_1.html" data-link="98" data-letter="S">����</a><a href="/cell_phone_index/subcate57_50840_list_1.html" data-link="50840" data-letter="R">��ҫ</a><a href="/cell_phone_index/subcate57_35579_list_1.html" data-link="35579" data-letter="Y">һ��</a><a href="/cell_phone_index/subcate57_544_list_1.html" data-link="544" data-letter="P">ƻ��</a><a href="/cell_phone_index/subcate57_1632_list_1.html" data-link="1632" data-letter="J">����</a><a href="/cell_phone_index/subcate57_1763_list_1.html" data-link="1763" data-letter="L">����</a><a href="/cell_phone_index/subcate57_1434_list_1.html" data-link="1434" data-letter="M">����</a><a href="/cell_phone_index/subcate57_642_list_1.html" data-link="642" data-letter="Z">����</a><a href="/cell_phone_index/subcate57_295_list_1.html" data-link="295" data-letter="M">Moto</a><a href="/cell_phone_index/subcate57_35005_list_1.html" data-link="35005" data-letter="N">Ŭ����</a><a href="/cell_phone_index/subcate57_35849_list_1.html" data-link="35849" data-letter="C">���ӿƼ�</a><a href="/cell_phone_index/subcate57_35350_list_1.html" data-link="35350" data-letter="3">360</a><a href="/cell_phone_index/subcate57_52602_list_1.html" data-link="52602" data-letter="G">�����ֻ�</a><a href="/cell_phone_index/subcate57_34645_list_1.html" data-link="34645" data-letter="X">С��</a><a href="/cell_phone_index/subcate57_300_list_1.html" data-link="300" data-letter="X">����</a><a href="/cell_phone_index/subcate57_227_list_1.html" data-link="227" data-letter="H">��˶</a><a href="/cell_phone_index/subcate57_35179_list_1.html" data-link="35179" data-letter="M">��ͼ</a><a href="/cell_phone_index/subcate57_297_list_1.html" data-link="297" data-letter="N">ŵ����</a><a href="/cell_phone_index/subcate57_33080_list_1.html" data-link="33080" data-letter="H">HTC</a><a href="/cell_phone_index/subcate57_49202_list_1.html" data-link="49202" data-letter="8">8848</a><a href="/cell_phone_index/subcate57_35224_list_1.html" data-link="35224" data-letter="S">SUGAR</a><a href="/cell_phone_index/subcate57_12772_list_1.html" data-link="12772" data-letter="H">��ݮ</a><a href="/cell_phone_index/subcate57_19_list_1.html" data-link="19" data-letter="H">����</a><a href="/cell_phone_index/subcate57_34660_list_1.html" data-link="34660" data-letter="A">AGM</a><a href="/cell_phone_index/subcate57_1069_list_1.html" data-link="1069" data-letter="S">�����ƶ�</a><a href="/cell_phone_index/subcate57_1922_list_1.html" data-link="1922" data-letter="G">�ȸ�</a><a href="/cell_phone_index/subcate57_143_list_1.html" data-link="143" data-letter="L">LG</a><a href="/cell_phone_index/subcate57_1606_list_1.html" data-link="1606" data-letter="K">����</a><a href="/cell_phone_index/subcate57_33626_list_1.html" data-link="33626" data-letter="Z">�й��ƶ�</a><a href="/cell_phone_index/subcate57_159_list_1.html" data-link="159" data-letter="F">������</a><a href="/cell_phone_index/subcate57_37319_list_1.html" data-link="37319" data-letter="L">����ZUK</a><a href="/cell_phone_index/subcate57_41412_list_1.html" data-link="41412" data-letter="V">VERTU</a><a href="/cell_phone_index/subcate57_33855_list_1.html" data-link="33855" data-letter="D">��Ψ</a><a href="/cell_phone_index/subcate57_34023_list_1.html" data-link="34023" data-letter="K">���</a><a href="/cell_phone_index/subcate57_599_list_1.html" data-link="599" data-letter="K">����</a><a href="/cell_phone_index/subcate57_1081_list_1.html" data-link="1081" data-letter="N">Ŧ��</a><a href="/cell_phone_index/subcate57_32729_list_1.html" data-link="32729" data-letter="T">����</a><a href="/cell_phone_index/subcate57_1590_list_1.html" data-link="1590" data-letter="L">����</a><a href="/cell_phone_index/subcate57_1589_list_1.html" data-link="1589" data-letter="C">����</a><a href="/cell_phone_index/subcate57_35320_list_1.html" data-link="35320" data-letter="X">С����</a><a href="/cell_phone_index/subcate57_171_list_1.html" data-link="171" data-letter="T">TCL</a><a href="/cell_phone_index/subcate57_364_list_1.html" data-link="364" data-letter="W">΢��</a><a href="/cell_phone_index/subcate57_36511_list_1.html" data-link="36511" data-letter="Y">YotaPhone</a><a href="/cell_phone_index/subcate57_750_list_1.html" data-link="750" data-letter="G">����</a><a href="/cell_phone_index/subcate57_35335_list_1.html" data-link="35335" data-letter="H">����</a><a href="/cell_phone_index/subcate57_221_list_1.html" data-link="221" data-letter="H">����</a><a href="/cell_phone_index/subcate57_34492_list_1.html" data-link="34492" data-letter="L">��Ŀ</a><a href="/cell_phone_index/subcate57_35121_list_1.html" data-link="35121" data-letter="M">MANN</a><a href="/cell_phone_index/subcate57_223_list_1.html" data-link="223" data-letter="H">����</a><a href="/cell_phone_index/subcate57_34906_list_1.html" data-link="34906" data-letter="B">�</a><a href="/cell_phone_index/subcate57_35004_list_1.html" data-link="35004" data-letter="C">COMIO</a><a href="/cell_phone_index/subcate57_53522_list_1.html" data-link="53522" data-letter="B">BDV</a><a href="/cell_phone_index/subcate57_33668_list_1.html" data-link="33668" data-letter="S">sonim</a><a href="/cell_phone_index/subcate57_51710_list_1.html" data-link="51710" data-letter="I">imoo</a><a href="/cell_phone_index/subcate57_36761_list_1.html" data-link="36761" data-letter="D">����</a><a href="/cell_phone_index/subcate57_34686_list_1.html" data-link="34686" data-letter="V">VEB</a><a href="/cell_phone_index/subcate57_52880_list_1.html" data-link="52880" data-letter="Y">�ƴ�ͨ</a><a href="/cell_phone_index/subcate57_342_list_1.html" data-link="342" data-letter="X">�ȷ�</a><a href="/cell_phone_index/subcate57_1050_list_1.html" data-link="1050" data-letter="L">��ħ</a><a href="/cell_phone_index/subcate57_35615_list_1.html" data-link="35615" data-letter="S">����</a><a href="/cell_phone_index/subcate57_139_list_1.html" data-link="139" data-letter="K">�´�</a><a href="/cell_phone_index/subcate57_34741_list_1.html" data-link="34741" data-letter="I">innos</a><a href="/cell_phone_index/subcate57_53640_list_1.html" data-link="53640" data-letter="I">ioutdoor</a><a href="/cell_phone_index/subcate57_174_list_1.html" data-link="174" data-letter="T">TP-LINK</a><a href="/cell_phone_index/subcate57_84_list_1.html" data-link="84" data-letter="S">����</a><a href="/cell_phone_index/subcate57_36409_list_1.html" data-link="36409" data-letter="F">������</a><a href="/cell_phone_index/subcate57_36538_list_1.html" data-link="36538" data-letter="M">manta</a><a href="/cell_phone_index/subcate57_36791_list_1.html" data-link="36791" data-letter="P">PPTV</a><a href="/cell_phone_index/subcate57_36792_list_1.html" data-link="36792" data-letter="S">��Ұ</a><a href="/cell_phone_index/subcate57_50829_list_1.html" data-link="50829" data-letter="V">VAIO</a><a href="/cell_phone_index/subcate57_53765_list_1.html" data-link="53765" data-letter="H">����</a><a href="/cell_phone_index/subcate57_37427_list_1.html" data-link="37427" data-letter="I">ivvi</a><a href="/cell_phone_index/subcate57_54243_list_1.html" data-link="54243" data-letter="S">˽��ҽ��</a><a href="/cell_phone_index/subcate57_49531_list_1.html" data-link="49531" data-letter="B">��ǧ��</a><a href="/cell_phone_index/subcate57_37433_list_1.html" data-link="37433" data-letter="X">��ʯ��</a><a href="/cell_phone_index/subcate57_34857_list_1.html" data-link="34857" data-letter="Q">���</a><a href="/cell_phone_index/subcate57_35228_list_1.html" data-link="35228" data-letter="2">21��</a><a href="/cell_phone_index/subcate57_34547_list_1.html" data-link="34547" data-letter="Y">�ƺ�</a><a href="/cell_phone_index/subcate57_53006_list_1.html" data-link="53006" data-letter="H">����</a><a href="/cell_phone_index/subcate57_531_list_1.html" data-link="531" data-letter="A">��������</a><a href="/cell_phone_index/subcate57_52034_list_1.html" data-link="52034" data-letter="D">��Ӱ��Ļ</a><a href="/cell_phone_index/subcate57_53520_list_1.html" data-link="53520" data-letter="K">������</a><a href="/cell_phone_index/subcate57_52848_list_1.html" data-link="52848" data-letter="S">�ػ���</a><a href="/cell_phone_index/subcate57_50842_list_1.html" data-link="50842" data-letter="Q">ȫ��</a><a href="/cell_phone_index/subcate57_41933_list_1.html" data-link="41933" data-letter="B">�ٺ�</a><a href="/cell_phone_index/subcate57_40737_list_1.html" data-link="40737" data-letter="L">�ʽ�</a><a href="/cell_phone_index/subcate57_37585_list_1.html" data-link="37585" data-letter="H">����</a><a href="/cell_phone_index/subcate57_34927_list_1.html" data-link="34927" data-letter="Q">���</a><a href="/cell_phone_index/subcate57_41365_list_1.html" data-link="41365" data-letter="Y">�װ���</a><a href="/cell_phone_index/subcate57_51281_list_1.html" data-link="51281" data-letter="S">����</a><a href="/cell_phone_index/subcate57_36647_list_1.html" data-link="36647" data-letter="K">������ŵ</a><a href="/cell_phone_index/subcate57_51194_list_1.html" data-link="51194" data-letter="C">��ʯ</a><a href="/cell_phone_index/subcate57_51808_list_1.html" data-link="51808" data-letter="Y">����</a><a href="/cell_phone_index/subcate57_37438_list_1.html" data-link="37438" data-letter="Y">���N</a><a href="/cell_phone_index/subcate57_53521_list_1.html" data-link="53521" data-letter="B">����</a><a href="/cell_phone_index/subcate57_32512_list_1.html" data-link="32512" data-letter="D">���Ƶ���</a><a href="/cell_phone_index/subcate57_35102_list_1.html" data-link="35102" data-letter="N">�῭��</a><a href="/cell_phone_index/subcate57_51558_list_1.html" data-link="51558" data-letter="X">С����</a><a href="/cell_phone_index/subcate57_41107_list_1.html" data-link="41107" data-letter="C">����</a><a href="/cell_phone_index/subcate57_51978_list_1.html" data-link="51978" data-letter="L">�컢</a><a href="/cell_phone_index/subcate57_35415_list_1.html" data-link="35415" data-letter="G">GEMRY</a><a href="/cell_phone_index/subcate57_51107_list_1.html" data-link="51107" data-letter="K">����</a><a href="/cell_phone_index/subcate57_51576_list_1.html" data-link="51576" data-letter="A">Ant one</a><a href="/cell_phone_index/subcate57_34874_list_1.html" data-link="34874" data-letter="K">���δ�</a><a href="/cell_phone_index/subcate57_37263_list_1.html" data-link="37263" data-letter="M">������</a><a href="/cell_phone_index/subcate57_49477_list_1.html" data-link="49477" data-letter="Q">����</a><a href="/cell_phone_index/subcate57_49232_list_1.html" data-link="49232" data-letter="T">ͼ��</a><a href="/cell_phone_index/subcate57_35147_list_1.html" data-link="35147" data-letter="X">С����</a><a href="/cell_phone_index/subcate57_50865_list_1.html" data-link="50865" data-letter="T">;Ϊ</a><a href="/cell_phone_index/subcate57_36594_list_1.html" data-link="36594" data-letter="M">����</a><a href="/cell_phone_index/subcate57_355_list_1.html" data-link="355" data-letter="B">����</a><a href="/cell_phone_index/subcate57_49354_list_1.html" data-link="49354" data-letter="C">����ά</a><a href="/cell_phone_index/subcate57_51993_list_1.html" data-link="51993" data-letter="Y">����</a><a href="/cell_phone_index/subcate57_1528_list_1.html" data-link="1528" data-letter="F">��̩</a><a href="/cell_phone_index/subcate57_53979_list_1.html" data-link="53979" data-letter="C">����</a><a href="/cell_phone_index/subcate57_43188_list_1.html" data-link="43188" data-letter="B">BROR</a><a href="/cell_phone_index/subcate57_49221_list_1.html" data-link="49221" data-letter="Y">�����ǻ�</a><a href="/cell_phone_index/subcate57_51417_list_1.html" data-link="51417" data-letter="V">VANO</a><a href="/cell_phone_index/subcate57_35405_list_1.html" data-link="35405" data-letter="Y">��Ʒ</a><a href="/cell_phone_index/subcate57_33382_list_1.html" data-link="33382" data-letter="O">ŷ��</a></div>
                    <div class="multi-submit">
                        <a id="J_MultiLink" data-url-type="param" href="/cell_phone_index/subcate57_MANUPLACEHOLDER_list_1.html" class="multi-link" target="_self">ȷ��</a>
                        <span id="J_MultiCansel" data-url-type="param" data-manu="0" class="multi-cansel">ȡ��</span>
                    </div>
                </div>
            </div>
            <script>document.write("");</script>            	
		    <div id="priceItem" class="filter-item filter-price">
		<strong class="filter-type">�۸�</strong>
		<div id="J_ParamPrice" class="param-value-list">
									<span class="all active">����</span>

			            			<a href="/cell_phone_index/subcate57_list_0_1.html">500Ԫ����</a>
            			            			<a href="/cell_phone_index/subcate57_list_500_1.html">500-1000Ԫ</a>
            			            			<a href="/cell_phone_index/subcate57_list_1000_1.html">1000-1500Ԫ</a>
            			            			<a href="/cell_phone_index/subcate57_list_1500_1.html">1500-2000Ԫ</a>
            			            			<a href="/cell_phone_index/subcate57_list_2000_1.html">2000-3000Ԫ</a>
            			            			<a href="/cell_phone_index/subcate57_list_3000_1.html">3000-4000Ԫ</a>
            			            			<a href="/cell_phone_index/subcate57_list_4000_1.html">4000-5000Ԫ</a>
            			            			<a href="/cell_phone_index/subcate57_list_5000_1.html">5000Ԫ����</a>
            					</div>
		<a class="J_ViewMore view-more" data-target="J_ParamPrice" href="javascript:;" target="_self">����<i></i></a>
		<div class="price-self">
			<input id="minPrice" type="text">
			<em>-</em>
			<input id="maxPrice" type="text">
			<span id="subPri" class="price-button">ȷ��</span>
		</div>
	</div>

		                	<div id="pamItem1" class="filter-item">
        <strong class="filter-type">�����ߴ磺</strong>
        <div id="J_ParamItem1" class="param-value-list">
                        <span class="all active">����</span>

    			            			<a href="/cell_phone_index/subcate57_list_s5371_1.html">6.0Ӣ������</a>

						            			<a href="/cell_phone_index/subcate57_list_s6258_1.html">5.6-6.0Ӣ��</a>

						            			<a href="/cell_phone_index/subcate57_list_s7545_1.html">5.5Ӣ��</a>

						            			<a href="/cell_phone_index/subcate57_list_s5024_1.html">5.1-5.4Ӣ��</a>

						            			<a href="/cell_phone_index/subcate57_list_s5023_1.html">5.0Ӣ��</a>

						            			<a href="/cell_phone_index/subcate57_list_s4218_1.html">4.5-4.9Ӣ��</a>

						            			<a href="/cell_phone_index/subcate57_list_s1586_1.html">4.4Ӣ������</a>



			</div>
		<a class="J_ViewMore view-more" data-target="J_ParamItem1" href="javascript:;" target="_self">����<i></i></a>
    </div>
			                	<div id="pamItem2" class="filter-item">
        <strong class="filter-type">���磺</strong>
        <div id="J_ParamItem2" class="param-value-list">
                        <span class="all active">����</span>

    			            			<a class="icon-4g" data-tips="�ֻ�֧���ƶ�����ͨ������������Ӫ�����磬���Խ���ͨ��������" href="/cell_phone_index/subcate57_list_s6256_1.html">ȫ��ͨ</a>

						            			<a href="/cell_phone_index/subcate57_list_s5770_1.html">˫4G</a>

						            			<a class="icon-4g" data-tips="���Ų���2013��12��4����ʽ����4G TD-LTE�������գ��ƶ�/��ͨ/���ŷֱ���130MHz/40MHz/40MHzƵ����Դ" href="/cell_phone_index/subcate57_list_s5395_1.html">�ƶ�4G</a>

						            			<a href="/cell_phone_index/subcate57_list_s5396_1.html">��ͨ4G</a>

						            			<a href="/cell_phone_index/subcate57_list_s5547_1.html">����4G</a>

						            			<a class="icon-4g" data-tips="�������Ӧ���ֻ�����ʹ���ƶ�2G/3G������ͨ2G��" href="/cell_phone_index/subcate57_list_s895_1.html">�ƶ�3G</a>

						            			<a class="icon-4g" data-tips="ֻ֧�ִ����������£��ֻ�ֻ����ʹ�õ��ŵ�2G/3G��" href="/cell_phone_index/subcate57_list_s1293_1.html">����3G</a>

						            			<a class="icon-4g" data-tips="�������Ӧ���ֻ�����ʹ����ͨ2G/3G�����ƶ�2G��" href="/cell_phone_index/subcate57_list_s140_1.html">��ͨ3G</a>



			</div>
		<a class="J_ViewMore view-more" data-target="J_ParamItem2" href="javascript:;" target="_self">����<i></i></a>
    </div>
			                	<div id="pamItem3" class="filter-item">
        <strong class="filter-type">��������</strong>
        <div id="J_ParamItem3" class="param-value-list">
                        <span class="all active">����</span>

    			            			<a href="/cell_phone_index/subcate57_list_s6658_1.html">ʮ��</a>

						            			<a href="/cell_phone_index/subcate57_list_s5226_1.html">�˺�</a>

						            			<a href="/cell_phone_index/subcate57_list_s7347_1.html">����</a>

						            			<a href="/cell_phone_index/subcate57_list_s3594_1.html">�ĺ�</a>

						            			<a href="/cell_phone_index/subcate57_list_s3006_1.html">˫�˼�����</a>



			</div>
		<a class="J_ViewMore view-more" data-target="J_ParamItem3" href="javascript:;" target="_self">����<i></i></a>
    </div>
			                	<div id="pamItem4" class="filter-item">
        <strong class="filter-type">RAM������</strong>
        <div id="J_ParamItem4" class="param-value-list">
                        <span class="all active">����</span>

    			            			<a href="/cell_phone_index/subcate57_list_s7318_1.html">8GB</a>

						            			<a href="/cell_phone_index/subcate57_list_s6509_1.html">6GB</a>

						            			<a href="/cell_phone_index/subcate57_list_s6134_1.html">4GB</a>

						            			<a href="/cell_phone_index/subcate57_list_s5293_1.html">3GB</a>

						            			<a href="/cell_phone_index/subcate57_list_s4142_1.html">2GB</a>



			</div>
		<a class="J_ViewMore view-more" data-target="J_ParamItem4" href="javascript:;" target="_self">����<i></i></a>
    </div>
				<div id="J_MoreFilterItem" class="hide">
                    	<div id="pamItem5" class="filter-item">
        <strong class="filter-type">ROM������</strong>
        <div id="J_ParamItem5" class="param-value-list">
                        <span class="all active">����</span>

    			            			<a href="/cell_phone_index/subcate57_list_s7832_1.html">1TB</a>

						            			<a href="/cell_phone_index/subcate57_list_s7831_1.html">512GB</a>

						            			<a href="/cell_phone_index/subcate57_list_s7075_1.html">256GB</a>

						            			<a href="/cell_phone_index/subcate57_list_s6193_1.html">128GB</a>

						            			<a href="/cell_phone_index/subcate57_list_s4150_1.html">64GB</a>

						            			<a href="/cell_phone_index/subcate57_list_s4149_1.html">32GB</a>

						            			<a href="/cell_phone_index/subcate57_list_s4148_1.html">16GB</a>



			</div>
		<a class="J_ViewMore view-more" data-target="J_ParamItem5" href="javascript:;" target="_self">����<i></i></a>
    </div>
			                	<div id="pamItem6" class="filter-item">
        <strong class="filter-type">���ԣ�</strong>
        <div id="J_ParamItem6" class="param-value-list">
                        <span class="all active">����</span>

    			            			<a href="/cell_phone_index/subcate57_list_x10_1.html">ȫ����</a>

						            			<a href="/cell_phone_index/subcate57_list_x1_1.html">����Ļ</a>

						            			<a href="/cell_phone_index/subcate57_list_x2_1.html">���������</a>

						            			<a href="/cell_phone_index/subcate57_list_x3_1.html">�����ֻ�</a>

						            			<a href="/cell_phone_index/subcate57_list_x4_1.html">�����ֻ�</a>

						            			<a href="/cell_phone_index/subcate57_list_x11_1.html">˫��˫��</a>

						            			<a href="/cell_phone_index/subcate57_list_x8_1.html">2K��</a>

						            			<a href="/cell_phone_index/subcate57_list_x21_1.html">�沿ʶ��</a>

						            			<a href="/cell_phone_index/subcate57_list_x12_1.html">ָ��ʶ��</a>

						            			<a href="/cell_phone_index/subcate57_list_x22_1.html">˫���ֻ�</a>

						            			<a href="/cell_phone_index/subcate57_list_x19_1.html">��Ϸ�ֻ�</a>

						            			<a href="/cell_phone_index/subcate57_list_x18_1.html">������</a>

						            			<a href="/cell_phone_index/subcate57_list_x16_1.html">���˻�</a>

						            			<a href="/cell_phone_index/subcate57_list_x7_1.html">ǧԪ��</a>

						            			<a href="/cell_phone_index/subcate57_list_x13_1.html">�����ֻ�</a>

						            			<a href="/cell_phone_index/subcate57_list_x17_1.html">����˫��</a>

						            			<a href="/cell_phone_index/subcate57_list_x20_1.html">ǰ��˫��</a>



			</div>
		<a class="J_ViewMore view-more" data-target="J_ParamItem6" href="javascript:;" target="_self">����<i></i></a>
    </div>
			                	<div id="pamItem7" class="filter-item color-item">
        <strong class="filter-type">�����ɫ��</strong>
        <div id="J_ParamItem7" class="param-value-list">
                        <span class="all active">����</span>

    			<a href="/cell_phone_index/subcate57_list_c13_1.html" class="color" style="border:1px solid #dbdbdb; background-color:#ffffff;"></a>
						            			<a href="/cell_phone_index/subcate57_list_c13_1.html">��ɫ</a>

						<a href="/cell_phone_index/subcate57_list_c14_1.html" class="color" style="border:1px solid #000000; background-color:#000000;"></a>
						            			<a href="/cell_phone_index/subcate57_list_c14_1.html">��ɫ</a>

						<a href="/cell_phone_index/subcate57_list_c15_1.html" class="color" style="border:1px solid #cccccc; background-color:#cccccc;"></a>
						            			<a href="/cell_phone_index/subcate57_list_c15_1.html">����ɫ</a>

						<a href="/cell_phone_index/subcate57_list_c16_1.html" class="color" style="border:1px solid #5a3737; background-color:#5a3737;"></a>
						            			<a href="/cell_phone_index/subcate57_list_c16_1.html">����ɫ</a>

						<a href="/cell_phone_index/subcate57_list_c17_1.html" class="color" style="border:1px solid #ff0903; background-color:#ff0903;"></a>
						            			<a href="/cell_phone_index/subcate57_list_c17_1.html">��ɫ</a>

						<a href="/cell_phone_index/subcate57_list_c18_1.html" class="color" style="border:1px solid #ffcc99; background-color:#ffcc99;"></a>
						            			<a href="/cell_phone_index/subcate57_list_c18_1.html">��ɫ</a>

						<a href="/cell_phone_index/subcate57_list_c20_1.html" class="color" style="border:1px solid #660066; background-color:#660066;"></a>
						            			<a href="/cell_phone_index/subcate57_list_c20_1.html">��ɫ</a>

						<a href="/cell_phone_index/subcate57_list_c21_1.html" class="color" style="border:1px solid #3333ff; background-color:#3333ff;"></a>
						            			<a href="/cell_phone_index/subcate57_list_c21_1.html">��ɫ</a>

						<a href="/cell_phone_index/subcate57_list_c22_1.html" class="color" style="border:1px solid #ffcccc; background-color:#ffcccc;"></a>
						            			<a href="/cell_phone_index/subcate57_list_c22_1.html">��ɫ</a>

						<a href="/cell_phone_index/subcate57_list_c23_1.html" class="color" style="border:1px solid #ffff00; background-color:#ffff00;"></a>
						            			<a href="/cell_phone_index/subcate57_list_c23_1.html">��ɫ</a>

						<a href="/cell_phone_index/subcate57_list_c24_1.html" class="color" style="border:1px solid #ff6600; background-color:#ff6600;"></a>
						            			<a href="/cell_phone_index/subcate57_list_c24_1.html">��ɫ</a>

						<a href="/cell_phone_index/subcate57_list_c25_1.html" class="color" style="border:1px solid #66ff33; background-color:#66ff33;"></a>
						            			<a href="/cell_phone_index/subcate57_list_c25_1.html">��ɫ</a>



			</div>
		<a class="J_ViewMore view-more" data-target="J_ParamItem7" href="javascript:;" target="_self">����<i></i></a>
    </div>






















		<div class="filter-other">
		<strong class="filter-type">����������</strong>
		<ul id="J_otherItem" class="other-items">
						<li>
				<strong>�ֻ�����<i></i></strong>
				<div class="param-value-list other-items-list">
																												<span class="all active">����</span>
																																                                                        <a href="/cell_phone_index/subcate57_list_s528_1.html">4G</a>
                            																															                                                        <a href="/cell_phone_index/subcate57_list_s533_1.html">����</a>
                            																															                                                        <a href="/cell_phone_index/subcate57_list_s2508_1.html">����</a>
                            																															                                                        <a href="/cell_phone_index/subcate57_list_s3053_1.html">����</a>
                            																															                                                        <a href="/cell_phone_index/subcate57_list_s6523_1.html">���</a>
                            																															                                                        <a href="/cell_phone_index/subcate57_list_s526_1.html">����</a>
                            																															                                                        <a href="/cell_phone_index/subcate57_list_s2605_1.html">ƽ��</a>
                            																															                                                        <a href="/cell_phone_index/subcate57_list_s531_1.html">����</a>
                            																															                                                        <a href="/cell_phone_index/subcate57_list_s7291_1.html">��Ϸ</a>
                            																															                                                        <a href="/cell_phone_index/subcate57_list_s6618_1.html">����</a>
                            																						</div>
			</li>
						<li>
				<strong>�����ֱ���<i></i></strong>
				<div class="param-value-list other-items-list">
																												<span class="all active">����</span>
																																                                                        <a href="/cell_phone_index/subcate57_list_s6510_1.html">4K</a>
                            																															                                                        <a href="/cell_phone_index/subcate57_list_s5528_1.html">2K</a>
                            																															                                                        <a href="/cell_phone_index/subcate57_list_s4328_1.html">1080p</a>
                            																															                                                        <a href="/cell_phone_index/subcate57_list_s2042_1.html">720p</a>
                            																						</div>
			</li>
						<li>
				<strong>��Ļ�����ܶ�<i></i></strong>
				<div class="param-value-list other-items-list">
																												<span class="all active">����</span>
																																                                                        <a href="/cell_phone_index/subcate57_list_s6192_1.html">500ppi����</a>
                            																															                                                        <a href="/cell_phone_index/subcate57_list_s4691_1.html">400ppi��500ppi</a>
                            																															                                                        <a href="/cell_phone_index/subcate57_list_s4690_1.html">350ppi��399ppi</a>
                            																															                                                        <a href="/cell_phone_index/subcate57_list_s4689_1.html">300ppi��349ppi</a>
                            																															                                                        <a href="/cell_phone_index/subcate57_list_s4688_1.html">300ppi����</a>
                            																						</div>
			</li>
						<li>
				<strong>CPU�ͺ�<i></i></strong>
				<div class="param-value-list other-items-list">
																												<span class="all active">����</span>
																																                                                        <a href="/cell_phone_index/subcate57_list_s2615_1.html">��ͨCPU</a>
                            																															<span class="khl">(</span>                                                        <a href="/cell_phone_index/subcate57_list_s7546_1.html">����845</a>
                            																															                                                        <a href="/cell_phone_index/subcate57_list_s7289_1.html">����835</a>
                            																															                                                        <a href="/cell_phone_index/subcate57_list_s7049_1.html">����821</a>
                            																															                                                        <a href="/cell_phone_index/subcate57_list_s6475_1.html">����820</a>
                            																															                                                        <a href="/cell_phone_index/subcate57_list_s7798_1.html">����710</a>
                            																															                                                        <a href="/cell_phone_index/subcate57_list_s7338_1.html">����660</a>
                            																															                                                        <a href="/cell_phone_index/subcate57_list_s6307_1.html">����653</a>
                            																															                                                        <a href="/cell_phone_index/subcate57_list_s7786_1.html">����636</a>
                            																															                                                        <a href="/cell_phone_index/subcate57_list_s7547_1.html">����630</a>
                            																															                                                        <a href="/cell_phone_index/subcate57_list_s7290_1.html">����625</a>
                            							<span class="khr">)</span>																								                                                        <a href="/cell_phone_index/subcate57_list_s4639_1.html">������CPU</a>
                            																															<span class="khl">(</span>                                                        <a href="/cell_phone_index/subcate57_list_s7374_1.html">����x30</a>
                            																															                                                        <a href="/cell_phone_index/subcate57_list_s6659_1.html">����x25</a>
                            																															                                                        <a href="/cell_phone_index/subcate57_list_s6660_1.html">����x20</a>
                            							<span class="khr">)</span>																								                                                        <a href="/cell_phone_index/subcate57_list_s5744_1.html">��˼CPU</a>
                            																															<span class="khl">(</span>                                                        <a href="/cell_phone_index/subcate57_list_s7373_1.html">����970</a>
                            																															                                                        <a href="/cell_phone_index/subcate57_list_s6661_1.html">����960</a>
                            																															                                                        <a href="/cell_phone_index/subcate57_list_s7799_1.html">����710</a>
                            							<span class="khr">)</span>																								                                                        <a href="/cell_phone_index/subcate57_list_s3743_1.html">����CPU</a>
                            																															                                                        <a href="/cell_phone_index/subcate57_list_s3742_1.html">ƻ��CPU</a>
                            																						</div>
			</li>
						<li>
				<strong>����ϵͳ<i></i></strong>
				<div class="param-value-list other-items-list">
																												<span class="all active">����</span>
																																                                                        <a href="/cell_phone_index/subcate57_list_s1398_1.html">��׿Android</a>
                            																															<span class="khl">(</span>                                                        <a href="/cell_phone_index/subcate57_list_s7548_1.html">8.0�汾</a>
                            																															                                                        <a href="/cell_phone_index/subcate57_list_s7549_1.html">7.1�汾</a>
                            																															                                                        <a href="/cell_phone_index/subcate57_list_s7074_1.html">7.0�汾</a>
                            																															                                                        <a href="/cell_phone_index/subcate57_list_s6500_1.html">6.0�汾</a>
                            																															                                                        <a href="/cell_phone_index/subcate57_list_s6502_1.html">5.1�汾</a>
                            							<span class="khr">)</span>																								                                                        <a href="/cell_phone_index/subcate57_list_s3410_1.html">ƻ��iPhone</a>
                            																															<span class="khl">(</span>                                                        <a href="/cell_phone_index/subcate57_list_s7550_1.html">iOS11</a>
                            																															                                                        <a href="/cell_phone_index/subcate57_list_s7076_1.html">iOS10</a>
                            																															                                                        <a href="/cell_phone_index/subcate57_list_s6501_1.html">iOS9</a>
                            							<span class="khr">)</span>																								                                                        <a href="/cell_phone_index/subcate57_list_s7339_1.html">΢��</a>
                            																															<span class="khl">(</span>                                                        <a href="/cell_phone_index/subcate57_list_s7341_1.html">WP10</a>
                            																															                                                        <a href="/cell_phone_index/subcate57_list_s7340_1.html">WP8</a>
                            							<span class="khr">)</span>																								                                                        <a href="/cell_phone_index/subcate57_list_s1278_1.html">����ϵͳ</a>
                            																						</div>
			</li>
						<li>
				<strong>��������ͷ<i></i></strong>
				<div class="param-value-list other-items-list">
																												<span class="all active">����</span>
																																                                                        <a href="/cell_phone_index/subcate57_list_s6270_1.html">2000����������</a>
                            																															                                                        <a href="/cell_phone_index/subcate57_list_s5536_1.html">1600������</a>
                            																															                                                        <a href="/cell_phone_index/subcate57_list_s4340_1.html">1300������</a>
                            																															                                                        <a href="/cell_phone_index/subcate57_list_s7572_1.html">1200������</a>
                            																															                                                        <a href="/cell_phone_index/subcate57_list_s946_1.html">800������</a>
                            																															                                                        <a href="/cell_phone_index/subcate57_list_s450_1.html">700����������</a>
                            																						</div>
			</li>
						<li>
				<strong>ǰ������ͷ<i></i></strong>
				<div class="param-value-list other-items-list">
																												<span class="all active">����</span>
																																                                                        <a href="/cell_phone_index/subcate57_list_s7348_1.html">2000����������</a>
                            																															                                                        <a href="/cell_phone_index/subcate57_list_s7349_1.html">1600������</a>
                            																															                                                        <a href="/cell_phone_index/subcate57_list_s7321_1.html">1300������</a>
                            																															                                                        <a href="/cell_phone_index/subcate57_list_s5747_1.html">800������</a>
                            																															                                                        <a href="/cell_phone_index/subcate57_list_s5746_1.html">500������</a>
                            																															                                                        <a href="/cell_phone_index/subcate57_list_s4327_1.html">400����������</a>
                            																						</div>
			</li>
					</ul>
	</div>
			</div>




</div>

<div class="more-filter">
			<span id="J_MoreFilter" class="more-filter-button" data-on="0">����ѡ�ROM���������ԣ���<i></i></span>
		<a class="advanced-search" href="/cell_phone_advSearch/subcate57_1.html" target="_blank">[�߼�����]</a>
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
								<a class="active" href="/cell_phone_index/subcate57_list_1.html" title="�л�����ͼ" data-mode="2"><i class="pic-mode"></i></a>
								<a href="/cell_phone_index/subcate57_0_list_1_0_1_1_0_1.html" title="�л����б�" data-mode="1"><i class="list-mode"></i></a>
							</div>
						<span class="total">�� <b>1790</b> ��</span>
									<div class="sort">
								<span class="active"><em>����</em></span>
								<a href="/cell_phone_index/subcate57_0_list_1_0_9_2_0_1.html"   ><em>ʱ��</em><i class="down"></i></a>
								<a href="/cell_phone_index/subcate57_0_list_1_0_3_2_0_1.html"   title="�۸��ɵ͵���" ><em>�۸�</em><i class="up"></i></a>
								<a href="/cell_phone_index/subcate57_0_list_1_0_7_2_0_1.html"   title="�������ɸߵ���" ><em>������</em><i class="down"></i></a>
								<a href="/cell_phone_index/subcate57_0_list_1_0_5_2_0_1.html"   title="��Ʒ�����ɸߵ���" ><em>��Ʒ����</em><i class="down"></i></a>
								<a href="/cell_phone_index/subcate57_0_list_1_0_8_2_0_1.html"   title="�����ɸߵ���" ><em>����</em><i class="down"></i></a>
							</div>
            		</div>


				<div class="pic-mode-box">
    <div class="adSpace" id="list_list_prolist_1"   style="display:none;"><script>write_group_ad('list_list_prolist_1','4diqu_list_first_ad_s_57_m_0_{LOCATIONID}.inc#1price_search_list_first_s_57_m_0.inc#5price_search_list_first_s_57_m_0.inc#0price_search_list_first_s_57.inc',0,57,0);</script><script>ad_w();</script><script>ad_w();</script><script>ad_w();</script><script>ad_w();</script></div>    <ul id="J_PicMode" class="clearfix">
                 <li data-follow-id="p1185512" >
                        <a href="/cell_phone/index1185512.shtml" class="pic" target="_blank"><img width="220" height="165" .src="https://2f.zol-img.com.cn/product/191_220x165/739/ceMGSYkHizU6.jpg" alt="��Ϊnova 3��ȫ��ͨ��"></a>
            <h3><a href="/cell_phone/index1185512.shtml" title="��Ϊnova 3��ȫ��ͨ��AI���ģ�����������ָ��ʶ��������ͷ" target="_blank">��Ϊnova 3��ȫ��ͨ�� <span>AI���ģ�����������ָ��ʶ��������ͷ</span></a></h3>
            <div class="price-row">
                                                <span class="price-tip">�ο��ۣ�</span><span class="price price-normal"><b class="price-sign">��</b><b class="price-type">2799</b></span>								<div class="goods-promotion">
										<span class="J_PicModeTuan" data-url="http://www.zol.com/detail/cell_phone/huawei/31496877.html?skuId=13606354?spm=784.0" data-price="2477" data-rel="modeTuan">�Ź�</span>
																								</div>
            </div>

			<div class="comment-row">
				<span class="star"><em style="width:69%"></em></span>
                <span class="score">6.9</span>
                <em>|</em>
				<a class="comment-num" href="/1186/1185512/review.shtml" target="_blank">55�˵���</a>
				<a class="review-active-v4" target="_blank" href="http://detail.zol.com.cn/reviewActivity/ReviewActV9.html" title="�������£���Ʒ����">�������£���Ʒ����</a>
			</div>

						<div class="function-v3">
                                <label id="comp1185512" class="compare-btn" hide-focus="true" data-rel='1185512,��Ϊnova 3��ȫ��ͨ��,/cell_phone/index1185512.shtml,https://2f.zol-img.com.cn/product/191_80x60/739/ceMGSYkHizU6.jpg,57' title="���������ӵ��Աȿ���"><i></i>�Ա�</label>
            </div>
			<div class="merchant-row"></div>
						<div class="rank-row">
								<a href="http://top.zol.com.cn/compositor/57/cell_phone.html" target="_blank">�������е�<span>1</span>��</a>
							</div>
			        </li>
            <li data-follow-id="p1225806" >
                        <a href="/cell_phone/index1225806.shtml" class="pic" target="_blank"><img width="220" height="165" .src="https://2c.zol-img.com.cn/product/192_220x165/610/ceWgKT2LVJXDI.jpg" alt="OPPO R17��8GB RAM/ȫ��ͨ��"></a>
            <h3><a href="/cell_phone/index1225806.shtml" title="OPPO R17��8GB RAM/ȫ��ͨ�������Ļָ�ƣ�AI����ʶ��ARʵ�����������������ɲ���" target="_blank">OPPO R17��8GB RAM/ȫ��ͨ�� <span>�����Ļָ�ƣ�AI����ʶ��ARʵ�����������������ɲ���</span></a></h3>
            <div class="price-row">
                                                <span class="price-tip">�ο��ۣ�</span><span class="price price-normal"><b class="price-sign">��</b><b class="price-type">3499</b></span>								<div class="goods-promotion">
																								</div>
            </div>

			<div class="comment-row">
				<span class="star"><em style="width:95%"></em></span>
                <span class="score">9.5</span>
                <em>|</em>
				<a class="comment-num" href="/1226/1225806/review.shtml" target="_blank">107�˵���</a>
				<a class="review-active-v4" target="_blank" href="http://detail.zol.com.cn/reviewActivity/ReviewActV9.html" title="�������£���Ʒ����">�������£���Ʒ����</a>
			</div>

						<div class="function-v3">
                                <label id="comp1225806" class="compare-btn" hide-focus="true" data-rel='1225806,OPPO R17��8GB RAM/ȫ��ͨ��,/cell_phone/index1225806.shtml,https://2c.zol-img.com.cn/product/192_80x60/610/ceWgKT2LVJXDI.jpg,57' title="���������ӵ��Աȿ���"><i></i>�Ա�</label>
            </div>
			<div class="merchant-row"></div>
						<div class="rank-row">
								<a href="http://top.zol.com.cn/compositor/57/cell_phone.html" target="_blank">�������е�<span>2</span>��</a>
							</div>
			        </li>
            <li class="nth-child-3n" data-follow-id="p1227284" data-live>
                        <a href="/cell_phone/index1227284.shtml" class="pic" target="_blank"><img width="220" height="165" .src="https://2f.zol-img.com.cn/product/192_220x165/747/ce63frgxJFc5.jpg" alt="vivo X23��ȫ��ͨ��"></a>
            <h3><a href="/cell_phone/index1227284.shtml" title="vivo X23��ȫ��ͨ��3D��Ӱ�����ƣ��鶯ˮ���������Ĵ������Ļָ�ƣ�AI��Ӱ" target="_blank">vivo X23��ȫ��ͨ�� <span>3D��Ӱ�����ƣ��鶯ˮ���������Ĵ������Ļָ�ƣ�AI��Ӱ</span></a></h3>
            <div class="price-row">
                                                <span class="price-tip">�ο��ۣ�</span><span class="price price-normal"><b class="price-sign">��</b><b class="price-type">3498</b></span>								<div class="goods-promotion">
																								</div>
            </div>

			<div class="comment-row">
				<span class="star"><em style="width:94%"></em></span>
                <span class="score">9.4</span>
                <em>|</em>
				<a class="comment-num" href="/1228/1227284/review.shtml" target="_blank">236�˵���</a>
				<a class="review-active-v4" target="_blank" href="http://detail.zol.com.cn/reviewActivity/ReviewActV9.html" title="�������£���Ʒ����">�������£���Ʒ����</a>
			</div>

						<div class="function-v3">
                                <label id="comp1227284" class="compare-btn" hide-focus="true" data-rel='1227284,vivo X23��ȫ��ͨ��,/cell_phone/index1227284.shtml,https://2f.zol-img.com.cn/product/192_80x60/747/ce63frgxJFc5.jpg,57' title="���������ӵ��Աȿ���"><i></i>�Ա�</label>
            </div>
			<div class="merchant-row"></div>
						<div class="rank-row">
								<a href="http://top.zol.com.cn/compositor/57/cell_phone.html" target="_blank">�������е�<span>3</span>��</a>
							</div>
			        </li>
            <li class="nth-child-4n" data-follow-id="p1229519" data-live>
                        <a href="/cell_phone/index1229519.shtml" class="pic" target="_blank"><img width="220" height="165" .src="https://2a.zol-img.com.cn/product/192_220x165/114/ceu5ISnPU1bo.jpg" alt="ƻ��iPhone XS��ȫ��ͨ��"></a>
            <h3><a href="/cell_phone/index1229519.shtml" title="ƻ��iPhone XS��ȫ��ͨ��������Ĥ��ʾ��������˫�㣬ƻ�� A12������" target="_blank">ƻ��iPhone XS��ȫ��ͨ�� <span>������Ĥ��ʾ��������˫�㣬ƻ�� A12������</span></a></h3>
            <div class="price-row">
                                                <span class="price-tip">�ο��ۣ�</span><span class="price price-normal"><b class="price-sign">��</b><b class="price-type">8699</b></span>								<div class="goods-promotion">
																								</div>
            </div>

			<div class="comment-row">
				<span class="star"><em style="width:61%"></em></span>
                <span class="score">6.1</span>
                <em>|</em>
				<a class="comment-num" href="/1230/1229519/review.shtml" target="_blank">33�˵���</a>
				<a class="review-active-v4" target="_blank" href="http://detail.zol.com.cn/reviewActivity/ReviewActV9.html" title="�������£���Ʒ����">�������£���Ʒ����</a>
			</div>

						<div class="function-v3">
                                <label id="comp1229519" class="compare-btn" hide-focus="true" data-rel='1229519,ƻ��iPhone XS��ȫ��ͨ��,/cell_phone/index1229519.shtml,https://2a.zol-img.com.cn/product/192_80x60/114/ceu5ISnPU1bo.jpg,57' title="���������ӵ��Աȿ���"><i></i>�Ա�</label>
            </div>
			<div class="merchant-row"></div>
						<div class="rank-row">
								<a href="http://top.zol.com.cn/compositor/57/cell_phone.html" target="_blank">�������е�<span>4</span>��</a>
							</div>
			        </li>
            <li data-follow-id="p1205469" >
                        <a href="/cell_phone/index1205469.shtml" class="pic" target="_blank"><img width="220" height="165" .src="https://2b.zol-img.com.cn/product/191_220x165/933/ceeRbjMDb5zFg.jpg" alt="һ��6��8GB RAM/ȫ��ͨ��"></a>
            <h3><a href="/cell_phone/index1205469.shtml" title="һ��6��8GB RAM/ȫ��ͨ���沿������ָ��ʶ��19:9ȫ������ȫ��������" target="_blank">һ��6��8GB RAM/ȫ��ͨ�� <span>�沿������ָ��ʶ��19:9ȫ������ȫ��������</span></a></h3>
            <div class="price-row">
                                                <span class="price-tip">�ο��ۣ�</span><span class="price price-normal"><b class="price-sign">��</b><b class="price-type">3599</b></span>								<div class="goods-promotion">
																								</div>
            </div>

			<div class="comment-row">
				<span class="star"><em style="width:85%"></em></span>
                <span class="score">8.5</span>
                <em>|</em>
				<a class="comment-num" href="/1206/1205469/review.shtml" target="_blank">327�˵���</a>
				<a class="review-active-v4" target="_blank" href="http://detail.zol.com.cn/reviewActivity/ReviewActV9.html" title="�������£���Ʒ����">�������£���Ʒ����</a>
			</div>

						<div class="function-v3">
                                <label id="comp1205469" class="compare-btn" hide-focus="true" data-rel='1205469,һ��6��8GB RAM/ȫ��ͨ��,/cell_phone/index1205469.shtml,https://2b.zol-img.com.cn/product/191_80x60/933/ceeRbjMDb5zFg.jpg,57' title="���������ӵ��Աȿ���"><i></i>�Ա�</label>
            </div>
			<div class="merchant-row"></div>
						<div class="rank-row">
								<a href="http://top.zol.com.cn/compositor/57/cell_phone.html" target="_blank">�������е�<span>5</span>��</a>
							</div>
			        </li>
            <li class="nth-child-3n" data-follow-id="p1212228" >
                        <a href="/cell_phone/index1212228.shtml" class="pic" target="_blank"><img width="220" height="165" .src="https://2d.zol-img.com.cn/product/192_220x165/907/cecakNAv3dQ.jpg" alt="����16th��6GB RAM/ȫ��ͨ��"></a>
            <h3><a href="/cell_phone/index1212228.shtml" title="����16th��6GB RAM/ȫ��ͨ��CD���������ʣ�������3D����������Ļָ��ʶ��Һ��ͭ��ɢ��" target="_blank">����16th��6GB RAM/ȫ��ͨ�� <span>CD���������ʣ�������3D����������Ļָ��ʶ��Һ��ͭ��ɢ��</span></a></h3>
            <div class="price-row">
                                                <span class="price-tip">�ο��ۣ�</span><span class="price price-normal"><b class="price-sign">��</b><b class="price-type">2698</b></span>								<div class="goods-promotion">
																								</div>
            </div>

			<div class="comment-row">
				<span class="star"><em style="width:69%"></em></span>
                <span class="score">6.9</span>
                <em>|</em>
				<a class="comment-num" href="/1213/1212228/review.shtml" target="_blank">196�˵���</a>
				<a class="review-active-v4" target="_blank" href="http://detail.zol.com.cn/reviewActivity/ReviewActV9.html" title="�������£���Ʒ����">�������£���Ʒ����</a>
			</div>

						<div class="function-v3">
                                <label id="comp1212228" class="compare-btn" hide-focus="true" data-rel='1212228,����16th��6GB RAM/ȫ��ͨ��,/cell_phone/index1212228.shtml,https://2d.zol-img.com.cn/product/192_80x60/907/cecakNAv3dQ.jpg,57' title="���������ӵ��Աȿ���"><i></i>�Ա�</label>
            </div>
			<div class="merchant-row"></div>
						<div class="rank-row">
								<a href="http://top.zol.com.cn/compositor/57/cell_phone.html" target="_blank">�������е�<span>6</span>��</a>
							</div>
			        </li>
            <li data-follow-id="p1213467" >
            <span class='award corner-icon-chinajoy2018'></span>            <a href="/cell_phone/index1213467.shtml" class="pic" target="_blank"><img width="220" height="165" .src="https://2b.zol-img.com.cn/product/191_220x165/573/cecLniZRe61iI.jpg" alt="OPPO Find X����׼��/ȫ��ͨ��"></a>
            <h3><a href="/cell_phone/index1213467.shtml" title="OPPO Find X����׼��/ȫ��ͨ��˫������������ȫ����ʽ3D����ͷ��VOOC���䣬3D�沿ʶ��" target="_blank">OPPO Find X����׼��/ȫ��ͨ�� <span>˫������������ȫ����ʽ3D����ͷ��VOOC���䣬3D�沿ʶ��</span></a></h3>
            <div class="price-row">
                                                <span class="price-tip">�ο��ۣ�</span><span class="price price-normal"><b class="price-sign">��</b><b class="price-type">4999</b></span>								<div class="goods-promotion">
																								</div>
            </div>

			<div class="comment-row">
				<span class="star"><em style="width:95%"></em></span>
                <span class="score">9.5</span>
                <em>|</em>
				<a class="comment-num" href="/1214/1213467/review.shtml" target="_blank">747�˵���</a>
				<a class="review-active-v4" target="_blank" href="http://detail.zol.com.cn/reviewActivity/ReviewActV9.html" title="�������£���Ʒ����">�������£���Ʒ����</a>
			</div>

						<div class="function-v3">
                                <label id="comp1213467" class="compare-btn" hide-focus="true" data-rel='1213467,OPPO Find X����׼��/ȫ��ͨ��,/cell_phone/index1213467.shtml,https://2b.zol-img.com.cn/product/191_80x60/573/cecLniZRe61iI.jpg,57' title="���������ӵ��Աȿ���"><i></i>�Ա�</label>
            </div>
			<div class="merchant-row"></div>
						<div class="rank-row">
								<a href="http://top.zol.com.cn/compositor/57/cell_phone.html" target="_blank">�������е�<span>7</span>��</a>
							</div>
			        </li>
            <li class="nth-child-4n" data-follow-id="p1182639" >
                        <a href="/cell_phone/index1182639.shtml" class="pic" target="_blank"><img width="220" height="165" .src="https://2a.zol-img.com.cn/product/186_220x165/536/cet1hjPNo0d6Q.jpg" alt="ƻ��iPhone X��ȫ��ͨ��"></a>
            <h3><a href="/cell_phone/index1182639.shtml" title="ƻ��iPhone X��ȫ��ͨ�����߳�磬����ID������˫�㣬ȫ����" target="_blank">ƻ��iPhone X��ȫ��ͨ�� <span>���߳�磬����ID������˫�㣬ȫ����</span></a></h3>
            <div class="price-row">
                                                <span class="price-tip">�ο��ۣ�</span><span class="price price-normal"><b class="price-sign">��</b><b class="price-type">6898</b></span>								<div class="goods-promotion">
																								</div>
            </div>

			<div class="comment-row">
				<span class="star"><em style="width:80%"></em></span>
                <span class="score">8.0</span>
                <em>|</em>
				<a class="comment-num" href="/1183/1182639/review.shtml" target="_blank">186�˵���</a>
				<a class="review-active-v4" target="_blank" href="http://detail.zol.com.cn/reviewActivity/ReviewActV9.html" title="�������£���Ʒ����">�������£���Ʒ����</a>
			</div>

						<div class="function-v3">
                                <label id="comp1182639" class="compare-btn" hide-focus="true" data-rel='1182639,ƻ��iPhone X��ȫ��ͨ��,/cell_phone/index1182639.shtml,https://2a.zol-img.com.cn/product/186_80x60/536/cet1hjPNo0d6Q.jpg,57' title="���������ӵ��Աȿ���"><i></i>�Ա�</label>
            </div>
			<div class="merchant-row"></div>
						<div class="rank-row">
								<a href="http://top.zol.com.cn/compositor/57/cell_phone.html" target="_blank">�������е�<span>9</span>��</a>
							</div>
			        </li>
            <li class="nth-child-3n" data-follow-id="p1207038" >
            <span class='award corner-icon-chinajoy2018'></span>            <a href="/cell_phone/index1207038.shtml" class="pic" target="_blank"><img width="220" height="165" .src="https://2e.zol-img.com.cn/product/190_220x165/910/cepZEfKxGBcY.jpg" alt="��ΪP20 Pro��6GB RAM/ȫ��ͨ��"></a>
            <h3><a href="/cell_phone/index1207038.shtml" title="��ΪP20 Pro��6GB RAM/ȫ��ͨ��4000���⿨���㣬AI��Ӱ������ȫ������ָ��ʶ��" target="_blank">��ΪP20 Pro��6GB RAM/ȫ��ͨ�� <span>4000���⿨���㣬AI��Ӱ������ȫ������ָ��ʶ��</span></a></h3>
            <div class="price-row">
                                                <span class="price-tip">�ο��ۣ�</span><span class="price price-normal"><b class="price-sign">��</b><b class="price-type">4488</b></span>								<div class="goods-promotion">
										<span class="J_PicModeTuan" data-url="http://www.zol.com/detail/cell_phone/huawei/31001890.html?skuId=12912671?spm=784.0" data-price="3869" data-rel="modeTuan">�Ź�</span>
																								</div>
            </div>

			<div class="comment-row">
				<span class="star"><em style="width:82%"></em></span>
                <span class="score">8.2</span>
                <em>|</em>
				<a class="comment-num" href="/1208/1207038/review.shtml" target="_blank">80�˵���</a>
				<a class="review-active-v4" target="_blank" href="http://detail.zol.com.cn/reviewActivity/ReviewActV9.html" title="�������£���Ʒ����">�������£���Ʒ����</a>
			</div>

						<div class="function-v3">
                                <label id="comp1207038" class="compare-btn" hide-focus="true" data-rel='1207038,��ΪP20 Pro��6GB RAM/ȫ��ͨ��,/cell_phone/index1207038.shtml,https://2e.zol-img.com.cn/product/190_80x60/910/cepZEfKxGBcY.jpg,57' title="���������ӵ��Աȿ���"><i></i>�Ա�</label>
            </div>
			<div class="merchant-row"></div>
						<div class="rank-row">
								<a href="http://top.zol.com.cn/compositor/57/cell_phone.html" target="_blank">�������е�<span>8</span>��</a>
							</div>
			        </li>
            <li data-follow-id="p1219823" >
            <span class='award corner-icon-chinajoy2018'></span>            <a href="/cell_phone/index1219823.shtml" class="pic" target="_blank"><img width="220" height="165" .src="https://2a.zol-img.com.cn/product/191_220x165/566/ceRo14zJK4flI.jpg" alt="vivo NEX�콢�棨ȫ��ͨ��"></a>
            <h3><a href="/cell_phone/index1219823.shtml" title="vivo NEX�콢�棨ȫ��ͨ��AI�ǻ�˫�㣬���ȫ����������ʽǰ������ͷ����Ļָ�ƽ���3.0" target="_blank">vivo NEX�콢�棨ȫ��ͨ�� <span>AI�ǻ�˫�㣬���ȫ����������ʽǰ������ͷ����Ļָ�ƽ���3.0</span></a></h3>
            <div class="price-row">
                                                <span class="price-tip">�ο��ۣ�</span><span class="price price-normal"><b class="price-sign">��</b><b class="price-type">4298</b></span>								<div class="goods-promotion">
																								</div>
            </div>

			<div class="comment-row">
				<span class="star"><em style="width:95%"></em></span>
                <span class="score">9.5</span>
                <em>|</em>
				<a class="comment-num" href="/1220/1219823/review.shtml" target="_blank">644�˵���</a>
				<a class="review-active-v4" target="_blank" href="http://detail.zol.com.cn/reviewActivity/ReviewActV9.html" title="�������£���Ʒ����">�������£���Ʒ����</a>
			</div>

						<div class="function-v3">
                                <label id="comp1219823" class="compare-btn" hide-focus="true" data-rel='1219823,vivo NEX�콢�棨ȫ��ͨ��,/cell_phone/index1219823.shtml,https://2a.zol-img.com.cn/product/191_80x60/566/ceRo14zJK4flI.jpg,57' title="���������ӵ��Աȿ���"><i></i>�Ա�</label>
            </div>
			<div class="merchant-row"></div>
						<div class="rank-row">
								<a href="http://top.zol.com.cn/compositor/57/cell_phone.html" target="_blank">�������е�<span>10</span>��</a>
							</div>
			        </li>
                    <script>
                    document.write("<li class=\" item-sale\" style=\"position:relative;\"><a rel='nofollow' href=\"http://tuan.zol.com/index.php?c=List&a=DanPinTuan&cid=1?spm=748.0\" target=\"_blank\"><img src=\"https://mercrt-fd.zol-img.com.cn/t_s220x300/g5/M00/0E/01/ChMkJ1tOp_GIHL0rAAA_h5BSKlMAApy4wAtXVwAAD-f115.jpg\" width=\"220\" height=\"300\"></a><span style=\"position: absolute; left: 0px; bottom: 0px; width: 29px; height: 16px; background-image: url(https://pic.zol-img.com.cn/201510/thisad_1016.png); background-position: initial initial; background-repeat: no-repeat no-repeat;\"></span></li>");
                </script>
				        <li class="nth-child-3n nth-child-4n" data-follow-id="p1175779" >
                        <a href="/cell_phone/index1175779.shtml" class="pic" target="_blank"><img width="220" height="165" .src="https://2c.zol-img.com.cn/product/190_220x165/902/cee1PflmqGzIw.jpg" alt="��ΪP20��ȫ��ͨ��"></a>
            <h3><a href="/cell_phone/index1175779.shtml" title="��ΪP20��ȫ��ͨ����������AI��Ӱ������ȫ������ָ��ʶ��" target="_blank">��ΪP20��ȫ��ͨ�� <span>��������AI��Ӱ������ȫ������ָ��ʶ��</span></a></h3>
            <div class="price-row">
                                                <span class="price-tip">�ο��ۣ�</span><span class="price price-normal"><b class="price-sign">��</b><b class="price-type">3388</b></span>								<div class="goods-promotion">
										<span class="J_PicModeTuan" data-url="http://www.zol.com/detail/cell_phone/huawei/31001878.html?skuId=12912691?spm=784.0" data-price="2899" data-rel="modeTuan">�Ź�</span>
																								</div>
            </div>

			<div class="comment-row">
				<span class="star"><em style="width:86%"></em></span>
                <span class="score">8.6</span>
                <em>|</em>
				<a class="comment-num" href="/1176/1175779/review.shtml" target="_blank">101�˵���</a>
				<a class="review-active-v4" target="_blank" href="http://detail.zol.com.cn/reviewActivity/ReviewActV9.html" title="�������£���Ʒ����">�������£���Ʒ����</a>
			</div>

						<div class="function-v3">
                                <label id="comp1175779" class="compare-btn" hide-focus="true" data-rel='1175779,��ΪP20��ȫ��ͨ��,/cell_phone/index1175779.shtml,https://2c.zol-img.com.cn/product/190_80x60/902/cee1PflmqGzIw.jpg,57' title="���������ӵ��Աȿ���"><i></i>�Ա�</label>
            </div>
			<div class="merchant-row"></div>
						<div class="rank-row">
								<a href="http://top.zol.com.cn/compositor/57/cell_phone.html" target="_blank">�������е�<span>11</span>��</a>
							</div>
			        </li>
            <li data-follow-id="p1205394" data-live>
                        <a href="/cell_phone/index1205394.shtml" class="pic" target="_blank"><img width="220" height="165" .src="https://2e.zol-img.com.cn/product/192_220x165/118/ceOwvk3XMlXeg.jpg" alt="ƻ��iPhone XR��ȫ��ͨ��"></a>
            <h3><a href="/cell_phone/index1205394.shtml" title="ƻ��iPhone XR��ȫ��ͨ��" target="_blank">ƻ��iPhone XR��ȫ��ͨ�� <span>�����ߴ�:6.1Ӣ�� ����ϵͳ:iOS 12 ��������:LCD �����ֱ���:1792x828���� ��Ļ�����ܶ�:324ppi 4G����:�ƶ�TD-LTE����ͨTD-LTE����ͨFDD-LTE������TD-LTE������FDD-LTE</span></a></h3>
            <div class="price-row">
                                                <span class="price-tip">�ο��ۣ�</span><span class="price price-normal"><b class="price-sign">��</b><b class="price-type">6499</b></span>								<div class="goods-promotion">
																								</div>
            </div>

			<div class="comment-row">
				<span class="star"><em style="width:44%"></em></span>
                <span class="score">4.4</span>
                <em>|</em>
				<a class="comment-num" href="/1206/1205394/review.shtml" target="_blank">27�˵���</a>
				<a class="review-active-v4" target="_blank" href="http://detail.zol.com.cn/reviewActivity/ReviewActV9.html" title="�������£���Ʒ����">�������£���Ʒ����</a>
			</div>

						<div class="function-v3">
                                <label id="comp1205394" class="compare-btn" hide-focus="true" data-rel='1205394,ƻ��iPhone XR��ȫ��ͨ��,/cell_phone/index1205394.shtml,https://2e.zol-img.com.cn/product/192_80x60/118/ceOwvk3XMlXeg.jpg,57' title="���������ӵ��Աȿ���"><i></i>�Ա�</label>
            </div>
			<div class="merchant-row"></div>
						<div class="rank-row">
								<a href="http://top.zol.com.cn/compositor/57/cell_phone.html" target="_blank">�������е�<span>12</span>��</a>
							</div>
			        </li>
            <li data-follow-id="p1203409" >
                        <a href="/cell_phone/index1203409.shtml" class="pic" target="_blank"><img width="220" height="165" .src="https://2e.zol-img.com.cn/product/192_220x165/660/ceUdiJ2ZsfE.jpg" alt="ƻ��iPhone 9��ȫ��ͨ��"></a>
            <h3><a href="/cell_phone/index1203409.shtml" title="ƻ��iPhone 9��ȫ��ͨ��" target="_blank">ƻ��iPhone 9��ȫ��ͨ�� <span>�����ߴ�:6.2Ӣ�� ����ϵͳ:iOS 12 �����ֱ���:2160x1080���� 4G����:�ƶ�TD-LTE����ͨTD-LTE����ͨFDD-LTE������TD-LTE������FDD-LTE CPU�ͺ�:ƻ�� A12 ������:�˺� RAM����:4GB</span></a></h3>
            <div class="price-row">
                                                <span class="price price-cp"><b class="price-type">�����Ʒ</b></span>								<div class="goods-promotion">
																								</div>
            </div>

			<div class="comment-row">
				<span class="star"><em style="width:63%"></em></span>
                <span class="score">6.3</span>
                <em>|</em>
				<a class="comment-num" href="/1204/1203409/review.shtml" target="_blank">23�˵���</a>
				<a class="review-active-v4" target="_blank" href="http://detail.zol.com.cn/reviewActivity/ReviewActV9.html" title="�������£���Ʒ����">�������£���Ʒ����</a>
			</div>

						<div class="function-v3">
                                <label id="comp1203409" class="compare-btn" hide-focus="true" data-rel='1203409,ƻ��iPhone 9��ȫ��ͨ��,/cell_phone/index1203409.shtml,https://2e.zol-img.com.cn/product/192_80x60/660/ceUdiJ2ZsfE.jpg,57' title="���������ӵ��Աȿ���"><i></i>�Ա�</label>
            </div>
			<div class="merchant-row"></div>
						<div class="rank-row">
								<a href="http://top.zol.com.cn/compositor/57/cell_phone.html" target="_blank">�������е�<span>14</span>��</a>
							</div>
			        </li>
            <li class="nth-child-3n" data-follow-id="p1208704" >
                        <a href="/cell_phone/index1208704.shtml" class="pic" target="_blank"><img width="220" height="165" .src="https://2b.zol-img.com.cn/product/191_220x165/921/ceOFxxMDoCBA.jpg" alt="vivo X21��ȫ��ͨ��"></a>
            <h3><a href="/cell_phone/index1208704.shtml" title="vivo X21��ȫ��ͨ���˹����ܣ�Jovi AI��ȫ�������������" target="_blank">vivo X21��ȫ��ͨ�� <span>�˹����ܣ�Jovi AI��ȫ�������������</span></a></h3>
            <div class="price-row">
                                                <span class="price-tip">�ο��ۣ�</span><span class="price price-normal"><b class="price-sign">��</b><b class="price-type">2498</b></span>								<div class="goods-promotion">
										<span class="J_PicModeTuan" data-url="http://www.zol.com/detail/cell_phone/vivo/31062623.html?skuId=13714062?spm=784.0" data-price="2099" data-rel="modeTuan">�Ź�</span>
																								</div>
            </div>

			<div class="comment-row">
				<span class="star"><em style="width:91%"></em></span>
                <span class="score">9.1</span>
                <em>|</em>
				<a class="comment-num" href="/1209/1208704/review.shtml" target="_blank">554�˵���</a>
				<a class="review-active-v4" target="_blank" href="http://detail.zol.com.cn/reviewActivity/ReviewActV9.html" title="�������£���Ʒ����">�������£���Ʒ����</a>
			</div>

						<div class="function-v3">
                                <label id="comp1208704" class="compare-btn" hide-focus="true" data-rel='1208704,vivo X21��ȫ��ͨ��,/cell_phone/index1208704.shtml,https://2b.zol-img.com.cn/product/191_80x60/921/ceOFxxMDoCBA.jpg,57' title="���������ӵ��Աȿ���"><i></i>�Ա�</label>
            </div>
			<div class="merchant-row"></div>
						<div class="rank-row">
								<a href="http://top.zol.com.cn/compositor/57/cell_phone.html" target="_blank">�������е�<span>13</span>��</a>
							</div>
			        </li>
            <li class="nth-child-4n" data-follow-id="p1213787" >
                        <a href="/cell_phone/index1213787.shtml" class="pic" target="_blank"><img width="220" height="165" .src="https://2d.zol-img.com.cn/product/191_220x165/557/cessHobf7QwFM.jpg" alt="С��8��6GB RAM/ȫ��ͨ��"></a>
            <h3><a href="/cell_phone/index1213787.shtml" title="С��8��6GB RAM/ȫ��ͨ��AI���������L1+L5˫Ƶ˫·��λ����������ʶ��AI ���й�˫��" target="_blank">С��8��6GB RAM/ȫ��ͨ�� <span>AI���������L1+L5˫Ƶ˫·��λ����������ʶ��AI ���й�˫��</span></a></h3>
            <div class="price-row">
                                                <span class="price-tip">�ο��ۣ�</span><span class="price price-normal"><b class="price-sign">��</b><b class="price-type">2599</b></span>								<div class="goods-promotion">
										<span class="J_PicModeTuan" data-url="http://www.zol.com/detail/cell_phone/xiaomi/31326768.html?skuId=13646731?spm=784.0" data-price="2528" data-rel="modeTuan">�Ź�</span>
																								</div>
            </div>

			<div class="comment-row">
				<span class="star"><em style="width:51%"></em></span>
                <span class="score">5.1</span>
                <em>|</em>
				<a class="comment-num" href="/1214/1213787/review.shtml" target="_blank">300�˵���</a>
				<a class="review-active-v4" target="_blank" href="http://detail.zol.com.cn/reviewActivity/ReviewActV9.html" title="�������£���Ʒ����">�������£���Ʒ����</a>
			</div>

						<div class="function-v3">
                                <label id="comp1213787" class="compare-btn" hide-focus="true" data-rel='1213787,С��8��6GB RAM/ȫ��ͨ��,/cell_phone/index1213787.shtml,https://2d.zol-img.com.cn/product/191_80x60/557/cessHobf7QwFM.jpg,57' title="���������ӵ��Աȿ���"><i></i>�Ա�</label>
            </div>
			<div class="merchant-row"></div>
						<div class="rank-row">
								<a href="http://top.zol.com.cn/compositor/57/cell_phone.html" target="_blank">�������е�<span>17</span>��</a>
							</div>
			        </li>
            <li data-follow-id="p1184309" >
                        <a href="/cell_phone/index1184309.shtml" class="pic" target="_blank"><img width="220" height="165" .src="https://2d.zol-img.com.cn/product/192_220x165/999/ce3tGDWGhyq6.jpg" alt="����GALAXY Note 9��6GB RAM/ȫ��ͨ��"></a>
            <h3><a href="/cell_phone/index1184309.shtml" title="����GALAXY Note 9��6GB RAM/ȫ��ͨ����ʯ�и�գ�S Pen����ģʽ������ Bibxy��Wi-Fi��LTE��ȫ��������" target="_blank">����GALAXY Note 9��6GB RAM/ȫ��ͨ�� <span>��ʯ�и�գ�S Pen����ģʽ������ Bibxy��Wi-Fi��LTE��ȫ��������</span></a></h3>
            <div class="price-row">
                                                <span class="price-tip">�ο��ۣ�</span><span class="price price-normal"><b class="price-sign">��</b><b class="price-type">6999</b></span>								<div class="goods-promotion">
																								</div>
            </div>

			<div class="comment-row">
				<span class="star"><em style="width:83%"></em></span>
                <span class="score">8.3</span>
                <em>|</em>
				<a class="comment-num" href="/1185/1184309/review.shtml" target="_blank">44�˵���</a>
				<a class="review-active-v4" target="_blank" href="http://detail.zol.com.cn/reviewActivity/ReviewActV9.html" title="�������£���Ʒ����">�������£���Ʒ����</a>
			</div>

						<div class="function-v3">
                                <label id="comp1184309" class="compare-btn" hide-focus="true" data-rel='1184309,����GALAXY Note 9��6GB RAM/ȫ��ͨ��,/cell_phone/index1184309.shtml,https://2d.zol-img.com.cn/product/192_80x60/999/ce3tGDWGhyq6.jpg,57' title="���������ӵ��Աȿ���"><i></i>�Ա�</label>
            </div>
			<div class="merchant-row"></div>
						<div class="rank-row">
								<a href="http://top.zol.com.cn/compositor/57/cell_phone.html" target="_blank">�������е�<span>15</span>��</a>
							</div>
			        </li>
            <li class="nth-child-3n" data-follow-id="p1229520" data-live>
                        <a href="/cell_phone/index1229520.shtml" class="pic" target="_blank"><img width="220" height="165" .src="https://2c.zol-img.com.cn/product/192_220x165/116/ceB2DF6b4D0s.jpg" alt="ƻ��iPhone XS Max��ȫ��ͨ��"></a>
            <h3><a href="/cell_phone/index1229520.shtml" title="ƻ��iPhone XS Max��ȫ��ͨ��������Ĥ��ʾ����˫��˫��������˫�㣬ƻ�� A12������" target="_blank">ƻ��iPhone XS Max��ȫ��ͨ�� <span>������Ĥ��ʾ����˫��˫��������˫�㣬ƻ�� A12������</span></a></h3>
            <div class="price-row">
                                                <span class="price-tip">�ο��ۣ�</span><span class="price price-normal"><b class="price-sign">��</b><b class="price-type">9599</b></span>								<div class="goods-promotion">
																								</div>
            </div>

			<div class="comment-row">
				<span class="star"><em style="width:66%"></em></span>
                <span class="score">6.6</span>
                <em>|</em>
				<a class="comment-num" href="/1230/1229520/review.shtml" target="_blank">18�˵���</a>
				<a class="review-active-v4" target="_blank" href="http://detail.zol.com.cn/reviewActivity/ReviewActV9.html" title="�������£���Ʒ����">�������£���Ʒ����</a>
			</div>

						<div class="function-v3">
                                <label id="comp1229520" class="compare-btn" hide-focus="true" data-rel='1229520,ƻ��iPhone XS Max��ȫ��ͨ��,/cell_phone/index1229520.shtml,https://2c.zol-img.com.cn/product/192_80x60/116/ceB2DF6b4D0s.jpg,57' title="���������ӵ��Աȿ���"><i></i>�Ա�</label>
            </div>
			<div class="merchant-row"></div>
						<div class="rank-row">
								<a href="http://top.zol.com.cn/compositor/57/cell_phone.html" target="_blank">�������е�<span>16</span>��</a>
							</div>
			        </li>
            <li data-follow-id="p1222342" >
                        <a href="/cell_phone/index1222342.shtml" class="pic" target="_blank"><img width="220" height="165" .src="https://2b.zol-img.com.cn/product/192_220x165/329/ceoplQ5Gua466.jpg" alt="��ҫNote10��6GB RAM/ȫ��ͨ��"></a>
            <h3><a href="/cell_phone/index1222342.shtml" title="��ҫNote10��6GB RAM/ȫ��ͨ��AI������ǿ��GPU Turbo��CPU Turbo��THE NINEҺ��ɢ��" target="_blank">��ҫNote10��6GB RAM/ȫ��ͨ�� <span>AI������ǿ��GPU Turbo��CPU Turbo��THE NINEҺ��ɢ��</span></a></h3>
            <div class="price-row">
                                                <span class="price-tip">�ο��ۣ�</span><span class="price price-normal"><b class="price-sign">��</b><b class="price-type">2799</b></span>								<div class="goods-promotion">
																								</div>
            </div>

			<div class="comment-row">
				<span class="star"><em style="width:88%"></em></span>
                <span class="score">8.8</span>
                <em>|</em>
				<a class="comment-num" href="/1223/1222342/review.shtml" target="_blank">39�˵���</a>
				<a class="review-active-v4" target="_blank" href="http://detail.zol.com.cn/reviewActivity/ReviewActV9.html" title="�������£���Ʒ����">�������£���Ʒ����</a>
			</div>

						<div class="function-v3">
                                <label id="comp1222342" class="compare-btn" hide-focus="true" data-rel='1222342,��ҫNote10��6GB RAM/ȫ��ͨ��,/cell_phone/index1222342.shtml,https://2b.zol-img.com.cn/product/192_80x60/329/ceoplQ5Gua466.jpg,57' title="���������ӵ��Աȿ���"><i></i>�Ա�</label>
            </div>
			<div class="merchant-row"></div>
						<div class="rank-row">
								<a href="http://top.zol.com.cn/compositor/57/cell_phone.html" target="_blank">�������е�<span>18</span>��</a>
							</div>
			        </li>
            <li class="nth-child-4n" data-follow-id="p1206990" >
                        <a href="/cell_phone/index1206990.shtml" class="pic" target="_blank"><img width="220" height="165" .src="https://2b.zol-img.com.cn/product/189_220x165/763/cedVwjOtfBbY.jpg" alt="OPPO R15��6GB RAM/ȫ��ͨ��"></a>
            <h3><a href="/cell_phone/index1206990.shtml" title="OPPO R15��6GB RAM/ȫ��ͨ��19:9����Ұȫ������˫�沣����ƣ�AI �������գ�VOOC����" target="_blank">OPPO R15��6GB RAM/ȫ��ͨ�� <span>19:9����Ұȫ������˫�沣����ƣ�AI �������գ�VOOC����</span></a></h3>
            <div class="price-row">
                                                <span class="price-tip">�ο��ۣ�</span><span class="price price-normal"><b class="price-sign">��</b><b class="price-type">2699</b></span>								<div class="goods-promotion">
																								</div>
            </div>

			<div class="comment-row">
				<span class="star"><em style="width:92%"></em></span>
                <span class="score">9.2</span>
                <em>|</em>
				<a class="comment-num" href="/1207/1206990/review.shtml" target="_blank">1052�˵���</a>
				<a class="review-active-v4" target="_blank" href="http://detail.zol.com.cn/reviewActivity/ReviewActV9.html" title="�������£���Ʒ����">�������£���Ʒ����</a>
			</div>

						<div class="function-v3">
                                <label id="comp1206990" class="compare-btn" hide-focus="true" data-rel='1206990,OPPO R15��6GB RAM/ȫ��ͨ��,/cell_phone/index1206990.shtml,https://2b.zol-img.com.cn/product/189_80x60/763/cedVwjOtfBbY.jpg,57' title="���������ӵ��Աȿ���"><i></i>�Ա�</label>
            </div>
			<div class="merchant-row"></div>
						<div class="rank-row">
								<a href="http://top.zol.com.cn/compositor/57/cell_phone.html" target="_blank">�������е�<span>19</span>��</a>
							</div>
			        </li>
            <li class="nth-child-3n" data-follow-id="p1221126" >
                        <a href="/cell_phone/index1221126.shtml" class="pic" target="_blank"><img width="220" height="165" .src="https://2b.zol-img.com.cn/product/191_220x165/731/ceIl6MFjoyY8k.jpg" alt="OPPO A5��ȫ��ͨ��"></a>
            <h3><a href="/cell_phone/index1221126.shtml" title="OPPO A5��ȫ��ͨ���沿ʶ��������ᣬOPPO������ȫ����" target="_blank">OPPO A5��ȫ��ͨ�� <span>�沿ʶ��������ᣬOPPO������ȫ����</span></a></h3>
            <div class="price-row">
                                                <span class="price-tip">�ο��ۣ�</span><span class="price price-normal"><b class="price-sign">��</b><b class="price-type">1500</b></span>								<div class="goods-promotion">
																								</div>
            </div>

			<div class="comment-row">
				<span class="star"><em style="width:87%"></em></span>
                <span class="score">8.7</span>
                <em>|</em>
				<a class="comment-num" href="/1222/1221126/review.shtml" target="_blank">303�˵���</a>
				<a class="review-active-v4" target="_blank" href="http://detail.zol.com.cn/reviewActivity/ReviewActV9.html" title="�������£���Ʒ����">�������£���Ʒ����</a>
			</div>

						<div class="function-v3">
                                <label id="comp1221126" class="compare-btn" hide-focus="true" data-rel='1221126,OPPO A5��ȫ��ͨ��,/cell_phone/index1221126.shtml,https://2b.zol-img.com.cn/product/191_80x60/731/ceIl6MFjoyY8k.jpg,57' title="���������ӵ��Աȿ���"><i></i>�Ա�</label>
            </div>
			<div class="merchant-row"></div>
						<div class="rank-row">
								<a href="http://top.zol.com.cn/compositor/57/cell_phone.html" target="_blank">�������е�<span>20</span>��</a>
							</div>
			        </li>
                    <script>
                    document.write("<li class=\" item-sale\" style=\"position:relative;\"><a rel='nofollow' href=\"http://www.zol.com/detail/cell_phone/rongyao/30708874.html?skuId=12356050&spm=921?spm=748.0\" target=\"_blank\"><img src=\"https://mercrt-fd.zol-img.com.cn/t_s220x300/g5/M00/0E/02/ChMkJ1tOrTGIU0pcAAA61LhpOKAAApy7QOsWTAAADrs696.jpg\" width=\"220\" height=\"300\"></a><span style=\"position: absolute; left: 0px; bottom: 0px; width: 29px; height: 16px; background-image: url(https://pic.zol-img.com.cn/201510/thisad_1016.png); background-position: initial initial; background-repeat: no-repeat no-repeat;\"></span></li>");
                </script>
				        <li data-follow-id="p1207689" >
                        <a href="/cell_phone/index1207689.shtml" class="pic" target="_blank"><img width="220" height="165" .src="https://2a.zol-img.com.cn/product/190_220x165/618/celLwSHVhvG9M.jpg" alt="��ҫ10��ȫ��ͨ��"></a>
            <h3><a href="/cell_phone/index1207689.shtml" title="��ҫ10��ȫ��ͨ����ɫ���ⲣ����ǰ������ʪ��ָ�ƽ�����2400��AI��Ӱ��ȫ����" target="_blank">��ҫ10��ȫ��ͨ�� <span>��ɫ���ⲣ����ǰ������ʪ��ָ�ƽ�����2400��AI��Ӱ��ȫ����</span></a></h3>
            <div class="price-row">
                                                <span class="price-tip">�ο��ۣ�</span><span class="price price-normal"><b class="price-sign">��</b><b class="price-type">2299</b></span>								<div class="goods-promotion">
										<span class="J_PicModeTuan" data-url="http://www.zol.com/detail/cell_phone/rongyao/31140055.html?skuId=12951598?spm=784.0" data-price="2249" data-rel="modeTuan">�Ź�</span>
																								</div>
            </div>

			<div class="comment-row">
				<span class="star"><em style="width:79%"></em></span>
                <span class="score">7.9</span>
                <em>|</em>
				<a class="comment-num" href="/1208/1207689/review.shtml" target="_blank">155�˵���</a>
				<a class="review-active-v4" target="_blank" href="http://detail.zol.com.cn/reviewActivity/ReviewActV9.html" title="�������£���Ʒ����">�������£���Ʒ����</a>
			</div>

						<div class="function-v3">
                                <label id="comp1207689" class="compare-btn" hide-focus="true" data-rel='1207689,��ҫ10��ȫ��ͨ��,/cell_phone/index1207689.shtml,https://2a.zol-img.com.cn/product/190_80x60/618/celLwSHVhvG9M.jpg,57' title="���������ӵ��Աȿ���"><i></i>�Ա�</label>
            </div>
			<div class="merchant-row"></div>
						<div class="rank-row">
								<a href="http://top.zol.com.cn/compositor/57/cell_phone.html" target="_blank">�������е�<span>21</span>��</a>
							</div>
			        </li>
            <li class="nth-child-3n nth-child-4n" data-follow-id="p1209676" data-live>
                        <a href="/cell_phone/index1209676.shtml" class="pic" target="_blank"><img width="220" height="165" .src="https://2b.zol-img.com.cn/product/192_220x165/883/ceIooc7zVhQQw.jpg" alt="��ҫ8X��4GB RAM/ȫ��ͨ��"></a>
            <h3><a href="/cell_phone/index1209676.shtml" title="��ҫ8X��4GB RAM/ȫ��ͨ��GPU Turbo��4D��У�AI��α��վ��AI����ģʽ��AI����" target="_blank">��ҫ8X��4GB RAM/ȫ��ͨ�� <span>GPU Turbo��4D��У�AI��α��վ��AI����ģʽ��AI����</span></a></h3>
            <div class="price-row">
                                                <span class="price-tip">�ο��ۣ�</span><span class="price price-normal"><b class="price-sign">��</b><b class="price-type">1399</b></span>								<div class="goods-promotion">
																								</div>
            </div>

			<div class="comment-row">
				<span class="star"><em style="width:63%"></em></span>
                <span class="score">6.3</span>
                <em>|</em>
				<a class="comment-num" href="/1210/1209676/review.shtml" target="_blank">17�˵���</a>
				<a class="review-active-v4" target="_blank" href="http://detail.zol.com.cn/reviewActivity/ReviewActV9.html" title="�������£���Ʒ����">�������£���Ʒ����</a>
			</div>

						<div class="function-v3">
                                <label id="comp1209676" class="compare-btn" hide-focus="true" data-rel='1209676,��ҫ8X��4GB RAM/ȫ��ͨ��,/cell_phone/index1209676.shtml,https://2b.zol-img.com.cn/product/192_80x60/883/ceIooc7zVhQQw.jpg,57' title="���������ӵ��Աȿ���"><i></i>�Ա�</label>
            </div>
			<div class="merchant-row"></div>
						<div class="rank-row">
								<a href="http://top.zol.com.cn/compositor/57/cell_phone.html" target="_blank">�������е�<span>22</span>��</a>
							</div>
			        </li>
            <li data-follow-id="p1225826" >
                        <a href="/cell_phone/index1225826.shtml" class="pic" target="_blank"><img width="220" height="165" .src="https://2a.zol-img.com.cn/product/192_220x165/438/ce5kSqjvJTxiI.jpg" alt="OPPO R17 Pro��ȫ��ͨ��"></a>
            <h3><a href="/cell_phone/index1225826.shtml" title="OPPO R17 Pro��ȫ��ͨ��Super VOOC���䣬TOF 3D��������ͷ��OPPO ARʵ�������������Ļָ��" target="_blank">OPPO R17 Pro��ȫ��ͨ�� <span>Super VOOC���䣬TOF 3D��������ͷ��OPPO ARʵ�������������Ļָ��</span></a></h3>
            <div class="price-row">
                                                 <span class="price-tip">�ο��ۣ�</span><span class="price price-na"><b class="price-sign">��</b><b class="price-type">4299</b><span class="price-status">[��������]</span></span>								<div class="goods-promotion">
																								</div>
            </div>

			<div class="comment-row">
				<span class="star"><em style="width:95%"></em></span>
                <span class="score">9.5</span>
                <em>|</em>
				<a class="comment-num" href="/1226/1225826/review.shtml" target="_blank">73�˵���</a>
				<a class="review-active-v4" target="_blank" href="http://detail.zol.com.cn/reviewActivity/ReviewActV9.html" title="�������£���Ʒ����">�������£���Ʒ����</a>
			</div>

						<div class="function-v3">
                                <label id="comp1225826" class="compare-btn" hide-focus="true" data-rel='1225826,OPPO R17 Pro��ȫ��ͨ��,/cell_phone/index1225826.shtml,https://2a.zol-img.com.cn/product/192_80x60/438/ce5kSqjvJTxiI.jpg,57' title="���������ӵ��Աȿ���"><i></i>�Ա�</label>
            </div>
			<div class="merchant-row"></div>
						<div class="rank-row">
								<a href="http://top.zol.com.cn/compositor/57/cell_phone.html" target="_blank">�������е�<span>47</span>��</a>
							</div>
			        </li>
            <li data-follow-id="p1215468" >
                        <a href="/cell_phone/index1215468.shtml" class="pic" target="_blank"><img width="220" height="165" .src="https://2f.zol-img.com.cn/product/191_220x165/741/ceM1LcyIUsgo.jpg" alt="��ҫPlay��4GB RAM/ȫ��ͨ��"></a>
            <h3><a href="/cell_phone/index1215468.shtml" title="��ҫPlay��4GB RAM/ȫ��ͨ��GPU Turbo���˹�����NPU��4D��Ϸ���飬�沿ʶ��" target="_blank">��ҫPlay��4GB RAM/ȫ��ͨ�� <span>GPU Turbo���˹�����NPU��4D��Ϸ���飬�沿ʶ��</span></a></h3>
            <div class="price-row">
                                                <span class="price-tip">�ο��ۣ�</span><span class="price price-normal"><b class="price-sign">��</b><b class="price-type">1799</b></span>								<div class="goods-promotion">
																								</div>
            </div>

			<div class="comment-row">
				<span class="star"><em style="width:58%"></em></span>
                <span class="score">5.8</span>
                <em>|</em>
				<a class="comment-num" href="/1216/1215468/review.shtml" target="_blank">103�˵���</a>
				<a class="review-active-v4" target="_blank" href="http://detail.zol.com.cn/reviewActivity/ReviewActV9.html" title="�������£���Ʒ����">�������£���Ʒ����</a>
			</div>

						<div class="function-v3">
                                <label id="comp1215468" class="compare-btn" hide-focus="true" data-rel='1215468,��ҫPlay��4GB RAM/ȫ��ͨ��,/cell_phone/index1215468.shtml,https://2f.zol-img.com.cn/product/191_80x60/741/ceM1LcyIUsgo.jpg,57' title="���������ӵ��Աȿ���"><i></i>�Ա�</label>
            </div>
			<div class="merchant-row"></div>
						<div class="rank-row">
								<a href="http://top.zol.com.cn/compositor/57/cell_phone.html" target="_blank">�������е�<span>24</span>��</a>
							</div>
			        </li>
            <li class="nth-child-3n" data-follow-id="p1182632" >
                        <a href="/cell_phone/index1182632.shtml" class="pic" target="_blank"><img width="220" height="165" .src="https://2f.zol-img.com.cn/product/186_220x165/325/ce06maMuqmn6c.jpg" alt="ƻ��iPhone 8 Plus��ȫ��ͨ��"></a>
            <h3><a href="/cell_phone/index1182632.shtml" title="ƻ��iPhone 8 Plus��ȫ��ͨ��˫�沣�������߳�磬Portrait Lighting������˫��" target="_blank">ƻ��iPhone 8 Plus��ȫ��ͨ�� <span>˫�沣�������߳�磬Portrait Lighting������˫��</span></a></h3>
            <div class="price-row">
                                                <span class="price-tip">�ο��ۣ�</span><span class="price price-normal"><b class="price-sign">��</b><b class="price-type">5468</b></span>								<div class="goods-promotion">
																								</div>
            </div>

			<div class="comment-row">
				<span class="star"><em style="width:85%"></em></span>
                <span class="score">8.5</span>
                <em>|</em>
				<a class="comment-num" href="/1183/1182632/review.shtml" target="_blank">79�˵���</a>
				<a class="review-active-v4" target="_blank" href="http://detail.zol.com.cn/reviewActivity/ReviewActV9.html" title="�������£���Ʒ����">�������£���Ʒ����</a>
			</div>

						<div class="function-v3">
                                <label id="comp1182632" class="compare-btn" hide-focus="true" data-rel='1182632,ƻ��iPhone 8 Plus��ȫ��ͨ��,/cell_phone/index1182632.shtml,https://2f.zol-img.com.cn/product/186_80x60/325/ce06maMuqmn6c.jpg,57' title="���������ӵ��Աȿ���"><i></i>�Ա�</label>
            </div>
			<div class="merchant-row"></div>
						<div class="rank-row">
								<a href="http://top.zol.com.cn/compositor/57/cell_phone.html" target="_blank">�������е�<span>23</span>��</a>
							</div>
			        </li>
            <li class="nth-child-4n" data-follow-id="p1213119" >
                        <a href="/cell_phone/index1213119.shtml" class="pic" target="_blank"><img width="220" height="165" .src="https://2e.zol-img.com.cn/product/192_220x165/410/cecJMeDBS7P9.jpg" alt="360 �ֻ�N7 Pro��ȫ��ͨ��"></a>
            <h3><a href="/cell_phone/index1213119.shtml" title="360 �ֻ�N7 Pro��ȫ��ͨ��������ͷ�����ٳ�磬ȫ������ָ��ʶ��" target="_blank">360 �ֻ�N7 Pro��ȫ��ͨ�� <span>������ͷ�����ٳ�磬ȫ������ָ��ʶ��</span></a></h3>
            <div class="price-row">
                                                <span class="price-tip">�ο��ۣ�</span><span class="price price-normal"><b class="price-sign">��</b><b class="price-type">1999</b></span>								<div class="goods-promotion">
																								</div>
            </div>

			<div class="comment-row">
				<span class="star"><em style="width:56%"></em></span>
                <span class="score">5.6</span>
                <em>|</em>
				<a class="comment-num" href="/1214/1213119/review.shtml" target="_blank">23�˵���</a>
				<a class="review-active-v4" target="_blank" href="http://detail.zol.com.cn/reviewActivity/ReviewActV9.html" title="�������£���Ʒ����">�������£���Ʒ����</a>
			</div>

						<div class="function-v3">
                                <label id="comp1213119" class="compare-btn" hide-focus="true" data-rel='1213119,360 �ֻ�N7 Pro��ȫ��ͨ��,/cell_phone/index1213119.shtml,https://2e.zol-img.com.cn/product/192_80x60/410/cecJMeDBS7P9.jpg,57' title="���������ӵ��Աȿ���"><i></i>�Ա�</label>
            </div>
			<div class="merchant-row"></div>
						<div class="rank-row">
								<a href="http://top.zol.com.cn/compositor/57/cell_phone.html" target="_blank">�������е�<span>25</span>��</a>
							</div>
			        </li>
            <li data-follow-id="p1211599" >
                        <a href="/cell_phone/index1211599.shtml" class="pic" target="_blank"><img width="220" height="165" .src="https://2e.zol-img.com.cn/product/190_220x165/122/cebTYLlwqfWX.jpg" alt="OPPO A3��ȫ��ͨ��"></a>
            <h3><a href="/cell_phone/index1211599.shtml" title="OPPO A3��ȫ��ͨ��128G���ڴ棬��ʯ������ƣ�����Ұȫ������AI�ǻ�����" target="_blank">OPPO A3��ȫ��ͨ�� <span>128G���ڴ棬��ʯ������ƣ�����Ұȫ������AI�ǻ�����</span></a></h3>
            <div class="price-row">
                                                <span class="price-tip">�ο��ۣ�</span><span class="price price-normal"><b class="price-sign">��</b><b class="price-type">1799</b></span>								<div class="goods-promotion">
																								</div>
            </div>

			<div class="comment-row">
				<span class="star"><em style="width:89%"></em></span>
                <span class="score">8.9</span>
                <em>|</em>
				<a class="comment-num" href="/1212/1211599/review.shtml" target="_blank">362�˵���</a>
				<a class="review-active-v4" target="_blank" href="http://detail.zol.com.cn/reviewActivity/ReviewActV9.html" title="�������£���Ʒ����">�������£���Ʒ����</a>
			</div>

						<div class="function-v3">
                                <label id="comp1211599" class="compare-btn" hide-focus="true" data-rel='1211599,OPPO A3��ȫ��ͨ��,/cell_phone/index1211599.shtml,https://2e.zol-img.com.cn/product/190_80x60/122/cebTYLlwqfWX.jpg,57' title="���������ӵ��Աȿ���"><i></i>�Ա�</label>
            </div>
			<div class="merchant-row"></div>
						<div class="rank-row">
								<a href="http://top.zol.com.cn/compositor/57/cell_phone.html" target="_blank">�������е�<span>27</span>��</a>
							</div>
			        </li>
            <li class="nth-child-3n" data-follow-id="p1215075" >
                        <a href="/cell_phone/index1215075.shtml" class="pic" target="_blank"><img width="220" height="165" .src="https://2d.zol-img.com.cn/product/191_220x165/587/cepwoMU3q3d0U.jpg" alt="vivo Z1��4GB RAM/ȫ��ͨ��"></a>
            <h3><a href="/cell_phone/index1215075.shtml" title="vivo Z1��4GB RAM/ȫ��ͨ���沿ʶ������660AIE�������������գ�ָ��ʶ��" target="_blank">vivo Z1��4GB RAM/ȫ��ͨ�� <span>�沿ʶ������660AIE�������������գ�ָ��ʶ��</span></a></h3>
            <div class="price-row">
                                                <span class="price-tip">�ο��ۣ�</span><span class="price price-normal"><b class="price-sign">��</b><b class="price-type">1598</b></span>								<div class="goods-promotion">
																								</div>
            </div>

			<div class="comment-row">
				<span class="star"><em style="width:89%"></em></span>
                <span class="score">8.9</span>
                <em>|</em>
				<a class="comment-num" href="/1216/1215075/review.shtml" target="_blank">43�˵���</a>
				<a class="review-active-v4" target="_blank" href="http://detail.zol.com.cn/reviewActivity/ReviewActV9.html" title="�������£���Ʒ����">�������£���Ʒ����</a>
			</div>

						<div class="function-v3">
                                <label id="comp1215075" class="compare-btn" hide-focus="true" data-rel='1215075,vivo Z1��4GB RAM/ȫ��ͨ��,/cell_phone/index1215075.shtml,https://2d.zol-img.com.cn/product/191_80x60/587/cepwoMU3q3d0U.jpg,57' title="���������ӵ��Աȿ���"><i></i>�Ա�</label>
            </div>
			<div class="merchant-row"></div>
						<div class="rank-row">
								<a href="http://top.zol.com.cn/compositor/57/cell_phone.html" target="_blank">�������е�<span>28</span>��</a>
							</div>
			        </li>
            <li data-follow-id="p1207608" >
                        <a href="/cell_phone/index1207608.shtml" class="pic" target="_blank"><img width="220" height="165" .src="https://2e.zol-img.com.cn/product/189_220x165/722/ceP4JLOWrGwMM.jpg" alt="��Ϊnova 3e��ȫ��ͨ��"></a>
            <h3><a href="/cell_phone/index1207608.shtml" title="��Ϊnova 3e��ȫ��ͨ������ʶ��19:9ȫ��������Ϸ���֣�������������" target="_blank">��Ϊnova 3e��ȫ��ͨ�� <span>����ʶ��19:9ȫ��������Ϸ���֣�������������</span></a></h3>
            <div class="price-row">
                                                <span class="price-tip">�ο��ۣ�</span><span class="price price-normal"><b class="price-sign">��</b><b class="price-type">1999</b></span>								<div class="goods-promotion">
																								</div>
            </div>

			<div class="comment-row">
				<span class="star"><em style="width:88%"></em></span>
                <span class="score">8.8</span>
                <em>|</em>
				<a class="comment-num" href="/1208/1207608/review.shtml" target="_blank">69�˵���</a>
				<a class="review-active-v4" target="_blank" href="http://detail.zol.com.cn/reviewActivity/ReviewActV9.html" title="�������£���Ʒ����">�������£���Ʒ����</a>
			</div>

						<div class="function-v3">
                                <label id="comp1207608" class="compare-btn" hide-focus="true" data-rel='1207608,��Ϊnova 3e��ȫ��ͨ��,/cell_phone/index1207608.shtml,https://2e.zol-img.com.cn/product/189_80x60/722/ceP4JLOWrGwMM.jpg,57' title="���������ӵ��Աȿ���"><i></i>�Ա�</label>
            </div>
			<div class="merchant-row"></div>
						<div class="rank-row">
								<a href="http://top.zol.com.cn/compositor/57/cell_phone.html" target="_blank">�������е�<span>31</span>��</a>
							</div>
			        </li>
            <li class="nth-child-4n" data-follow-id="p1222100" >
                        <a href="/cell_phone/index1222100.shtml" class="pic" target="_blank"><img width="220" height="165" .src="https://2e.zol-img.com.cn/product/192_220x165/500/ceQ9iYyhz0Vhk.jpg" alt="��Ϊnova 3i��4GB RAM/ȫ��ͨ��"></a>
            <h3><a href="/cell_phone/index1222100.shtml" title="��Ϊnova 3i��4GB RAM/ȫ��ͨ��GPU Turbo��������ͷ��AI���գ�ȫ����" target="_blank">��Ϊnova 3i��4GB RAM/ȫ��ͨ�� <span>GPU Turbo��������ͷ��AI���գ�ȫ����</span></a></h3>
            <div class="price-row">
                                                <span class="price-tip">�ο��ۣ�</span><span class="price price-normal"><b class="price-sign">��</b><b class="price-type">1999</b></span>								<div class="goods-promotion">
																								</div>
            </div>

			<div class="comment-row">
				<span class="star"><em style="width:70%"></em></span>
                <span class="score">7.0</span>
                <em>|</em>
				<a class="comment-num" href="/1223/1222100/review.shtml" target="_blank">9�˵���</a>
				<a class="review-active-v4" target="_blank" href="http://detail.zol.com.cn/reviewActivity/ReviewActV9.html" title="�������£���Ʒ����">�������£���Ʒ����</a>
			</div>

						<div class="function-v3">
                                <label id="comp1222100" class="compare-btn" hide-focus="true" data-rel='1222100,��Ϊnova 3i��4GB RAM/ȫ��ͨ��,/cell_phone/index1222100.shtml,https://2e.zol-img.com.cn/product/192_80x60/500/ceQ9iYyhz0Vhk.jpg,57' title="���������ӵ��Աȿ���"><i></i>�Ա�</label>
            </div>
			<div class="merchant-row"></div>
						<div class="rank-row">
								<a href="http://top.zol.com.cn/compositor/57/cell_phone.html" target="_blank">�������е�<span>29</span>��</a>
							</div>
			        </li>
                    <script>
                    document.write("<li class=\"nth-child-3n item-sale\" style=\"position:relative;\"><a rel='nofollow' href=\"http://www.zol.com/detail/cell_phone/vivo/30961770.html?skuId=12876890?spm=748.0\" target=\"_blank\"><img src=\"https://mercrt-fd.zol-img.com.cn/t_s220x300/g5/M00/05/06/ChMkJlrypUyIeGXVAAA_s6YIF_0AAoQFgEOIB8AAD_L116.jpg\" width=\"220\" height=\"300\"></a><span style=\"position: absolute; left: 0px; bottom: 0px; width: 29px; height: 16px; background-image: url(https://pic.zol-img.com.cn/201510/thisad_1016.png); background-position: initial initial; background-repeat: no-repeat no-repeat;\"></span></li>");
                </script>
				        <li data-follow-id="p394162" >
                        <a href="/cell_phone/index394162.shtml" class="pic" target="_blank"><img width="220" height="165" .src="https://2e.zol-img.com.cn/product/186_220x165/324/ceu0Ld6zstn7c.jpg" alt="ƻ��iPhone 8��ȫ��ͨ��"></a>
            <h3><a href="/cell_phone/index394162.shtml" title="ƻ��iPhone 8��ȫ��ͨ��˫�沣�������߳�磬AR��Ϸ��ָ��ʶ��" target="_blank">ƻ��iPhone 8��ȫ��ͨ�� <span>˫�沣�������߳�磬AR��Ϸ��ָ��ʶ��</span></a></h3>
            <div class="price-row">
                                                <span class="price-tip">�ο��ۣ�</span><span class="price price-normal"><b class="price-sign">��</b><b class="price-type">4528</b></span>								<div class="goods-promotion">
																								</div>
            </div>

			<div class="comment-row">
				<span class="star"><em style="width:68%"></em></span>
                <span class="score">6.8</span>
                <em>|</em>
				<a class="comment-num" href="/395/394162/review.shtml" target="_blank">254�˵���</a>
				<a class="review-active-v4" target="_blank" href="http://detail.zol.com.cn/reviewActivity/ReviewActV9.html" title="�������£���Ʒ����">�������£���Ʒ����</a>
			</div>

						<div class="function-v3">
                                <label id="comp394162" class="compare-btn" hide-focus="true" data-rel='394162,ƻ��iPhone 8��ȫ��ͨ��,/cell_phone/index394162.shtml,https://2e.zol-img.com.cn/product/186_80x60/324/ceu0Ld6zstn7c.jpg,57' title="���������ӵ��Աȿ���"><i></i>�Ա�</label>
            </div>
			<div class="merchant-row"></div>
						<div class="rank-row">
								<a href="http://top.zol.com.cn/compositor/57/cell_phone.html" target="_blank">�������е�<span>26</span>��</a>
							</div>
			        </li>
            <li data-follow-id="p1181907" >
                        <a href="/cell_phone/index1181907.shtml" class="pic" target="_blank"><img width="220" height="165" .src="https://2b.zol-img.com.cn/product/188_220x165/629/ceeATQX7XShA.jpg" alt="��ҫV10��4GB RAM/ȫ��ͨ��"></a>
            <h3><a href="/cell_phone/index1181907.shtml" title="��ҫV10��4GB RAM/ȫ��ͨ����ҫHi-Five��ָ��ʶ������ʶ��AI����" target="_blank">��ҫV10��4GB RAM/ȫ��ͨ�� <span>��ҫHi-Five��ָ��ʶ������ʶ��AI����</span></a></h3>
            <div class="price-row">
                                                <span class="price-tip">�ο��ۣ�</span><span class="price price-normal"><b class="price-sign">��</b><b class="price-type">1899</b></span>								<div class="goods-promotion">
																								</div>
            </div>

			<div class="comment-row">
				<span class="star"><em style="width:82%"></em></span>
                <span class="score">8.2</span>
                <em>|</em>
				<a class="comment-num" href="/1182/1181907/review.shtml" target="_blank">183�˵���</a>
				<a class="review-active-v4" target="_blank" href="http://detail.zol.com.cn/reviewActivity/ReviewActV9.html" title="�������£���Ʒ����">�������£���Ʒ����</a>
			</div>

						<div class="function-v3">
                                <label id="comp1181907" class="compare-btn" hide-focus="true" data-rel='1181907,��ҫV10��4GB RAM/ȫ��ͨ��,/cell_phone/index1181907.shtml,https://2b.zol-img.com.cn/product/188_80x60/629/ceeATQX7XShA.jpg,57' title="���������ӵ��Աȿ���"><i></i>�Ա�</label>
            </div>
			<div class="merchant-row"></div>
						<div class="rank-row">
								<a href="http://top.zol.com.cn/compositor/57/cell_phone.html" target="_blank">�������е�<span>30</span>��</a>
							</div>
			        </li>
            <li class="nth-child-3n nth-child-4n" data-follow-id="p1215577" >
                        <a href="/cell_phone/index1215577.shtml" class="pic" target="_blank"><img width="220" height="165" .src="https://2a.zol-img.com.cn/product/191_220x165/52/ce9buWJb9cW2s.jpg" alt="vivo NEX��6GB RAM/ȫ��ͨ��"></a>
            <h3><a href="/cell_phone/index1215577.shtml" title="vivo NEX��6GB RAM/ȫ��ͨ������ʽǰ������ͷ����Ļָ�ƽ���3.0����Ϸģʽ4.0��JOVI������������" target="_blank">vivo NEX��6GB RAM/ȫ��ͨ�� <span>����ʽǰ������ͷ����Ļָ�ƽ���3.0����Ϸģʽ4.0��JOVI������������</span></a></h3>
            <div class="price-row">
                                                <span class="price-tip">�ο��ۣ�</span><span class="price price-normal"><b class="price-sign">��</b><b class="price-type">3698</b></span>								<div class="goods-promotion">
																								</div>
            </div>

			<div class="comment-row">
				<span class="star"><em style="width:95%"></em></span>
                <span class="score">9.5</span>
                <em>|</em>
				<a class="comment-num" href="/1216/1215577/review.shtml" target="_blank">644�˵���</a>
				<a class="review-active-v4" target="_blank" href="http://detail.zol.com.cn/reviewActivity/ReviewActV9.html" title="�������£���Ʒ����">�������£���Ʒ����</a>
			</div>

						<div class="function-v3">
                                <label id="comp1215577" class="compare-btn" hide-focus="true" data-rel='1215577,vivo NEX��6GB RAM/ȫ��ͨ��,/cell_phone/index1215577.shtml,https://2a.zol-img.com.cn/product/191_80x60/52/ce9buWJb9cW2s.jpg,57' title="���������ӵ��Աȿ���"><i></i>�Ա�</label>
            </div>
			<div class="merchant-row"></div>
						<div class="rank-row">
								<a href="http://top.zol.com.cn/compositor/57/cell_phone.html" target="_blank">�������е�<span>32</span>��</a>
							</div>
			        </li>
            <li data-follow-id="p1209808" >
                        <a href="/cell_phone/index1209808.shtml" class="pic" target="_blank"><img width="220" height="165" .src="https://2e.zol-img.com.cn/product/190_220x165/522/ce6loy8E8ovW.jpg" alt="vivo Y85��ȫ��ͨ��"></a>
            <h3><a href="/cell_phone/index1209808.shtml" title="vivo Y85��ȫ��ͨ��ȫ����һ��ʽ��ۣ�����˫�㣬����ģʽ��ǰ��AI����" target="_blank">vivo Y85��ȫ��ͨ�� <span>ȫ����һ��ʽ��ۣ�����˫�㣬����ģʽ��ǰ��AI����</span></a></h3>
            <div class="price-row">
                                                <span class="price-tip">�ο��ۣ�</span><span class="price price-normal"><b class="price-sign">��</b><b class="price-type">1398</b></span>								<div class="goods-promotion">
																								</div>
            </div>

			<div class="comment-row">
				<span class="star"><em style="width:82%"></em></span>
                <span class="score">8.2</span>
                <em>|</em>
				<a class="comment-num" href="/1210/1209808/review.shtml" target="_blank">61�˵���</a>
				<a class="review-active-v4" target="_blank" href="http://detail.zol.com.cn/reviewActivity/ReviewActV9.html" title="�������£���Ʒ����">�������£���Ʒ����</a>
			</div>

						<div class="function-v3">
                                <label id="comp1209808" class="compare-btn" hide-focus="true" data-rel='1209808,vivo Y85��ȫ��ͨ��,/cell_phone/index1209808.shtml,https://2e.zol-img.com.cn/product/190_80x60/522/ce6loy8E8ovW.jpg,57' title="���������ӵ��Աȿ���"><i></i>�Ա�</label>
            </div>
			<div class="merchant-row"></div>
						<div class="rank-row">
								<a href="http://top.zol.com.cn/compositor/57/cell_phone.html" target="_blank">�������е�<span>33</span>��</a>
							</div>
			        </li>
            <li data-follow-id="p1170480" >
                        <a href="/cell_phone/index1170480.shtml" class="pic" target="_blank"><img width="220" height="165" .src="https://2c.zol-img.com.cn/product/190_220x165/592/cepiPCapqsDgk.jpg" alt="С��6X��4GB RAM/ȫ��ͨ��"></a>
            <h3><a href="/cell_phone/index1170480.shtml" title="С��6X��4GB RAM/ȫ��ͨ��ǰ��2000������ϵ�����ģ�AI������������������660 AIE��������ȫ����" target="_blank">С��6X��4GB RAM/ȫ��ͨ�� <span>ǰ��2000������ϵ�����ģ�AI������������������660 AIE��������ȫ����</span></a></h3>
            <div class="price-row">
                                                <span class="price-tip">�ο��ۣ�</span><span class="price price-normal"><b class="price-sign">��</b><b class="price-type">1349</b></span>								<div class="goods-promotion">
																								</div>
            </div>

			<div class="comment-row">
				<span class="star"><em style="width:53%"></em></span>
                <span class="score">5.3</span>
                <em>|</em>
				<a class="comment-num" href="/1171/1170480/review.shtml" target="_blank">103�˵���</a>
				<a class="review-active-v4" target="_blank" href="http://detail.zol.com.cn/reviewActivity/ReviewActV9.html" title="�������£���Ʒ����">�������£���Ʒ����</a>
			</div>

						<div class="function-v3">
                                <label id="comp1170480" class="compare-btn" hide-focus="true" data-rel='1170480,С��6X��4GB RAM/ȫ��ͨ��,/cell_phone/index1170480.shtml,https://2c.zol-img.com.cn/product/190_80x60/592/cepiPCapqsDgk.jpg,57' title="���������ӵ��Աȿ���"><i></i>�Ա�</label>
            </div>
			<div class="merchant-row"></div>
						<div class="rank-row">
								<a href="http://top.zol.com.cn/compositor/57/cell_phone.html" target="_blank">�������е�<span>34</span>��</a>
							</div>
			        </li>
            <li class="nth-child-3n" data-follow-id="p1104332" >
            <span class="icon award award2_2016"></span>            <a href="/cell_phone/index1104332.shtml" class="pic" target="_blank"><img width="220" height="165" .src="https://2f.zol-img.com.cn/product/185_220x165/593/ceH9bUUFouWg.jpg" alt="ƻ��iPhone 7 Plus��ȫ��ͨ��"></a>
            <h3><a href="/cell_phone/index1104332.shtml" title="ƻ��iPhone 7 Plus��ȫ��ͨ������˫����ͷ������������ͬʱ��ʾ��4K��Ƶ��¼��Siri����" target="_blank">ƻ��iPhone 7 Plus��ȫ��ͨ�� <span>����˫����ͷ������������ͬʱ��ʾ��4K��Ƶ��¼��Siri����</span></a></h3>
            <div class="price-row">
                                                <span class="price-tip">�ο��ۣ�</span><span class="price price-normal"><b class="price-sign">��</b><b class="price-type">4499</b></span>								<div class="goods-promotion">
																								</div>
            </div>

			<div class="comment-row">
				<span class="star"><em style="width:81%"></em></span>
                <span class="score">8.1</span>
                <em>|</em>
				<a class="comment-num" href="/1105/1104332/review.shtml" target="_blank">335�˵���</a>
				<a class="review-active-v4" target="_blank" href="http://detail.zol.com.cn/reviewActivity/ReviewActV9.html" title="�������£���Ʒ����">�������£���Ʒ����</a>
			</div>

						<div class="function-v3">
                                <label id="comp1104332" class="compare-btn" hide-focus="true" data-rel='1104332,ƻ��iPhone 7 Plus��ȫ��ͨ��,/cell_phone/index1104332.shtml,https://2f.zol-img.com.cn/product/185_80x60/593/ceH9bUUFouWg.jpg,57' title="���������ӵ��Աȿ���"><i></i>�Ա�</label>
            </div>
			<div class="merchant-row"></div>
						<div class="rank-row">
								<a href="http://top.zol.com.cn/compositor/57/cell_phone.html" target="_blank">�������е�<span>35</span>��</a>
							</div>
			        </li>
            <li class="nth-child-4n" data-follow-id="p1216612" >
                        <a href="/cell_phone/index1216612.shtml" class="pic" target="_blank"><img width="220" height="165" .src="https://2d.zol-img.com.cn/product/191_220x165/585/cev71NIc7PKmc.jpg" alt="����Galaxy A9 Star��ȫ��ͨ��"></a>
            <h3><a href="/cell_phone/index1216612.shtml" title="����Galaxy A9 Star��ȫ��ͨ��Bixby�������ָ��ʶ��AI���գ��ű�ȫ����" target="_blank">����Galaxy A9 Star��ȫ��ͨ�� <span>Bixby�������ָ��ʶ��AI���գ��ű�ȫ����</span></a></h3>
            <div class="price-row">
                                                <span class="price-tip">�ο��ۣ�</span><span class="price price-normal"><b class="price-sign">��</b><b class="price-type">2969</b></span>								<div class="goods-promotion">
										<span class="J_PicModeTuan" data-url="http://www.zol.com/detail/cell_phone/samsung/31369324.html?skuId=13232796?spm=784.0" data-price="2399" data-rel="modeTuan">�Ź�</span>
																								</div>
            </div>

			<div class="comment-row">
				<span class="star"><em style="width:75%"></em></span>
                <span class="score">7.5</span>
                <em>|</em>
				<a class="comment-num" href="/1217/1216612/review.shtml" target="_blank">194�˵���</a>
				<a class="review-active-v4" target="_blank" href="http://detail.zol.com.cn/reviewActivity/ReviewActV9.html" title="�������£���Ʒ����">�������£���Ʒ����</a>
			</div>

						<div class="function-v3">
                                <label id="comp1216612" class="compare-btn" hide-focus="true" data-rel='1216612,����Galaxy A9 Star��ȫ��ͨ��,/cell_phone/index1216612.shtml,https://2d.zol-img.com.cn/product/191_80x60/585/cev71NIc7PKmc.jpg,57' title="���������ӵ��Աȿ���"><i></i>�Ա�</label>
            </div>
			<div class="merchant-row"></div>
						<div class="rank-row">
								<a href="http://top.zol.com.cn/compositor/57/cell_phone.html" target="_blank">�������е�<span>36</span>��</a>
							</div>
			        </li>
            <li data-follow-id="p1221465" >
                        <a href="/cell_phone/index1221465.shtml" class="pic" target="_blank"><img width="220" height="165" .src="https://2c.zol-img.com.cn/product/192_220x165/968/ces6G1t2lkego.jpg" alt="����16th Plus��6GB RAM/ȫ��ͨ��"></a>
            <h3><a href="/cell_phone/index1221465.shtml" title="����16th Plus��6GB RAM/ȫ��ͨ��Super mBack 2.0��ȫ�������ƽ�����Music Link �����𶯣���Ļָ��ʶ��" target="_blank">����16th Plus��6GB RAM/ȫ��ͨ�� <span>Super mBack 2.0��ȫ�������ƽ�����Music Link �����𶯣���Ļָ��ʶ��</span></a></h3>
            <div class="price-row">
                                                <span class="price-tip">�ο��ۣ�</span><span class="price price-normal"><b class="price-sign">��</b><b class="price-type">3198</b></span>								<div class="goods-promotion">
																								</div>
            </div>

			<div class="comment-row">
				<span class="star"><em style="width:69%"></em></span>
                <span class="score">6.9</span>
                <em>|</em>
				<a class="comment-num" href="/1222/1221465/review.shtml" target="_blank">21�˵���</a>
				<a class="review-active-v4" target="_blank" href="http://detail.zol.com.cn/reviewActivity/ReviewActV9.html" title="�������£���Ʒ����">�������£���Ʒ����</a>
			</div>

						<div class="function-v3">
                                <label id="comp1221465" class="compare-btn" hide-focus="true" data-rel='1221465,����16th Plus��6GB RAM/ȫ��ͨ��,/cell_phone/index1221465.shtml,https://2c.zol-img.com.cn/product/192_80x60/968/ces6G1t2lkego.jpg,57' title="���������ӵ��Աȿ���"><i></i>�Ա�</label>
            </div>
			<div class="merchant-row"></div>
						<div class="rank-row">
								<a href="http://top.zol.com.cn/compositor/57/cell_phone.html" target="_blank">�������е�<span>44</span>��</a>
							</div>
			        </li>
            <li class="nth-child-3n" data-follow-id="p1227474" >
                        <a href="/cell_phone/index1227474.shtml" class="pic" target="_blank"><img width="220" height="165" .src="https://2e.zol-img.com.cn/product/192_220x165/204/ceLwG8i0WsnQc.jpg" alt="���ӿƼ����Pro 2S��4GB RAM/ȫ��ͨ��"></a>
            <h3><a href="/cell_phone/index1227474.shtml" title="���ӿƼ����Pro 2S��4GB RAM/ȫ��ͨ��ȫ���������ӵ����ţ�TV-OUT�������ӳ���Ϸ����" target="_blank">���ӿƼ����Pro 2S��4GB RAM/ȫ��ͨ�� <span>ȫ���������ӵ����ţ�TV-OUT�������ӳ���Ϸ����</span></a></h3>
            <div class="price-row">
                                                <span class="price-tip">�ο��ۣ�</span><span class="price price-normal"><b class="price-sign">��</b><b class="price-type">1798</b></span>								<div class="goods-promotion">
																								</div>
            </div>

			<div class="comment-row">
				<span class="star"><em style="width:65%"></em></span>
                <span class="score">6.5</span>
                <em>|</em>
				<a class="comment-num" href="/1228/1227474/review.shtml" target="_blank">14�˵���</a>
				<a class="review-active-v4" target="_blank" href="http://detail.zol.com.cn/reviewActivity/ReviewActV9.html" title="�������£���Ʒ����">�������£���Ʒ����</a>
			</div>

						<div class="function-v3">
                                <label id="comp1227474" class="compare-btn" hide-focus="true" data-rel='1227474,���ӿƼ����Pro 2S��4GB RAM/ȫ��ͨ��,/cell_phone/index1227474.shtml,https://2e.zol-img.com.cn/product/192_80x60/204/ceLwG8i0WsnQc.jpg,57' title="���������ӵ��Աȿ���"><i></i>�Ա�</label>
            </div>
			<div class="merchant-row"></div>
			        </li>
            <li data-follow-id="p1184227" >
                        <a href="/cell_phone/index1184227.shtml" class="pic" target="_blank"><img width="220" height="165" .src="https://2d.zol-img.com.cn/product/191_220x165/453/cesBAnMf9mb6.jpg" alt="��ҫ9i��ȫ��ͨ��"></a>
            <h3><a href="/cell_phone/index1184227.shtml" title="��ҫ9i��ȫ��ͨ����С������ȫ������1600��ǰ�øй���ǿ��ͷ��ȫϵ4GB���ڴ棬ָ��ʶ��" target="_blank">��ҫ9i��ȫ��ͨ�� <span>��С������ȫ������1600��ǰ�øй���ǿ��ͷ��ȫϵ4GB���ڴ棬ָ��ʶ��</span></a></h3>
            <div class="price-row">
                                                <span class="price-tip">�ο��ۣ�</span><span class="price price-normal"><b class="price-sign">��</b><b class="price-type">1298</b></span>								<div class="goods-promotion">
																								</div>
            </div>

			<div class="comment-row">
				<span class="star"><em style="width:57%"></em></span>
                <span class="score">5.7</span>
                <em>|</em>
				<a class="comment-num" href="/1185/1184227/review.shtml" target="_blank">25�˵���</a>
				<a class="review-active-v4" target="_blank" href="http://detail.zol.com.cn/reviewActivity/ReviewActV9.html" title="�������£���Ʒ����">�������£���Ʒ����</a>
			</div>

						<div class="function-v3">
                                <label id="comp1184227" class="compare-btn" hide-focus="true" data-rel='1184227,��ҫ9i��ȫ��ͨ��,/cell_phone/index1184227.shtml,https://2d.zol-img.com.cn/product/191_80x60/453/cesBAnMf9mb6.jpg,57' title="���������ӵ��Աȿ���"><i></i>�Ա�</label>
            </div>
			<div class="merchant-row"></div>
						<div class="rank-row">
								<a href="http://top.zol.com.cn/compositor/57/cell_phone.html" target="_blank">�������е�<span>39</span>��</a>
							</div>
			        </li>
            <li class="nth-child-4n" data-follow-id="p1165672" >
                        <a href="/cell_phone/index1165672.shtml" class="pic" target="_blank"><img width="220" height="165" .src="https://2b.zol-img.com.cn/product/186_220x165/539/cekSQ5i8WuvA.jpg" alt="��ΪMate 10��4GB RAM/ȫ��ͨ��"></a>
            <h3><a href="/cell_phone/index1165672.shtml" title="��ΪMate 10��4GB RAM/ȫ��ͨ��֧��4.5G LTE��֧��PCģʽ������970 AI��������ָ��ʶ��" target="_blank">��ΪMate 10��4GB RAM/ȫ��ͨ�� <span>֧��4.5G LTE��֧��PCģʽ������970 AI��������ָ��ʶ��</span></a></h3>
            <div class="price-row">
                                                <span class="price-tip">�ο��ۣ�</span><span class="price price-normal"><b class="price-sign">��</b><b class="price-type">3399</b></span>								<div class="goods-promotion">
										<span class="J_PicModeTuan" data-url="http://www.zol.com/detail/cell_phone/huawei/30549520.html?skuId=12068178?spm=784.0" data-price="2629" data-rel="modeTuan">�Ź�</span>
																								</div>
            </div>

			<div class="comment-row">
				<span class="star"><em style="width:83%"></em></span>
                <span class="score">8.3</span>
                <em>|</em>
				<a class="comment-num" href="/1166/1165672/review.shtml" target="_blank">115�˵���</a>
				<a class="review-active-v4" target="_blank" href="http://detail.zol.com.cn/reviewActivity/ReviewActV9.html" title="�������£���Ʒ����">�������£���Ʒ����</a>
			</div>

						<div class="function-v3">
                                <label id="comp1165672" class="compare-btn" hide-focus="true" data-rel='1165672,��ΪMate 10��4GB RAM/ȫ��ͨ��,/cell_phone/index1165672.shtml,https://2b.zol-img.com.cn/product/186_80x60/539/cekSQ5i8WuvA.jpg,57' title="���������ӵ��Աȿ���"><i></i>�Ա�</label>
            </div>
			<div class="merchant-row"></div>
						<div class="rank-row">
								<a href="http://top.zol.com.cn/compositor/57/cell_phone.html" target="_blank">�������е�<span>41</span>��</a>
							</div>
			        </li>
            <li class="nth-child-3n" data-follow-id="p384973" >
                        <a href="/cell_phone/index384973.shtml" class="pic" target="_blank"><img width="220" height="165" .src="https://2b.zol-img.com.cn/product/181_220x165/937/cewK6OFuhJxQ.jpg" alt="ƻ��iPhone 7��ȫ��ͨ��"></a>
            <h3><a href="/cell_phone/index384973.shtml" title="ƻ��iPhone 7��ȫ��ͨ����ˮ������True Tone����ƣ�4K��Ƶ��¼���ǰ�ѹʽָ��ʶ��" target="_blank">ƻ��iPhone 7��ȫ��ͨ�� <span>��ˮ������True Tone����ƣ�4K��Ƶ��¼���ǰ�ѹʽָ��ʶ��</span></a></h3>
            <div class="price-row">
                                                <span class="price-tip">�ο��ۣ�</span><span class="price price-normal"><b class="price-sign">��</b><b class="price-type">3628</b></span>								<div class="goods-promotion">
																								</div>
            </div>

			<div class="comment-row">
				<span class="star"><em style="width:80%"></em></span>
                <span class="score">8.0</span>
                <em>|</em>
				<a class="comment-num" href="/385/384973/review.shtml" target="_blank">475�˵���</a>
				<a class="review-active-v4" target="_blank" href="http://detail.zol.com.cn/reviewActivity/ReviewActV9.html" title="�������£���Ʒ����">�������£���Ʒ����</a>
			</div>

						<div class="function-v3">
                                <label id="comp384973" class="compare-btn" hide-focus="true" data-rel='384973,ƻ��iPhone 7��ȫ��ͨ��,/cell_phone/index384973.shtml,https://2b.zol-img.com.cn/product/181_80x60/937/cewK6OFuhJxQ.jpg,57' title="���������ӵ��Աȿ���"><i></i>�Ա�</label>
            </div>
			<div class="merchant-row"></div>
						<div class="rank-row">
								<a href="http://top.zol.com.cn/compositor/57/cell_phone.html" target="_blank">�������е�<span>40</span>��</a>
							</div>
			        </li>
            <li data-follow-id="p1209686" >
                        <a href="/cell_phone/index1209686.shtml" class="pic" target="_blank"><img width="220" height="165" .src="https://2a.zol-img.com.cn/product/192_220x165/524/ceu7aWurxxPas.jpg" alt="ƻ��iPhone 11��ȫ��ͨ��"></a>
            <h3><a href="/cell_phone/index1209686.shtml" title="ƻ��iPhone 11��ȫ��ͨ��" target="_blank">ƻ��iPhone 11��ȫ��ͨ�� <span>�����ߴ�:5.8Ӣ�� ����ϵͳ:iOS 12 �����ֱ���:2160x1080���� 4G����:�ƶ�TD-LTE����ͨTD-LTE����ͨFDD-LTE������TD-LTE������FDD-LTE CPU�ͺ�:ƻ�� A12 ������:�˺� RAM����:4GB</span></a></h3>
            <div class="price-row">
                                                <span class="price price-cp"><b class="price-type">�����Ʒ</b></span>								<div class="goods-promotion">
																								</div>
            </div>

			<div class="comment-row">
				<span class="star"><em style="width:65%"></em></span>
                <span class="score">6.5</span>
                <em>|</em>
				<a class="comment-num" href="/1210/1209686/review.shtml" target="_blank">12�˵���</a>
				<a class="review-active-v4" target="_blank" href="http://detail.zol.com.cn/reviewActivity/ReviewActV9.html" title="�������£���Ʒ����">�������£���Ʒ����</a>
			</div>

						<div class="function-v3">
                                <label id="comp1209686" class="compare-btn" hide-focus="true" data-rel='1209686,ƻ��iPhone 11��ȫ��ͨ��,/cell_phone/index1209686.shtml,https://2a.zol-img.com.cn/product/192_80x60/524/ceu7aWurxxPas.jpg,57' title="���������ӵ��Աȿ���"><i></i>�Ա�</label>
            </div>
			<div class="merchant-row"></div>
						<div class="rank-row">
								<a href="http://top.zol.com.cn/compositor/57/cell_phone.html" target="_blank">�������е�<span>37</span>��</a>
							</div>
			        </li>
            <li data-follow-id="p1217453" >
                        <a href="/cell_phone/index1217453.shtml" class="pic" target="_blank"><img width="220" height="165" .src="https://2c.zol-img.com.cn/product/191_220x165/574/cedZwTDSZzzA.jpg" alt="С��8 SE��4GB RAM/ȫ��ͨ��"></a>
            <h3><a href="/cell_phone/index1217453.shtml" title="С��8 SE��4GB RAM/ȫ��ͨ��2.5D���沣����ȫ��ͨ 5.0���沿ʶ��ȫ����" target="_blank">С��8 SE��4GB RAM/ȫ��ͨ�� <span>2.5D���沣����ȫ��ͨ 5.0���沿ʶ��ȫ����</span></a></h3>
            <div class="price-row">
                                                <span class="price-tip">�ο��ۣ�</span><span class="price price-normal"><b class="price-sign">��</b><b class="price-type">1699</b></span>								<div class="goods-promotion">
																								</div>
            </div>

			<div class="comment-row">
				<span class="star"><em style="width:53%"></em></span>
                <span class="score">5.3</span>
                <em>|</em>
				<a class="comment-num" href="/1218/1217453/review.shtml" target="_blank">72�˵���</a>
				<a class="review-active-v4" target="_blank" href="http://detail.zol.com.cn/reviewActivity/ReviewActV9.html" title="�������£���Ʒ����">�������£���Ʒ����</a>
			</div>

						<div class="function-v3">
                                <label id="comp1217453" class="compare-btn" hide-focus="true" data-rel='1217453,С��8 SE��4GB RAM/ȫ��ͨ��,/cell_phone/index1217453.shtml,https://2c.zol-img.com.cn/product/191_80x60/574/cedZwTDSZzzA.jpg,57' title="���������ӵ��Աȿ���"><i></i>�Ա�</label>
            </div>
			<div class="merchant-row"></div>
						<div class="rank-row">
								<a href="http://top.zol.com.cn/compositor/57/cell_phone.html" target="_blank">�������е�<span>42</span>��</a>
							</div>
			        </li>
            <li class="nth-child-3n nth-child-4n" data-follow-id="p1177170" >
                        <a href="/cell_phone/index1177170.shtml" class="pic" target="_blank"><img width="220" height="165" .src="https://2c.zol-img.com.cn/product/190_220x165/438/cerf6VtutNcIU.jpg" alt="����GALAXY S9+��ȫ��ͨ��"></a>
            <h3><a href="/cell_phone/index1177170.shtml" title="����GALAXY S9+��ȫ��ͨ����Ĥʶ���沿ʶ�����߿�䣬Bixby�˹�����ʵʱ����" target="_blank">����GALAXY S9+��ȫ��ͨ�� <span>��Ĥʶ���沿ʶ�����߿�䣬Bixby�˹�����ʵʱ����</span></a></h3>
            <div class="price-row">
                                                <span class="price-tip">�ο��ۣ�</span><span class="price price-normal"><b class="price-sign">��</b><b class="price-type">6699</b></span>								<div class="goods-promotion">
																								</div>
            </div>

			<div class="comment-row">
				<span class="star"><em style="width:84%"></em></span>
                <span class="score">8.4</span>
                <em>|</em>
				<a class="comment-num" href="/1178/1177170/review.shtml" target="_blank">128�˵���</a>
				<a class="review-active-v4" target="_blank" href="http://detail.zol.com.cn/reviewActivity/ReviewActV9.html" title="�������£���Ʒ����">�������£���Ʒ����</a>
			</div>

						<div class="function-v3">
                                <label id="comp1177170" class="compare-btn" hide-focus="true" data-rel='1177170,����GALAXY S9+��ȫ��ͨ��,/cell_phone/index1177170.shtml,https://2c.zol-img.com.cn/product/190_80x60/438/cerf6VtutNcIU.jpg,57' title="���������ӵ��Աȿ���"><i></i>�Ա�</label>
            </div>
			<div class="merchant-row"></div>
						<div class="rank-row">
								<a href="http://top.zol.com.cn/compositor/57/cell_phone.html" target="_blank">�������е�<span>45</span>��</a>
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
			<div class="pagebar"><span class="sel">1</span><a href="/cell_phone_index/subcate57_0_list_1_0_1_2_0_2.html"  target="_self">2</a><a href="/cell_phone_index/subcate57_0_list_1_0_1_2_0_3.html"  target="_self">3</a><a href="/cell_phone_index/subcate57_0_list_1_0_1_2_0_4.html"  target="_self">4</a><a href="/cell_phone_index/subcate57_0_list_1_0_1_2_0_5.html"  target="_self">5</a><span >...</span><a href="/cell_phone_index/subcate57_0_list_1_0_1_2_0_2.html" class="next" target="_self">��һҳ<i></i></a></div>
			<div class="history-tips"><i></i>���п��ֻ�<b>&gt;&gt;</b></div>
		</div>

		<div class="adSpace" id="list_pagenavi_bottom_tonglan"   style="display:none;"><script>write_group_ad('list_pagenavi_bottom_tonglan','3pagenavi_bottom_tonglan.inc',0,57,0);</script><script>ad_w();</script></div>

		        <div id="userTalkPro" class="hide"></div>


				<div class="section">
			<div class="section-header">
				<h3>�ֻ�Ʒ�Ʊ��۴�ȫ</h3>
				<p class="link"><a href="/category/57.html" target="_blank">�鿴����Ʒ��<b>&gt;&gt;</b></a></p>
			</div>
			<ul class="text-list clearfix">
								<li><a href="/cell_phone_index/subcate57_1673_list_1.html" target="_blank">OPPO�ֻ�</a>(47)</li>
								<li><a href="/cell_phone_index/subcate57_1795_list_1.html" target="_blank">vivo�ֻ�</a>(46)</li>
								<li><a href="/cell_phone_index/subcate57_613_list_1.html" target="_blank">��Ϊ�ֻ�</a>(94)</li>
								<li><a href="/cell_phone_index/subcate57_98_list_1.html" target="_blank">�����ֻ�</a>(120)</li>
								<li><a href="/cell_phone_index/subcate57_50840_list_1.html" target="_blank">��ҫ�ֻ�</a>(74)</li>
								<li><a href="/cell_phone_index/subcate57_35579_list_1.html" target="_blank">һ���ֻ�</a>(11)</li>
								<li><a href="/cell_phone_index/subcate57_544_list_1.html" target="_blank">ƻ���ֻ�</a>(34)</li>
								<li><a href="/cell_phone_index/subcate57_1632_list_1.html" target="_blank">�����ֻ�</a>(38)</li>
								<li><a href="/cell_phone_index/subcate57_1763_list_1.html" target="_blank">�����ֻ�</a>(31)</li>
								<li><a href="/cell_phone_index/subcate57_1434_list_1.html" target="_blank">�����ֻ�</a>(61)</li>
								<li><a href="/cell_phone_index/subcate57_642_list_1.html" target="_blank">�����ֻ�</a>(46)</li>
								<li><a href="/cell_phone_index/subcate57_295_list_1.html" target="_blank">Moto�ֻ�</a>(44)</li>
								<li><a href="/cell_phone_index/subcate57_35005_list_1.html" target="_blank">Ŭ�����ֻ�</a>(37)</li>
								<li><a href="/cell_phone_index/subcate57_35849_list_1.html" target="_blank">���ӿƼ��ֻ�</a>(15)</li>
								<li><a href="/cell_phone_index/subcate57_35350_list_1.html" target="_blank">360�ֻ�</a>(31)</li>
								<li><a href="/cell_phone_index/subcate57_52602_list_1.html" target="_blank">�����ֻ��ֻ�</a>(13)</li>
								<li><a href="/cell_phone_index/subcate57_34645_list_1.html" target="_blank">С���ֻ�</a>(94)</li>
								<li><a href="/cell_phone_index/subcate57_300_list_1.html" target="_blank">�����ֻ�</a>(19)</li>
							</ul>
		</div>

				<div class="section">
			<div class="section-header">
				<h3>�����ֻ��������</h3>
								<p class="link"><a href="/history/subcate57_0_1_0_0_1.html" target="_blank">�鿴ͣ����Ʒ<b>&gt;&gt;</b></a></p>
							</div>
			<ul class="text-list clearfix">
									<li><a href="http://detail.zol.com.cn/cell_phone/index1229519.shtml" target="_blank">ƻ��XS</a></li>
									<li><a href="http://detail.zol.com.cn/cell_phone/index1205394.shtml" target="_blank">ƻ��xr</a></li>
									<li><a href="http://detail.zol.com.cn/cell_phone/index1212228.shtml" target="_blank">����16</a></li>
									<li><a href="http://apple.zol.com.cn/" target="_blank">ƻ��������</a></li>
									<li><a href="http://detail.zol.com.cn/cell_phone/index1227474.shtml" target="_blank">���Pro2S</a></li>
									<li><a href="http://detail.zol.com.cn/cell_phone/index1215577.shtml" target="_blank">vivonex</a></li>
									<li><a href="http://detail.zol.com.cn/cell_phone/index1229520.shtml" target="_blank">ƻ��xsmax</a></li>
									<li><a href="http://detail.zol.com.cn/cell_phone/index1221465.shtml" target="_blank">����16plus</a></li>
									<li><a href="http://detail.zol.com.cn/cell_phone/index1222342.shtml" target="_blank">��ҫnote10</a></li>
									<li><a href="http://detail.zol.com.cn/cell_phone/index1216973.shtml" target="_blank">С��8͸��̽����</a></li>
									<li><a href="http://detail.zol.com.cn/cell_phone/index1227284.shtml" target="_blank">vivox23</a></li>
							</ul>
		</div>

				<div id="btmMerSale"></div>

		<div class="adSpace" id="list_bottom_tonglan"   style="display:none;"><script>write_group_ad('list_bottom_tonglan','3list_bottom_tonglan.inc',0,57,0);</script><script>ad_w();</script></div>
	</div>

		<div class="side">
	   <dl id="J_CategoryCurrent" class="category-current">

    	<dt class="open"><i></i>�ֻ�</dt>
	<dd>
		<ul class="category-current-list clearfix">
		    			<li class="active"><a href="/cell_phone_index/subcate57_list_1.html">�ֻ�</a></li>
						<li><a href="/phonebattery/">�ֻ����</a></li>
						<li><a href="/cellcharger/">�ֻ������</a></li>
						<li><a href="/datacable/">�ֻ�������</a></li>
						<li><a href="/mobile-base/">�ֻ�����</a></li>
						<li><a href="/mobile-laoding/">�ֻ���Ĥ</a></li>
						<li><a href="/mobile-demeo/">�ֻ�������</a></li>
						<li><a href="/mobile-car-accessories/">�ֻ��������</a></li>
						<li><a href="/phone_annex/">�ֻ���������</a></li>
					</ul>


    		<h4>�ֻ��������</h4>
		<ul class="category-current-list clearfix">
					<li><a href="http://detail.zol.com.cn/flash_memory/s741/">�ֻ��洢��</a></li>
					<li><a href="http://detail.zol.com.cn/microphone/s5004/">��������</a></li>
					<li><a href="http://detail.zol.com.cn/microphone/s2984/">�ֻ�����</a></li>

		</ul>

		</dd>

    	<dt><i></i>ͨѶ��Ʒ</dt>
	<dd class="hide">
		<ul class="category-current-list clearfix">
		    			<li><a href="/groupphone/">���ŵ绰</a></li>
						<li><a href="/interphone/">�Խ���</a></li>
						<li><a href="/telephone/">�绰��</a></li>
						<li><a href="/dictaphone/">�绰¼��</a></li>
						<li><a href="/phonepartner/">�绰IT����</a></li>
						<li><a href="/netphone/">����绰</a></li>
						<li><a href="/phonemeeting/">����绰</a></li>
						<li><a href="/callcenter/">���������豸</a></li>
						<li><a href="/beeper/">������</a></li>
					</ul>


    		<h4>ͨѶ��Ʒ�������</h4>
		<ul class="category-current-list clearfix">
					<li><a href="http://detail.zol.com.cn/Program-controlled_switches/">�̿ؽ�����</a></li>
					<li><a href="http://detail.zol.com.cn/videomeeting/">��Ƶ����</a></li>
					<li><a href="http://detail.zol.com.cn/AudioandConference_System/">��Ƶ������ϵͳ</a></li>

		</ul>

		</dd>
	</dl>                <div class="adSpace" id="list_list_right_first_ad"   style="display:none;"><script>write_group_ad('list_list_right_first_ad','3list_right_first_ad.inc',0,57,0);</script><script>ad_w();</script></div>
        		<div id="J_CompetitiveGoods" class="competitive-goods hide" style="position:relative;"></div>

								<div id="J_CompetitiveGoods-5-10" class="competitive-goods hide" ></div>

		<div class="adSpace" id="list_list_right_area_bottom"   style="display:none;"><script>write_group_ad('list_list_right_area_bottom','4diqu_pro_list_right_location_button_s_57_m_0_{LOCATIONID}.inc#1price_search_right_1_s_57_m_0.inc#5price_search_right_1_s_57_m_0.inc#0price_search_right_1_s_57.inc',0,57,0);</script><script>ad_w();</script><script>ad_w();</script><script>ad_w();</script><script>ad_w();</script></div>				<div class="adSpace" id="list_list_right_sub_attention_button"   style="display:none;"><script>write_group_ad('list_list_right_sub_attention_button','4diqu_list_right_sub_attention_button_s_57_m_0_{LOCATIONID}.inc#3list_right_sub_attention_button_1_s_57.inc#1list_right_sub_attention_button_s_57_m_0.inc#5list_right_sub_attention_button_s_57_m_0.inc',0,57,0);</script><script>ad_w();</script><script>ad_w();</script><script>ad_w();</script><script>ad_w();</script></div>
				<div class="module">
    <div class="module-header">
        <h3>���˵</h3>
    </div>
    <ul class="comment-list">
                <li class="">
            <div class="comm-header clearfix">
                <span class="face">
                    <img width="36" height="36" src="https://mypp-fd.zol-img.com.cn/t_s100x100/g5/M00/09/04/ChMkJ1rJiESIBKvIAAAKzhPMKroAAnflAH8EYAAAArm237.jpg">
                </span>
                <div class="comment-box">
                    <span class="name"><a target="_blank" href="//my.zol.com.cn/40jifo/">�԰�</a></span>
                    <div class="start"><span class="start-box"><em style="width:80%"></em></span><strong>8.0</strong></div>
                </div>
            </div>
            <p class="comment-content"><strong>�ŵ㣺</strong>���������ǿ���Ƚ��ʺ����ε����������û�����ֻ��ܱȵ�<a target="_blank" href="http://t.zol.com.cn/57/1212229/evaluation_5430.html">�鿴ȫ��&gt;</a></p>
            <div class="comm-tag"><span class="time">37����ǰ</span><span class="prov">���� <a title="360 �ֻ�N7��6GB RAM/ȫ��ͨ��" target="_blank" href="/cell_phone/index1212229.shtml">360 �ֻ�N7��6GB RAM/ȫ��ͨ��</a></span></div>
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
            <p class="comment-content"><strong>�ŵ㣺</strong>���ó��������ӣ���Ʒ�ƣ��бƸ�<a target="_blank" href="http://t.zol.com.cn/57/1182639/evaluation_5429.html">�鿴ȫ��&gt;</a></p>
            <div class="comm-tag"><span class="time">50����ǰ</span><span class="prov">���� <a title="ƻ��iPhone X��ȫ��ͨ��" target="_blank" href="/cell_phone/index1182639.shtml">ƻ��iPhone X��ȫ��ͨ��</a></span></div>
        </li>
                <li class="">
            <div class="comm-header clearfix">
                <span class="face">
                    <img width="36" height="36" src="https://mypp-fd.zol-img.com.cn/t_s100x100/g5/M00/03/02/ChMkJlubT4iIcmDqAAAAy-kFPysAArthgP__uoAAAEW872.jpg">
                </span>
                <div class="comment-box">
                    <span class="name"><a target="_blank" href="//my.zol.com.cn/8azaraiyk/">���Ͻ��ϰ�</a></span>
                    <div class="start"><span class="start-box"><em style="width:80%"></em></span><strong>8.0</strong></div>
                </div>
            </div>
            <p class="comment-content"><strong>�ŵ㣺</strong>����о����Ǻܲ�����Լ۱Ȼ�����<a target="_blank" href="http://t.zol.com.cn/57/1185512/evaluation_5427.html">�鿴ȫ��&gt;</a></p>
            <div class="comm-tag"><span class="time">1Сʱǰ</span><span class="prov">���� <a title="��Ϊnova 3��ȫ��ͨ��" target="_blank" href="/cell_phone/index1185512.shtml">��Ϊnova 3��ȫ��ͨ��</a></span></div>
        </li>
                <li class="">
            <div class="comm-header clearfix">
                <span class="face">
                    <img width="36" height="36" src="https://icon.zol-img.com.cn/group/default_zoler/zoler_100.jpg">
                </span>
                <div class="comment-box">
                    <span class="name"><a target="_blank" href="//my.zol.com.cn/sina_56322851t3/">ˮ������</a></span>
                    <div class="start"><span class="start-box"><em style="width:100%"></em></span><strong>10.0</strong></div>
                </div>
            </div>
            <p class="comment-content"><strong>�ŵ㣺</strong>FindX�ڴ�������Ϻܳ��ʣ��������ʵĻ��������õ�AI�������֣���ȫ...<a target="_blank" href="http://detail.zol.com.cn/1214/1213467/review_0_0_1710250_1.shtml#tagNav">�鿴ȫ��&gt;</a></p>
            <div class="comm-tag"><span class="time">2018-09-13</span><span class="prov">���� <a title="OPPO Find X����׼��/ȫ��ͨ��" target="_blank" href="/cell_phone/index1213467.shtml">OPPO Find X����׼��/ȫ��ͨ��</a></span></div>
        </li>
                <li class="">
            <div class="comm-header clearfix">
                <span class="face">
                    <img width="36" height="36" src="https://icon.zol-img.com.cn/group/default_zoler/zoler_100.jpg">
                </span>
                <div class="comment-box">
                    <span class="name"><a target="_blank" href="//my.zol.com.cn/sina_3451398571/">�������ˣ�</a></span>
                    <div class="start"><span class="start-box"><em style="width:96%"></em></span><strong>9.6</strong></div>
                </div>
            </div>
            <p class="comment-content"><strong>�ŵ㣺</strong>��ô����ռ�ȵ��ֻ��һ��ǵ�һ���ã����Ǵ�����ǰ��δ�е��Ӿ����飬������...<a target="_blank" href="http://detail.zol.com.cn/1214/1213467/review_0_0_1710249_1.shtml#tagNav">�鿴ȫ��&gt;</a></p>
            <div class="comm-tag"><span class="time">2018-09-13</span><span class="prov">���� <a title="OPPO Find X����׼��/ȫ��ͨ��" target="_blank" href="/cell_phone/index1213467.shtml">OPPO Find X����׼��/ȫ��ͨ��</a></span></div>
        </li>
                <li class="">
            <div class="comm-header clearfix">
                <span class="face">
                    <img width="36" height="36" src="https://icon.zol-img.com.cn/group/default_zoler/zoler_100.jpg">
                </span>
                <div class="comment-box">
                    <span class="name"><a target="_blank" href="//my.zol.com.cn/sina_8f11p45787/">�������</a></span>
                    <div class="start"><span class="start-box"><em style="width:100%"></em></span><strong>10.0</strong></div>
                </div>
            </div>
            <p class="comment-content"><strong>�ŵ㣺</strong>�õ��ⲿ�ֻ���ʱ����ľ�һ�ָо��������ˡ�����ռ�ȸߴ�93.8%����...<a target="_blank" href="http://detail.zol.com.cn/1214/1213467/review_0_0_1710240_1.shtml#tagNav">�鿴ȫ��&gt;</a></p>
            <div class="comm-tag"><span class="time">2018-09-13</span><span class="prov">���� <a title="OPPO Find X����׼��/ȫ��ͨ��" target="_blank" href="/cell_phone/index1213467.shtml">OPPO Find X����׼��/ȫ��ͨ��</a></span></div>
        </li>

    </ul>
</div>


		<div class="module">
	<div class="module-header">
		<h3>����������Ʒ</h3>
	</div>
	<ul class="rank-list">
				<li class="current">
			<em class="n1">1</em>		
			<a href="/cell_phone/index1227167.shtml" class="pic" title="��Ϊ��â7��ȫ��ͨ��" target="_blank">
				<img width="80" height="60" alt="��Ϊ��â7��ȫ��ͨ��" src="https://2d.zol-img.com.cn/product/192_80x60/749/ceIGTCqrLVnCg.jpg">
			</a>
			<p><a title="��Ϊ��â7��ȫ��ͨ��" href="/cell_phone/index1227167.shtml" target="_blank">��Ϊ��â7��ȫ��ͨ��</a></p>
			<p class="price"><em>��2399</em></p>
		</li>
				<li>
			<em class="n1">2</em>		
			<a href="/cell_phone/index1205394.shtml" class="pic" title="ƻ��iPhone XR��ȫ��ͨ��" target="_blank">
				<img width="80" height="60" alt="ƻ��iPhone XR��ȫ��ͨ��" .src="https://2e.zol-img.com.cn/product/192_80x60/118/ceOwvk3XMlXeg.jpg">
			</a>
			<p><a title="ƻ��iPhone XR��ȫ��ͨ��" href="/cell_phone/index1205394.shtml" target="_blank">ƻ��iPhone XR��ȫ��ͨ��</a></p>
			<p class="price"><em>��6499</em></p>
		</li>
				<li>
			<em class="n1">3</em>		
			<a href="/cell_phone/index1203409.shtml" class="pic" title="ƻ��iPhone 9��ȫ��ͨ��" target="_blank">
				<img width="80" height="60" alt="ƻ��iPhone 9��ȫ��ͨ��" .src="https://2e.zol-img.com.cn/product/192_80x60/660/ceUdiJ2ZsfE.jpg">
			</a>
			<p><a title="ƻ��iPhone 9��ȫ��ͨ��" href="/cell_phone/index1203409.shtml" target="_blank">ƻ��iPhone 9��ȫ��ͨ��</a></p>
			<p class="price"><em>�����Ʒ</em></p>
		</li>
				<li>
			<em class="n2">4</em>		
			<a href="/cell_phone/index1209676.shtml" class="pic" title="��ҫ8X��4GB RAM/ȫ��ͨ��" target="_blank">
				<img width="80" height="60" alt="��ҫ8X��4GB RAM/ȫ��ͨ��" .src="https://2b.zol-img.com.cn/product/192_80x60/883/ceIooc7zVhQQw.jpg">
			</a>
			<p><a title="��ҫ8X��4GB RAM/ȫ��ͨ��" href="/cell_phone/index1209676.shtml" target="_blank">��ҫ8X��4GB RAM/ȫ��ͨ��</a></p>
			<p class="price"><em>��1399</em></p>
		</li>
				<li>
			<em class="n2">5</em>		
			<a href="/cell_phone/index1227284.shtml" class="pic" title="vivo X23��ȫ��ͨ��" target="_blank">
				<img width="80" height="60" alt="vivo X23��ȫ��ͨ��" .src="https://2f.zol-img.com.cn/product/192_80x60/747/ce63frgxJFc5.jpg">
			</a>
			<p><a title="vivo X23��ȫ��ͨ��" href="/cell_phone/index1227284.shtml" target="_blank">vivo X23��ȫ��ͨ��</a></p>
			<p class="price"><em>��3498</em></p>
		</li>
				<li>
			<em class="n2">6</em>		
			<a href="/cell_phone/index1229492.shtml" class="pic" title="����Z5 Pro��ȫ��ͨ��" target="_blank">
				<img width="80" height="60" alt="����Z5 Pro��ȫ��ͨ��" .src="https://2f.zol-img.com.cn/product/192_80x60/85/cenixuR7hwPNg.jpg">
			</a>
			<p><a title="����Z5 Pro��ȫ��ͨ��" href="/cell_phone/index1229492.shtml" target="_blank">����Z5 Pro��ȫ��ͨ��</a></p>
			<p class="price"><em>�����Ʒ</em></p>
		</li>
				<li>
			<em class="n2">7</em>		
			<a href="/cell_phone/index1172306.shtml" class="pic" title="���������콢8��˫4G��" target="_blank">
				<img width="80" height="60" alt="���������콢8��˫4G��" .src="https://2d.zol-img.com.cn/product/185_80x60/903/cexURs6fDSvs.jpg">
			</a>
			<p><a title="���������콢8��˫4G��" href="/cell_phone/index1172306.shtml" target="_blank">���������콢8��˫4G��</a></p>
			<p class="price"><em>��8358</em></p>
		</li>
				<li>
			<em class="n2">8</em>		
			<a href="/cell_phone/index1163244.shtml" class="pic" title="����R9��ʱ�а�/�ƶ�4G��" target="_blank">
				<img width="80" height="60" alt="����R9��ʱ�а�/�ƶ�4G��" .src="https://2f.zol-img.com.cn/product/179_80x60/67/ceNkSizvy0vg.jpg">
			</a>
			<p><a title="����R9��ʱ�а�/�ƶ�4G��" href="/cell_phone/index1163244.shtml" target="_blank">����R9��ʱ�а�/�ƶ�4G��</a></p>
			<p class="price"><em>��1299</em></p>
		</li>
				<li>
			<em class="n2">9</em>		
			<a href="/cell_phone/index1208704.shtml" class="pic" title="vivo X21��ȫ��ͨ��" target="_blank">
				<img width="80" height="60" alt="vivo X21��ȫ��ͨ��" .src="https://2b.zol-img.com.cn/product/191_80x60/921/ceOFxxMDoCBA.jpg">
			</a>
			<p><a title="vivo X21��ȫ��ͨ��" href="/cell_phone/index1208704.shtml" target="_blank">vivo X21��ȫ��ͨ��</a></p>
			<p class="price"><em>��2498</em></p>
		</li>
				<li>
			<em class="n2">10</em>		
			<a href="/cell_phone/index1229520.shtml" class="pic" title="ƻ��iPhone XS Max��ȫ��ͨ��" target="_blank">
				<img width="80" height="60" alt="ƻ��iPhone XS Max��ȫ��ͨ��" .src="https://2c.zol-img.com.cn/product/192_80x60/116/ceB2DF6b4D0s.jpg">
			</a>
			<p><a title="ƻ��iPhone XS Max��ȫ��ͨ��" href="/cell_phone/index1229520.shtml" target="_blank">ƻ��iPhone XS Max��ȫ��ͨ��</a></p>
			<p class="price"><em>��9599</em></p>
		</li>
			</ul>
</div>
		<div class="adSpace" id="list_list_right_last_pro_button"   style="display:none;"><script>write_group_ad('list_list_right_last_pro_button','4diqu_list_right_last_pro_button_s_57_m_0_{LOCATIONID}.inc#1list_right_last_pro_button_s_57_m_0.inc#0list_right_last_pro_button_1_s_57.inc#5list_right_last_pro_button_s_57_m_0.inc',0,57,0);</script><script>ad_w();</script><script>ad_w();</script><script>ad_w();</script><script>ad_w();</script></div>


<div class="module">
	<div class="module-header">
				<h3>�ֻ���Ʒ</h3>
	</div>
		<ul class="rank-list">
				<li class="current">
			<em class='n1'>1</em>									<a href="/cell_phone/index1231386.shtml" class="pic" title="AGM H1��3GB RAM/ȫ��ͨ��" target="_blank">
				<img width="80" height="60" alt="AGM H1��3GB RAM/ȫ��ͨ��" src="https://2e.zol-img.com.cn/product_small/13_80x60/950/ceUGZXSQRmutA.jpg">
			</a>
			<p><a title="AGM H1��3GB RAM/ȫ��ͨ��" href="/cell_phone/index1231386.shtml" target="_blank">AGM H1��3GB RAM/ȫ��ͨ��</a></p>
			<p><em class="price">��1799</em></p>
					</li>
				<li>
			<em class='n1'>2</em>									<a href="/cell_phone/index1231314.shtml" class="pic" title="����Blade A4��ȫ��ͨ��" target="_blank">
				<img width="80" height="60" alt="����Blade A4��ȫ��ͨ��" .src="https://2b.zol-img.com.cn/product_small/13_80x60/863/ceMmzU5T3ozL6.jpg">
			</a>
			<p><a title="����Blade A4��ȫ��ͨ��" href="/cell_phone/index1231314.shtml" target="_blank">����Blade A4��ȫ��ͨ��</a></p>
			<p><em class="price">��899</em></p>
					</li>
				<li>
			<em class='n1'>3</em>									<a href="/cell_phone/index1231213.shtml" class="pic" title="Moto P30 Note��6GB RAM/ȫ��ͨ��" target="_blank">
				<img width="80" height="60" alt="Moto P30 Note��6GB RAM/ȫ��ͨ��" .src="https://2b.zol-img.com.cn/product_small/13_80x60/725/cenkIgJehjobc.jpg">
			</a>
			<p><a title="Moto P30 Note��6GB RAM/ȫ��ͨ��" href="/cell_phone/index1231213.shtml" target="_blank">Moto P30 Note��6GB RAM/ȫ..</a></p>
			<p><em class="price">��2399</em></p>
					</li>
				<li>
			<em class='n2'>4</em>									<a href="/cell_phone/index1231118.shtml" class="pic" title="��ƷYP99���ƶ�/��ͨ2G��" target="_blank">
				<img width="80" height="60" alt="��ƷYP99���ƶ�/��ͨ2G��" .src="https://2a.zol-img.com.cn/product_small/13_80x60/610/cesfKjfiQbtnw.jpg">
			</a>
			<p><a title="��ƷYP99���ƶ�/��ͨ2G��" href="/cell_phone/index1231118.shtml" target="_blank">��ƷYP99���ƶ�/��ͨ2G��</a></p>
			<p><em class="price">��99</em></p>
					</li>
				<li>
			<em class='n2'>5</em>									<a href="/cell_phone/index1231115.shtml" class="pic" title="��ƷN105C������2G��" target="_blank">
				<img width="80" height="60" alt="��ƷN105C������2G��" .src="https://2a.zol-img.com.cn/product_small/13_80x60/604/ceqdZdAXgUg.jpg">
			</a>
			<p><a title="��ƷN105C������2G��" href="/cell_phone/index1231115.shtml" target="_blank">��ƷN105C������2G��</a></p>
			<p><em class="price">��188</em></p>
					</li>
				<li>
			<em class='n2'>6</em>									<a href="/cell_phone/index1231110.shtml" class="pic" title="�ػ���F555���ƶ�/��ͨ2G��" target="_blank">
				<img width="80" height="60" alt="�ػ���F555���ƶ�/��ͨ2G��" .src="https://2f.zol-img.com.cn/product_small/13_80x60/597/ceGo156YEbBo.jpg">
			</a>
			<p><a title="�ػ���F555���ƶ�/��ͨ2G��" href="/cell_phone/index1231110.shtml" target="_blank">�ػ���F555���ƶ�/��ͨ2G��</a></p>
			<p><em class="price">��268</em></p>
					</li>
				<li>
			<em class='n2'>7</em>									<a href="/cell_phone/index1231077.shtml" class="pic" title="����S2���ƶ�/��ͨ2G��" target="_blank">
				<img width="80" height="60" alt="����S2���ƶ�/��ͨ2G��" .src="https://2f.zol-img.com.cn/product_small/13_80x60/549/ceOnjhTxZZFko.jpg">
			</a>
			<p><a title="����S2���ƶ�/��ͨ2G��" href="/cell_phone/index1231077.shtml" target="_blank">����S2���ƶ�/��ͨ2G��</a></p>
			<p><em class="price">��149</em></p>
					</li>
				<li>
			<em class='n2'>8</em>									<a href="/cell_phone/index1231075.shtml" class="pic" title="����S10���ƶ�/��ͨ2G��" target="_blank">
				<img width="80" height="60" alt="����S10���ƶ�/��ͨ2G��" .src="https://2e.zol-img.com.cn/product_small/13_80x60/548/cezFKz1OzJ72w.jpg">
			</a>
			<p><a title="����S10���ƶ�/��ͨ2G��" href="/cell_phone/index1231075.shtml" target="_blank">����S10���ƶ�/��ͨ2G��</a></p>
			<p><em class="price">��79</em></p>
					</li>
				<li>
			<em class='n2'>9</em>									<a href="/cell_phone/index1231072.shtml" class="pic" title="��ΪP20 Pro��8GB RAM/ȫ��ͨ��" target="_blank">
				<img width="80" height="60" alt="��ΪP20 Pro��8GB RAM/ȫ��ͨ��" .src="https://2b.zol-img.com.cn/product_small/13_80x60/545/cenNwGeGc8E6U.jpg">
			</a>
			<p><a title="��ΪP20 Pro��8GB RAM/ȫ��ͨ��" href="/cell_phone/index1231072.shtml" target="_blank">��ΪP20 Pro��8GB RAM/ȫ��..</a></p>
			<p><em class="price">��4488</em></p>
					</li>
				<li>
			<em class='n2'>10</em>									<a href="/cell_phone/index1231048.shtml" class="pic" title="С��8�ഺ�棨ȫ��ͨ��" target="_blank">
				<img width="80" height="60" alt="С��8�ഺ�棨ȫ��ͨ��" .src="https://2c.zol-img.com.cn/product_small/13_80x60/510/ceagwowShKfKg.jpg">
			</a>
			<p><a title="С��8�ഺ�棨ȫ��ͨ��" href="/cell_phone/index1231048.shtml" target="_blank">С��8�ഺ�棨ȫ��ͨ��</a></p>
			<p><em class="price">�����Ʒ</em></p>
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
				<a href="http://detail.zol.com.cn/subcategory.html" class="more" target="_blank">����&gt;&gt;</a>
				<h3>����Ƽ�</h3>
	</div>
		<strong class="related-category-type">������</strong>
		<ul class="related-category-list">
				<li>
									<a title="�ֻ�������" href="/mobile-demeo/" target="_blank">�ֻ�������</a>
					</li>
				<li>
									<a title="�ֻ����" href="/phonebattery/" target="_blank">�ֻ����</a>
					</li>
				<li>
									<a title="�ֻ������" href="/cellcharger/" target="_blank">�ֻ������</a>
					</li>
				<li>
									<a title="�ֻ���������" href="/phone_annex/" target="_blank">�ֻ���������</a>
					</li>
				<li>
									<a title="�ֻ���Ĥ" href="/mobile-laoding/" target="_blank">�ֻ���Ĥ</a>
					</li>
			</ul>
		<strong class="hot-category-type">�������</strong>
	<ul class="related-category-list">
		<li><a title="�ֻ�" href="/cell_phone_index/subcate57_list_1.html" target="_blank">�ֻ�</a></li>
		<li><a title="�ʼǱ�" href="/notebook_index/subcate16_list_1.html" target="_blank">�ʼǱ�</a></li>
		<li><a title="�������" href="/digital_camera_index/subcate15_list_1.html" target="_blank">�������</a></li>
		<li><a title="ƽ�����" href="/tablepc/" target="_blank">ƽ�����</a></li>
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