<template>
  <div>
    <div class="extra-item">
      <a @click="clickTime(item)" v-for="item in dateList">{{ dateMap[item] }}</a>
    </div>
    <div ref="container" class="chart"></div>
  </div>
</template>
<script>
import * as echarts from 'echarts'
export default {
  props: {
    // 标题
    title: {
      type: String
    },
    // 显示日周月年格式: ['day','week', 'month', 'year']
    dateList: {
      type: Array,
      default: ()=>[],
    },
    // ajax请求后端数据
    method: {
      type: Function,
      default: async () => {null},
    },
    // 是否堆叠柱状图：true堆叠
    stack: {
      type: false,
      default: false,
    }
  },

  data: function() {
    return {
      dateMap: {
        day: '日',
        week: '周',
        month: '月',
        year: '年'
      },
      params: {
        pageNo: 1,
        pageSize: 10
      },
      series: [],
      source: [],
      xType: 'category'
    }
  },

  mounted: function() {
    this.myChart = echarts.init(this.$refs.container)
    this.initChart()
  },

  methods: {
    // 初始化echarts
    initChart() {
      let seriesItem = this.stack ? {type: 'bar', seriesLayoutBy: 'row', stack:'month'} : {type: 'bar', seriesLayoutBy: 'row'}
      this.method(this.params).then(res => {
        console.log(res)
        // 处理 res
        // res = []
        let data = res
        let source = [
            ['month', '1月', '2月', '3月', '4月', '5月', '6月', '7月', '8月', '9月', '10月', '11月', '12月'],
            ['急需审批', 43.3, 85.8, 93.7, 43.3, 85.8, 93.7,, 43.3, 85.8, 93.7, 43.3, 85.8, 93.7],
            ['普通审批', 83.1, 73.4, 55.1, 85.8, 93.7, 43.3, 85.8, 93.7, 43.3, 85.8, 93.7, 43.3],
            ['延时办件', 86.4, 65.2, 82.5, 83.1, 73.4, 55.1, 85.8, 93.7, 43.3, 85.8, 93.7,, 43.3],
            ['超时未办', 72.4, 53.9, 39.1, 65.2, 82.5, 83.1, 73.4, 55.1, 85.8, 65.2, 82.5, 83.1],
            ['已办', 72.4, 53.9, 39.1, 53.9, 39.1, 65.2, 82.5, 83.1, 73.4, 55.1, 85.8, 65.2],
        ]
        for(let i=0; i<source.length -1; i++) {
            this.series.push(seriesItem)
        }
        this.myChart.setOption({
          title: {
            text: this.title,
            left: 'center'
          },
          legend:{
            top: "12%",
          },
          grid:{
            top: '30%',
          },
          tooltip: {},
          xAxis: {
            type: 'category'
          },
          yAxis: {},
          series: this.series,
          dataset: {
              source: source,
          }
        })
      })
    },
    // 点击月周日调用函数
    clickTime(dateType) {
      this.params.dateType = dateType
      // this.method
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
