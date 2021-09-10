#!/usr/bin/env python
# encoding: utf-8

row_data = [
    {
        'name': '红豆',
        'goods_brief': '红豆可增加肠胃蠕动,减少便秘,促进排尿。可在睡前将红豆用电锅炖煮浸泡一段时间,隔天将无糖的红豆汤水当开水喝,能有效促进排毒。',
        'image': 'goods/images/red_bean.jpg',
        'type': 'sqz'
    },
    {
        'name': '薏米仁',
        'goods_brief': '薏仁可促进体内血液循环、水分代谢,发挥利尿消肿的效果,有助于改善水肿型肥胖。薏仁水是不错的排毒方法,直接将薏仁用开水煮烂后,适个人口味添加少许的糖,是肌肤美白的天然保养品。',
        'image': 'goods/images/ymr.jpg',
        'type': 'sqz'
    },
    {
        'name': '姜片',
        'goods_brief': '吃生姜对于排湿是有帮助的，生姜是温性食物，温性的食物能够帮助排湿。造成身体湿气过重，一方面是因为饮食出现错误导致的，例如，吃了凉性的食物;另一方面则是身体自身调节出现紊乱，新陈代谢出现失调。而想要把湿气排出，这个时候就不得不依靠脾部进行，因而健脾化湿的食物都是不错的选择。而生姜刚好有解表化湿的作用，能够温养脾胃，对于减少内湿的形成是非常有帮助的。',
        'image': 'goods/images/ginger.jpg',
        'type': 'sqz'
    },
    {
        'name': '白酒',
        'goods_brief': '有节制适量喝酒对去湿气很有效。如果不能喝酒，则可以用酒做姜汤(往姜汤里加点酒)，如果能耐住那个酒味，就用白酒；如果完全喝不惯酒，就加甜酒或是黄酒。',
        'image': 'goods/images/white_wine.jpg',
        'type': 'sqz'
    },
    {
        'name': '艾叶',
        'goods_brief': '在药理研究方面发现艾叶有抗菌、抗病毒、平喘、镇咳、祛痰、抗过敏、止血和抗凝血、增强免疫功能等作用。用艾叶水泡脚能有效的祛虚火、寒火，可以治疗门腔溃疡、咽喉肿痛、牙周炎、牙龈炎、中耳炎等头面部反复发作的与虚火、寒火有关的疾病。',
        'image': 'goods/images/ay.jpg',
        'type': 'sqz'
    },
    {
        'name': '马齿苋',
        'goods_brief': '马齿苋性寒，味酸，无毒，入肝、脾、大肠三经，有疏肝理气，健脾养胃，润肠解毒、消肿之功效。',
        'image': 'goods/images/mc.jpg',
        'type': 'sqz'
    },
    {
        'name': '冬瓜',
        'goods_brief': '冬瓜是日常生活中比较常见的食物,冬瓜具有利尿消肿的功效,经常食用冬瓜可以去除湿气',
        'image': 'goods/images/dg.jpg',
        'type': 'sqz'
    },
    {
        'name': '水芹',
        'goods_brief': '平肝清热、清肠利便、降低血压',
        'image': 'goods/images/celery.jpg',
        'type': 'sqz'
    },
    {
        'name': '洋葱',
        'goods_brief': '促进消化、杀菌消炎、祛痰利尿',
        'image': 'goods/images/onion.jpg',
        'type': 'sqz'
    },
    {
        'name': '玉米',
        'goods_brief': '益肺宁心、健脾开胃、利水通淋',
        'image': 'goods/images/ym.jpg',
        'type': 'sqz'
    },
    {
        'name': '黑豆',
        'goods_brief': '黑豆能起到不错的补肾效果，从而这也能为肾脏进行精气的补充，防止头发脱落以及促进新发的生长。',
        'image': 'goods/images/black_bean.jpg',
        'type': 'little_hair'
    },
    {
        'name': '黑芝麻',
        'goods_brief': '黑芝麻多吃可以黑发，同时也能防止脱发，有兴趣的可以试一试，而且黑芝麻对肾脏也有一定的保养效果。',
        'image': 'goods/images/hzm.jpg',
        'type': 'little_hair'
    },
    {
        'name': '牛肉',
        'goods_brief': '补气血健脾胃，并且提供大量蛋白质',
        'image': 'goods/images/steak.jpg',
        'type': 'little_hair'
    },
    {
        'name': '鸡蛋',
        'goods_brief': '鸡蛋中有很多蛋白质，维生素B12，铁，锌和其他对人体有益的物质，多吃鸡蛋可以有效地防止脱发。',
        'image': 'goods/images/egg.jpg',
        'type': 'little_hair'
    },
    {
        'name': '何首乌',
        'goods_brief': '补肝肾、益精血、乌须发、强筋骨、化浊降湿',
        'image': 'goods/images/hsw.jpg',
        'type': 'little_hair'
    },
    {
        'name': '动物肝脏',
        'goods_brief': '含有丰富的蛋白质、维生素、微量元素和胆固醇等营养物质,对促进儿童的生长发育,维持成人的身体健康都有一定的益处',
        'image': 'goods/images/gz.jpg',
        'type': 'little_hair'
    },
    {
        'name': '杂食杂粮',
        'goods_brief': '五谷杂粮中的营养素非常丰富，其中的纤维素和矿物质是普通白米的数倍，所含的维生素A、维生素B1、维生素B2、维生素C、维生素E 和钙、钾、铁、锌等微量元素，更为丰富。五谷杂粮是膳食纤维的主要来源，且大都含有较多的不饱和脂肪酸，能够提供人体必需的大多数营养素。',
        'image': 'goods/images/zl.jpg',
        'type': 'little_hair'
    },
    {
        'name': '杏仁',
        'goods_brief': '杏仁中含有丰富的维生素E，这种物质被人体摄取之后能有效的抑制细胞免受自由基的损害，从而这对于乌发、润肺都发挥重要的作用。',
        'image': 'goods/images/xr.jpg',
        'type': 'little_hair'
    },
    {
        'name': '桑葚',
        'goods_brief': '滋阴补血、补肝益肾、生津止渴、乌发明目',
        'image': 'goods/images/ss.jpg',
        'type': 'little_hair'
    },
    {
        'name': '黑豆',
        'goods_brief': '益肺宁心、健脾开胃、利水通淋',
        'image': 'goods/images/ym.jpg',
        'type': 'little_hair'
    },
    {
        'name': '枸杞',
        'goods_brief': '补肾益精，养肝明目，补血安神，生津止渴，润肺止咳。',
        'image': 'goods/images/gq.jpg',
        'type': 'little_hair'
    },
    {
        'name': '牛奶',
        'goods_brief': '牛奶中含有的色氨酸能够起到镇静的效果，而牛奶中富含的钙质能够让大脑能够更好的将这种色氨酸利用起来，将温和的牛奶盛在奶瓶中，那更会带给你一种回到幼年的温馨之感，轻轻地告诉你“放松些，一切都很好”。',
        'image': 'goods/images/milk.jpg',
        'type': 'poor_sleep'
    },
    {
        'name': '小米',
        'goods_brief': '在所有谷物中，小米含色氨酸最为丰富。此外，小米含有大量淀粉，吃后容易让人产生温饱感，可以促进胰岛素的分泌，提高进入脑内的色氨酸数量。',
        'image': 'goods/images/xm.jpg',
        'type': 'poor_sleep'
    },
    {
        'name': '莲子',
        'goods_brief': '莲子有安神功效。莲子含有莲心碱、芸香甙等成分，具有镇静作用。睡前可将莲子用水煎，加盐少许服用或将莲子煮熟加白糖食用。',
        'image': 'goods/images/lz.jpg',
        'type': 'poor_sleep'
    },
    {
        'name': '全麦面包',
        'goods_brief': '全麦面包是一种相对而言比较健康的面包，里面含有丰富的维生素，而这些维生素则能够缓解情绪，促进睡眠，改善睡眠质量。',
        'image': 'goods/images/qmmb.jpg',
        'type': 'poor_sleep'
    },
    {
        'name': '龙眼肉',
        'goods_brief': '龙眼肉具有补心益脑、养血安神之功效。临睡前饮用龙眼茶或取龙眼加白糖煎汤饮服，均可改善睡眠。',
        'image': 'goods/images/lyr.jpg',
        'type': 'poor_sleep'
    },
    {
        'name': '苹果',
        'goods_brief': '苹果中含有果糖、苹果酸，还有浓郁的芳香。可诱发机体产生血清素，有助于人们进入梦乡。',
        'image': 'goods/images/apple.jpg',
        'type': 'poor_sleep'
    },
    {
        'name': '核桃',
        'goods_brief': '在临床上，核桃被证明可以改善睡眠质量，因此常用来治疗神经衰弱、失眠、健忘、多梦等症状。具体吃法是配以黑芝麻，捣成糊状，睡前服用15克，效果非常明显。',
        'image': 'goods/images/ht.jpg',
        'type': 'poor_sleep'
    },
    {
        'name': '葵花子',
        'goods_brief': '葵花子含多种氨基酸和维生素，可调节新陈代谢，改善脑细胞抑制机能，起到镇静安神的作用。晚餐后嗑一些葵花子，还可以促进消化液分泌，有利于消食化滞，帮助睡眠。',
        'image': 'goods/images/khz.jpg',
        'type': 'poor_sleep'
    },
    {
        'name': '香蕉',
        'goods_brief': '香蕉实际上就是包着果皮的“安眠药”，它除了含有丰富的复合胺和N-乙酰-5-甲氧基色胺之外，还富有能使肌肉放松的镁。',
        'image': 'goods/images/banana.jpg',
        'type': 'poor_sleep'
    },
    {
        'name': '土豆',
        'goods_brief': '一个小小的烤土豆是不会破坏你的胃肠道的，相反它能够清除那些妨碍色氨酸发挥催眠作用的酸化合物。如果混合温奶做成土豆泥的话，效果会更加的棒哦！',
        'image': 'goods/images/potato.jpg',
        'type': 'poor_sleep'
    },
    {
        'name': '牛初乳',
        'goods_brief': '牛初乳里面的营养丰富，有许多免疫活性成分，这些免疫活性成分的作用很大，可以维持机体免疫功能自稳态，并且还能够提高机体免疫功能。',
        'image': 'goods/images/ncr.jpg',
        'type': 'low_dkl'
    },
    {
        'name': '海鲜',
        'goods_brief': '海鲜的营养价值可是极其丰富的，像铁，锌，镁等营养素含量都十分丰富。经常食用海鲜是有利于提高我们身体免疫力的。',
        'image': 'goods/images/seafood.jpg',
        'type': 'low_dkl'
    },
    {
        'name': '食用菌类',
        'goods_brief': '这指的是是蘑菇、香菇、猴头菇、草菇、黑木耳、银耳、百合、灵芝等食物，这些食物都可以增强免疫力。尤其是灵芝含有抗癌成分，含有丰富的锗元素，可加速身体代谢，延缓细胞衰老。',
        'image': 'goods/images/mg.jpg',
        'type': 'low_dkl'
    },
    {
        'name': '橄榄油',
        'goods_brief': '单不饱和脂肪酸有助于改善我们的抵抗力，提高我们的免疫功能。',
        'image': 'goods/images/gly.jpg',
        'type': 'low_dkl'
    },
    {
        'name': '螺旋藻',
        'goods_brief': '其蛋白质含量高达60%—70%，含有丰富的胡萝卜素、维生素E、维生素C，可纠正酸性体质，从而提高人体免疫力。',
        'image': 'goods/images/lxz.jpg',
        'type': 'low_dkl'
    },
    {
        'name': '萝卜',
        'goods_brief': '萝卜中含有丰富的干扰素，以及一系列的维生素，能够帮助我们有效地提高身体的免疫力。',
        'image': 'goods/images/lb.jpg',
        'type': 'low_dkl'
    },
    {
        'name': '大蒜',
        'goods_brief': '英国研究人员的实验结果表明，食用大蒜可让感冒发生几率降低2/3。它还是保护肝脏及心血管的正常功能、调节血糖、降血脂、预防动脉硬化的最佳配料，经常咀嚼大蒜的人患结肠癌和胃癌的几率也会大大降低。因此，建议每天生吃两瓣蒜，们最好是切成碎末状，当作配料来使用，在烹饪菜肴时加入一些大蒜末。',
        'image': 'goods/images/ds.jpg',
        'type': 'low_dkl'
    },
    {
        'name': '红薯',
        'goods_brief': '可以增强皮肤抵抗力。皮肤是人体免疫系统的一员，是人体抵抗细菌、病毒等一切外界侵袭的第一道屏障，维生素A则在缔造皮肤组织的过程中起到重要作用，补充维生素A最有效的方法则是从食物中获取β胡萝卜素，红薯是获得这种营养的最快途径，它含有丰富的β胡萝卜素，且热量低。',
        'image': 'goods/images/hs.jpg',
        'type': 'low_dkl'
    },
    {
        'name': '蜂胶',
        'goods_brief': '蜂胶能提高人体巨噬细胞吞噬病毒、细菌的能力，使机体免疫系统处于动态平衡的最佳状态，被称为“天然的免疫增强剂”。 ',
        'image': 'goods/images/fj.jpg',
        'type': 'low_dkl'
    },
    {
        'name': '茶',
        'goods_brief': '研究表明，茶叶中所含有的茶氨酸可以增强免疫细胞的活性，及时消灭想入侵身体的细菌',
        'image': 'goods/images/tea.jpg',
        'type': 'low_dkl'
    }
]

pass
