<template>
  <div>
    <el-card shadow="hover" class="card">
      <el-tabs v-model="activeName" @tab-click="handleClick">
        <el-tab-pane label="问题描述" name="first">
          <SalesQuestion />
        </el-tab-pane>
      </el-tabs>
    </el-card>
  </div>
</template>

<script>
import SalesQuestion from "./question";
export default {
  name: "ten",
  components: { SalesQuestion },
  props: {},
  data() {
    return {
      options: [],
      value: "选项1",
      tableData: [],
      loading: false,
      classState: [],
      stateflag: false,
      activeName: "first",
      isFirst: true,
      labelPosition: "right",
      formLabelAlign: {
        name: "",
        region: "",
        type: "",
      },
    };
  },
  computed: {},
  watch: {},
  created() {},
  mounted() {},
  methods: {},
};
</script>

<style scoped lang="less">
/deep/ .el-table .error-row {
  background: #fff0f0;
}
/deep/ .el-table .success-row {
  background-color: #f7fff9;
}
.item {
  margin-bottom: 10px;
}
.clearfix:before,
.clearfix:after {
  display: table;
  content: "";
}
.clearfix:after {
  clear: both;
}
.main-form {
  margin-top: 10px;
}
.main-button {
  width: 100%;
  margin-top: 10px;
}
.card {
  background-color: #eddeaa;
  border: 1px solid #ccc; /* 可选：添加边框 */
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* 添加边框阴影 */
  border-radius: 8px; /* 可选：添加圆角 */
  padding: 16px; /* 可选：添加内边距 */
}
.box-card {
  padding: 0;
}
.single-form {
  width: 600px;
  top: 50%;
  left: 50%;
}
.block {
}
</style>
