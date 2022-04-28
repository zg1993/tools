<template>
  <div class="position">
    <div class="extra-item">
      <a @click="clickTime(item)" v-for="item in dateList">{{ dateMap[item] }}</a>
    </div>

    <div ref="container" class="chart" ></div>
  </div>
</template>
<script>
import * as echarts from 'echarts'
import { setTimeout } from 'timers'
export default {
  // props: ['title', 'method', 'dateList','className'], // dateList: ['day','week', 'month', 'year']
  props: {
    title: { 
      type: String,
      default: '',},
    method: {
      type: Function,
      default: async ()=>{null},
    },
    dateList:{
      type: Array,
      default: function(){return ['week', 'month', 'year']},
    },
  },
  data: function() {
    return {
      chartData: {},
      dateMap: {
        day: '日',
        week: '周',
        month: '月',
        year: '年'
      },
      params: {
        pageNo: 1,
        pageSize: 10,
        dateType: 'day'
      }
    }
  },
  mounted: function() {
    // console.log(this.title)
    // console.log(this.method)
    // console.log(typeof this.method)
    // console.log(this.dateList)
    this.myChart = echarts.init(this.$refs.container)
    this.initEcharts()
  },
  methods: {
    initEcharts() {
      this.method(this.params).then(res => {
        console.log(res);
        res = {
          value: [5, 20, 36, 10, 10, 20, 5, 20, 36, 10, 10, 20],
          category: [
            'xx部门',
            'xx部门',
            'xx部门',
            'xx部门',
            'xx部门',
            'xx部门',
            'xx部门',
            'xx部门',
            'xx部门',
            'xx部门',
            'xx部门',
            'xx部门'
          ]
        }
        // 处理res
       let data = res
       this.myChart.setOption({
        title: {
          text: this.title,
          left: 'center'
        },
        tooltip: {
          top: '12%',
        },
        xAxis: {
          data: data.category
        },
        grid:{

        },
        yAxis: {},
        series: [
          {
            type: 'bar',
            data: data.value,
            color: ['rgb(58 161 255)']
          }
        ]
      })

      })
    },

    clickTime(dateType) {
      let options
     
      if ('day' === dateType) {
        // request({''})
        options = {
          series: [
            {
              type: 'bar',
              data: [35, 20, 36, 10, 10, 20, 5, 20, 36, 10, 10, 20],
              color: ['rgb(58 161 255)']
            }
          ]
        }
      } else if ('week' === dateType) {
        options = {
          series: [
            {
              type: 'bar',
              data: [35, 20, 36, 20, 20, 20, 25, 20, 35, 10, 10, 20],
              color: ['rgb(58 161 255)']
            }
          ]
        }
      } else if ('month' === dateType) {
        
        options = {}
      } else if ('year' === dateType) {
        
        options = {}
      }else{
        console.log('sssssss')
      }
      this.updateChart(options)
    },

    updateChart(data) {
      this.myChart.setOption(data)
    },
    expose(){
      console.log('expose')
    }
  }
}
</script>
<style lang="less" scoped>
@width: 600px;
@height: 300px;
.chart {
  width: @width;
  height: @height;
}
.extra-item {
  width: @width;
  font-size: 16px;
  text-align: right;
  a {
    padding: 0 5px;
  }
}
</style>
