<template>
  <div class="header">
    <div class="img">
      <img src="Tj.png" alt="Header Image" />
    </div>
    <div class="hhh">
      <p>同济大学软件测试</p>
    </div>
  </div>
</template>

<script>
export default {
  name: "HeadBar",
  components: {},
  props: {},
  data() {
    return {};
  },
  computed: {},
  watch: {},
  created() {},
  mounted() {},
  methods: {
    changeCollapse() {
      this.$emit("changeCollapse", 0);
    },
  },
};
</script>

<style scoped lang="less">
.header {
  background-color: rgb(242, 242, 242);

  display: flex;
  flex-direction: row;

  height: 65px;
}
.hhh {
  // background-color: aqua;
  // padding: 0px 0 0 0;
  width: 210px;
  height: 100px;
  margin-bottom: 20px;
  margin-top: 0px;
  // border: 1px solid blue;
}

.img {
  // background-color: black;
  margin-top: 2px;
  padding: 6px 10px 0 40px; /* 设置图像框的内边距 */
  // border: 1px solid blue;
  width: 70px;
  max-width: 120px;
  height: 50px;
  max-height: 50px;
  // border: 1px solid blue;
}

.img img {
  max-width: 100%; /* 图片的最大宽度不超过父元素的宽度 */
  max-height: 100%; /* 图片的最大高度不超过父元素的高度 */
  display: block; /* 让图片以块级元素显示 */
}
p {
  font-style: italic;
  font-family: "宋体", SimSun, sans-serif;
  font-size: 23px;
  color: rgb(12, 12, 12);
}
</style>
