(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-133a292d"],{"36a3":function(e,t,n){"use strict";n("d17e")},c3f8:function(e,t,n){"use strict";n.r(t);var a=function(){var e=this,t=e.$createElement,n=e._self._c||t;return n("div",[n("div",{directives:[{name:"show",rawName:"v-show",value:e.isNewApplicant||e.isBatchControl||e.isSelectApplicant||e.isSelectRelatedId||e.isBatchControl2,expression:"isNewApplicant || isBatchControl || isSelectApplicant || isSelectRelatedId || isBatchControl2"}],staticClass:"maskLayer",on:{click:e.close}}),n("batch-input",{directives:[{name:"show",rawName:"v-show",value:e.isBatchControl,expression:"isBatchControl"}],staticClass:"newApplicant",attrs:{batchType:"ApplicantInfo"},on:{close:e.close}}),n("batch-output",{directives:[{name:"show",rawName:"v-show",value:e.isBatchControl2,expression:"isBatchControl2"}],staticClass:"newApplicant",attrs:{batchType:"ApplicantInfo"},on:{close:e.close}}),n("new-element",{attrs:{isNewApplicant:e.isNewApplicant},on:{close:e.close2}}),""!=e.model?n("select-applicant",{attrs:{Applicant:e.model,isSelectApplicant:e.isSelectApplicant},on:{close:e.close}}):e._e(),""!=e.recruitmentModel?n("select-recruitment",{attrs:{model:e.recruitmentModel,isSelectRelatedId:e.isSelectRelatedId},on:{close:e.close,confirm:e.relatedConfirm}}):e._e(),n("a-table",{attrs:{columns:e.columns,"data-source":e.data,bordered:"",pagination:{pageSize:15},scroll:{x:1500,y:550}},scopedSlots:e._u([{key:"filterDropdown",fn:function(t){var a=t.setSelectedKeys,i=t.selectedKeys,o=t.confirm,r=t.clearFilters,s=t.column;return n("div",{staticStyle:{padding:"8px"}},[n("a-input",{directives:[{name:"ant-ref",rawName:"v-ant-ref",value:function(t){return e.searchInput=t},expression:"c => (searchInput = c)"}],staticStyle:{width:"188px","margin-bottom":"8px",display:"block"},attrs:{placeholder:"Search "+s.dataIndex,value:i[0]},on:{change:function(e){return a(e.target.value?[e.target.value]:[])},pressEnter:function(){return e.handleSearch(i,o,s.dataIndex)}}}),n("a-button",{staticStyle:{width:"90px","margin-right":"8px"},attrs:{type:"primary",icon:"search",size:"small"},on:{click:function(){return e.handleSearch(i,o,s.dataIndex)}}},[e._v(" Search ")]),n("a-button",{staticStyle:{width:"90px"},attrs:{size:"small"},on:{click:function(){return e.handleReset(r)}}},[e._v(" Reset ")])],1)}},{key:"filterIcon",fn:function(e){return n("a-icon",{style:{color:e?"#108ee9":void 0},attrs:{type:"search"}})}},{key:"customRender",fn:function(t,a,i,o){return[e.searchText&&e.searchedColumn===o.dataIndex?n("span",[e._l(t.toString().split(new RegExp("(?<="+e.searchText+")|(?="+e.searchText+")","i")),(function(t,a){return[t.toLowerCase()===e.searchText.toLowerCase()?n("mark",{key:a,staticClass:"highlight"},[e._v(e._s(t+""))]):[e._v(e._s(t+""))]]}))],2):[e._v(" "+e._s(t)+" ")]]}},e._l(["name","phone_num","graduated_from","education","major","working_seniority","job","region","related","pdu","project_name","arrival_time","recommender","recommend_time","own_interviewer","own_interview_results","reason1","own_interview_time","machine_test_type","machine_test_score","machine_test_time","hw_interviewer1","hw_interview_results1","reason2","hw_interview_time1","hw_interviewer2","hw_interview_results2","reason3","hw_interview_time2","final_result","final_time","reason4","process_status","resume_status","sex","suggest_level","giveup_time","entrance","graduation"],(function(t){return{key:t,fn:function(a,i){return[n("div",{key:t},[i.editable?["machine_test_time"==t?n("a-date-picker",{staticStyle:{margin:"-5px 0"},attrs:{"show-time":"",placeholder:"机试时间"},on:{change:function(n){return e.handleChange(n.format("YYYY-MM-DD HH:MM:ss"),i.key,t)},ok:function(n){return e.handleChange(n.format("YYYY-MM-DD HH:MM:ss"),i.key,t)}}}):"hw_interview_time1"==t?n("a-date-picker",{staticStyle:{margin:"-5px 0"},attrs:{"show-time":"",placeholder:"华为技面时间"},on:{change:function(n){return e.handleChange(n.format("YYYY-MM-DD HH:MM:ss"),i.key,t)},ok:function(n){return e.handleChange(n.format("YYYY-MM-DD HH:MM:ss"),i.key,t)}}}):"recommend_time"==t?n("a-date-picker",{staticStyle:{margin:"-5px 0"},attrs:{"show-time":"",placeholder:"推荐时间"},on:{change:function(n){return e.handleChange(n.format("YYYY-MM-DD HH:MM:ss"),i.key,t)},ok:function(n){return e.handleChange(n.format("YYYY-MM-DD HH:MM:ss"),i.key,t)}}}):"hw_interview_time2"==t?n("a-date-picker",{staticStyle:{margin:"-5px 0"},attrs:{"show-time":"",placeholder:"华为综面时间"},on:{change:function(n){return e.handleChange(n.format("YYYY-MM-DD HH:MM:ss"),i.key,t)},ok:function(n){return e.handleChange(n.format("YYYY-MM-DD HH:MM:ss"),i.key,t)}}}):"own_interview_time"==t?n("a-date-picker",{staticStyle:{margin:"-5px 0"},attrs:{"show-time":"",placeholder:"软通面试时间"},on:{change:function(n){return e.handleChange(n.format("YYYY-MM-DD HH:MM:ss"),i.key,t)},ok:function(n){return e.handleChange(n.format("YYYY-MM-DD HH:MM:ss"),i.key,t)}}}):"arrival_time"==t?n("a-date-picker",{staticStyle:{margin:"-5px 0"},attrs:{placeholder:"能够到岗时间"},on:{change:function(n){return e.handleChange(n.format("YYYY-MM-DD"),i.key,t)}}}):"entrance"==t?n("a-date-picker",{staticStyle:{margin:"-5px 0"},attrs:{placeholder:"入学日期"},on:{change:function(n){return e.handleChange(n.format("YYYY-MM-DD"),i.key,t)}}}):"graduation"==t?n("a-date-picker",{staticStyle:{margin:"-5px 0"},attrs:{placeholder:"毕业日期"},on:{change:function(n){return e.handleChange(n.format("YYYY-MM-DD"),i.key,t)}}}):"final_time"==t?n("a-date-picker",{staticStyle:{margin:"-5px 0"},attrs:{placeholder:"入项时间"},on:{change:function(n){return e.handleChange(n.format("YYYY-MM-DD"),i.key,t)}}}):"giveup_time"==t?n("a-date-picker",{staticStyle:{margin:"-5px 0"},attrs:{placeholder:"放弃offer时间"},on:{change:function(n){return e.handleChange(n.format("YYYY-MM-DD"),i.key,t)}}}):"related"==t?n("a-input",{staticStyle:{margin:"-5px 0"},attrs:{placeholder:"关联需求",value:a},on:{click:function(t){return e.selectRelated(i.key)},change:function(n){return e.handleChange(n.target.value,i.key,t)}}}):"process_status"==t?n("a-select",{ref:"select",refInFor:!0,staticStyle:{margin:"-5px 0"},attrs:{value:a},on:{change:function(n){return e.handleChange(n,i.key,t)}}},e._l(e.process_status_case,(function(t,a){return n("a-select-option",{key:a,attrs:{value:a}},[e._v(e._s(t))])})),1):n("a-input",{staticStyle:{margin:"-5px 0"},attrs:{value:a},on:{change:function(n){return e.handleChange(n.target.value,i.key,t)}}})]:["name"==t?[n("a",{on:{click:function(t){return e.selectId(i)}}},[e._v(e._s(a))])]:["machine_test_time"==t||"hw_interview_time1"==t||"recommend_time"==t||"hw_interview_time2"==t||"own_interview_time"==t?[e._v(" "+e._s(e._f("datetime")(a))+" ")]:"giveup_time"==t||"final_time"==t||"graduation"==t||"entrance"==t||"arrival_time"==t?[e._v(" "+e._s(e._f("date")(a))+" ")]:"process_status"==t?[e._v(" "+e._s(e.process_status_case[a])+" ")]:[e._v(" "+e._s(a)+" ")]]]],2)]}}})),{key:"operation",fn:function(t,a){return[n("div",{staticClass:"editable-row-operations"},[a.editable?n("span",[n("a",{on:{click:function(){return e.save(a.key)}}},[e._v("Save")]),n("a-popconfirm",{attrs:{title:"Sure to cancel?"},on:{confirm:function(){return e.cancel(a.key)}}},[n("a",[e._v("Cancel")])])],1):n("span",[n("a",{attrs:{disabled:""!==e.editingKey},on:{click:function(){return e.edit(a.key)}}},[e._v("Edit")])])])]}}],null,!0)})],1)},i=[],o=n("ebb4"),r=n("045d"),s=n("597f"),c=(n("2788"),n("aa08"),n("89a8"),n("d5ee"),n("10dd"),n("8ea3"),n("51b3"),n("5a05"),n("5cd2")),l=n("88e0"),d=n("26f9"),u=n("1bab"),h=n("67da"),p=n("d07d"),f=n("caaf"),m=n.n(f),g=void 0,w=[{title:"姓名",dataIndex:"name",width:100,fixed:"left",scopedSlots:{filterDropdown:"filterDropdown",filterIcon:"filterIcon",customRender:"name"},onFilter:function(e,t){return t.name.toString().toLowerCase().includes(e.toLowerCase())},onFilterDropdownVisibleChange:function(e){e&&setTimeout((function(){g.searchInput.focus()}),0)}},{title:"软通工号",dataIndex:"rt_num",width:130,scopedSlots:{filterDropdown:"filterDropdown",filterIcon:"filterIcon",customRender:"process_status"},onFilter:function(e,t){return t.process_status.toString().toLowerCase().includes(e.toLowerCase())},onFilterDropdownVisibleChange:function(e){e&&setTimeout((function(){g.searchInput.focus()}),0)}},{title:"调级时间",dataIndex:"resume_status",width:130,scopedSlots:{filterDropdown:"filterDropdown",filterIcon:"filterIcon",customRender:"resume_status"},onFilter:function(e,t){return t.resume_status.toString().toLowerCase().includes(e.toLowerCase())},onFilterDropdownVisibleChange:function(e){e&&setTimeout((function(){g.searchInput.focus()}),0)}},{title:"上次级别",dataIndex:"phone_num",width:200,scopedSlots:{filterDropdown:"filterDropdown",filterIcon:"filterIcon",customRender:"phone_num"},onFilter:function(e,t){return t.phone_num.toString().toLowerCase().includes(e.toLowerCase())},onFilterDropdownVisibleChange:function(e){e&&setTimeout((function(){g.searchInput.focus()}),0)}},{title:"调后级别",dataIndex:"graduated_from",width:250,scopedSlots:{customRender:"graduated_from"}},{title:"调薪时间",dataIndex:"education",width:100,scopedSlots:{customRender:"education"}},{title:"调整前薪资",dataIndex:"major",width:250,scopedSlots:{customRender:"major"}},{title:"涨幅",dataIndex:"working_seniority",width:100,scopedSlots:{customRender:"working_seniority"}},{title:"调薪类型",dataIndex:"job",width:200,scopedSlots:{filterDropdown:"filterDropdown",filterIcon:"filterIcon",customRender:"job"},onFilter:function(e,t){return t.job.toString().toLowerCase().includes(e.toLowerCase())},onFilterDropdownVisibleChange:function(e){e&&setTimeout((function(){g.searchInput.focus()}),0)}},{title:"备注",dataIndex:"region",width:100,scopedSlots:{filterDropdown:"filterDropdown",filterIcon:"filterIcon",customRender:"region"},onFilter:function(e,t){return t.region.toString().toLowerCase().includes(e.toLowerCase())},onFilterDropdownVisibleChange:function(e){e&&setTimeout((function(){g.searchInput.focus()}),0)}},{title:"operation",dataIndex:"operation",fixed:"right",scopedSlots:{customRender:"operation"},width:180}],_=[],v={components:{BatchInput:c["a"],NewElement:d["a"],SelectApplicant:h["a"],SelectRecruitment:p["a"],BatchOutput:l["a"]},data:function(){return this.cacheData=_.map((function(e){return Object(s["a"])({},e)})),{data:_,columns:w,editingKey:"",isNewApplicant:!1,isBatchControl:!1,isBatchControl2:!1,userName:void 0,recommender:void 0,region:void 0,sex:void 0,education:void 0,entrance:void 0,graduation:void 0,graduated_from:void 0,major:void 0,phone_num:void 0,job:void 0,searchText:"",searchInput:void 0,searchedColumn:"",isSelectApplicant:!1,model:"",isSelectRelatedId:!1,recruitmentModel:"",process_status_case:{created:"创建",fail1:"初筛不通过",pass1:"初筛通过",fail2:"初试不通过",pass2:"初试通过",fail3:"客户技面不通过",pass3:"客户技面通过",fail4:"客户综面不通过",pass4:"客户综面通过",discuss:"谈offer中",standBy:"待入职",giveUp:"放弃offer",fellow:"已入职"}}},props:{newSwitch:{type:Number},filterData:{type:Object},BatchNum:{type:Number}},methods:{handleChange:function(e,t,n){var a=Object(r["a"])(this.data),i=a.filter((function(e){return t===e.key}))[0];i&&(i[n]=e,this.data=a)},edit:function(e){var t=Object(r["a"])(this.data),n=t.filter((function(t){return e===t.key}))[0];this.editingKey=e,n&&(n.editable=!0,this.data=t)},save:function(e){var t=Object(r["a"])(this.data),n=Object(r["a"])(this.cacheData),a=t.filter((function(t){return e===t.key}))[0],i=n.filter((function(t){return e===t.key}))[0];a&&i&&(delete a.editable,this.data=t,Object.assign(i,a),this.cacheData=n),this.updateApplicant(e),this.editingKey=""},cancel:function(e){var t=Object(r["a"])(this.data),n=t.filter((function(t){return e===t.key}))[0];this.editingKey="",n&&(Object.assign(n,this.cacheData.filter((function(t){return e===t.key}))[0]),delete n.editable,this.data=t)},handleSearch:function(e,t,n){t(),this.searchText=e[0],this.searchedColumn=n},log:function(){},handleReset:function(e){e(),this.searchText=""},newApplicant:function(){this.isNewApplicant=!0,console.log(this.newSwitch)},close:function(){this.isNewApplicant=!1,this.isBatchControl=!1,this.isBatchControl2=!1,this.isSelectApplicant=!1,this.isSelectRelatedId=!1},close2:function(){this.isNewApplicant=!1,this.isBatchControl=!1,this.isBatchControl2=!1,this.isSelectApplicant=!1,this.isSelectRelatedId=!1,this.getApplicantInfo()},updateApplicant:function(e){var t,n=Object(o["a"])(this.data);try{for(n.s();!(t=n.n()).done;){var a=t.value;a.key===e&&(console.log(a),console.log(e),console.log(a.key),u["a"]({url:this.getBaseUrl()+"update_applicant_info/",method:"post",data:{data:a}}).then((function(e){console.log(e)})).catch((function(e){console.log(e)})))}}catch(i){n.e(i)}finally{n.f()}},getApplicantInfo:function(){var e=this;this.cacheData=[],this.data=this.cacheData,u["a"]({url:this.getBaseUrl()+"get_applicant_info/",method:"post",data:{filterData:this.filterData,filterRegion:this.$cookies.get("region")}}).then((function(t){var n=t.data.applicantList;e.data.length=0;for(var a=0;a<n.length;a++)e.data.push(n[a]);e.cacheData=e.data.map((function(e){return Object(s["a"])({},e)}))})).catch((function(e){console.log(e)}))},selectId:function(e){console.log(e),this.model=e,this.isSelectApplicant=!0},selectRelated:function(e){console.log(e);var t,n=Object(o["a"])(this.data);try{for(n.s();!(t=n.n()).done;){var a=t.value;a.key===e&&(this.recruitmentModel=a)}}catch(i){n.e(i)}finally{n.f()}console.log(this.recruitmentModel),this.isSelectRelatedId=!0},relatedConfirm:function(e){this.close();var t=e.key;this.handleChange(e.related,t,"related"),this.handleChange(e.pdu,t,"pdu"),this.handleChange(e.project_name,t,"project_name")}},created:function(){this.getApplicantInfo()},watch:{newSwitch:"newApplicant",filterData:{handler:function(e){console.log(e),this.getApplicantInfo()}},BatchNum:{handler:function(e,t){console.log(e),console.log(t),e>t&&(this.isBatchControl=!0),t>e&&(this.isBatchControl2=!0)}},cleanNum:{handler:function(e,t){console.log(e),console.log(t),this.isBatchControl=!0}}},filters:{datetime:function(e){return e?m()(e).format("YYYY-MM-DD HH:MM:ss"):e},date:function(e){return e?m()(e).format("YYYY-MM-DD"):e},phone:function(e){return console.log(e),e+" "}}},y=v,k=(n("36a3"),n("cba8")),C=Object(k["a"])(y,a,i,!1,null,"17441bdb",null);t["default"]=C.exports},d17e:function(e,t,n){}}]);
//# sourceMappingURL=chunk-133a292d.a236f931.js.map