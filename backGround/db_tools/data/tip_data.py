#!/usr/bin/env python
# encoding: utf-8

row_data = [
    {
        'content': '忌油腻，少吃油炸和肥肉',
        'type': 'sqz'
    },
    {
        'content': '多运动，运动可以让人体以更健康的方式排出汗液，流出的汗水带走的也是体内多余出来的水分，所以说祛湿千万不能忽略了运动',
        'type': 'sqz'
    },
    {
        'content': '切忌直接躺倒地板上玩手机、看书甚至睡觉，，地板里的湿气是很重的，想要祛湿千万不能这样做',
        'type': 'sqz'
    },
    {
        'content': '吃点利水、利尿的食物，或者能起到清热、祛湿的食物，多吃蔬菜水果',
        'type': 'sqz'
    },
    {
        'content': '不要贪凉，出汗后不要立马喝冷饮吃冰淇淋',
        'type': 'sqz'
    },
    {
        'content': '天气潮湿时候不要开窗，拖地，洗衣服',
        'type': 'sqz'
    },
    {
        'content': '适当性吃辣椒和喝点白酒可以排除身体的湿气',
        'type': 'sqz'
    },
    {
        'content': '拔罐可以有效去除身体内的湿气，但是也容易引发其他疾病，所以拔罐后保护好身体，不要洗澡，隔上一天再洗澡',
        'type': 'sqz'
    },
    {
        'content': '饮食清淡，不要过咸，炒菜少放盐',
        'type': 'sqz'
    },
    {
        'content': '早上吃点姜片，姜片可以使身体发热，有热量排除，导出湿气',
        'type': 'sqz'
    },
    {
        'content': '少吹空调',
        'type': 'sqz'
    },
    {
        'content': '如果人的压力特别大，就容易大把大把的掉头发，所以为了不秃顶，那么就不要给自己太大的压力，放松心情',
        'type': 'little_hair'
    },
    {
        'content': '头发也要吸收营养，可以吃一些如黑芝麻、黑豆等对头发好的食物',
        'type': 'little_hair'
    },
    {
        'content': '反省一下自己最近是否睡得特别晚，如果是，那么就不要再熬夜了',
        'type': 'little_hair'
    },
    {
        'content': '头发太长了，吸收的营养就会多，为了让头发的营养跟的上，不脱发，那么就把头发剪短吧！',
        'type': 'little_hair'
    },
    {
        'content': '洗头发的时候一定要洗干净，至少洗10分钟，条件允许可以用生姜洗头发',
        'type': 'little_hair'
    },
    {
        'content': '多吃富含蛋白质的食物',
        'type': 'little_hair'
    },
    {
        'content': '选择弱酸性洗发露，适当的按摩头皮',
        'type': 'little_hair'
    },
    {
        'content': '白天洗发，不要晚上洗发，切忌湿着头发睡觉。',
        'type': 'little_hair'
    },
    {
        'content': '少抽烟',
        'type': 'little_hair'
    },
    {
        'content': '炒菜不要放太多味精',
        'type': 'little_hair'
    },
    {
        'content': '补肾',
        'type': 'little_hair'
    },
    {
        'content': '睡前多做一些小运动，但是不要做过于激烈的运动，就跑跑步、散散步、打一下太极拳之类的就可以了',
        'type': 'poor_sleep'
    },
    {
        'content': '不要喝咖啡和茶等一些刺激性的重口味的东西，睡前的话，喝一杯牛奶或者温水是比较好的',
        'type': 'poor_sleep'
    },
    {
        'content': '避免思虑过度。临睡前的两个小时最好不要看一些要动脑思考的电影书籍',
        'type': 'poor_sleep'
    },
    {
        'content': '多泡脚。每天晚上用热水泡泡脚，十多分钟即可',
        'type': 'poor_sleep'
    },
    {
        'content': '睡前按摩。在睡觉之前也可以做一些简单的按摩，帮助放松身体肌肉，对提高睡眠质量也有帮助',
        'type': 'poor_sleep'
    },
    {
        'content': '晚饭少而精。一定要注意晚上不要吃太多东西',
        'type': 'poor_sleep'
    },
    {
        'content': '保证规律的睡眠，生活规律',
        'type': 'poor_sleep'
    },
    {
        'content': '睡觉前想着自己头皮松了',
        'type': 'poor_sleep'
    },
    {
        'content': '当你真的很疲倦的时候你再睡，不要很逼着自己睡',
        'type': 'poor_sleep'
    },
    {
        'content': '睡觉姿势侧卧最佳',
        'type': 'poor_sleep'
    },
    {
        'content': '全面均衡营养，不要挑食，保证摄取各种微量元素',
        'type': 'low_dkl'
    },
    {
        'content': '劳逸结合，切忌过劳过逸',
        'type': 'low_dkl'
    },
    {
        'content': '适当的进行有氧运动，如爬山、快步走等',
        'type': 'low_dkl'
    },
    {
        'content': '放松心情，缓解压力，多进行一些娱乐项目',
        'type': 'low_dkl'
    },
    {
        'content': '按揉足三里穴、涌泉穴，以酸胀感为宜',
        'type': 'low_dkl'
    },
    {
        'content': '规律生活，作息要有规律，避免过度熬夜，保证充足的睡眠',
        'type': 'low_dkl'
    },
    {
        'content': '多饮水，利于体内排毒，加快病毒的排出，一天至少1L水',
        'type': 'low_dkl'
    },
    {
        'content': '补充维生素。每天水果大约200克，可以在加餐的时候吃，保证维生素的摄入',
        'type': 'low_dkl'
    },
    {
        'content': '每天晒晒太阳是有助于钙元素的吸收的，还能提高身体的免疫力，早上八九点和下午四五点的太阳晒起来会比较舒服',
        'type': 'low_dkl'
    },
    {
        'content': '亲近自然，多在森林中呼吸一下新鲜空气，摄入自然因子负离子',
        'type': 'low_dkl'
    }
]

pass