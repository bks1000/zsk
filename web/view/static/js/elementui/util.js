/**
 * 合并列函数
 * @param {Object} row
 * @param {Object} column
 * @param {Object} rowIndex
 * @param {Object} columnIndex
 * @param {Object} colIdx  要合并的列索引
 * @param {Object} data 表格全部数据
 */
/*function elColspan(row, column, rowIndex, columnIndex,colIdx,data){
	//要点
	//1.columnIndex很重要，合并哪一列，全看这个了。
	//2.就算终止代码继续运行，必须return [0,0]！
	if(columnIndex===colIdx){
	   if(rowIndex+1==data.length){
	   	   return[0,0];
	   }
	   if(rowIndex>0){
	   	 var frontrow = data[rowIndex-1];
	   	 if(frontrow.name===row.name){
	   	 	return[0,0];
	   	 }
	   }
	   var rowspan=1;
	   for(var rowidx=rowIndex+1;rowidx<data.length;rowidx++){
	   	  var nextrow = data[rowidx];
	   	  if(row.name===nextrow.name){
	   	  	rowspan++;
	   	  }
	   }
	   
	   if(rowspan>1){
	   		return{
	   			rowspan: rowspan,
	            colspan: 1
	   		};
	   }else{
	   	return{
	   		rowspan: 0,
	        colspan: 0
	   	}
	   }
	}
}*/

/**
 * 合并列函数
 * Auth:hw
 * Date:2018-1-3
 * @param {Object} row
 * @param {Object} column
 * @param {Object} rowIndex
 * @param {Object} columnIndex
 * @param {Object} colIdx  要合并的列索引
 * @param {Object} data 表格全部数据
 * @param {object} columnname 列字段名
 * demo:
 * <el-table :data="tableData" stripe style="width: 100%"  :span-method="objectSpanMethod">
 * methods:{
 *      objectSpanMethod({ row, column, rowIndex, columnIndex }) {
 	* 		if(row.columnIndex==1){
 	* 			return elColspan(row,column,rowIndex,columnIndex,1,this.tableData);//合并第2列(索引从0开始)
 	* 		}
 *          
 *      }
 * }
 */
function elColspan(row, column, rowIndex, columnIndex,colIdx,data,columnname){
    if(row.columnIndex==undefined){
        return;
    }
    if(row.columnIndex===colIdx){
        if(row.rowIndex+1==data.length){
            var frontrow = data[row.rowIndex-1];
            if(frontrow[columnname]===row.row[columnname]){
                return[0,0];
            }else {
                return[1,1];
            }
        }
        if(row.rowIndex>0){
            var frontrow = data[row.rowIndex-1];
            if(frontrow[columnname]===row.row[columnname]){
                return[0,0];
            }
        }

        var rowspan=1;
        for(var rowidx=row.rowIndex+1;rowidx<data.length;rowidx++){
            var nextrow = data[rowidx];
            if(row.row[columnname]===nextrow[columnname]){
                rowspan++;
            }
        }

        if(rowspan>1){
            return{
                rowspan: rowspan,
                colspan: 1
            };
        }else{
            return{
                rowspan: 0,
                colspan: 0
            }
        }
    }
}

