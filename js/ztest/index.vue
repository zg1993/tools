<template>
  <div class="container">
    <a-card>
      <Start
        id="main"
        ref="startRef"
        title="延时办件统计"
        v-bind:method="request"
        v-bind:dateList="['day', 'week', 'month', 'year']"
      ></Start>
    </a-card>
    <a-card>
      <StackedBar
        ref="barRef"
        title="审批数量统计"
        :method="request"
        :dateList="['day', 'week', 'month', 'year']"
        :stack="true"
      ></StackedBar> </a-card
    ><a-card><Pie ref="pieRef" title="市级产业画像"></Pie></a-card>
  </div>
</template>
<script>
import * as echarts from 'echarts'
import Start from './modules/Start.vue'
import StackedBar from './modules/StackedBar.vue'
import Pie from './modules/Pie.vue'
import { getEntEntryList } from '@/api/benefitCompany/home'

export default {
  data: function() {
    return {
      list: ['day', 'week']
    }
  },
  components: {
    Start: Start,
    StackedBar: StackedBar,
    Pie: Pie
  },
  // mounted: function(){
  //   this.$refs.startRef.expose()
  // },
  methods: {
    request: getEntEntryList
  }
}
</script>
<style lang="less" scoped>
.container {
  display: flex;
  flex-wrap: wrap;
}
</style>
