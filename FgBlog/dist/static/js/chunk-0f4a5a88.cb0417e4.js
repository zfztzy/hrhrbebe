(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-0f4a5a88"],{"572c":function(t,n,e){"use strict";e.r(n);var a=function(){var t=this,n=t.$createElement,e=t._self._c||n;return e("a-layout-content",[e("a-button",{staticClass:"tableButton",on:{click:t.batchInput}},[t._v("批量导入")]),e("a-button",{staticClass:"tableButton",on:{click:t.batchOutput}},[t._v("批量导出")]),e("a-space",{staticStyle:{float:"right"}},[e("a-button",{directives:[{name:"show",rawName:"v-show",value:t.showAddBtn,expression:"showAddBtn"}],staticClass:"tableButton",attrs:{id:"newAdd"},on:{click:t.newInfo}},[t._v("新增")])],1),e("router-view",{attrs:{tableType:"test",BatchNum:t.BatchNum,newSwitch:t.newSwitch,filterData:t.filterData,cleanNum:t.cleanNum},on:{save:t.log}})],1)},c=[],o={name:"Profile",data:function(){return{newSwitch:0,BatchNum:0,isShow:!1,filterData:{},cleanNum:0,visible:!1,selectDate:"",showAddBtn:!0}},methods:{refresh:function(){window.scrollTo(0,0)},batchInput:function(){this.BatchNum+=1},batchOutput:function(){this.BatchNum-=1},newInfo:function(){this.newSwitch+=1},log:function(t){console.log(t)}},watch:{$route:{handler:function(){this.refresh()}}},mounted:function(){}},u=o,i=(e("eb23"),e("cba8")),s=Object(i["a"])(u,a,c,!1,null,null,null);n["default"]=s.exports},"9d05":function(t,n,e){},eb23:function(t,n,e){"use strict";e("9d05")}}]);
//# sourceMappingURL=chunk-0f4a5a88.cb0417e4.js.map