(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-7101cfdb"],{3384:function(t,e,o){},4125:function(t,e,o){},"5dfc":function(t,e,o){"use strict";o("3384")},6220:function(t,e,o){"use strict";o.r(e);var s=function(){var t=this,e=t.$createElement,o=t._self._c||e;return o("a-layout",[o("Navbar"),o("router-view")],1)},a=[],n=o("d178"),i={name:"appHome",components:{Navbar:n["a"]},methods:{},created:function(){},watch:{$route:{handler:function(){}}}},c=i,u=(o("cb7f"),o("cba8")),r=Object(u["a"])(c,s,a,!1,null,null,null);e["default"]=r.exports},cb7f:function(t,e,o){"use strict";o("4125")},d178:function(t,e,o){"use strict";var s=function(){var t=this,e=t.$createElement,o=t._self._c||e;return o("a-layout-header",{staticClass:"header",staticStyle:{"background-color":"rgba(67,126,255)"}},[o("div",{staticClass:"ipsaLogo",staticStyle:{float:"left"}}),o("div",{staticClass:"userInfo",staticStyle:{float:"right"}},[o("a-dropdown",[o("div",{staticClass:"userHead"},[o("a-badge",{attrs:{count:t.count}},[o("a-avatar",{attrs:{shape:"square",icon:"user"}}),t._v(" "+t._s(t.nickname))],1)],1),o("a-menu",{attrs:{slot:"overlay"},slot:"overlay"},[o("a-menu-item",[o("a",{attrs:{href:"javascript:;"},on:{click:t.add}},[t._v("用户主页")])]),o("a-menu-item",[o("a",{attrs:{href:"javascript:;"}},[t._v("用户设置")])]),o("a-menu-item",[o("a",{attrs:{href:"javascript:;"},on:{click:t.logOut}},[t._v("注销")])])],1)],1)],1),o("a-menu",{staticStyle:{"background-color":"rgba(67,126,255)"},style:{lineHeight:"64px"},attrs:{theme:"dark",mode:"horizontal","default-selected-keys":["1"]}},[o("a-menu-item",{key:"1",on:{click:t.showTopMenu}},[t._v(" 招聘管理 ")]),o("a-menu-item",{key:"2",on:{click:t.showTopMenu2}},[t._v(" 项目管理 ")]),o("a-menu-item",{key:"3",on:{click:t.showTopMenu3}},[t._v(" 运营管理 ")])],1),o("div",{directives:[{name:"show",rawName:"v-show",value:t.isShow,expression:"isShow"}],staticClass:"topMenu",on:{mouseleave:t.close}},[o("a-space",{staticStyle:{"margin-left":"10%"},attrs:{size:200}},[o("a",{on:{click:function(e){return t.jumpPath("Applicant")}}},[o("h5",[t._v("候选人管理")])]),o("a",{on:{click:function(e){return t.jumpPath("Recruitment")}}},[o("h5",[t._v("招聘需求")])]),o("a",{on:{click:function(e){return t.jumpPath("PojectStatus")}}},[o("h5",[t._v("项目满足度")])]),o("a",{on:{click:function(e){return t.jumpPath("RecruitChart")}}},[o("h5",[t._v("招聘看板")])])])],1),o("div",{directives:[{name:"show",rawName:"v-show",value:t.isShow2,expression:"isShow2"}],staticClass:"topMenu",on:{mouseleave:t.close}},[o("a-space",{staticStyle:{"margin-left":"10%"},attrs:{size:200}},[o("a",{on:{click:function(e){return t.jumpPath2("pduinfo")}}},[o("h5",[t._v("PDU信息")])]),o("a",{on:{click:function(e){return t.jumpPath2("ProjectInfo")}}},[o("h5",[t._v("项目信息")])]),o("a",{on:{click:function(e){return t.jumpPath2("PoInfo")}}},[o("h5",[t._v("PO信息")])])])],1),o("div",{directives:[{name:"show",rawName:"v-show",value:t.isShow3,expression:"isShow3"}],staticClass:"topMenu",on:{mouseleave:t.close}},[o("a-space",{staticStyle:{"margin-left":"10%"},attrs:{size:200}},[o("a",{on:{click:function(e){return t.jumpPath3("PoList")}}},[o("h5",[t._v("PO运营")])])])],1)],1)},a=[],n={data:function(){return{collapsed:!1,isShow:!1,nickname:"用户名",count:0,isShow2:!1,isShow3:!1}},methods:{showTopMenu:function(){this.close(),this.isShow=!0},showTopMenu2:function(){this.close(),this.isShow2=!0},showTopMenu3:function(){this.close(),this.isShow3=!0},close:function(){this.isShow=!1,this.isShow2=!1,this.isShow3=!1},jumpPath:function(t){this.checkLogin(),this.$router.push({path:"/hrManageTable/"+t}),this.close()},jumpPath2:function(t){this.checkLogin(),this.$router.push({path:"/projectManager/"+t}),this.close()},jumpPath3:function(t){this.checkLogin(),this.$router.push({path:"/businessManager/"+t}),this.close()},add:function(){this.count+=1},logOut:function(){this.$cookies.remove("userName"),this.$cookies.remove("password"),this.$cookies.remove("nickname"),this.$cookies.remove("region"),alert("注销成功"),this.$router.push("/Login")}},mounted:function(){this.nickname=this.$cookies.get("nickname")}},i=n,c=(o("5dfc"),o("cba8")),u=Object(c["a"])(i,s,a,!1,null,null,null);e["a"]=u.exports}}]);
//# sourceMappingURL=chunk-7101cfdb.e323efa6.js.map