(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-a5ca5840"],{"1a12":function(e,t,n){},"3b42":function(e,t,n){"use strict";n.r(t);var s=function(){var e=this,t=e.$createElement,n=e._self._c||t;return n("div",{staticClass:"profile"},[n("Navbar",e._l(e.links,(function(t){return n("a",{key:t.msg,class:{right:t.isRight},on:{click:function(n){return e.profileDetail(t.type)}}},[e._v(e._s(t.msg))])})),0),n("router-view")],1)},r=[],o=n("d178"),i={components:{Navbar:o["a"]},name:"Profile",data:function(){return{links:[{type:"me",msg:"关于我自己"},{type:"page",msg:"关于这个网页"},{type:"work",msg:"关于工作"},{type:"skill",msg:"关于技能"}]}},methods:{profileDetail:function(e){this.$router.push({path:"/profile/partprofile",query:{type:e}})},refresh:function(){window.scrollTo(0,0)}},watch:{$route:"refresh"}},a=i,u=n("2877"),c=Object(u["a"])(a,s,r,!1,null,null,null);t["default"]=c.exports},"4e04":function(e,t,n){e.exports=n.p+"static/img/Reward.14c40fc2.jpeg"},"5dfc":function(e,t,n){"use strict";n("1a12")},d178:function(e,t,n){"use strict";var s=function(){var e=this,t=e.$createElement,s=e._self._c||t;return s("div",{staticStyle:{position:"sticky",top:"0","z-index":"3"}},[s("div",{class:{navbar:!0},style:e.pagestyle},[e._t("default"),s("a",{class:{barright:!0},on:{mouseover:function(t){return e.show()},mouseleave:function(t){return e.none()}}},[e._v("二维码")])],2),s("img",{directives:[{name:"show",rawName:"v-show",value:e.isShow,expression:"isShow"}],staticClass:"navbarImg",attrs:{src:n("4e04"),alt:""},on:{mouseover:function(t){return e.show()},mouseleave:function(t){return e.none()}}})])},r=[],o={name:"Navbar",props:{links:Array,pagestyle:{type:String,default:"background-color: #333333;"}},data:function(){return{isShow:!1}},methods:{show:function(){this.isShow=!0},none:function(){this.isShow=!1}}},i=o,a=(n("5dfc"),n("2877")),u=Object(a["a"])(i,s,r,!1,null,null,null);t["a"]=u.exports}}]);
//# sourceMappingURL=chunk-a5ca5840.e6b1a9ed.js.map