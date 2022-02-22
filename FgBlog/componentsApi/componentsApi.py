class CompontentsApi:
    NavbarList = {
        'study': [
            {'type': 'front-end', 'msg': '前端', },
            {'type': 'back-end', 'msg': '后端', },
            {'type': 'test', 'msg': '测试', },
            {'type': 'leetcode', 'msg': '力扣', },
            {'type': 'ai', 'msg': '人工智能', },
        ],
    }

    def getNavbarList(self, Ntype):
        return self.NavbarList[Ntype]


if __name__ == '__main__':
    a = CompontentsApi()
