from pyquery import PyQuery as pq


class StudyInfo:
    p0 = pq(filename='/root/fg/pycharm_project_FgBlog/FgBlog/paragraph/dtmdjjb.html')('body').html()
    studyInfo0 = {
        'imsgp': p0,
        'menulist': ['锚点的基本实现方法', '通过a标签直接跳转', '通过js方法跳转', '动态锚点的实现方法', '进坑的做法', '改良的做法'],
        'imsg': '动态锚点的实现和踩坑',
        'imsgb': '博客开发过程中，文章要使用动态锚点时总结',
        'imsgt': '2020-12-04',
        'heightList': [0, 100, 200, 300, 9999],
        'munNum': [1, 2, 3, 4, 5]
    }
    p1 = pq(filename='/root/fg/pycharm_project_FgBlog/FgBlog/paragraph/htscHomeSwiper.html')('body').html()
    studyInfo1 = {
        'imsgp': p1,
        'menulist': ['仿写一个轮播组件', '分析仿写对象', '内容盒子', '轮播组件盒子', '组装和JS'],
        'imsg': '华泰官网--华泰观点底部轮播组件仿写',
        'imsgb': '记录抄袭一个轮播组件',
        'imsgt': '2020-12-04',
        'heightList': [0, 100, 200, 300, 9999],
        'munNum': [1, 2, 3, 4]
    }

    p2 = pq(filename='/root/fg/pycharm_project_FgBlog/FgBlog/paragraph/backEndCros.html')('body').html()
    studyInfo2 = {
        'imsgp': p2,
        'menulist': ['Django后端', '事情是这样的', '具体操作是这样的', '别的方法'],
        'imsg': 'Django后端跨域问题',
        'imsgb': 'vue-cli启动服务，本地页面调阿里云后端接口的跨域问题解决',
        'imsgt': '2020-12-04',
        'heightList': [0, 100, 200, 300, 9999],
        'munNum': [1, 2, 3]
    }

    p3 = pq(filename='/root/fg/pycharm_project_FgBlog/FgBlog/paragraph/pyquery.html')('body').html()
    studyInfo3 = {
        'imsgp': p3,
        'menulist': ['pyquery读html文件乱码', '故事背景', '解决思路', '具体操作'],
        'imsg': 'pyquery 解析乱码的处理',
        'imsgb': '后端用文件存富文本，pyquery解析传到前端的踩坑',
        'imsgt': '2021-03-03',
        'heightList': [0, 100, 200, 300, 9999],
        'munNum': [1, 2, 3]
    }

    p4 = pq(filename='/root/fg/pycharm_project_FgBlog/FgBlog/paragraph/isValidBST.html')('body').html()
    studyInfo4 = {
        'imsgp': p4,
        'menulist': ['验证二叉搜索树', '递归'],
        'imsg': '验证二叉搜索树',
        'imsgb': 'leetcode解题',
        'imsgt': '2021-03-04',
        'heightList': [0, 100, 200, 300, 9999],
        'munNum': [1]
    }

    p5 = pq(filename='/root/fg/pycharm_project_FgBlog/FgBlog/paragraph/NQueen.html')('body').html()
    studyInfo5 = {
        'imsgp': p5,
        'menulist': ['N 皇后', '递归'],
        'imsg': 'N 皇后',
        'imsgb': 'leetcode解题',
        'imsgt': '2021-03-08',
        'heightList': [0, 100, 200, 300, 9999],
        'munNum': [1]
    }

    p6 = pq(filename='/root/fg/pycharm_project_FgBlog/FgBlog/paragraph/人工智能必备数学知识-函数.html')('body').html()
    studyInfo6 = {
        'imsgp': p6,
        'menulist': ['函数 - 人工智能的本质', '函数定义', '函数类型', '函数性质', '多元函数和人工智能的关系', '代码题'],
        'imsg': '人工智能必备数学知识-函数',
        'imsgb': '人工智能学习笔记',
        'imsgt': '2021-03-10',
        'heightList': [0, 100, 200, 300, 9999],
        'munNum': [1, 2, 3, 4, 5]
    }

    p7 = pq(filename='/root/fg/pycharm_project_FgBlog/FgBlog/paragraph/人工智能必备数学知识-微积分.html')('body').html()
    studyInfo7 = {
        'imsgp': p7,
        'menulist': ['微积分 - 机器学习的学习原理', '极限', '导数', '积分', '代码题'],
        'imsg': '人工智能必备数学知识-微积分',
        'imsgb': '人工智能学习笔记',
        'imsgt': '2021-03-10',
        'heightList': [0, 100, 200, 300, 9999],
        'munNum': [1, 2, 3, 4]
    }

    p8 = pq(filename='/root/fg/pycharm_project_FgBlog/FgBlog/paragraph/人工智能必备数学知识-矩阵运算.html')('body').html()
    studyInfo8 = {
        'imsgp': p8,
        'menulist': ['矩阵运算 - 神经网络的底层肌理', '矩阵介绍', '矩阵计算与人工智能', '矩阵基本运算', '向量', '代码题'],
        'imsg': '人工智能必备数学知识-矩阵运算',
        'imsgb': '人工智能学习笔记',
        'imsgt': '2021-03-10',
        'heightList': [0, 100, 200, 300, 9999],
        'munNum': [1, 2, 3, 4, 5]
    }

    p9 = pq(filename='/root/fg/pycharm_project_FgBlog/FgBlog/paragraph/人工智能必备数学知识-概率于统计.html')('body').html()
    studyInfo9 = {
        'imsgp': p9,
        'menulist': ['概率与统计 - 评估和优化AI模型的表现', '概率', '统计', '分布', '代码题'],
        'imsg': '人工智能必备数学知识-概率与统计',
        'imsgb': '人工智能学习笔记',
        'imsgt': '2021-03-11',
        'heightList': [0, 100, 200, 300, 9999],
        'munNum': [1, 2, 3, 4]
    }

    p10 = pq(filename='/root/fg/pycharm_project_FgBlog/FgBlog/paragraph/人工智能必备数学知识-线性回归.html')('body').html()
    studyInfo10 = {
        'imsgp': p10,
        'menulist': ['线性回归 — 一个典型的机器学习', '人工智能', '回归', '代码题'],
        'imsg': '人工智能必备数学知识-线性回归',
        'imsgb': '人工智能学习笔记',
        'imsgt': '2021-03-13',
        'heightList': [0, 100, 200, 300, 9999],
        'munNum': [1, 2, 3]
    }

    p11 = pq(filename='/root/fg/pycharm_project_FgBlog/FgBlog/paragraph/人工智能必备数学知识-逻辑运算.html')('body').html()
    studyInfo11 = {
        'imsgp': p11,
        'menulist': ['逻辑计算 - 人工智能模型的应用于配套', '背景', '运算', '搭配AI配套模型实现具体'],
        'imsg': '人工智能必备数学知识-逻辑计算',
        'imsgb': '人工智能学习笔记',
        'imsgt': '2021-03-15',
        'heightList': [0, 100, 200, 300, 9999],
        'munNum': [1, 2, 3]
    }

    p12 = pq(filename='/root/fg/pycharm_project_FgBlog/FgBlog/paragraph/人工智能必备数学知识-马尔科夫链.html')('body').html()
    studyInfo12 = {
        'imsgp': p12,
        'menulist': ['马尔科夫链 - 强化学习的基础', '定义', '样例', '马尔科夫链收敛和平稳条件', '马尔科夫奖励过程', '马尔科夫决策过程'],
        'imsg': '人工智能必备数学知识-马尔科夫链',
        'imsgb': '人工智能学习笔记',
        'imsgt': '2021-03-15',
        'heightList': [0, 100, 200, 300, 9999],
        'munNum': [1, 2, 3, 4, 5]
    }

    p13 = pq(filename='/root/fg/pycharm_project_FgBlog/FgBlog/paragraph/SequentialDigits.html')('body').html()
    studyInfo13 = {
        'imsgp': p13,
        'menulist': ['顺次数', '需求分析', '解法一', '解法二', '解法三', '解法四'],
        'imsg': '顺次数',
        'imsgb': 'leetcode解题',
        'imsgt': '2021-03-16',
        'heightList': [0, 100, 200, 300, 9999],
        'munNum': [1, 2, 3, 4, 5]
    }

    p14 = pq(filename='/root/fg/pycharm_project_FgBlog/FgBlog/paragraph/PalindromePermutationLCCI.html')('body').html()
    studyInfo14 = {
        'imsgp': p14,
        'menulist': ['回文排列', '字典', '栈'],
        'imsg': '回文排列',
        'imsgb': 'leetcode解题',
        'imsgt': '2021-03-19',
        'heightList': [0, 100, 200, 300, 9999],
        'munNum': [1, 2]
    }


    p15 = pq(filename='/root/fg/pycharm_project_FgBlog/FgBlog/paragraph/人工智能-机器学习介绍.html')('body').html()
    studyInfo15 = {
        'imsgp': p15,
        'menulist': ['人工智能-机器学习介绍', '引子', '机器学习的应用场景', '学习框架', '四大学习方法类别', '四大方法的应用场景'],
        'imsg': '人工智能-机器学习介绍',
        'imsgb': '人工智能学习笔记',
        'imsgt': '2021-03-23',
        'heightList': [0, 100, 200, 300, 9999],
        'munNum': [1, 2, 3, 4, 5]
    }


    p16 = pq(filename='/root/fg/pycharm_project_FgBlog/FgBlog/paragraph/人工智能-线性回归模型.html')('body').html()
    studyInfo16 = {
        'imsgp': p16,
        'menulist': ['人工智能-线性回归模型', '先来一个问题', '梯度下降法', '机器学习处理问题实战'],
        'imsg': '人工智能-线性回归模型',
        'imsgb': '人工智能学习笔记',
        'imsgt': '2021-03-23',
        'heightList': [0, 100, 200, 300, 9999],
        'munNum': [1, 2, 3]
    }

    p17 = pq(filename='/root/fg/pycharm_project_FgBlog/FgBlog/paragraph/MaximumSwap.html')('body').html()
    studyInfo17 = {
        'imsgp': p17,
        'menulist': ['最大交换', '题目分析', '解法一', '解法二'],
        'imsg': '最大交换',
        'imsgb': 'leetcode解题',
        'imsgt': '2021-03-23',
        'heightList': [0, 100, 200, 300, 9999],
        'munNum': [1, 2, 3]
    }

    p18 = pq(filename='/root/fg/pycharm_project_FgBlog/FgBlog/paragraph/Django正则接口+vue路由.html')('body').html()
    studyInfo18 = {
        'imsgp': p18,
        'menulist': ['Django正则接口+vue路由', '前情提要', '出现问题', '面向百度编程'],
        'imsg': 'Django正则接口+vue路由',
        'imsgb': '代码开发填坑',
        'imsgt': '2021-03-24',
        'heightList': [0, 100, 200, 300, 9999],
        'munNum': [1, 2, 3]
    }

    p19 = pq(filename='/root/fg/pycharm_project_FgBlog/FgBlog/paragraph/人工智能-分类任务与逻辑回归-序.html')('body').html()
    studyInfo19 = {
        'imsgp': p19,
        'menulist': ['人工智能-分类任务与逻辑回归-序', '来一道题', '再来几道题', '基本方法', '思考一下', '知识巩固'],
        'imsg': '人工智能-分类任务与逻辑回归-序',
        'imsgb': '人工智能学习笔记',
        'imsgt': '2021-03-29',
        'heightList': [0, 100, 200, 300, 9999],
        'munNum': [1, 2, 3, 4, 5]
    }

    p20 = pq(filename='/root/fg/pycharm_project_FgBlog/FgBlog/paragraph/人工智能-分类任务与逻辑回归-逻辑回归.html')('body').html()
    studyInfo20 = {
        'imsgp': p20,
        'menulist': ['人工智能-分类任务与逻辑回归-逻辑回归', '先来道题', '逻辑回归', '怎么使用呢', '求解逻辑回归模型'],
        'imsg': '人工智能-分类任务与逻辑回归-分类预测',
        'imsgb': '人工智能学习笔记',
        'imsgt': '2021-03-29',
        'heightList': [0, 100, 200, 300, 9999],
        'munNum': [1, 2, 3, 4]
    }

    p21 = pq(filename='/root/fg/pycharm_project_FgBlog/FgBlog/paragraph/人工智能-分类任务与逻辑回归-代码实战(一).html')('body').html()
    studyInfo21 = {
        'imsgp': p21,
        'menulist': ['人工智能-分类任务与逻辑回归-代码实战(一)', '今天做这道题', '做题流程', '实战代码'],
        'imsg': '人工智能-分类任务与逻辑回归-代码实战(一)',
        'imsgb': '人工智能学习笔记',
        'imsgt': '2021-03-29',
        'heightList': [0, 100, 200, 300, 9999],
        'munNum': [1, 2, 3]
    }

    p22 = pq(filename='/root/fg/pycharm_project_FgBlog/FgBlog/paragraph/人工智能-分类任务与逻辑回归-代码实战(二).html')('body').html()
    studyInfo22 = {
        'imsgp': p22,
        'menulist': ['人工智能-分类任务与逻辑回归-代码实战(二)', '今天做这道题', '直接开做', '增加二次项，从新敲一次代码', '看看最后的图'],
        'imsg': '人工智能-分类任务与逻辑回归-代码实战(二)',
        'imsgb': '人工智能学习笔记',
        'imsgt': '2021-04-1',
        'heightList': [0, 100, 200, 300, 9999],
        'munNum': [1, 2, 3, 4]
    }

    p23 = pq(filename='/root/fg/pycharm_project_FgBlog/FgBlog/paragraph/人工智能-其他分类技术-kNN模型.html')('body').html()
    studyInfo23 = {
        'imsgp': p23,
        'menulist': ['人工智能-其他分类技术-kNN模型', 'kNN-k近邻分类模型', 'kNN模型算法步骤', 'kNN里的距离计算方式', '看一个kNN的分类图', '网上抄的', '交叉验证法'],
        'imsg': '人工智能-分类任务与逻辑回归-代码实战(二)',
        'imsgb': '人工智能学习笔记',
        'imsgt': '2021-04-1',
        'heightList': [0, 100, 200, 300, 9999],
        'munNum': [1, 2, 3, 4, 5, 6]
    }

    studyInfo = [studyInfo0, studyInfo1, studyInfo2, studyInfo3, studyInfo4, studyInfo5, studyInfo6, studyInfo7,
                 studyInfo8, studyInfo9, studyInfo10, studyInfo11, studyInfo12, studyInfo13, studyInfo14, studyInfo15,
                 studyInfo16, studyInfo17, studyInfo18, studyInfo19, studyInfo20, studyInfo21, studyInfo22, studyInfo23
                 ]

    studyType = {
        'front-end': '<h2>前端:</h2><h3 style="text-indent:2em; margin-top: 15px;">B站填坑:</h3><p style="text-indent:4em; ">B站看到视频的学习记录，好看的组件、厉害的动画、炫酷的交互</p><h3 style="text-indent:2em; margin: 0;">源码学习:</h3><p style="text-indent:4em;">记录读源码，写源码的过程和心得</p><h3 style="text-indent:2em; margin: 0;">开发记录:</h3><p style="text-indent:4em;">博客开发过程中遇到的坑呀、以后工作中敲代码自己写的觉得炫酷的组件呀，都会写在这里</p>',
        'back-end': '<h2>后端:</h2><h3 style="text-indent:2em; margin-top: 15px;">代码开发填坑:</h3><p style="text-indent:4em; ">记录后端开发过程中的坑</p><h3 style="text-indent:2em; margin: 0;">源码学习:</h3><p style="text-indent:4em;">记录读源码，写源码的过程和心得</p><h3 style="text-indent:2em; margin: 0;">部署填坑:</h3><p style="text-indent:4em;">一些环境设置的坑，部署服务的系统、配置、版本、兼容各方面的的坑</p>',
        'test': '<h2>测试:</h2><h3 style="text-indent:2em; margin-top: 15px;">自动化框架开发记录:</h3><p style="text-indent:4em; ">这里是个大坑，复刻印象里的华为自动化框架的开发记录</p><h3 style="text-indent:2em; margin: 0;">源码学习:</h3><p style="text-indent:4em;">记录读源码，写源码的过程和心得</p><h3 style="text-indent:2em; margin: 0;">工作心得:</h3><p style="text-indent:4em;">写一下测试工作里的各种心路历程、工作灵感</p>',
        'leetcode': '<h2>力扣:</h2><h3 style="text-indent:2em; margin-top: 15px;">刷题记录:</h3><p style="text-indent:4em; ">力扣刷题记录，包括解题思路、错题整理、性能调优</p><h3 style="text-indent:2em; margin: 0;">数据结构:</h3><p style="text-indent:4em;">数据结构的学习记录过程</p><h3 style="text-indent:2em; margin: 0;">算法:</h3><p style="text-indent:4em;">不同算法的学习、复习和对需求的应用</p>',
        'ai': '<h2>人工智能学习:</h2><h3 style="text-indent:2em; margin-top: 15px;">基础数学:</h3><p style="text-indent:4em; ">线性代数、微积分、概率等以及他们在numpy等工具中的代码实战</p><h3 style="text-indent:2em; margin: 0;">人工智能入门:</h3><p style="text-indent:4em;">机器学习：模型评估、主成分分析（PCA）、各类贝叶斯算法和具体应用</p><h3 style="text-indent:2em; margin: 0;">深度学习与计算视觉:</h3><p style="text-indent:4em;">卷积神经网络学习，经典的CNN模型学习</p>',

    }

    studyList = {
        'front-end': [
            {
                'id': '0',
                'title': '动态锚点的实现和踩坑',
                'content': '就是你文章嘛不是有个标题目录嘛，然后呢把这个目录放在文章的旁边，你一点它就跳转啦。这个时候你就需要啥呀，需要一个高亮在目录上显示你跳到哪了。然后呢再通过你的上下滚动到下个目录，这个高亮自然就会跟过去在下一个目录高亮。呐这个就是动态锚点了。还不能理解你就看看👈左边，如果你是在掘金上看的就看看👉右边，对这个目录就是动态锚点做的。'
            },
            {
                'id': '1',
                'title': '华泰官网--华泰观点底部轮播组件仿写',
                'content': '每个组件构成是上面一长图片，下面一个1行的类型，一个2行的标题，2行的日期，3行的内容，超出显示... 在动画过程的时候最左边的移动移出盒子，右边开始移进来。...'
            },
        ],
        'back-end': [
            {
                'id': '2',
                'title': 'Django后端跨域',
                'content': '我在学习vue的时候用，脚手架搭建了一个vue项目，然后呢启动项目时输入npm run serve就会在电脑上起一个node的服务嘛。然后呢我自己的Django服务呢，是部署在在阿里云的机器上的，然后vue项目调接口的时候就有个报错了，查了一下是后端禁止跨域引起的。然后就开始面向百度编程了'
            },
            {
                'id': '3',
                'title': 'pyquery 解析乱码的处理',
                'content': '我的后端需要传一个富文本，但是呢数据库保存一个富文本太长了。我就把富文本写到一个html文件里然后数据库保存一个html文件的path。然后去读取这个文件的时候就要用到py...'
            },
            {
                'id': '18',
                'title': 'Django正则接口+vue路由',
                'content': '在自己的个人博客项目，从Django+jquery进化到Django+vue.js的过程中。使用了vue的路由，vue自己通过index.html页面和router的ind...'
            },
        ],
        'test': [],
        'leetcode': [
            {
                'id': '4',
                'title': '验证二叉搜索树',
                'content': '给定一个二叉树，判断其是否是一个有效的二叉搜索树。 节点的左子树只包含小于当前节点的数。 节点的右子树只包含大于当前节点的数。 所有左子树和右子树自身必须也是二叉搜索树。...'
            },
            {
                'id': '5',
                'title': 'N 皇后',
                'content': '你一个整数 n ，返回所有不同的 n 皇后问题 的解决方案。 每一种解...'
            },
            {
                'id': '13',
                'title': '顺次数',
                'content': '我们定义「顺次数」为：每一位上的数字都比前一位上的数字大 1 的整数。请你返回由[low, high]范围内所有顺次数组成的 有序 列表（从小到大排序）。'
            },
            {
                'id': '14',
                'title': '回文排列',
                'content': '给定一个字符串，编写一个函数判定其是否为某个回文串的排列之一。 回文串是指正反两个方向都一样的单词或短语。排列是指字母的重新排列。 回文串不一定是字典当中的单词。...'
            },
            {
                'id': '17',
                'title': '最大交换',
                'content': '给定一个非负整数，你至多可以交换一次数字中的任意两位。返回你能得到的最大值。 因为每次只能调换一个那么8位数的时候最多也就只有28种,for循环遍历一下，然后加到列表里，s...'
            },
        ],
        'ai': [
            {
                'id': '6',
                'title': '人工智能必备数学知识-函数',
                'content': ''
            },
            {
                'id': '7',
                'title': '人工智能必备数学知识-微积分',
                'content': ''
            },
            {
                'id': '8',
                'title': '人工智能必备数学知识-矩阵运算',
                'content': ''
            },
            {
                'id': '9',
                'title': '人工智能必备数学知识-概率与统计',
                'content': ''
            },
            {
                'id': '10',
                'title': '人工智能必备数学知识-线性回归',
                'content': ''
            },
            {
                'id': '11',
                'title': '人工智能必备数学知识-逻辑运算',
                'content': ''
            },
            {
                'id': '12',
                'title': '人工智能必备数学知识-马尔科夫链',
                'content': ''
            },
            {
                'id': '15',
                'title': '人工智能-机器学习介绍',
                'content': ''
            },
            {
                'id': '16',
                'title': '人工智能-线性回归模型',
                'content': ''
            },
            {
                'id': '19',
                'title': '人工智能-分类任务与逻辑回归-序',
                'content': ''
            },
            {
                'id': '20',
                'title': '人工智能-分类任务与逻辑回归-逻辑回归',
                'content': ''
            },
            {
                'id': '21',
                'title': '人工智能-分类任务与逻辑回归-代码实战(一)',
                'content': ''
            },
            {
                'id': '22',
                'title': '人工智能-分类任务与逻辑回归-代码实战(二)',
                'content': ''
            },
            {
                'id': '23',
                'title': '人工智能 - 其他分类技术 - kNN模型',
                'content': ''
            },
        ],
    }

    topInfo = {
        'front-end': {
            'id': 20,
            'title': '人工智能-分类任务与逻辑回归-逻辑回归',
            'date': '2021-03-23',
            'content': '由于我们在这个分类问题里， 我们把分类的问题归结成一个他是某一类别的概率，那么在概率大于0.5的时候我们判断他是1，小于0.5时我们判断他是0。 把数据带入进逻辑回归方程，就可以求出来这个点如果在直线上方那么e的指数就会是个正数，如果点在直线下方e的指数就是个负数。是不是就发现跟之前的那个放水问题差不多了'
        }
    }

    midInfo = {
        'front-end': {
            'leftId': 3,
            'leftBigTitle': 'leetcode解题',
            'leftContentTitle': '验证二叉搜索树',
            'leftDate': '2021-03-04',
            'leftContent': '给定一个二叉树，判断其是否是一个有效的二叉搜索树。 节点的左子树只包含小于当前节点的数。 节点的右子树只包含大于当前节点的数。 所有左子树和右子树自身必须也是二叉搜索树。...',
            'rightId': 18,
            'rightBigTitle': '代码开发填坑',
            'rightContentTitle': 'Django正则接口+vue路由',
            'rightDate': '2021-03-24',
            'rightContent': '在自己的个人博客项目，从Django+jquery进化到Django+vue.js的过程中。使用了vue的路由，vue自己通过index.html页面和router的ind...'
        }
    }

    botInfo = {
        'front-end': {
            'leftId': 12,
            'leftBigTitle': '人工智能学习笔记',
            'leftContentTitle': '人工智能必备数学知识-马尔科夫链',
            'leftDate': '2021-03-15',
            'leftContent': '状态空间中，经过从一个状态到另一个状态的转换的随机过程，下一状态的概率分布只能由当前状态决定，且与它前面的时间均无关链这种东西就考虑以下区块链，每个链节点，记录了一定的交易信息，然后传到下一个链去大概就是这样。从概念上来说吼，你可能听的很莫名其妙，让我来稍微用自己的理解解释以下。就是呢，我们先举个不那么恰当的例子。还是用开车来假设，第一个链的状态记录的是你的车现在当前这个位置，有什么状态呢车速50，油门踩死，刹车坏了。前面100米斑马线有个人过马路，过马路的速度是5。然后呢第二个呢记录到行人受到了惊吓速度变成了20，你车突然刹车好了，踩下了刹车车速降到了20，和斑马线的距离剩下20。那么第三个状态就只能由你当前的这个状态去计算，比如第三个状态的刹车情况，有没有撞上人，这些的都不受第一个状态影响。',
            'rightId': 0,
            'rightBigTitle': '开发记录',
            'rightContentTitle': '动态锚点的实现和踩坑',
            'rightDate': ' 2020-12-04',
            'botRightTime': ' 2020-12-04',
            'rightContent': '那么锚点知道怎么做了，接下来就是要做动态锚点了首先解释一下是什么个意思就是你文章嘛不是有个标题目录嘛，然后呢把这个目录放在文章的旁边，你一点它就跳转啦。这个时候你就需要啥呀，需要一个高亮在目录上显示你跳到哪了。然后呢再通过你的上下滚动到下个目录，这个高亮自然就会跟过去在下一个目录高亮。呐这个就是动态锚点了。还不能理解你就看看👈左边，如果你是在掘金上看的就看看👉右边，对这个目录就是动态锚点做的。'
        }
    }

    studyBotSwiper = {
        'leetcode': [
            {'id': 17,
             'url': '/static/img/TB1.58d30225.png',
             'type': '难度：中等',
             'title': '最大交换',
             'date': '2021-03-04',
             'text': '给定一个非负整数，你至多可以交换一次数字中的任意两位。返回你能得到的最大值。 因为每次只能调换一个那么8位数的时候最多也就只有28种,for循环遍历一下，然后加到列表里，s...'
             },
            {'id': 5,
             'url': '/static/img/TB2.7da57f6f.png',
             'type': '递归，难度：困难',
             'title': 'N皇后',
             'date': '2021-03-08',
             'text': 'n 皇后问题 研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。 给你一个整数 n ，返回所有不同的 n 皇后问题 的解决方案。 每一种解...'
             },
            {'id': 13,
             'url': '/static/img/TB3.39e4689a.png',
             'type': '字符串切割，难度：中等',
             'title': '顺次数',
             'date': '2021-3-16',
             'text': '我们定义「顺次数」为：每一位上的数字都比前一位上的数字大 1 的整数。请你返回由[low, high]范围内所有顺次数组成的 有序 列表（从小到大排序）。'
             },
            {'id': 14,
             'url': '/static/img/TB4.2b47ac58.png',
             'type': '栈，字典，难度：简单',
             'title': '回文排列',
             'date': '2021-3-19',
             'text': '给定一个字符串，编写一个函数判定其是否为某个回文串的排列之一。 回文串是指正反两个方向都一样的单词或短语。排列是指字母的重新排列。 回文串不一定是字典当中的单词。...'
             },
        ],
    }

    def getStudyInfo(self, index):
        return self.studyInfo[index]

    def getStudyType(self, sType):
        return self.studyType[sType]

    def getStudyList(self, sType):
        return self.studyList[sType]

    def getStudyTopInfo(self, sType):
        return self.topInfo[sType]

    def getStudyMidInfo(self, sType):
        return self.midInfo[sType]

    def getStudyBotInfo(self, sType):
        return self.botInfo[sType]

    def getStudySwiper(self, sType):
        return self.studyBotSwiper[sType]


if __name__ == '__main__':
    a = StudyInfo()
    print(a.getStudyInfo(1))
