(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-75c0b416"],{"0560":function(t,a,e){"use strict";var n=e("88d4"),i=e("34cd").find,c=e("d421"),o="find",s=!0;o in[]&&Array(1)[o]((function(){s=!1})),n({target:"Array",proto:!0,forced:s},{find:function(t){return i(this,t,arguments.length>1?arguments[1]:void 0)}}),c(o)},"2cc0":function(t,a,e){"use strict";e.r(a);for(var n=function(){var t=this,a=t.$createElement,e=t._self._c||a;return t.columns?e("a-table",{attrs:{columns:t.columns,"data-source":t.data,bordered:"",pagination:{pageSize:15},scroll:{x:1500,y:400}},scopedSlots:t._u([t._l(t.colList,(function(a){return{key:a,fn:function(n,i){return[e("div",{key:a},[i.editable?e("a-input",{staticStyle:{margin:"-5px 0"},attrs:{value:n},on:{change:function(e){return t.handleChange(e.target.value,i.key,a)}}}):[t._v(" "+t._s(n)+" ")]],2)]}}})),{key:"operation",fn:function(a,n){return[e("div",{staticClass:"editable-row-operations"},[n.editable?e("span",[e("a",{on:{click:function(){return t.save(n.key)}}},[t._v("Save")]),e("a-popconfirm",{attrs:{title:"Sure to cancel?"},on:{confirm:function(){return t.cancel(n.key)}}},[e("a",[t._v("Cancel")])])],1):e("span",[e("a",{attrs:{disabled:""!==t.editingKey},on:{click:function(){return t.edit(n.key)}}},[t._v("Edit")])])])]}}],null,!0)}):t._e()},i=[],c=e("045d"),o=e("597f"),s=(e("51b3"),e("8ea3"),e("0560"),e("89a8"),e("1a91"),e("1bab")),r=[],d=0;d<100;d++)r.push({key:d,name:"Edrward ".concat(d),age:32,address:"London Park no. ".concat(d)});var u={props:{tableType:{type:String},newSwitch:{type:Number}},data:function(){return this.cacheData=r.map((function(t){return Object(o["a"])({},t)})),{data:r,columns:void 0,editingKey:"",colList:[],isNewing:!1}},methods:{handleChange:function(t,a,e){var n=Object(c["a"])(this.data),i=n.find((function(t){return a===t.key}));i&&(i[e]=t,this.data=n)},edit:function(t){var a=Object(c["a"])(this.data),e=a.find((function(a){return t===a.key}));this.editingKey=t,e&&(e.editable=!0,this.data=a)},save:function(t){var a=Object(c["a"])(this.data),e=Object(c["a"])(this.cacheData),n=a.find((function(a){return t===a.key})),i=e.find((function(a){return t===a.key}));n&&i&&(delete n.editable,this.data=a,Object.assign(i,n),this.cacheData=e),this.$emit("save",a,this.editingKey),this.editingKey="",this.cacheData=this.data.map((function(t){return Object(o["a"])({},t)}))},cancel:function(t){var a=Object(c["a"])(this.data),e=a.find((function(a){return t===a.key}));if(this.editingKey="",e&&(Object.assign(e,this.cacheData.find((function(a){return t===a.key}))),delete e.editable,this.data=a),this.isNewing){this.isNewing=!1;var n=Object(c["a"])(this.data);n.remove(0),this.data=n}},getColumns:function(){var t=this;s["a"]({url:this.getBaseUrl()+"get_columns/",method:"post",data:{tableType:this.tableType}}).then((function(a){t.columns=a.data.columns,t.columns.forEach((function(a){t.colList.push(a.dataIndex)})),console.log(t.colList)})).catch((function(t){console.log(t)}))},getData:function(){var t=this;s["a"]({url:this.getBaseUrl()+"get_common_data/",method:"post",data:{tableType:this.tableType,filterRegion:this.$cookies.get("region")}}).then((function(a){t.data=a.data.tableData,t.cacheData=t.data.map((function(t){return Object(o["a"])({},t)}))})).catch((function(t){console.log(t)}))}},created:function(){this.getColumns(),this.getData()},watch:{newSwitch:{handler:function(){this.isNewing=!0;for(var t=0;t<this.data.length;t++)this.data[t].key+=1;this.data.unshift({key:0}),this.cacheData=this.data.map((function(t){return Object(o["a"])({},t)}));var a=Object(c["a"])(this.data),e=a.find((function(t){return 0===t.key}));this.editingKey=0,e&&(e.editable=!0,this.data=a)}}}},h=u,l=(e("daab"),e("cba8")),f=Object(l["a"])(h,n,i,!1,null,"3a52a726",null);a["default"]=f.exports},d14f:function(t,a,e){},daab:function(t,a,e){"use strict";e("d14f")}}]);
//# sourceMappingURL=chunk-75c0b416.abde08cb.js.map