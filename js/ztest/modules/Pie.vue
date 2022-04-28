<template>
  <div>
    <div ref="container" class="chart" v-if="total"></div>
  </div>
</template>
<script>
import * as echarts from 'echarts'

export default{
    props: {
        title: {
            type: String,
        },
        method: {
            type: Function,
            default: async ()=>{null},
        }
    },
    data: function(){
        return {
            total: 1,
            params: {
                pageNo: 1,
                pageSize: 10,
            }
        }
    },
    mounted: function(){
        this.mychart = echarts.init(this.$refs.container)
        this.initChart()
    },
    methods:{
        // initChart(){} dataSet
        initChart(){
            this.method(this.params).then(res=>{
                console.log(res)
                // 计算 total
                let data = [
        {
          value: 335,
          name: '直接访问'
        },
        {
          value: 234,
          name: '联盟广告'
        },
        {
          value: 1548,
          name: '搜索引擎'
        }
      ]
                this.total = data.reduce((x,y)=>{
                    return x+y.value}, this.total)
                console.log(this.total)
                // this.total= 0
                this.mychart.setOption({
                    title: {
                        text: this.title,
                        left: 'center',
                        subtext: `总数${this.total}`,
                        subtextStyle:{
                            // color: '#fff'
                        }
                    },
                    
                    legend:{
                        show: true,
                        orient: 'vertical',
                        // x: 'right',
                        // y: 'bottom',
                        right: 15,
                        bottom: 20,
                    },
                    series: [
                        {
                            type: 'pie',
                            center: ['35%', '60%'],
                            data: data,
                            label:{
                                formatter: '{c}',
                                position: 'inner',
                            }
                        }
                    ]
                })

            })
        }
    }

}
</script>
<style lang="less" scoped>
@width: 480px;
@height: 380px;
.chart {
  width: @width;
  height: @height;
}
</style>
