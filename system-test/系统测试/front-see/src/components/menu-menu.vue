<template>
  <div id="father">
    <div id="header">
      <div class="img">
        <img src="Tj.png" alt="Header Image" />
      </div>
      <div class="hhh">
        <p>同济大学软件管理与经济</p>
      </div>
    </div>
    <div id="father-c">
      <!-- 侧栏 -->
      <div id="aside">
        <div class="container ta-c">
          <nav class="menu animated flipInX">
            <ul class="no-ls ta-l t-all">
              <li id="yolo">
                <a href="http://localhost:8080/#/menu/menu2/r1">
                  <h3>YOLO</h3>
                </a>
              </li>
              <li id="svm">
                <a href="http://localhost:8080/#/menu/menu2/r2">
                  <h3>SVM</h3>
                </a>
              </li>
            </ul>
          </nav>
        </div>
      </div>
      <div id="main"><router-view></router-view></div>
    </div>
  </div>
</template>

<script setup></script>
<style scoped>
#father {
  flex-direction: column;
  height: 100vh; /* 使布局占满整个视口高度 */
}

#header {
  background-color: rgba(
    242,
    243,
    245,
    1
  ); /* 设置 header 的背景颜色为灰色，透明度为 80% */
  flex: 0 0 8%; /* header 占父容器的 8% 高度 */
  display: flex;
  flex-direction: row;
}

#father-c {
  display: flex;
  flex-direction: row;
  flex: 1 0 80%; /* father-c 占剩余的 80% 高度 */
}
#aside {
  background-color: rgba(255, 255, 255, 0.2);
  width: 250px; /* 假设一个固定宽度 */
  border-right: 1px solid #d0d0d0; /* 只在右边添加黑色边框 */
  border-top: 1px solid #d0d0d0; /* 在上边添加黑色边框 */
}

#main {
  background-color: rgba(255, 255, 255, 0.2); /* 设置 main 的背景颜色 */
  flex: 1;
  border-top: 1px solid #d0d0d0; /* 在上边添加黑色边框 */
}

.img {
  padding: 6px 0 0 4%; /* 设置图像框的内边距 */
  /* border: 1px solid blue; */
  width: 150px;
  max-width: 120px;
  height: 50px;
  max-height: 50px;
}

.img img {
  max-width: 100%; /* 图片的最大宽度不超过父元素的宽度 */
  max-height: 100%; /* 图片的最大高度不超过父元素的高度 */
  display: block; /* 让图片以块级元素显示 */
}
.hhh {
  padding: 17px 0 0 0; /* 设置图像框的内边距 */

  /* border: 1px solid rgb(224, 88, 26); */
}
p {
  font-style: italic;
  font-family: "宋体", SimSun, sans-serif;
  font-size: 20px;
  color: rgb(12, 12, 12);
}

/* 侧栏 */

ul {
  list-style-type: none;

  padding: 0; /* 去除内边距 */
  margin: 0; /* 去除外边距 */
  display: flex; /* 设置为 flex 布局 */
  flex-direction: column; /* 使子元素垂直排列 */
  align-items: center; /* 使子元素水平居中 */
}

.container {
  /* margin: 0 auto; */
  margin-top: 25px; /* 设置上边距为20px */
  width: 250px;
  max-width: 250px;
  /* background-color: black; */
}

h2 {
  padding: 1.8rem 0;

  font-size: 2.8rem;

  text-shadow: 0px 1px 1px rgba(255, 255, 255, 0.4);
}
h3 {
  color: #414141; /* 设置链接的字体颜色为红色 */
  font-size: 16px; /* 设置链接的字体大小为 16 像素 */
  text-align: center; /* 将链接居中对齐 */
}

nav {
  -webkit-box-flex: auto;
  -webkit-flex: auto;
  -ms-flex: auto;
  flex: auto;
  position: relative;
  padding: 0.6125rem 0.6152rem 1.6125rem;
}

li a {
  text-decoration: none;
  color: RGBA(67, 83, 99, 1);
  cursor: -webkit-zoom-in;
  cursor: zoom-in;
}

ul:hover a {
  opacity: 0.8;

  -webkit-transform: scale(0.85);
  transform: scale(0.85);
}

ul a {
  display: block;
  position: relative;
  padding: 0.75rem 1rem 1rem;

  width: 200px; /* 设置列表项的宽度为 200px */
  height: 50px; /* 设置列表项的高度为 50px */
  border-radius: 10px; /*设置圆角矩形 */
  -webkit-transition: -webkit-transform 0.22s, box-shadow 0.22s;
  transition: transform 0.22s, box-shadow 0.22s;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
  user-drag: none;
  box-shadow: 0 0 0 -0.25rem rgba(0, 0, 0, 0.1);
}

ul a:focus,
ul a:hover {
  outline: 0;
  box-shadow: 0 0.5rem 0 -0.25rem rgba(0, 0, 0, 0.1);
  opacity: 1;
  -webkit-transform: scale(1.15);
  transform: scale(1.15);
  -webkit-transition: -webkit-transform 0.088s, box-shadow 0.088s;
  transition: transform 0.088s, box-shadow 0.088s;
  z-index: 1;
}

ul.no-ls li {
  margin-bottom: 12px; /* 设置列表项之间的垂直间距为 10px */
}

.menu a:nth-child(1) {
  background: #0e8206;
}
.menu a:nth-child(2) {
  background: #cdd0d6;
}
.menu a:nth-child(3) {
  background: #cdd0d6;
}

.animated {
  -webkit-animation-duration: 1s;
  animation-duration: 1s;
  -webkit-animation-fill-mode: both;
  animation-fill-mode: both;
}

@-webkit-keyframes flipInX {
  0% {
    -webkit-transform: perspective(400px) rotateX(90deg);
    transform: perspective(400px) rotateX(90deg);
    opacity: 0;
  }

  40% {
    -webkit-transform: perspective(400px) rotateX(-10deg);
    transform: perspective(400px) rotateX(-10deg);
  }

  70% {
    -webkit-transform: perspective(400px) rotateX(10deg);
    transform: perspective(400px) rotateX(10deg);
  }

  100% {
    -webkit-transform: perspective(400px) rotateX(0deg);
    transform: perspective(400px) rotateX(0deg);
    opacity: 1;
  }
}

@keyframes flipInX {
  0% {
    -webkit-transform: perspective(400px) rotateX(90deg);
    -ms-transform: perspective(400px) rotateX(90deg);
    transform: perspective(400px) rotateX(90deg);
    opacity: 0;
  }

  40% {
    -webkit-transform: perspective(400px) rotateX(-10deg);
    -ms-transform: perspective(400px) rotateX(-10deg);
    transform: perspective(400px) rotateX(-10deg);
  }

  70% {
    -webkit-transform: perspective(400px) rotateX(10deg);
    -ms-transform: perspective(400px) rotateX(10deg);
    transform: perspective(400px) rotateX(10deg);
  }

  100% {
    -webkit-transform: perspective(400px) rotateX(0deg);
    -ms-transform: perspective(400px) rotateX(0deg);
    transform: perspective(400px) rotateX(0deg);
    opacity: 1;
  }
}

.flipInX {
  -webkit-backface-visibility: visible !important;
  -ms-backface-visibility: visible !important;
  backface-visibility: visible !important;
  -webkit-animation-name: flipInX;
  animation-name: flipInX;
}
</style>
