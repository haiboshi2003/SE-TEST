<template>
  <div style="height: 100%" ref="tabs">
    <el-card id="main-card" style="height: 100%" shadow="hover">
      <el-tabs v-model="activeName">
        <el-tab-pane label="问题描述" name="first">
          <TriangleQuestion />
        </el-tab-pane>

        <el-tab-pane
          class="main-container"
          label="系统测试用例测试"
          name="second"
        >
          <SystemTest :parentHeight="parentHeight" />
        </el-tab-pane>

        <el-tab-pane label="单测试用例输入" name="third">
          <SingleCase />
        </el-tab-pane>

        <el-tab-pane label="测试用例文件处理" name="fourth">
          <ExcelFile />
        </el-tab-pane>

        <el-tab-pane label="缺陷版本记录" name="fifth">
          <BugRecord :parentHeight="parentHeight" />
        </el-tab-pane>
      </el-tabs>
    </el-card>
  </div>
</template>

<script>
import TriangleQuestion from "./question";
import SystemTest from "./systemtest";
import SingleCase from "./singlecase";
import ExcelFile from "./excelfile";
import BugRecord from "./bug";

export default {
  name: "Triangle",
  components: {
    TriangleQuestion,
    SystemTest,
    SingleCase,
    ExcelFile,
    BugRecord,
  },
  props: {},
  data() {
    return {
      activeName: "first",
      parentHeight: 3333,
    };
  },
  computed: {},
  watch: {},
  created() {
    window.addEventListener("resize", this.getHeight);
  },
  mounted() {},
  methods: {
    getHeight() {
      try {
        this.parentHeight = this.$refs.tabs.offsetHeight;
      } catch (err) {}
    },
  },
};
</script>

<style scoped lang="less">
#main-card {
  background-color: #eddeaa;

  border: 1px solid #ccc; /* 可选：添加边框 */
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* 添加边框阴影 */
  border-radius: 8px; /* 可选：添加圆角 */
  padding: 16px; /* 可选：添加内边距 */
}
</style>
