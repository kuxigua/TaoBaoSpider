# TaoBaoSpider
淘宝关键词爬虫
### AntiReptile包实现反爬虫功能，主要用于破解阿里反爬机制
 - 经测试已经可以破解阿里巴巴滑动验证码，由于不是同一台机器，所以并没有配置到爬虫中
 -  imgCodeHandle： 破解爬虫是出现的滑块验证码，需要注意使用的Chrome版本，版本不对是破解不了验证码的
 - 后期需要增加ip代理， cookies代理池，尽量避免滑块验证码出现，毕竟打开浏览器破解验证码，并重新获取cookies需要很长时间
### config : 用于配置
 - config 配置文件
### DataHandle: 数据处理
 - dataHandle： 处理返回的不标准的JavaScript Json数据，返回商品信息列表
 - urlStitching: 生成100页淘宝url数据信息
 - 提取数据, 只提取了标题和图片url
 
 
 瑞士进口怀尔德美白牙膏牙齿美白去口臭牙
//g-search1.alicdn.com/img/bao/uploaded/i4/imgextra/i4/125908813/TB2zRCfniMnBKNjSZFzXXc_qVXa_!!0-saturn_solar.jpg
德国泰瑞美儿童牙膏婴儿宝宝可吞咽防蛀牙
//g-search1.alicdn.com/img/bao/uploaded/i4/imgextra/i4/116504913/O1CN01YaMMcP1mACMt8RVKr_!!0-saturn_solar.jpg
舒客早晚牙膏6只美白去口臭抗敏感清火
//g-search1.alicdn.com/img/bao/uploaded/i4/imgextra/i1/95596204/TB2ZJE6dqSWBuNjSsrbXXa0mVXa_!!0-saturn_solar.jpg
高露洁小苏打牙膏包邮去口臭清新口气美白去黄去牙渍家用套装正品
//g-search2.alicdn.com/img/bao/uploaded/i4/i2/1818112330/O1CN01HrutCd1T5BKTBN4Lr_!!0-item_pic.jpg
联合利华中华魔丽迅白牙齿美白笔正品1.95ml
//g-search1.alicdn.com/img/bao/uploaded/i4/i3/700459267/O1CN01jHLOb82IKKqH3eQw5_!!0-item_pic.jpg
正品包邮云南白药牙膏去口臭薄荷210g*4支大规格套装去火清新口气
//g-search3.alicdn.com/img/bao/uploaded/i4/i2/3394916097/O1CN01voLiJO1uuTJFhzVR9_!!0-item_pic.jpg
舒客美白去黄去口臭家用牙膏舒克口气清新去牙渍男女组合家庭装
//g-search1.alicdn.com/img/bao/uploaded/i4/i2/3010156995/O1CN0121XkwlUkvCSSn4i_!!0-item_pic.jpg
舒客舒克宝贝儿童牙膏可吞咽3-6-12岁换牙期正品牙刷套装宝宝小孩
//g-search3.alicdn.com/img/bao/uploaded/i4/i4/3027930901/O1CN01E42nTp1IWhLHevVpP_!!0-item_pic.jpg
参半燕窝冷杉牙膏家庭装亮白牙齿清新口气去黄成人牙膏家用120g*2
//g-search2.alicdn.com/img/bao/uploaded/i4/i2/3012171978/O1CN01iZKonk1QTxukPTeVA_!!0-item_pic.jpg
云南白药牙膏薄荷清爽型210g减轻牙龈问题祛异味清新口气包邮
//g-search3.alicdn.com/img/bao/uploaded/i4/i3/2346229159/O1CN01FW4bS42HWs3TAdEto_!!0-item_pic.jpg
日本进口ora2皓乐齿果味牙膏3支清新口气吸附异味
//g-search2.alicdn.com/img/bao/uploaded/i4/i1/1748416497/O1CN018dVBF81xrfjreuzim_!!0-item_pic.jpg
牙美南京同仁堂正品牙齿牙黄护理牙膏官网靓齿佳清新洁白慕斯喷剂
//g-search3.alicdn.com/img/bao/uploaded/i4/i3/2200611606038/O1CN01HV6RG01uTRwYH5vEX_!!2200611606038.jpg
纳美白牙膏纳美小苏打牙膏去牙渍去黄清新口气减轻口臭包邮205g
//g-search2.alicdn.com/img/bao/uploaded/i4/i4/1015804794/TB1V4N3bkZmBKNjSZPiXXXFNVXa_!!0-item_pic.jpg
口腔管家7日健白亮齿买一发7
//g-search3.alicdn.com/img/bao/uploaded/i4/i1/1911180117/O1CN01hHA5jA1Cjcpl5EWLP_!!1911180117.jpg
elmex0-6岁儿童防蛀固齿牙膏50ml原装进口
//g-search3.alicdn.com/img/bao/uploaded/i4/i1/3548057076/O1CN01FRaPAN228r3kHdYXU_!!0-item_pic.jpg
参半燕窝牙膏亮白牙齿去黄去牙渍清新口气液体牙膏成人家用120g
//g-search3.alicdn.com/img/bao/uploaded/i4/i4/3012171978/O1CN01XFh09w1QTxusH3zvv_!!0-item_pic.jpg
联合利华中华金纯牙膏魔丽迅白冰晶双重薄荷正品170g*3孟美岐同款
//g-search3.alicdn.com/img/bao/uploaded/i4/i2/700459267/O1CN01IvRYFf2IKKqFBgcIL_!!0-item_pic.jpg
洁灵改善溃疡问题牙膏2支适用嘴巴口腔起泡黏膜溃破口舌上火疼痛
//g-search2.alicdn.com/img/bao/uploaded/i4/i1/2345687106/O1CN01YiVwgT22MawRz4wz9_!!0-item_pic.jpg
冷酸灵极地白双支装套装按压式牙膏官网正品美白牙膏套装清薄荷味
//g-search2.alicdn.com/img/bao/uploaded/i4/i3/1071280830/O1CN01TW8JMr1I0BEYT2mkj_!!0-item_pic.jpg
按压式牙膏440g
//g-search2.alicdn.com/img/bao/uploaded/i4/i2/1672884924/O1CN01Eixwbk1mFEiw3XSzz_!!1672884924.jpg
云南白药牙膏薄荷清爽型210g*4支装缓解牙龈出血口腔问题清新口气
//g-search2.alicdn.com/img/bao/uploaded/i4/i3/2448339147/O1CN019HR88f2HRNIYz5cR7_!!0-item_pic.jpg
【3支任选】新西兰进口RedSeal/红印牙膏护龈去渍亮白清新口气
//g-search3.alicdn.com/img/bao/uploaded/i4/i2/2608180479/O1CN01KXNnTC1FPQDSCaZ78_!!0-item_pic.jpg
洁灵改善牙周问题牙膏两支牙周袋红肿疼痛牙龈萎缩口腔牙齿松动
//g-search2.alicdn.com/img/bao/uploaded/i4/i4/2345687106/O1CN01MmG57I22MawUN9CsG_!!0-item_pic.jpg
草珊瑚牙膏美白去黄口气清新去口臭烟渍牙齿亮白家用套装2支250g
//g-search3.alicdn.com/img/bao/uploaded/i4/i4/2408174527/O1CN01WUHyKm1jJPU6MwIde_!!0-item_pic.jpg
联合利华中华魔丽迅白魅力牙膏金纯薄荷味清新口气170g*3家庭套装
//g-search1.alicdn.com/img/bao/uploaded/i4/i2/700459267/O1CN01pFhHrH2IKKqA4T0g4_!!0-item_pic.jpg
正品avecmoi海洋之风均衡牙膏益生菌去口臭牙菌斑口气清新送牙刷
//g-search3.alicdn.com/img/bao/uploaded/i4/i3/1696187918/O1CN01mf2hTB28MUY1ScLV6_!!0-item_pic.jpg
LION/狮王日本进口齿力佳酵素儿童牙膏60g*2支巧虎版牙膏防蛀固齿
//g-search1.alicdn.com/img/bao/uploaded/i4/i4/605623409/O1CN01VnToLB1b3MgBa90s4_!!0-item_pic.jpg
无限极植雅牙膏口气清新清洁牙齿官方旗艦店官网正品140克2支装
//g-search1.alicdn.com/img/bao/uploaded/i4/i2/4084364047/O1CN019KSCqY1flZN1aCcEg_!!0-item_pic.jpg
 