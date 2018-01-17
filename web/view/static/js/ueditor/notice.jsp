<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<meta name="viewport"
      content="width=device-width, user-scalable=yes, initial-scale=1.0, maximum-scale=2.0, minimum-scale=0.5">
<meta http-equiv="X-UA-Compatible" content="IE=Edge">
<meta name="renderer" content="webkit">
<title></title>
<link rel="stylesheet" href="../resources/common/font-awesome.css"/>
<link rel="stylesheet" href="../resources/common/element.css"/>
<link rel="stylesheet" href="../resources/css/base.css"/>
<script src="../resources/common/vue.js"></script>
<script src="../resources/common/vue-resource.min.js"></script>
<script src="../resources/js/base.js"></script>
<script src="../resources/common/element.js"></script>
<script src="../resources/common/array.js"></script>
<script src="../resources/common/store.modern.min.js"></script>
<script src="../resources/js/common.js" ></script>
<script src="../resources/common/store.modern.min.js"></script>
<script src="../resources/common/jquery-1.12.4.min.js"></script>
<script src="../static/js/ueditor/ueditor.config.js" type="text/javascript"></script>
<script src="../static/js/ueditor/ueditor.all.js" type="text/javascript"></script>
<script src="../static/js/ueditor/lang/zh-cn/zh-cn.js" type="text/javascript"></script>
<script type="text/javascript" src="../static/kitui/ajaxfileupload.js"></script>
<style type="text/css">
	.el-dialog__wrapper{
		z-index: 1003!important;
	} 
	.v-modal{
		z-index: 1002!important;
	}
	.kitui-layout-table {width:100%;height:100%;padding-right:0px;table-layout:fixed;border-collapse: collapse;}
</style>
</head>
<body  style="overflow:hidden;">
	<div id="notice" class="v__addAnimationBg">
		<el-row>
			<el-col :span="18" >
	        	<el-button type="primary" size="mini" @click="handleHelp()" ><i class="fa fa-home fa-lg" ></i></el-button>
	        	<a href="" style="top: 20px;">农保信息平台-通知公告管理</a>
	        </el-col>
	        <el-col :span="6" style="text-align: right">
	        	<el-button type="primary" size="small"  icon="plus" @click="xztzgg()" style="margin-left:5px">新增</el-button>
            <el-button type="primary" size="small" icon="edit" @click="bjtzgg()">编辑</el-button>
            <el-button type="primary" size="small" icon="delete" @click="tzggdel()">删除</el-button>
	        </el-col>
	    </el-row>
	    
	      
	   <!-- 查询条件 begin-->
	    <el-row style="background-color:#FAFAFA;">
	       <el-col >
	          	<el-form :inline="true" >
				    <el-form-item label="名称:">
					    <el-input v-model="selMc" placeholder="请输入名称"></el-input>
			  		</el-form-item>
			  		 <el-form-item label="类别:"  :label-width="formLabelWidth" >
				    	<el-select  v-model="currentSelLb" :clearable="true">
							    <el-option v-for="item in selLb"  :key="item.Guid" :label="item.Lawscatname" :value="item.Guid">
							    </el-option>
						</el-select>		    
				    </el-form-item>
	 				<el-button type="primary" size="small" class="fa fa-search" style="margin-top:4px;" @click="pagelist()"> 查询</el-button>
				</el-form> 
	       </el-col>
	     </el-row>
	   	 <!-- 查询条件结束end -->
	   	 
	   	 	<!--  table-begin -->
		<el-row class="v__tableDock" style="position: absolute;top: 90px;bottom: 30px;width: 100%">
	        <el-col :span="24">
				<el-table :data="tabledata" ref="multipleTable" :height="v__tableDockHeight"   highlight-current-row 
                		@row-click="clickRow1"  border style="width:100%" 
							@selection-change="selecttablechange" @row-dblclick="tabledoubleclick">
					<el-table-column type="selection" width="55"></el-table-column>
					<el-table-column type="index" label="序号" width="75"></el-table-column>	
					<el-table-column prop="MC" label="通知名称" width="700"></el-table-column>										
					<el-table-column prop="TZLB" label="通知类别" width="200"></el-table-column>
					<el-table-column prop="TZRQ" label="通知日期" width="200"></el-table-column>
				</el-table>
			</el-col>
		</el-row>
		
		<el-row style="position: absolute;bottom: 0;">
	        <el-col :span="24">
	            <el-pagination :current-page="page.currentpage" :page-sizes="[20, 50, 100]" :page-size="page.pagesize"
                               layout="total, sizes, prev, pager, next, jumper" :total="page.total"
                               @current-change="handleCurrentChange" @size-change="handleSizeChange">
                </el-pagination>
	        </el-col>
	     </el-row>
	   	<!--  table-end --> 
	   	
	   	<!-- 查看通知公告 -->
		<el-dialog title="查看通知公告" :visible.sync="dialogFormVisible1" :modal-append-to-body="false" size="large">
		  	<el-form ref="form1"  :model="form1" label-position="right" label-width="90px" >
				  	<el-form-item label="名称：" >
				    	<el-input v-model="form1.mc"  :readonly="true"></el-input>
				  	</el-form-item>
				  	<el-row>
					  	<el-col :span="6">
					      <el-form-item label="文号：">
	    					<el-input v-model="form1.wh"  :readonly="true"></el-input>
	  					</el-form-item>
					    </el-col>
					    <el-col :span="6">
					      <el-form-item label="通知机构：">
	    					<el-input v-model="form1.fwjg"  :readonly="true"></el-input>
	  					</el-form-item>
					    </el-col>
					    <el-col :span="6">
					      <el-form-item label="类别：">
	    					<el-input v-model="form1.NOTICECATNAME"  :readonly="true"></el-input>
	  					</el-form-item>
					    </el-col>
					    <el-col :span="6">
					      <el-form-item label="通知日期：">
	    					<el-input v-model="form1.fwrq"  :readonly="true"></el-input>
	  					</el-form-item>
					    </el-col>
				    </el-row>
				    <div style="border: 1px solid #d4d4d4;height:auto;min-height: 300px">
				    <p v-html="form1.SB"></p>
				    </div>
				    <el-table :data="fjData" :show-header="false" border style="width: 100%">    
							<el-table-column label="" width="1100px" >
								<template scope="scope">
							        <el-button type="text" size="small"  @click="downloadFj(scope.row)">
							        	<div style="color:black;">{{scope.row.name}}</div>
							        </el-button>
	      						</template>
    						</el-table-column>    
    						
  						</el-table>
			</el-form></el-dialog>
		<!-- 查看通知公告end -->
		
		<!-- 新增通知公告 -->
		<el-dialog title="新增通知公告" :visible.sync="dialogFormVisible2" :modal-append-to-body="false" :close-on-click-modal="false" size="large">
		  	<el-form ref="form2"  :rules="rules" :model="form2" label-position="right" label-width="90px" >
				  	<el-form-item label="名称：" prop="mc" :label-width="formLabelWidth">
				    	<el-input v-model="form2.mc"  ></el-input>
				  	</el-form-item>
				  	<el-row>
					  	<el-col :span="6">
					      <el-form-item label="文号：" :label-width="formLabelWidth">
	    					<el-input v-model="form2.wh"  ></el-input>
	  					</el-form-item>
					    </el-col>
					    <el-col :span="6">
					      <el-form-item label="通知机构：" :label-width="formLabelWidth">
	    					<el-input v-model="form2.fwjg"  ></el-input>
	  					</el-form-item>
					    </el-col>
					    <el-col :span="6">
					      <el-form-item label="类别："  :label-width="formLabelWidth">
	    					<el-select  v-model="form2.NOTICECATNAME" :clearable="true">
							    <el-option v-for="item in selLb"  :key="item.Guid" :label="item.Lawscatname" :value="item.Guid">
							    </el-option>
						</el-select>
	  					</el-form-item>
					    </el-col>
					    <el-col :span="6">
					      <el-form-item label="通知日期："  :label-width="formLabelWidth">
	    					<el-date-picker  v-model="form2.fwrq" type="date"  placeholder="选择日期" :picker-options="pickerOptions0"></el-date-picker>
	  					</el-form-item>
					    </el-col>
				    </el-row>
				 	<!-- 编辑器 -->
				  	<div id='ueditor' style="width:100%;height:100%;" >
						<table  id='layout0'  cellSpacing=0 cellPadding=0 class= 'kitui-layout-table' >
							<tr style='vertical-align:top' >
								<td>
									<textarea id="SB"  ></textarea>
								</td>
							</tr>	
						</table>
					</div>
					
					<!-- <el-button type="primary" >上传附件</el-button> -->
					<table cellSpacing=0 cellPadding=0 style="height:100%;width:100%;">
					<tr>
						<td width="10%">
								<input type='file' name='zyf_file' id='zyf_file' @change='scfj(form2.NOTICECATNAME)' style='display: none;'/>
								<el-button type="primary" id='uploadBtn' @click="sc()" style='width:90px;height:25px;font-size:8;margin-left:0px;border-color:#12bdf1;'><img src='${pageContext.request.contextPath}/static/images/icons/upload.png' ><span >上传附件</span></el-button>
						</td>
						<td width="75%">
						<el-table :data="fjData1" :show-header="false" border style="width: 100%">    
							<el-table-column label="" width="900" >
								<template scope="scope">
							        <el-button type="text" size="small"  @click="downloadFj(scope.row)">
							        	<div style="color:black;">{{scope.row.name}}</div>
							        </el-button>
	      						</template>
    						</el-table-column>    
    						<el-table-column  label="" > 
	    						<template scope="scope">       
							        <el-button type="text" size="small" @click="delfj(scope.row)"> 
							        	<i class="el-icon-delete"></i>删除附件
							        </el-button>
	     				 		</template>
    						</el-table-column>
  						</el-table>
  						</td>		
  					</tr>
					</table>
			</el-form>
				 
 
			<div slot="footer" class="dialog-footer">
				<el-button  @click="dialogFormVisible2 = false">取 消</el-button>
			  	<el-button type="primary" @click="xztzggsave('form2')">保 存</el-button>    
	  		</div>
			</el-dialog>
		<!-- 新增通知公告end -->
		
		<!-- 编辑通知公告 -->
		<el-dialog title="编辑通知公告" :visible.sync="dialogFormVisible3" :modal-append-to-body="false" size="large">
		  	<el-form ref="form3"  :rules="rules" :model="form3" label-position="right" label-width="90px" >
				  	<el-form-item label="名称：" prop="mc" :label-width="formLabelWidth">
				    	<el-input v-model="form3.mc"  ></el-input>
				  	</el-form-item>
				  	<el-row>
					  	<el-col :span="6">
					      <el-form-item label="文号：" :label-width="formLabelWidth">
	    					<el-input v-model="form3.wh"  ></el-input>
	  					</el-form-item>
					    </el-col>
					    <el-col :span="6">
					      <el-form-item label="通知机构：" :label-width="formLabelWidth">
	    					<el-input v-model="form3.fwjg"  ></el-input>
	  					</el-form-item>
					    </el-col>
					    <el-col :span="6">
					      <el-form-item label="类别：" :label-width="formLabelWidth">
	    					<el-select  v-model="form3.selLb" :clearable="true">
							    <el-option v-for="item in selLb"  :key="item.Guid" :label="item.Lawscatname" :value="item.Guid">
							    </el-option>
						</el-select>
	  					</el-form-item>
					    </el-col>
					    <el-col :span="6">
					      <el-form-item label="通知日期："  :label-width="formLabelWidth">
	    					<el-date-picker  v-model="form3.fwrq" type="date"  placeholder="选择日期" :picker-options="pickerOptions0"></el-date-picker>
	  					</el-form-item>
					    </el-col>
				    </el-row>
				  	<!-- 编辑器 -->
				  	<div id='ueditor' style="width:100%;height:100%;" >
						<table  id='layout0'  cellSpacing=0 cellPadding=0 class= 'kitui-layout-table' >
							<tr style='vertical-align:top' >
								<td>
									<textarea id="bjSB"  ></textarea>
								</td>
							</tr>	
						</table>
					</div>
					
					<!-- <el-button type="primary" >上传附件</el-button> -->
					<table cellSpacing=0 cellPadding=0 style="height:100%;width:100%;">
					<tr>
						<td width="10%">
								<input type='file' name='zyf_file' id='zyf_file' @change='scfj(form3.selLb)' style='display: none;'/>
								<el-button type="primary" id='uploadBtn' @click="sc()" style='width:90px;height:25px;font-size:8;margin-left:0px;border-color:#12bdf1;'><img src='${pageContext.request.contextPath}/static/images/icons/upload.png' ><span >上传附件</span></el-button>
						</td>
						<td width="75%">
						<el-table :data="fjData1" :show-header="false" border style="width: 100%">    
							<el-table-column label="" width="900" >
								<template scope="scope">
							        <el-button type="text" size="small"  @click="downloadFj(scope.row)">
							        	<div style="color:black;">{{scope.row.name}}</div>
							        </el-button>
	      						</template>
    						</el-table-column>    
    						<el-table-column  label="" > 
	    						<template scope="scope">       
							        <el-button type="text" size="small" @click="delfj(scope.row)"> 
							        	<i class="el-icon-delete"></i>删除附件
							        </el-button>
	     				 		</template>
    						</el-table-column>
  						</el-table>
  						</td>		
  					</tr>
					</table> 
			</el-form>
			<div slot="footer" class="dialog-footer">
				<el-button  @click="dialogFormVisible3 = false">取 消</el-button>
			  	<el-button type="primary" @click="bjtzggsave('form3')">保 存</el-button>    
	  		</div>
			</el-dialog>
		<!-- 编辑通知公告end -->
		
	 </div>

</body>

<script type="text/javascript">
	Vue.http.options.emulateJSON = true;
	var vo = new Vue({
		el: "#notice",
	    data: function () {
	    	return{
	    		dialogFormVisible1: false,
	    		dialogFormVisible2: false,
	    		dialogFormVisible3: false,
	    		formLabelWidth:'100px',
	    		v__tableDockHeight:'0',
	    		currentSelLb:'',
	    		tableselectdata:[],
	    		selMc:'',
	    		selLb:[],
	    		tabledata:[],
	    		fjData:[],
	    		fjData1:[],
	    		tzguid:'',
	    		ue:null,//ueditor
	    		ue1:null,//ueditor
	    		pickerOptions0:'',
	    		rules: {
               		mc: [ { required: true, message: '请输入名称！'}],
 		        },
 		       page:{
 					total:'0',
 					pagesize:20,
 					currentpage:1
     				},
      			form1:{
      				mc: '',//测试
      				wh: '',//文号
      				fwjg: '',//统治机构
      		      	NOTICECATNAME: '',//类别
      		    	fwrq: '',//通知日期
      		    	SB: '',//文本域
      		        },
      			form2:{
          			mc: '',//测试
          			wh: '',//文号
          			fwjg: '',//统治机构
          		    NOTICECATNAME: '',//类别
          		    fwrq: '',//通知日期
          		    SB: '',//文本域
          		  	insertData: '',
          		    },
          		form3:{
            		mc: '',//测试
            		wh: '',//文号
            		fwjg: '',//统治机构
            		selLb: '',//类别
            		fwrq: '',//通知日期
            		SB: '',//文本域
            		    },

	    	}
	    },
		mounted:function(){
			this.$nextTick(function() {
			    vo.getselLb();	 
			    vo.pagelist();
			    vo.ueditorLoad();
			  });
    	}, 
    	methods:{
    		ueditorLoad: function(){
    		 
    			   vo.ue = new UE.ui.Editor({
    				   initialFrameHeight:150,
    				   initialFrameWidth:document.body.clientWidth-200,
    				   elementPathEnabled:false,
    				   toolbars: [['souWrce','|',
    			                   'bold','italic','underline','removeformat','|','forecolor','backcolor',
    			                   'fontfamily','fontsize','|','justifyleft','justifycenter','justifyright','justifyjustify']],
    			        maximumWords:5000
    			   });
    			   vo.ue1 = new UE.ui.Editor({
    				   initialFrameHeight:150,
    				   initialFrameWidth:document.body.clientWidth-200,
    				   elementPathEnabled:false,
    				   toolbars: [['souWrce','|',
    			                   'bold','italic','underline','removeformat','|','forecolor','backcolor',
    			                   'fontfamily','fontsize','|','justifyleft','justifycenter','justifyright','justifyjustify']],
    			        maximumWords:5000
    			   });
    			   
    		},
    		
    		pagelist:function(){//获取数据
    			vo.$http.post('${pageContext.request.contextPath }/noticeController/getNotice',{
    				'mc':vo.selMc,
    				'lb':vo.currentSelLb, 
    				'pageIndex':vo.page.currentpage-1,
    				'pageSize':vo.page.pagesize,
    			}).then(function(data){
	    			vo.tabledata=data.body.data;
	    			vo.page.total=data.body.total;
	    		})
    		},
    		
    		//获取类别
    		getselLb:function(){
    			vo.$http.post('${pageContext.request.contextPath }/noticeController/getCateGory').then(function(data){
	    			vo.selLb=data.body.data;
	    		})
    		},
    		//新增通知公告
    		xztzgg:function(){
    			vo.form2.wh='';
	           	vo.form2.mc='';
	           	vo.form2.NOTICECATNAME='';
	           	vo.form2.fwjg='';
	           	vo.form2.fwrq='';
	           	vo.form2.SB='';
	           	vo.form2.insertData='';
	           	vo.fjData1=[];
	         // 重置表单
        		if(this.$refs.hasOwnProperty('form2')){
        			this.$refs.form2.resetFields();
        		}
	           	this.dialogFormVisible2 = true; 
	           	//console.log(vo.ue);
    			//渲染ueditor
    			setTimeout(function () { if( vo.ue.key!="SB"){vo.ue.render("SB");}}, 10);
    			vo.ue.ready(function() {//编辑器初始化完成再赋值  
    	            vo.ue.setContent('');  //赋值给UEditor  
    	        });
    			
    		},
    		
    		
    		
    		//编辑通知公告
    		bjtzgg:function(){
    			vo.fjData1=[];
    			if(vo.tableselectdata[0]==null||this.tableselectdata[1]!=null){
	 				this.$message({
			              message: '请选择一条信息！',
			              duration:1000,
			             type:'error',
			         });
	 			} else{
	 				this.tzguid=vo.tableselectdata[0].Guid;
	 			this.$http.get('${pageContext.request.contextPath}/noticeController/getNoticeByID',
    					{params: { "gid":this.tzguid,
    							   }
    					}).then(function(res){
    						
    						this.form3=res.body.data[0];
    						this.dialogFormVisible3 = true;
    						setTimeout(function () { if( vo.ue1.key!="bjSB"){vo.ue1.render("bjSB");}}, 10);
    						if(res.body.data[0].SB!=null){
    							vo.ue1.ready(function() {//编辑器初始化完成再赋值     		    				
        		    	            vo.ue1.setContent(res.body.data[0].SB);  //赋值给UEditor  
        		    	        }); 
    						}
    						if(res.body.data[0].FILEGUID!=null){
    							for(var i=0;i<res.body.data.length;i++){
        		    				var obj=new Object();
        							obj.id=res.body.data[i].FILEGUID;
        							obj.name=res.body.data[i].FILETITLE;
        							vo.fjData1.push(obj);
        		    			}
    						}
    				});
	 			}
    		},
    		
    		
    		//新增通知公告中的保存
            xztzggsave:function(form2){
            	if(this.form2.NOTICECATNAME==null||this.form2.NOTICECATNAME==''){
	 				this.$message({
			              message: '请选择类别！',
			              duration:1000,
			             type:'error',
			         });
	 				return;
	 			}
				for(var i=0;i<vo.fjData1.length;i++){
					vo.form2.insertData+=vo.fjData1[i].id+","+vo.fjData1[i].name+";";
				}
            	this.form2.SB=document.getElementById('SB').value;
   			 this.$refs[form2].validate((valid) => {
		          if (valid) {
 						var url="${pageContext.request.contextPath}/noticeController/saveNotice";
 					  	this.$http.get(url,	{params: { 
							   "wh":this.form2.wh,
							   "mc":this.form2.mc,
							   "lb":this.form2.NOTICECATNAME,
							   "fwjg":this.form2.fwjg,
							   "fwrq":JSON.stringify(this.form2.fwrq),
							   "contents":this.form2.SB,
							   "insertData":this.form2.insertData,
 					  			}
						   } ).then(function(res){
 					  		if(res.ok){
 					  			 this.$message({
 						              message: '新增成功！',
 						              duration:1000,
 						              type: 'success', 						             
 						            });
 					  			this.dialogFormVisible2 = false;
 					  			this.pagelist();
 					  		}else{
 					  			this.$message({
 						              message: '新增失败！',
 						              duration:1000,
 						             type:'error',
 						            });
 					  			this.dialogFormVisible2 = false;
 					  			this.pagelist();
 					  		}				    	 
 						});   
 			          } else {
 			        	 this.$message({
				              message: '新增失败！',
				              duration:1000,
				             type:'error',
				         });
 			             return false;
 			            this.dialogFormVisible2 = false;
				  			this.pagelist();
 			          }
 			        });
 			},
 			
 			//编辑通知公告中的保存
            bjtzggsave:function(form3){
            	vo.form3.insertData='';
            	for(var i=0;i<vo.fjData1.length;i++){
					vo.form3.insertData+=vo.fjData1[i].id+","+vo.fjData1[i].name+";";
				}
				this.form3.SB=document.getElementById('bjSB').value;
   			 this.$refs[form3].validate((valid) => {
		          if (valid) {
 						var url="${pageContext.request.contextPath}/noticeController/editLawPol";
 					  	this.$http.get(url,	{params: { 
 					  			"guid":this.tzguid,
							   	"wh":this.form3.wh,
							   	"mc":this.form3.mc,
							   	"lb":this.form3.selLb,
							   	"fwjg":this.form3.fwjg,
							   	"fwrq":JSON.stringify(this.form3.fwrq),
							   	"contents":this.form3.SB,
								"insertData":this.form3.insertData,
 					  			}
						   } ).then(function(res){
 					  		if(res.ok){
 					  			 this.$message({
 						              message: '修改成功！',
 						              duration:1000,
 						              type: 'success',
 						            });
 					  			this.dialogFormVisible3 = false;
 					  			this.pagelist();
 					  		}else{
 					  			this.$message({
 						              message: '修改失败！',
 						              duration:1000,
 						             type:'error',
 						            });
 					  			this.dialogFormVisible3 = false;
 					  			this.pagelist();
 					  		}				    	 
 						});   
 			          } else {
 			        	this.$message({
				             message: '修改失败！',
				             duration:1000,
				             type:'error',
				         });
 			            return false;
 			            this.dialogFormVisible3 = false;
				  		this.pagelist();
 			          }
 			        });
 			},
 			
 			//删除通知公告
 			tzggdel:function() {		
 				if(vo.tableselectdata[0]==null){
	 				this.$message({
			              message: '请选择一条信息！',
			              duration:1000,
			             type:'error',
			         });
	 			} else{
					for(var i=0;i<vo.tableselectdata.length;i++)
					{
						this.tzguid+="','"+vo.tableselectdata[i].Guid;
					}
		  			this.$confirm('确定要删除这条信息吗？', '提示', {
			              confirmButtonText: '确定',
			              cancelButtonText: '取消',
			              type: 'warning'
			            }).then(() => {
			            	 this.$http.get("${pageContext.request.contextPath}/noticeController/deleteNotice",
									 {   params: { "gid":this.tzguid, }
					        }).then(function(res){ 
						  		if(res.ok){
						  			 this.$message({
							              message: '删除成功！',
							              duration:1000,
							              type: 'success' ,
							            });
						  			this.tzguid='';
						  			this.pagelist();
						  			
						  		}else{
						  			this.$message({
							              message: '删除失败！',
							              duration:1000,
							              type: 'success' 
							            });
						  			this.tzguid='';
						  		}
							});  
					        
			            }).catch(() => {
			              this.$message({
			                type: 'info',
			                duration:1000,
			                message: '已取消删除'
			              });          
			            });
		    	 }
		    }, 
		    
		    sc:function(row) {
		    	document.getElementById('zyf_file').click();
		    	
		    },
		    
    		scfj: function(row) {//上传附件
    			var selLb = row;
    			var filename = document.getElementById("zyf_file").value;
    			if(filename==""){
    				return;
    			}
    			var strs= new Array(); //定义一数组 
    			strs=filename.split("\\"); 
    			filename=strs[strs.length-1];
    			if(selLb=='84c7797f-e720-4360-82ae-ac0781fbbff6'||selLb=='be9d90e6-ae0b-446c-9287-78a304a10ed1'
    				||selLb=='4d5e9953-8871-437f-b59d-b18f445bcaac'||selLb=='442208d2-be9c-4776-bae0-a6e7ecd35ce4'){
    				if(vo.fjData1.length != 0){
    					alert("已有上传文件，请删除原文件后再上传！");
    					return;
    				}
    				if(filename.substr(filename.length-4) != ".xls"){
    					alert("文件格式不符，请导入一个后缀为.xls的Excel文件！");
    					return;
    				}
    			}

    			$.ajaxFileUpload({
					url : "${pageContext.request.contextPath}/noticeController/upload",
					secureuri : false,
					fileElementId : 'zyf_file',
					dataType : 'text',
					data : {
						"workid" : "0"
					},
					success : function(data) {
					 	data = decodeURIComponent(data, "UTF-8");
						data = $.parseJSON(data);
						if (data.id != null) {
							var obj=new Object();
							obj.id=data.id;
							obj.name=filename;
							vo.fjData1.push(obj);
							//console.log(vo.fjData1);
							/* var trHTML = "<tr><td style='display:none'>"
									+ data.id
									+ "</td><td width='70%'>"
									+ "<a href='javascript: void(0)' id ='"+data.id+"' name='" +filename+"' onclick='pro_download(this)'>"+filename+"</a>"
									+ "</td><td width='30%'>"
									+ "<a href='#' @click='delfj()' style='color:blue'>删除附件</a>"
									+ "</td></tr>"
							$("#fujian").append(trHTML); */	
							document.getElementById('zyf_file').value = '';
						} else {
							alert(data.flag);
						} 
						 
					},
					
					complete: function(xmlHttpRequest) {  
		                 $("#zyf_file").on("change", function(){  
		                        vo.scfj(row);
		                 });
	                },  
				});  
    		 
			},
			
			//文件下载
			downloadFj: function(row){
				var fid = row.id;
				var fname = row.name;
				var url = "${pageContext.request.contextPath}/noticeController/downloadFile?fid=" + fid + "&fname="+ encodeURI(fname);
				$.ajax({
					url : url,
					type : "POST",
					data : {},
					success : function(response, status, request) {
						var disp = request.getResponseHeader('Content-Disposition');
						if (disp && disp.search('attachment') != -1) {
							var form = $('<form method="POST" action="' + url + '"> </form>');
							form.appendTo('body').submit().remove(); 
							return;
						}
						if (response.status == "ok") {
							showResult(response.data);
						} else {
							showError('Error: ', response.msg);
						}
					}
				});
			},
			
			//文件删除
			delfj:function(row){
				var attaid = row.id;
				if(confirm("确定要删除吗？"))
				$.ajax({
							type : 'post',
							url : '${pageContext.request.contextPath }/noticeController/deleteAttadata',
							data : {"attaid" : attaid},
							dataType : 'json',
							success : function(b) {
								if (b.code > 0) {
									for(var i=0; i<vo.fjData1.length; i++) {
	 								    if(vo.fjData1[i].id == attaid) {
	 								    	vo.fjData1.splice(i, 1);
	 								      break;
	 								    }
	 								  }
									//console.log(vo.fjData1);
									alert("删除成功");
								}
							}
						});
			},
    		clickRow1:function(row) {//单击行
    			 this.$refs.multipleTable.toggleRowSelection(row);
			},
			tabledoubleclick:function(row) {//双击行	
				vo.fjData=[];
				this.tzguid=row.Guid;
				this.$http.get('${pageContext.request.contextPath}/noticeController/getNoticeByID',
    					{params: { "gid":this.tzguid,
    							   }
    					}).then(function(res){
    						this.form1=res.body.data[0];    						
    						this.dialogFormVisible1=true;
    						if(res.body.data[0].FILEGUID!=null){
    							for(var i=0;i<res.body.data.length;i++){
        		    				var obj=new Object();
        							obj.id=res.body.data[i].FILEGUID;
        							obj.name=res.body.data[i].FILETITLE;
        							vo.fjData.push(obj);
        		    			}
    						}
    				});
				
			},
    		selecttablechange:function(val){
    			vo.tableselectdata=val;
    		},
    		handleCurrentChange:function(val){
				vo.page.currentpage=val;//当前页
				vo.pagelist();
			},
			handleSizeChange:function(val) {//每页显示多少条
 				 vo.page.pagesize=val;
 				 vo.pagelist();
 		     },
    	}
	
	
	
	})
	Hp.createNew(vo);
</script>
</html>